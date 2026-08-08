# -*- coding: utf-8 -*-
"""
Cliente simples para a API pública da Scryfall.

Problema que este módulo resolve:
- O endpoint /cards/named?...&format=image tem rate limit de 2 requisições
  por segundo. Se o HTML pedir 30 imagens de uma vez (10 boxes + 20 cartas),
  o navegador dispara todas em paralelo e a Scryfall começa a recusar/atrasar
  pedidos, fazendo várias imagens "quebrarem" na página.

Solução:
- Buscamos os dados de cada carta UMA VEZ, no servidor, respeitando o rate
  limit (uma pausa entre chamadas), e guardamos as URLs reais das imagens
  (hospedadas em cards.scryfall.io) em um cache local (scryfall_cache.json).
- O HTML final aponta direto para essas URLs de imagem, que não têm esse
  limite de 2 req/s — então o navegador carrega tudo normalmente.
- Em execuções seguintes, o cache já existe em disco e nada precisa ser
  buscado de novo (carregamento instantâneo, sem depender da rede na hora
  de servir a página).
"""

import json
import os
import time
import requests

CACHE_PATH = os.path.join(os.path.dirname(__file__), "scryfall_cache.json")
REQUEST_DELAY = 0.15   # segundos entre chamadas -> bem abaixo do limite de 2/s
REQUEST_TIMEOUT = 5    # segundos -> falha rápido em vez de travar o terminal
API_URL = "https://api.scryfall.com/cards/named"

_cache = None


def _load_cache():
    global _cache
    if _cache is not None:
        return _cache
    if os.path.exists(CACHE_PATH):
        try:
            with open(CACHE_PATH, "r", encoding="utf-8") as f:
                _cache = json.load(f)
        except (json.JSONDecodeError, OSError):
            _cache = {}
    else:
        _cache = {}
    return _cache


def _save_cache():
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(_cache, f, ensure_ascii=False, indent=2)


def _request_card(name, fuzzy=False):
    params = {"fuzzy": name} if fuzzy else {"exact": name}
    try:
        resp = requests.get(API_URL, params=params, timeout=REQUEST_TIMEOUT)
    except requests.RequestException:
        return None
    if resp.status_code != 200:
        return None
    return resp.json()


def has_internet():
    """Testa rapidamente se dá pra alcançar a API antes de tentar buscar tudo."""
    try:
        requests.get("https://api.scryfall.com", timeout=REQUEST_TIMEOUT)
        return True
    except requests.RequestException:
        return False


def get_card_images(name):
    """
    Retorna um dict {"normal": url, "art_crop": url} para o nome da carta,
    usando cache em disco. Retorna None se a carta não for encontrada
    (o template deve exibir um placeholder nesse caso).
    """
    cache = _load_cache()

    if name in cache:
        return cache[name] or None  # None fica salvo p/ não tentar de novo toda hora

    data = _request_card(name, fuzzy=False)
    if data is None:
        time.sleep(REQUEST_DELAY)
        data = _request_card(name, fuzzy=True)

    time.sleep(REQUEST_DELAY)

    if data is None:
        cache[name] = None
        _save_cache()
        return None

    image_uris = data.get("image_uris")
    if not image_uris and "card_faces" in data:
        # cartas de dupla face guardam as imagens dentro de card_faces
        faces = data.get("card_faces") or []
        if faces:
            image_uris = faces[0].get("image_uris")

    if not image_uris:
        cache[name] = None
        _save_cache()
        return None

    result = {
        "normal": image_uris.get("normal"),
        "art_crop": image_uris.get("art_crop"),
    }
    cache[name] = result
    _save_cache()
    return result


def warm_cache(names):
    """Pré-busca uma lista de nomes de carta, mostrando progresso no terminal."""
    cache = _load_cache()
    pending = [n for n in names if n not in cache]

    if not pending:
        print("[scryfall] cache já completo, nada para buscar.", flush=True)
        return

    print(f"[scryfall] buscando {len(pending)} imagens na Scryfall (só na primeira vez)...", flush=True)

    if not has_internet():
        print("[scryfall] AVISO: não consegui conectar à api.scryfall.com. "
              "Verifique sua internet/firewall. O site vai subir mesmo assim, "
              "mas as imagens aparecerão como placeholder até isso ser resolvido.", flush=True)
        return

    for i, name in enumerate(pending, start=1):
        get_card_images(name)
        print(f"[scryfall] {i}/{len(pending)}: {name}", flush=True)

    print("[scryfall] cache pronto — próximas execuções serão instantâneas.", flush=True)
