"""Saray Döner Altenberg – eigene Seite nur für Altenberg (mit Zugzeiten und Wintersaison).
Speisekarte und Bilder kommen von „saray“; Chef-App-Daten hat Altenberg für sich (laeden/altenberg/daten/).
"""
from konfig import basis

globals().update(basis("saray"))
SPEISEKARTE_VON = "saray"
BILDER_VON = "saray"

PRAEFIX = "sarayaltenberg"
KURZNAME = "Saray Altenberg"
VORSCHAU_URL = "https://michael-linuxdev.github.io/laden-vorlage/altenberg/"
STANDORTE = [s for s in STANDORTE if s["id"] == "altenberg"]
FOTO = None          # das Foto zeigt den Laden in Freital
STICKER = None

TITEL = "Saray Döner Altenberg – Döner und Pizza direkt am Bahnhof"
BESCHREIBUNG = ("Saray Döner in Altenberg, Dresdner Str. 23, direkt am Bahnhof: Döner, Dürüm, Pizza, Lahmacun und Salate. "
                "Vorbestellen und warm abholen – passend zum Zug.")
OG_TITEL = "Saray Döner Altenberg"
OG_TEXT = "Döner, Dürüm, Pizza und Salate direkt am Bahnhof. Vorbestellen und warm abholen."
HELD = ("Warm vom Spieß.<br> Direkt am Bahnhof.", "Hot off the skewer.<br> Right by the station.")
EINLEITUNG = ("Döner, Dürüm, Pizza und Salate in Altenberg – vorbestellen und passend zum Zug abholen.",
              "Döner, dürüm, pizza and salads in Altenberg – pre-order and pick up in time for your train.")
KARTE_GILT = None
ORTE_INTRO = None
GUTSCHEIN_TEXT = ("zum Geburtstag, zu Weihnachten oder als Dankeschön – an der Theke.",
                  "for birthdays, Christmas or as a thank-you – available at the counter.")

IMPRESSUM = """<p><b>Saray Döner Altenberg</b><br>Ahmet Saglam<br>Bahnhof 3<br>01773 Altenberg</p>
        <p>Telefon: <a href="tel:+493505623674">035056 23674</a><br>
        Telefax: 035056 23676<br>
        E-Mail: <a href="mailto:solino1@hotmail.de">solino1@hotmail.de</a></p>"""
VERANTWORTLICH = """<p>Ahmet Saglam, Saray Döner Altenberg, Bahnhof 3, 01773 Altenberg, Telefon 035056 23674, E-Mail solino1@hotmail.de.</p>"""

_WEG = {"wa-freital", "impressum-freital", "eine-oder-zwei", "betreiber"}
CHECKLISTE = [[g, [p for p in punkte if p[0] not in _WEG]] for g, punkte in CHECKLISTE]
