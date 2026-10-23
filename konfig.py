"""Welcher Laden wird gebaut? Lädt dessen Konfiguration aus laeden/<id>/.

    LADEN=freital python3 build.py      (ohne LADEN: der Referenz-Laden „saray“)

Jeder Laden hat einen Ordner laeden/<id>/ mit
    laden.py          Name, Standorte, Farben, Texte, Schalter (siehe laeden/saray/laden.py, alles kommentiert)
    speisekarte.py    Gerichte, Preise, Allergene      (oder SPEISEKARTE_VON = "<anderer Laden>")
    englisch.py       englische Namen der Gerichte      (gehört zur Speisekarte)
    bilder/           Foto, Logo, Karten-Ausschnitte    (oder BILDER_VON = "<anderer Laden>")
    daten/            anpassungen.json und fotos/ – schreibt die Chef-App dieses Ladens
"""
import importlib.util
import os
import pathlib
import re

HIER = pathlib.Path(__file__).parent
ID = os.environ.get("LADEN", "saray")
ORDNER = HIER / "laeden" / ID
if not (ORDNER / "laden.py").exists():
    raise SystemExit(f"Laden „{ID}“ gibt es nicht (erwartet: {ORDNER / 'laden.py'})")


def _modul(name, pfad):
    spec = importlib.util.spec_from_file_location(name, pfad)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def basis(laden_id):
    """Einstellungen eines anderen Ladens als Grundlage (für Filialen): globals().update(basis("saray"))"""
    m = _modul(f"basis_{laden_id}", HIER / "laeden" / laden_id / "laden.py")
    return {k: v for k, v in vars(m).items() if not k.startswith("__")}


K = _modul("laden_konfig", ORDNER / "laden.py")
KARTE_ORDNER = HIER / "laeden" / getattr(K, "SPEISEKARTE_VON", ID)
BILDER = HIER / "laeden" / getattr(K, "BILDER_VON", ID) / "bilder"
DATEN = ORDNER / "daten"
menu = _modul("speisekarte", KARTE_ORDNER / "speisekarte.py")
EN_TEXTE = _modul("englisch_texte", KARTE_ORDNER / "englisch.py")


def rel(pfad):
    """Pfad relativ zum Repo (für die Chef-App, die über die GitHub-API schreibt)."""
    return pathlib.Path(pfad).relative_to(HIER).as_posix()


def alle():
    """Alle Läden (Ordner mit laden.py), Referenz-Laden zuerst."""
    ids = sorted(p.parent.name for p in (HIER / "laeden").glob("*/laden.py"))
    return sorted(ids, key=lambda i: (i != "saray", i))


# Farben: Code und Vorlagen benutzen die Saray-Farben; ein Laden mit FARBEN = {...} bekommt sie beim Bauen ersetzt
STANDARD_FARBEN = {"gelb": "#FFD21F", "gelb-blass": "#FFF3C2", "tinte": "#3A1531", "tinte-weich": "#6B4A62",
                   "tinte-tief": "#2A0E23", "paprika": "#C8371A", "gruen": "#1E7B3C"}


def _rgb(h):
    h = h.lstrip("#")
    return ",".join(str(int(h[i:i + 2], 16)) for i in (0, 2, 4))


def farben(text):
    """Ersetzt die Standardfarben (#RRGGBB, %23RRGGBB in data:-Adressen, rgba(r,g,b,…)) durch die des Ladens."""
    eigene = getattr(K, "FARBEN", None) or {}
    paare = {}
    for name, alt in STANDARD_FARBEN.items():
        neu = eigene.get(name)
        if neu and neu.lower() != alt.lower():
            paare[alt.lower()] = neu
            paare["%23" + alt[1:].lower()] = "%23" + neu[1:]
            paare["rgba(" + _rgb(alt) + ","] = "rgba(" + _rgb(neu) + ","
    if not paare:
        return text
    muster = re.compile("|".join(re.escape(k) for k in sorted(paare, key=len, reverse=True)), re.I)
    return muster.sub(lambda m: paare[m.group(0).lower()], text)
