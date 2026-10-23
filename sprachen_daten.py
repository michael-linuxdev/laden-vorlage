"""Weitere Sprachen der Seite. Je Sprache ein Wörterbuch Englisch -> Sprache in sprachen/<code>.json.

Die Seite schlägt jeden englischen Text nach; fehlt er, bleibt er Englisch. Zahlen im Text stehen im
Wörterbuch als {n} („{n} dishes found“), Platzhalter wie {zeit} oder {list} bleiben unübersetzt stehen.
Die Bestellung an den Laden bleibt immer deutsch. Liste der zu übersetzenden Texte: python3 sprachen_daten.py
"""
import json
import pathlib
import re

HIER = pathlib.Path(__file__).parent
LISTE = [["de", "Deutsch"], ["en", "English"], ["cs", "Čeština"], ["tr", "Türkçe"], ["ru", "Русский"], ["ar", "العربية"]]


# Texte, die der Code zusammensetzt (Zahlen als {n}, Platzhalter in geschweiften Klammern)
EXTRA = ["({ort} only)", "We would love a Google review for {name} {ort}.", " · waiting time approx. {n} min",
         "Busy right now: earliest pickup in about {n} minutes.", "{n} dishes are not available at the chosen time. Please change them above.",
         "choose {n} more toppings", "Closed, opens tomorrow at {zeit}", "Closed, opens on {tag} at {zeit}", "Closed, opens today at {zeit}",
         "Open now, until {zeit}", "{list} sauce", "no {list}", "with {list}", "option {x}", "extra {x}", "and", "not available", "fries", "rice",
         "no sauce", "choose option", "choose topping", "No.", "Train {n} → pickup {n}", "Closing soon – open until {zeit}", "Closing soon: last pickup today at {n}.", "Code {x} does not apply to this pickup.", "{x}: {p} % off", "Online orders paused until {zeit} – please call", "Your order at {name} {ort}", "Family & party boxes", "Box", "instead of ", "New", "Very busy right now: online orders for today are paused until {n}. Please call or pre-order for another day.", "You have already ordered {n} times at {name} {ort} – thank you!", "Order day: collect the order at {kurz}"]


def woerterbuecher():
    """Allgemeine Wörterbücher (sprachen/) plus die des Ladens (laeden/<id>/sprachen/, z. B. eigene Gerichte) – der Laden gewinnt."""
    import konfig
    aus = {}
    for code, _ in LISTE[2:]:
        aus[code] = {}
        for f in (HIER / "sprachen" / f"{code}.json", konfig.KARTE_ORDNER / "sprachen" / f"{code}.json", konfig.ORDNER / "sprachen" / f"{code}.json"):
            if f.exists():
                aus[code].update(json.loads(f.read_text(encoding="utf-8")))
    return aus


def texte():
    """Alle englischen Texte der fertigen Seite (docs/), die übersetzt werden."""
    import html
    import os
    seite = HIER / "docs" / os.environ.get("LADEN", "saray")
    h = (seite / "index.html").read_text(encoding="utf-8")
    j = (seite / "js" / "main.js").read_text(encoding="utf-8")
    t = set()
    for attr in ("data-en", "data-en-aria", "data-en-ph", "data-en-title", "data-nen", "data-dn", "data-en-html"):
        t |= {html.unescape(x) for x in re.findall(attr + r'="([^"]*)"', h)}
    for en in re.findall(r"L\('(?:[^'\\]|\\.)*','((?:[^'\\]|\\.)*)'\)", j):
        t.add(en.encode().decode("unicode_escape").encode("latin-1").decode("utf-8"))
    for en in re.findall(r"T\('((?:[^'\\]|\\.)*)'\)", j):
        t.add(en)
    w = re.search(r"var W=\{(.*?)\};", j, re.S)
    t |= set(re.findall(r":'([^']*)'", w.group(1)))
    t |= set(EXTRA)
    norm = {re.sub(r"\d+(?:[.,:]\d+)*", "{n}", x) if re.search(r"\d", x) and not x.startswith("No.") else x for x in t}
    norm = {x for x in norm if not re.match(r"^Add .+ to my order$", x)} | {"Add {x} to my order"}
    import konfig
    kurz = getattr(konfig.K, "KURZNAME", konfig.K.NAME)
    norm = {x.replace(konfig.K.NAME, "{name}").replace(kurz, "{kurz}") for x in norm}
    return sorted(x for x in norm if x.strip() and re.search(r"[A-Za-z]", x))


if __name__ == "__main__":
    for code, _ in LISTE[2:]:
        d = woerterbuecher()[code]
        fehlt = [x for x in texte() if x not in d]
        print(f"{code}: {len(fehlt)} fehlen")
