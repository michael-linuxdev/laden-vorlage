"""Feuerspieß Bannewitz – ERFUNDENER Beispiel-Laden: Döner, Bowls und Burger vom Grill.
Zeigt eigene Farben, eigenes Logo, eigene Karte und die Varianten-Schalter (Fleisch, Käse) mit anderen Gerichten.
"""

# ---------- Grunddaten ----------
NAME = "Feuerspieß"
PRAEFIX = "feuerspiess"
DOMAIN = "https://michael-linuxdev.github.io/laden-vorlage/bannewitz/"
VORSCHAU = True
VORSCHAU_URL = "https://michael-linuxdev.github.io/laden-vorlage/bannewitz/"
REPO = "michael-linuxdev/laden-vorlage"
ZAEHLER = ""
VORSCHAU_TEXT = ("Erfundener Beispiel-Laden – zeigt, was die Vorlage kann. Bestellungen gehen an eine Testnummer.",
                 "Made-up example shop – shows what the template can do. Orders go to a test number.")

STANDORTE = [
    {
        "id": "bannewitz", "name": "Bannewitz", "strasse": "Musterweg 3", "plz": "01728", "ort": "Bannewitz",
        "tel": "0160 1836249 (Test)", "tel_href": "+491601836249", "tel_ld": "+49 160 1836249",
        "bar": True,
        "google": "",
        "whatsapp": "491601836249",   # Testnummer
        "zeilen": [("Montag bis Samstag", "11–21 Uhr", [1, 2, 3, 4, 5, 6]), ("Sonntag", "12–20 Uhr", [0])],
        "zeilen_en": ["Monday to Saturday", "Sunday"], "extra_en": "Parking right in front of the shop.",
        "kurz": "Mo–Sa 11–21 Uhr, So 12–20 Uhr",
        "extra": "Parkplätze direkt vor dem Laden.",
        "lage": "an der Hauptstraße",
    },
]
ZUG = None

# ---------- Empfehlungen und Art der Gerichte ----------
EMPFEHLUNG = ["1", "20", "31", "5"]
BELIEBT = ["3", "10", "22", "40"]
NUR_DIAET = set()


def gericht_typ(nr, gruppe, abschnitt):
    """"D" Döner-artig: Soße wählen, „ohne …“, Fleisch/Käse wechseln. Burger und Wurst ohne Anpassen."""
    return "D" if gruppe in ("Döner & Dürüm", "Bowls") else ""


ANPASSEN = {
    "sossen": ["Knoblauch", "Kräuter", "Scharf"],
    "ohne": ["Zwiebeln", "Tomaten", "Gurken", "Rotkohl", "Salat"],
    "gemuese": [], "fleisch": [], "kaese": [], "belag": [], "pizza_woerter": [], "kaese_paare": [],
    "extra_gemuese": 150, "extra_fleisch": 200,
    "fuellungen": {"kalb": ["Kalbfleisch", "Veal"], "huhn": ["Hähnchen", "Chicken"], "halloumi": ["Halloumi", "Halloumi"], "falafel": ["Falafel", "Falafel"]},
    "fleisch_fuellungen": ["kalb", "huhn"], "fisch_fuellungen": [],
    "varianten": [
        ["1", "doener", "kalb", 0, 0], ["2", "doener", "kalb", 0, 1], ["3", "doener", "huhn", 0, 0], ["4", "doener", "huhn", 0, 1],
        ["5", "doener", "halloumi", 0, 0],
        ["10", "duerum", "kalb", 0, 0], ["11", "duerum", "kalb", 0, 1], ["12", "duerum", "huhn", 0, 0], ["13", "duerum", "huhn", 0, 1],
        ["20", "bowl", "kalb", 0, 0], ["21", "bowl", "huhn", 0, 0], ["22", "bowl", "falafel", 0, 0],
    ],
    "getraenk": {"gericht": "Cola, Fanta oder Wasser", "sorten": [["Cola", "Cola"], ["Fanta", "Fanta"], ["Wasser", "Water"]], "pfand": True},
}

# ---------- Texte ----------
KURZNAME = "Feuerspieß"
UNTERZEILE = ("Döner, Bowls & Burger", "Döner, bowls & burgers")
TITEL = "Feuerspieß Bannewitz – Döner, Bowls und Burger vom Grill (Beispiel)"
BESCHREIBUNG = "Erfundener Beispiel-Imbiss in Bannewitz: Döner, Dürüm, Bowls, Burger und Currywurst. Online vorbestellen und abholen."
OG_TITEL = "Feuerspieß Bannewitz (Beispiel)"
OG_TEXT = "Döner, Bowls und Burger vom Grill – online vorbestellen und abholen."
OG_ALT = "Feuerspieß: Grill-Imbiss in Bannewitz"
HELD = ("Vom Grill.<br> Für Bannewitz.", "From the grill.<br> For Bannewitz.")
EINLEITUNG = ("Döner, Bowls und Burger – frisch vom Holzkohlegrill. Online vorbestellen, Parkplatz vor der Tür.",
              "Döner, bowls and burgers – fresh from the charcoal grill. Pre-order online, parking right outside.")
KARTE_INFO = ("Alle Preise in Euro inkl. MwSt. Nur Abholung. Soße nach Wahl: Knoblauch, Kräuter oder Scharf.",
              "All prices in euros incl. VAT. Pickup only. Sauce of your choice: garlic, herb or hot.")
KARTE_GILT = None
ORTE_INTRO = None
GUTSCHEIN_TEXT = None
MOTTO = ("Heiß serviert, ehrlich gegrillt.", "Served hot, grilled honestly.")
GRUSS = '<span data-en="Enjoy your meal!">Guten Appetit!</span>'
STICKER = None

# ---------- Bilder ----------
LOGO = "logo.svg"
FIGUR = "figur.svg"
FOTO = None
FARBEN = {"gelb": "#FFB627", "gelb-blass": "#FFF1CF", "tinte": "#2B2D42", "tinte-weich": "#5C5F7A",
          "tinte-tief": "#1B1C2B", "paprika": "#E4572E", "gruen": "#2D6A4F"}
WINTER = None

# ---------- Rechtliches ----------
IMPRESSUM = """<p><b>Feuerspieß</b> – erfundener Beispiel-Laden, kein echtes Unternehmen.<br>
        Angaben zum Betreiber nach § 5 DDG stehen hier bei einem echten Laden.</p>"""
VERANTWORTLICH = """<p>Beispiel – bei einem echten Laden: Name, Anschrift, E-Mail des Inhabers.</p>"""

# ---------- Chef-App ----------
GOOGLE_TEXT = "Döner, Dürüm, Bowls, Burger und Currywurst – frisch vom Holzkohlegrill."
SPERR_REIHENFOLGE = ["huhn", "falafel", "halloumi", "doener", "bowls", "grill"]
ZUTATEN_SCHALTER = [
    ["Soßen", ["Knoblauch", "Kräuter", "Scharf"]],
    ["Salat und Gemüse", ["Salat", "Tomate", "Gurken", "Zwiebel", "Rotkohl"]],
    ["Beilagen", ["Pommes", "Reis"]],
]
CHECKLISTE = [
    ["Beispiel-Laden", [
        ["echt", "Erfundener Laden", "Diese Seite zeigt nur, was die Vorlage kann. Für einen echten Laden alles in laeden/bannewitz/ ersetzen.", 0],
        ["impressum", "Impressum und Datenschutz", "Angaben des Inhabers eintragen und vom Anwalt prüfen lassen.", 1],
        ["whatsapp", "WhatsApp-Nummer", "Bestellungen gehen an eine Testnummer.", 1],
    ]],
]

# ---------- Druck ----------
SEIT = ""
DRUCK_UNTERZEILE = "Döner · Bowls · Burger"
DRUCK_FUSS = "Alle Döner, Dürüm und Bowls mit Soße nach Wahl: Knoblauch, Kräuter, Scharf."
FLYER = {"innen": [["doener"], ["bowls"], ["grill"]], "klappe": ["getraenke"], "rueck": []}
ANGEBOT = {
    "de": "Döner, Bowls und Burger", "en": "Döner, bowls and burgers", "cs": "Döner, bowly a burgery",
    "tr": "Döner, bowl ve burgerler", "ru": "Дёнер, боулы и бургеры", "ar": "دونر وبول وبرغر",
}
