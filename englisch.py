"""Englische Texte für die Speisekarte – Wörterbücher kommen vom Laden (laeden/<id>/englisch.py)."""
import re

from konfig import EN_TEXTE as _T

NAMEN = getattr(_T, "NAMEN", {})
SAETZE = getattr(_T, "SAETZE", {})
WOERTER = getattr(_T, "WOERTER", {})
UEBERSCHRIFTEN = getattr(_T, "UEBERSCHRIFTEN", {})

def name(de):
    if de in NAMEN:
        return NAMEN[de]
    return de.replace(" mit Käse", " with cheese")


def text(de):
    if not de:
        return ""
    if de in SAETZE:
        return SAETZE[de]
    teile = [t.strip() for t in de.split(",")]
    aus = []
    for t in teile:
        m = re.match(r"(\d+) Stück$", t)
        if m:
            aus.append(f"{m.group(1)} pieces"); continue
        aus.append(WOERTER.get(t, t))
    s = ", ".join(aus)
    return s[:1].upper() + s[1:]


def titel(de):
    return UEBERSCHRIFTEN.get(de, de)
