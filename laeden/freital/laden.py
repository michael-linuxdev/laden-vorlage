"""Saray Döner Freital – eigene Seite nur für Freital. Alles wie beim Referenz-Laden „saray“, nur ein Standort.
Speisekarte und Bilder kommen von „saray“; Chef-App-Daten (Preise, Zeiten, Sperren) hat Freital für sich (laeden/freital/daten/).
"""
from konfig import basis

globals().update(basis("saray"))
SPEISEKARTE_VON = "saray"
BILDER_VON = "saray"

PRAEFIX = "sarayfreital"
KURZNAME = "Saray Freital"
VORSCHAU_URL = "https://michael-linuxdev.github.io/laden-vorlage/freital/"
STANDORTE = [s for s in STANDORTE if s["id"] == "freital"]
ZUG = None
WINTER = None

TITEL = "Saray Döner Freital – Döner, Pizza und Salate seit 1997"
BESCHREIBUNG = ("Saray Döner in Freital, Dresdner Str. 87: Döner, Dürüm, Pizza, Lahmacun und Salate. "
                "Speisekarte mit Preisen, Öffnungszeiten, online vorbestellen und abholen.")
OG_TITEL = "Saray Döner Freital"
EINLEITUNG = ("Döner, Dürüm, Pizza und Salate – in Freital an der Dresdner Straße, Ecke Turnerstraße.",
              "Döner, dürüm, pizza and salads – in Freital on Dresdner Straße, corner of Turnerstraße.")
KARTE_GILT = None
ORTE_INTRO = None
GUTSCHEIN_TEXT = ("zum Geburtstag, zu Weihnachten oder als Dankeschön – an der Theke.",
                  "for birthdays, Christmas or as a thank-you – available at the counter.")

IMPRESSUM = """<p><b>Saray Döner Freital</b><br><span class="platzhalter">[Inhaber Khan – vollständiger Name, Anschrift, E-Mail, ggf. Firmenform und USt-IdNr.]</span><br>Dresdner Str. 87<br>01705 Freital<br>
        Telefon: <a href="tel:+4935127676660">0351 27676660</a></p>"""
VERANTWORTLICH = """<p><span class="platzhalter">[Khan – Name, Anschrift, E-Mail]</span>, Saray Döner Freital, Dresdner Str. 87, 01705 Freital, Telefon 0351 27676660.</p>"""

_WEG = {"wa-altenberg", "impressum", "zeiten-altenberg", "fahrplan", "eine-oder-zwei", "betreiber"}
CHECKLISTE = [[g, [p for p in punkte if p[0] not in _WEG]] for g, punkte in CHECKLISTE]
