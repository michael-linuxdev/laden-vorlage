"""Pizzeria Fiamma Pirna – ERFUNDENER Beispiel-Laden. Zeigt, dass die Vorlage auch für eine Pizzeria taugt:
eigener Name, eigene Farben, eigenes Logo, andere Karte, nur ein Standort.

So legt man einen neuen Laden an: diesen Ordner kopieren (laeden/<neu>/), hier alles anpassen,
speisekarte.py und englisch.py ersetzen, Bilder mit  python3 bilder.py <neu>  erzeugen – fertig (siehe README).
"""

# ---------- Grunddaten ----------
NAME = "Pizzeria Fiamma"
PRAEFIX = "fiamma"                    # kurz, nur a–z, je Laden verschieden (Speicher im Browser, Benachrichtigungen)
DOMAIN = "https://michael-linuxdev.github.io/laden-vorlage/pirna/"   # endgültige Adresse (hier: Beispiel)
VORSCHAU = True
VORSCHAU_URL = "https://michael-linuxdev.github.io/laden-vorlage/pirna/"
REPO = "michael-linuxdev/laden-vorlage"
ZAEHLER = ""
VORSCHAU_TEXT = ("Erfundener Beispiel-Laden – zeigt, was die Vorlage kann. Bestellungen gehen an eine Testnummer.",
                 "Made-up example shop – shows what the template can do. Orders go to a test number.")

STANDORTE = [
    {
        "id": "pirna", "name": "Pirna", "strasse": "Beispielstraße 7", "plz": "01796", "ort": "Pirna",
        "tel": "0160 1836249 (Test)", "tel_href": "+491601836249", "tel_ld": "+49 160 1836249",
        "bar": False,                 # False: Karte und bar
        "google": "",                 # Google-Place-ID für „Bewerten“; leer = kein Bewertungslink
        "whatsapp": "491601836249",   # Testnummer
        "zeilen": [("Dienstag bis Sonntag", "11–22 Uhr", [2, 3, 4, 5, 6, 0])],   # Montag Ruhetag
        "zeilen_en": ["Tuesday to Sunday"], "extra_en": "Closed on Mondays. Terrace with a view of the old town.",
        "kurz": "Di–So 11–22 Uhr",
        "extra": "Montag Ruhetag. Terrasse mit Blick auf die Altstadt.",
        "lage": "in der Altstadt",
    },
]
ZUG = None                            # Abholung passend zum Zug: siehe laeden/saray/laden.py

# ---------- Empfehlungen und Art der Gerichte ----------
EMPFEHLUNG = ["1", "6", "10", "25"]
BELIEBT = ["2", "7", "22", "40"]
NUR_DIAET = set()


def gericht_typ(nr, gruppe, abschnitt):
    """"P" Pizza (Zutaten abwählen, Extras), "S" Pizza mit 3 Zutaten nach Wahl, "" ohne Anpassen."""
    if abschnitt == "Pizza":
        return "S" if nr == "10" else "P"
    return ""


ANPASSEN = {
    "sossen": [], "ohne": [],
    "gemuese": ["Paprika", "Zwiebel", "Champignon", "Tomate", "Peperoni", "Ananas", "Oliven", "Rucola", "Mais"],
    "fleisch": ["Schinken", "Salami", "Thunfisch"],
    "kaese": ["Mozzarella", "Gorgonzola", "Parmesan"],
    "extra_gemuese": 150, "extra_fleisch": 200,
    "belag": [],
    "pizza_woerter": [["thunfisch", "Thunfisch"], ["scharfe salami", "Salami"], ["salami", "Salami"], ["schinken", "Schinken"],
                      ["champignon", "Champignon"], ["paprika", "Paprika"], ["zwiebel", "Zwiebel"], ["oliven", "Oliven"],
                      ["ananas", "Ananas"], ["peperoni", "Peperoni"], ["basilikum", "Basilikum"], ["mozzarella", "Mozzarella"]],
    "kaese_paare": [], "fuellungen": {}, "fleisch_fuellungen": [], "fisch_fuellungen": [], "varianten": [],
    "getraenk": {"gericht": "Cola, Limonade oder Wasser", "sorten": [["Cola", "Cola"], ["Limonade", "Lemonade"], ["Wasser", "Water"]], "pfand": True},
}

# ---------- Texte (Deutsch, Englisch) ----------
KURZNAME = "Fiamma"
UNTERZEILE = ("Pizza aus dem Steinofen", "Stone-oven pizza")
TITEL = "Pizzeria Fiamma Pirna – Pizza aus dem Steinofen (Beispiel)"
BESCHREIBUNG = "Erfundene Beispiel-Pizzeria in Pirna: Pizza aus dem Steinofen, Pasta, Salate. Speisekarte, Öffnungszeiten, online vorbestellen."
OG_TITEL = "Pizzeria Fiamma Pirna (Beispiel)"
OG_TEXT = "Pizza aus dem Steinofen, Pasta und Salate – online vorbestellen und abholen."
OG_ALT = "Pizzeria Fiamma: Pizza aus dem Steinofen"
HELD = ("Aus dem Steinofen.<br> In Pirna.", "From the stone oven.<br> In Pirna.")
EINLEITUNG = ("Pizza, Pasta und Salate – frisch gemacht in der Altstadt von Pirna. Online vorbestellen und warm abholen.",
              "Pizza, pasta and salads – freshly made in Pirna’s old town. Pre-order online and pick up hot.")
KARTE_INFO = ("Alle Preise in Euro inkl. MwSt. Nur Abholung. Bezahlen bar oder mit Karte.",
              "All prices in euros incl. VAT. Pickup only. Pay cash or by card.")
KARTE_GILT = None
ORTE_INTRO = None
GUTSCHEIN_TEXT = ("zum Geburtstag oder als Dankeschön – an der Theke.", "for birthdays or as a thank-you – available at the counter.")
MOTTO = ("Langsam gereift, schnell gebacken.", "Slowly rested, quickly baked.")
GRUSS = '<span lang="it">Buon appetito</span> – <span data-en="enjoy your meal!">guten Appetit!</span>'
STICKER = ("Margherita", "1")

# ---------- Bilder (erzeugt mit  python3 bilder.py pirna) ----------
LOGO = "logo.svg"
FIGUR = "figur.svg"
FOTO = None
FARBEN = {"gelb": "#F4E4C1", "gelb-blass": "#FBF4E4", "tinte": "#1E4D2B", "tinte-weich": "#4E6E57",
          "tinte-tief": "#123220", "paprika": "#C0392B", "gruen": "#2E7D32"}

WINTER = None

# ---------- Rechtliches (HTML) ----------
IMPRESSUM = """<p><b>Pizzeria Fiamma</b> – erfundener Beispiel-Laden, kein echtes Unternehmen.<br>
        Angaben zum Betreiber nach § 5 DDG stehen hier bei einem echten Laden.</p>"""
VERANTWORTLICH = """<p>Beispiel – bei einem echten Laden: Name, Anschrift, E-Mail des Inhabers.</p>"""

# ---------- Chef-App ----------
GOOGLE_TEXT = "Pizza aus dem Steinofen, Pasta, Salate und Dessert – mitten in der Altstadt."
SPERR_REIHENFOLGE = ["pizza", "pasta", "salate", "dessert", "fisch"]
ZUTATEN_SCHALTER = [
    ["Gemüse", ["Paprika", "Zwiebel", "Champignon", "Tomate", "Peperoni", "Ananas", "Oliven", "Rucola", "Mais"]],
    ["Käse", ["Mozzarella", "Gorgonzola", "Parmesan"]],
    ["Fleisch und Fisch", ["Schinken", "Salami", "Thunfisch"]],
]
CHECKLISTE = [
    ["Beispiel-Laden", [
        ["echt", "Erfundener Laden", "Diese Seite zeigt nur, was die Vorlage kann. Für einen echten Laden alles in laeden/pirna/ ersetzen.", 0],
        ["impressum", "Impressum und Datenschutz", "Angaben des Inhabers eintragen und vom Anwalt prüfen lassen.", 1],
        ["whatsapp", "WhatsApp-Nummer", "Bestellungen gehen an eine Testnummer.", 1],
    ]],
]

# ---------- Druck ----------
SEIT = ""
DRUCK_UNTERZEILE = "Pizza · Pasta · Salate"
DRUCK_FUSS = "Alle Pizzen auch mit Extra-Zutaten."
FLYER = {"innen": [["pizza"], ["pasta"], ["salate", "dessert"]], "klappe": ["getraenke"], "rueck": []}
ANGEBOT = {
    "de": "Pizza, Pasta und Salate", "en": "Pizza, pasta and salads", "cs": "Pizza, těstoviny a saláty",
    "tr": "Pizza, makarna ve salatalar", "ru": "Пицца, паста и салаты", "ar": "بيتزا ومعكرونة وسلطات",
}
