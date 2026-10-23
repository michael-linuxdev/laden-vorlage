"""Saray Döner – Referenz-Laden der Vorlage (beide Läden auf einer Seite, wie saray-doener).
Alle Tests laufen gegen diesen Laden. Neue Läden: Ordner kopieren und hier alles anpassen (siehe README).
"""

# ---------- Grunddaten ----------
NAME = "Saray Döner"                  # Name des Ladens (Kopf, Titel, Nachrichten, Druck)
PRAEFIX = "saray"                     # kurz, nur a–z: Schlüssel im Browser-Speicher, Benachrichtigungen – je Laden verschieden!
DOMAIN = "https://xn--saraydner-57a.de/"   # endgültige Adresse (saraydöner.de), Canonical für Google
VORSCHAU = True                       # True: Entwurf – Suchmaschinen sperren, „ENTWURF“-Streifen
VORSCHAU_URL = "https://michael-linuxdev.github.io/laden-vorlage/saray/"   # wo die Seite jetzt erreichbar ist (QR-Codes, Vorschaubild)
REPO = "michael-linuxdev/laden-vorlage"    # Chef-App speichert in diesem Repo (laeden/<id>/daten/anpassungen.json)
ZAEHLER = ""                          # GoatCounter-Kürzel; leer = kein Zählen

STANDORTE = [
    {
        "id": "freital", "name": "Freital", "strasse": "Dresdner Str. 87", "plz": "01705", "ort": "Freital",
        "tel": "0351 27676660", "tel_href": "+4935127676660", "tel_ld": "+49 351 27676660",
        "bar": True,  # nur Barzahlung
        "google": "ChIJi62UlB_FCUcRyZITkeCfe8Q",  # Google-Place-ID (Bewertungslink)
        "whatsapp": "491601836249",  # Vorlage: Testnummer (Michael); leer: Knopf ausgeblendet
        "zeilen": [("Montag bis Freitag", "10–22 Uhr", [1, 2, 3, 4, 5]), ("Samstag und Sonntag", "11–22 Uhr", [6, 0])],
        "zeilen_en": ["Monday to Friday", "Saturday and Sunday"], "extra_en": "Outdoor seating in good weather.",
        "kurz": "Mo–Fr 10–22 Uhr, Sa–So 11–22 Uhr",
        "extra": "Bei schönem Wetter sitzen Sie draußen.",
        "lage": "an der Dresdner Straße",
    },
    {
        "id": "altenberg", "name": "Altenberg", "strasse": "Dresdner Str. 23", "plz": "01773", "ort": "Altenberg",
        "tel": "035056 23674", "tel_href": "+493505623674", "tel_ld": "+49 35056 23674",
        "bar": True,
        "google": "ChIJ7XWZiUmTCUcRxe2o2WmxkxQ",
        "whatsapp": "491601836249",  # Testnummer (Michael)
        "zeilen": [("Montag bis Samstag", "10–21 Uhr", [1, 2, 3, 4, 5, 6]), ("Sonntag", "11–21 Uhr", [0])],
        "zeilen_en": ["Monday to Saturday", "Sunday"], "extra_en": "Right by the station.",
        "kurz": "Mo–Sa 10–21 Uhr, So 11–21 Uhr",
        "extra": "Direkt am Bahnhof.",
        "lage": "direkt am Bahnhof",
    },
]


# Zug ab Altenberg (Müglitztalbahn RB 72 / RE 19 Richtung Heidenau–Dresden): Abholung passend zur Abfahrt.
# Quelle: DB-Kursbuch 246, gültig 14.12.2025–12.12.2026 (Stand 24.10.2025). Nach "gueltig_bis" blendet sich der
# Vorschlag von selbst aus, bis der neue Fahrplan hier eingetragen ist. Feiertage = Tage in "werktags_nicht".
ZUG = {
    "laden": "altenberg", "gueltig_bis": "2026-12-12", "puffer": 15,
    "taeglich": ["06:18", "08:18", "10:18", "12:18", "18:18", "20:18"],
    "werktags": ["04:18", "05:18", "07:18", "09:18", "11:18", "13:18", "14:18", "15:18", "16:18", "17:18", "19:18", "21:18"],
    "werktags_nicht": ["2025-12-25", "2025-12-26", "2026-01-01", "2026-04-03", "2026-04-06", "2026-05-01", "2026-05-14",
                       "2026-05-25", "2026-11-18"],
    "extra": [  # RE 19 nur am Wochenende in diesen Zeiträumen, dazu an einzelnen Tagen
        {"zeit": "15:18", "wochenende": [["2025-12-14", "2026-02-22"], ["2026-11-07", "2026-12-12"]],
         "auch": ["2025-12-25", "2025-12-26", "2026-01-01", "2026-11-18"]},
        {"zeit": "17:18", "wochenende": [["2026-02-28", "2026-11-01"]],
         "auch": ["2026-04-03", "2026-04-06", "2026-05-01", "2026-05-14", "2026-05-25"]},
    ],
}


# ---------- Empfehlungen und Art der Gerichte (für „Anpassen“ im Bestellzettel) ----------
EMPFEHLUNG = ["87", "1", "3", "26", "91", "125"]   # „Wir empfehlen“: alle gleich groß, ohne Koch
BELIEBT = ["52", "5", "58", "24", "84", "50", "23", "130", "100", "105", "124"]
# nur sichtbar, wenn „Vegetarisch“ oder „Pescetarisch“ eingeschaltet ist (Döner vegetarisch statt Döner Kebap usw.);
# Fischgerichte darunter (Pizza Tonno) erscheinen nur bei „Pescetarisch“
NUR_DIAET = {"87", "3", "52", "5", "58", "24", "84"}   # Reihenfolge wie vom Inhaber gewünscht; 23 = Döner-Teller mit Salat und Pommes


D_NR = {"18", "19", "60", "61", "121", "123", "124"}


def gericht_typ(nr, gruppe, abschnitt):
    if abschnitt == "Pizza":
        return {"91": "S", "105": "R"}.get(nr, "P")
    if nr and (gruppe in ("Döner", "Dürüm") or abschnitt in ("Dönerbox", "Dönerteller") or nr in D_NR):
        return "D"
    if gruppe == "Salate":
        return "SA"
    if abschnitt == "Pizzabrötchen":
        return "B"
    return ""
