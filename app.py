# -*- coding: utf-8 -*-
from flask import Flask, render_template, abort
from data import BOOSTER_BOXES, CARDS, REPRESENTATIVE_CARD
import scryfall_client

app = Flask(__name__)

print("[app] iniciando Planar Cache...", flush=True)

# Pré-busca (e cacheia em disco) as imagens de todas as cartas usadas no site
# assim que o servidor sobe, respeitando o rate limit da Scryfall. Depois
# disso os templates só usam URLs diretas do CDN de imagens, sem limite.
_ALL_NAMES = [c["name"] for c in CARDS] + list(REPRESENTATIVE_CARD.values())
scryfall_client.warm_cache(_ALL_NAMES)

print("[app] pronto! Acesse http://127.0.0.1:5000", flush=True)


def _boxes_with_art():
    boxes = []
    for box in BOOSTER_BOXES:
        representative = REPRESENTATIVE_CARD.get(box["id"])
        images = scryfall_client.get_card_images(representative) if representative else None
        boxes.append(dict(box, art=(images["art_crop"] if images else None)))
    return boxes


def _cards_with_images():
    cards = []
    for card in CARDS:
        images = scryfall_client.get_card_images(card["name"])
        cards.append(dict(card, image=(images["normal"] if images else None)))
    return cards


@app.route("/")
def index():
    return render_template("index.html", boxes=_boxes_with_art(), cards=_cards_with_images())


@app.route("/carta/<card_id>")
def card_detail(card_id):
    card = next((c for c in CARDS if c["id"] == card_id), None)
    if card is None:
        abort(404)
    images = scryfall_client.get_card_images(card["name"])
    card = dict(card, image=(images["normal"] if images else None))
    return render_template("card.html", card=card)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
