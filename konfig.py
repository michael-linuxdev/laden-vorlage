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
