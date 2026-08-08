# -*- coding: utf-8 -*-
"""
Dados estáticos do site: booster boxes (coleções/lançamentos) e cartas avulsas.
As imagens das cartas usam o endpoint público de imagens da Scryfall
(https://api.scryfall.com/cards/named?...&format=image), que devolve
a arte oficial da carta sem precisarmos hospedar os arquivos.
Os ícones dos sets usam os SVGs públicos da Scryfall (svgs.scryfall.io).
"""

def set_icon(code: str) -> str:
    return f"https://svgs.scryfall.io/sets/{code}.svg"


# Carta usada como arte de capa de cada booster box (uma carta marcante do set)
REPRESENTATIVE_CARD = {
    "eoe": "Void Rend",
    "tdm": "Ojer Taq, Deepest Foundation",
    "dft": "Lord Xander, the Collector",
    "fdn": "Wrath of God",
    "dsk": "Overlord of the Balemurk",
    "blb": "Kellan, the Fae-Blooded",
    "mh3": "Ugin, the Spirit Dragon",
    "otj": "Vraska, Betrayal's Sting",
    "mkm": "Alquist Proft, Master Sleuth",
    "fin": "Cloud Strife, ex-SOLDIER",
}


# ---------------------------------------------------------------------------
# BOOSTER BOXES — principais coleções e lançamentos
# ---------------------------------------------------------------------------
BOOSTER_BOXES = [
    {
        "id": "eoe",
        "name": "Edge of Eternities",
        "set_code": "eoe",
        "release_date": "2025-08-01",
        "description": "Uma expansão de ficção científica que leva os planeswalkers a confins "
                        "estelares nunca vistos, com naves, colônias alienígenas e magia cósmica.",
        "icon": set_icon("eoe"),
        "price": "R$ 999,90",
        "boosters": 30,
    },
    {
        "id": "tdm",
        "name": "Tarkir: Dragonstorm",
        "set_code": "tdm",
        "release_date": "2025-04-11",
        "description": "O retorno a Tarkir com os cinco clãs dracônicos em guerra e a magia "
                        "élfica antiga despertando dragões lendários.",
        "icon": set_icon("tdm"),
        "price": "R$ 949,90",
        "boosters": 30,
    },
    {
        "id": "dft",
        "name": "Aetherdrift",
        "set_code": "dft",
        "release_date": "2025-02-14",
        "description": "Uma corrida interplanar de veículos turbinados a éter, cheia de "
                        "velocidade, explosões e pilotos lendários de todo o multiverso.",
        "icon": set_icon("dft"),
        "price": "R$ 899,90",
        "boosters": 30,
    },
    {
        "id": "fdn",
        "name": "Foundations",
        "set_code": "fdn",
        "release_date": "2024-11-15",
        "description": "Um pilar atemporal do jogo, reunindo cartas essenciais e "
                        "reimpressões icônicas para começar ou reforçar qualquer coleção.",
        "icon": set_icon("fdn"),
        "price": "R$ 799,90",
        "boosters": 36,
    },
    {
        "id": "dsk",
        "name": "Duskmourn: House of Horror",
        "set_code": "dsk",
        "release_date": "2024-09-27",
        "description": "Um plano inteiro transformado em uma casa mal-assombrada viva, "
                        "repleto de terror gótico e criaturas que espreitam nas sombras.",
        "icon": set_icon("dsk"),
        "price": "R$ 899,90",
        "boosters": 30,
    },
    {
        "id": "blb",
        "name": "Bloomburrow",
        "set_code": "blb",
        "release_date": "2024-08-02",
        "description": "Um plano habitado inteiramente por animais antropomórficos, dividido "
                        "em biomas vibrantes e clãs com identidades próprias.",
        "icon": set_icon("blb"),
        "price": "R$ 899,90",
        "boosters": 30,
    },
    {
        "id": "mh3",
        "name": "Modern Horizons 3",
        "set_code": "mh3",
        "release_date": "2024-06-14",
        "description": "Expansão premium voltada ao formato Modern, trazendo mecânicas "
                        "novas e cartas de alto impacto competitivo direto no papel.",
        "icon": set_icon("mh3"),
        "price": "R$ 1.299,90",
        "boosters": 24,
    },
    {
        "id": "otj",
        "name": "Outlaws of Thunder Junction",
        "set_code": "otj",
        "release_date": "2024-04-19",
        "description": "Um faroeste multiversal cheio de fora da lei, assaltos a trens "
                        "e duelos ao pôr do sol em um plano árido e perigoso.",
        "icon": set_icon("otj"),
        "price": "R$ 849,90",
        "boosters": 30,
    },
    {
        "id": "mkm",
        "name": "Murders at Karlov Manor",
        "set_code": "mkm",
        "release_date": "2024-02-09",
        "description": "Um mistério noir em Ravnica: as dez guildas se envolvem em uma "
                        "investigação de assassinato cheia de pistas e reviravoltas.",
        "icon": set_icon("mkm"),
        "price": "R$ 849,90",
        "boosters": 30,
    },
    {
        "id": "fin",
        "name": "Final Fantasy",
        "set_code": "fin",
        "release_date": "2025-06-13",
        "description": "Um crossover Universes Beyond que reúne heróis, invocações e "
                        "momentos icônicos de décadas da saga Final Fantasy.",
        "icon": set_icon("fin"),
        "price": "R$ 1.199,90",
        "boosters": 24,
    },
]

# ---------------------------------------------------------------------------
# CARTAS AVULSAS
# ---------------------------------------------------------------------------
CARDS = [
    {
        "id": "black-lotus",
        "name": "Black Lotus",
        "mana_cost": "{0}",
        "type_line": "Artefato",
        "rarity": "Especial",
        "set": "Limited Edition Alpha",
        "release_date": "1993-08-05",
        "oracle_text": "{T}, Sacrifique Lótus Negra: Adicione três manas de uma única cor.",
        "flavor_text": "A carta mais lendária de todo o multiverso, símbolo do início do jogo.",
    },
    {
        "id": "lightning-bolt",
        "name": "Lightning Bolt",
        "mana_cost": "{R}",
        "type_line": "Instantânea",
        "rarity": "Comum",
        "set": "Limited Edition Alpha",
        "release_date": "1993-08-05",
        "oracle_text": "Lightning Bolt causa 3 pontos de dano a qualquer alvo.",
        "flavor_text": "O feitiço vermelho mais eficiente já impresso.",
    },
    {
        "id": "sol-ring",
        "name": "Sol Ring",
        "mana_cost": "{1}",
        "type_line": "Artefato",
        "rarity": "Incomum",
        "set": "Commander Masters",
        "release_date": "2023-08-04",
        "oracle_text": "{T}: Adicione {C}{C}.",
        "flavor_text": "Presente em quase todo deck de Commander competitivo.",
    },
    {
        "id": "counterspell",
        "name": "Counterspell",
        "mana_cost": "{U}{U}",
        "type_line": "Instantânea",
        "rarity": "Comum",
        "set": "Masters Edition",
        "release_date": "1993-12-01",
        "oracle_text": "Anule a mágica alvo.",
        "flavor_text": "O contramágica mais icônico do jogo, síntese da cor azul.",
    },
    {
        "id": "swords-to-plowshares",
        "name": "Swords to Plowshares",
        "mana_cost": "{W}",
        "type_line": "Instantânea",
        "rarity": "Incomum",
        "set": "Masters Edition",
        "release_date": "1993-12-01",
        "oracle_text": "Exile a criatura alvo. Seu controlador ganha vida igual à força dela.",
        "flavor_text": "A remoção branca mais eficiente já criada.",
    },
    {
        "id": "wrath-of-god",
        "name": "Wrath of God",
        "mana_cost": "{2}{W}{W}",
        "type_line": "Feitiço",
        "rarity": "Rara",
        "set": "Tenth Edition",
        "release_date": "2007-07-13",
        "oracle_text": "Destrua todas as criaturas. Elas não podem ser regeneradas.",
        "flavor_text": "Um reset completo do campo de batalha.",
    },
    {
        "id": "birds-of-paradise",
        "name": "Birds of Paradise",
        "mana_cost": "{G}",
        "type_line": "Criatura — Ave",
        "rarity": "Rara",
        "set": "Fourth Edition",
        "release_date": "1995-04-01",
        "oracle_text": "Voar. {T}: Adicione uma mana de qualquer cor.",
        "flavor_text": "A aceleração de mana verde mais jogada da história.",
    },
    {
        "id": "tarmogoyf",
        "name": "Tarmogoyf",
        "mana_cost": "{1}{G}",
        "type_line": "Criatura — Lhama",
        "rarity": "Mítica",
        "set": "Modern Horizons",
        "release_date": "2019-06-14",
        "oracle_text": "Força e resistência de Tarmogoyf são iguais ao número de "
                        "tipos de carta entre os cemitérios, dividido em: instantânea, feitiço, "
                        "artefato, criatura, encantamento, terreno e planeswalker.",
        "flavor_text": "Cresce mais forte quanto mais tipos de carta existem nos cemitérios.",
    },
    {
        "id": "snapcaster-mage",
        "name": "Snapcaster Mage",
        "mana_cost": "{1}{U}",
        "type_line": "Criatura — Humano Mago",
        "rarity": "Mítica",
        "set": "Innistrad",
        "release_date": "2011-09-30",
        "oracle_text": "Flash. Quando Snapcaster Mage entra no campo de batalha, escolha "
                        "uma carta de instantânea ou feitiço em seu cemitério. Até o final "
                        "do turno, você pode conjurar aquela carta.",
        "flavor_text": "Reaproveita o melhor feitiço já jogado.",
    },
    {
        "id": "liliana-of-the-veil",
        "name": "Liliana of the Veil",
        "mana_cost": "{1}{B}{B}",
        "type_line": "Planeswalker — Liliana",
        "rarity": "Mítica",
        "set": "Innistrad",
        "release_date": "2011-09-30",
        "oracle_text": "+1: Cada jogador descarta uma carta. −2: Destrua a criatura alvo, "
                        "seu controlador a regenera. −6: Separe permanentes do campo de "
                        "batalha em dois grupos e cada oponente sacrifica um grupo.",
        "flavor_text": "Uma das planeswalkers mais dominantes do Modern.",
    },
    {
        "id": "jace-the-mind-sculptor",
        "name": "Jace, the Mind Sculptor",
        "mana_cost": "{2}{U}{U}",
        "type_line": "Planeswalker — Jace",
        "rarity": "Mítica",
        "set": "Worldwake",
        "release_date": "2010-02-05",
        "oracle_text": "+2: Vire a criatura alvo. +0: Compre uma carta, depois devolva uma "
                        "carta de sua mão ao topo do grimório. −1: Devolva a criatura alvo "
                        "ao topo do grimório de seu dono. −12: Exile todas as cartas do "
                        "grimório de um jogador, depois embaralhe o cemitério dele.",
        "flavor_text": "Considerado o planeswalker azul mais poderoso já impresso.",
    },
    {
        "id": "teferi-time-raveler",
        "name": "Teferi, Time Raveler",
        "mana_cost": "{1}{W}{U}",
        "type_line": "Planeswalker — Teferi",
        "rarity": "Mítica",
        "set": "War of the Spark",
        "release_date": "2019-05-03",
        "oracle_text": "Cada jogador pode conjurar mágicas apenas durante seu próprio turno. "
                        "+1: Até o próximo turno, permanentes que seus oponentes controlam "
                        "perdem todas as habilidades ativadas. −3: Devolva até uma carta que "
                        "não seja terreno alvo à mão de seu dono, depois compre uma carta.",
        "flavor_text": "Uma força tão dominante que foi banido em múltiplos formatos.",
    },
    {
        "id": "ragavan-nimble-pilferer",
        "name": "Ragavan, Nimble Pilferer",
        "mana_cost": "{R}",
        "type_line": "Criatura — Macaco Pirata",
        "rarity": "Mítica",
        "set": "Modern Horizons 2",
        "release_date": "2021-06-18",
        "oracle_text": "Golpe furtivo. Sempre que Ragavan causar dano de combate a um "
                        "jogador, crie um Tesouro e exile a carta do topo do grimório desse "
                        "jogador. Até o final do turno, você pode jogar a carta exilada.",
        "flavor_text": "O one-drop vermelho mais valioso do Modern moderno.",
    },
    {
        "id": "wrenn-and-six",
        "name": "Wrenn and Six",
        "mana_cost": "{R}{G}",
        "type_line": "Planeswalker — Wrenn",
        "rarity": "Mítica",
        "set": "Modern Horizons",
        "release_date": "2019-06-14",
        "oracle_text": "+1: Wrenn and Six causa 1 ponto de dano a uma criatura alvo. "
                        "−1: Devolva um terreno alvo do seu cemitério à sua mão. "
                        "−7: Emblema: sempre que um terreno entrar sob seu controle, cause 5 de dano a um alvo.",
        "flavor_text": "Um planeswalker compacto e extremamente eficiente.",
    },
    {
        "id": "fury",
        "name": "Fury",
        "mana_cost": "{1}{R}{R}",
        "type_line": "Criatura — Elemental Incarnação",
        "rarity": "Mítica",
        "set": "Modern Horizons 2",
        "release_date": "2021-06-18",
        "oracle_text": "Ímpeto. Você pode desprezar Fury sem pagar seu custo de mana "
                        "descartando-a se ela causar 2 pontos de dano divididos como "
                        "quiser entre uma ou duas criaturas e/ou planeswalkers alvo.",
        "flavor_text": "Uma das cinco Incarnações que redefiniram removedores gratuitos.",
    },
    {
        "id": "solitude",
        "name": "Solitude",
        "mana_cost": "{2}{W}{W}",
        "type_line": "Criatura — Elemental Incarnação",
        "rarity": "Mítica",
        "set": "Modern Horizons 2",
        "release_date": "2021-06-18",
        "oracle_text": "Voo. Você pode desprezar Solitude sem pagar seu custo de mana "
                        "exilando uma carta branca de sua mão. Quando Solitude entrar, "
                        "exile a criatura alvo. Seu controlador ganha vida igual à força dela.",
        "flavor_text": "Um Swords to Plowshares com corpo — e de graça.",
    },
    {
        "id": "grief",
        "name": "Grief",
        "mana_cost": "{2}{B}{B}",
        "type_line": "Criatura — Elemental Incarnação",
        "rarity": "Mítica",
        "set": "Modern Horizons 2",
        "release_date": "2021-06-18",
        "oracle_text": "Golpe furtivo. Você pode desprezar Grief sem pagar seu custo de mana "
                        "exilando uma carta preta de sua mão. Quando Grief entrar, um oponente "
                        "revela sua mão e você escolhe uma carta não-terreno dela; esse jogador descarta essa carta.",
        "flavor_text": "Arranca a resposta do oponente antes mesmo de ela existir.",
    },
    {
        "id": "subtlety",
        "name": "Subtlety",
        "mana_cost": "{1}{U}{U}",
        "type_line": "Criatura — Elemental Incarnação",
        "rarity": "Mítica",
        "set": "Modern Horizons 2",
        "release_date": "2021-06-18",
        "oracle_text": "Voo. Você pode desprezar Subtlety sem pagar seu custo de mana "
                        "exilando uma carta azul de sua mão. Quando Subtlety entrar, "
                        "vire a mágica alvo de um oponente e coloque-a no fundo do grimório do dono.",
        "flavor_text": "Protege seus planos enquanto atrapalha os do oponente.",
    },
    {
        "id": "endurance",
        "name": "Endurance",
        "mana_cost": "{2}{G}{G}",
        "type_line": "Criatura — Elemental Incarnação",
        "rarity": "Mítica",
        "set": "Modern Horizons 2",
        "release_date": "2021-06-18",
        "oracle_text": "Alcance. Você pode desprezar Endurance sem pagar seu custo de mana "
                        "exilando uma carta verde de sua mão. Quando Endurance entrar, "
                        "embaralhe até uma carta alvo do seu cemitério para seu grimório.",
        "flavor_text": "A resposta verde para estratégias de cemitério.",
    },
    {
        "id": "orcish-bowmasters",
        "name": "Orcish Bowmasters",
        "mana_cost": "{1}{B}",
        "type_line": "Criatura — Orc Arqueiro",
        "rarity": "Rara",
        "set": "Commander Masters",
        "release_date": "2023-08-04",
        "oracle_text": "Sempre que um oponente compra uma carta, exceto a primeira que "
                        "compra em cada turno dele, você pode criar um Duende com voo 1/1. "
                        "Se fizer isso, Orcish Bowmasters causa 1 ponto de dano a qualquer alvo.",
        "flavor_text": "Pune quem compra demais em um único turno.",
    },
    {
        "id": "atraxa-praetors-voice",
        "name": "Atraxa, Praetors' Voice",
        "mana_cost": "{G}{W}{U}{B}",
        "type_line": "Criatura — Anjo Praetor",
        "rarity": "Mítica",
        "set": "Commander 2016",
        "release_date": "2016-11-11",
        "oracle_text": "Voo, vigilância, ligação vital, contra-ataque. No início de sua "
                        "etapa final, coloque um marcador +1/+1, um marcador de lealdade, "
                        "um marcador de energia e um marcador de veneno em cada permanente alvo que você controla.",
        "flavor_text": "A anfitriã oficial de incontáveis decks de Commander.",
    },
]
