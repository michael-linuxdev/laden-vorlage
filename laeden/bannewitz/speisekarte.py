# Speisekarte Feuerspieß Bannewitz – ERFUNDENER Beispiel-Laden für die Vorlage (Gerichte und Preise ausgedacht)
GRUNDSTAND = "01.10.2026"

GRUPPEN = [
    {
        "id": "doener", "titel": "Döner & Dürüm",
        "abschnitte": [
            {
                "titel": "Döner", "info": "im Fladenbrot vom Holzkohlegrill",
                "gerichte": [
                    ("1", "Döner", "Fladenbrot, Kalbfleisch, Salat, Soße", ["7,50"]),
                    ("2", "Döner mit Käse", "Fladenbrot, Kalbfleisch, Salat, Soße, Käse", ["8,50"]),
                    ("3", "Hähnchen-Döner", "Fladenbrot, Hähnchenfleisch, Salat, Soße", ["7,50"]),
                    ("4", "Hähnchen-Döner mit Käse", "Fladenbrot, Hähnchenfleisch, Salat, Soße, Käse", ["8,50"]),
                    ("5", "Halloumi-Döner vegetarisch", "Fladenbrot, gegrillter Halloumi, Salat, Soße", ["7,50"]),
                ],
            },
            {
                "titel": "Dürüm", "info": "in der Teigrolle",
                "gerichte": [
                    ("10", "Dürüm", "Teigrolle, Kalbfleisch, Salat, Soße", ["8,50"]),
                    ("11", "Dürüm mit Käse", "Teigrolle, Kalbfleisch, Salat, Soße, Käse", ["9,50"]),
                    ("12", "Hähnchen-Dürüm", "Teigrolle, Hähnchenfleisch, Salat, Soße", ["8,50"]),
                    ("13", "Hähnchen-Dürüm mit Käse", "Teigrolle, Hähnchenfleisch, Salat, Soße, Käse", ["9,50"]),
                ],
            },
        ],
    },
    {
        "id": "bowls", "titel": "Bowls", "icon": "bowl",
        "abschnitte": [
            {
                "titel": "Bowls", "info": "auf Reis mit Salat und Soße",
                "gerichte": [
                    ("20", "Döner-Bowl", "Reis, Kalbfleisch, Salat, Soße", ["10,00"]),
                    ("21", "Hähnchen-Bowl", "Reis, Hähnchenfleisch, Salat, Soße", ["10,00"]),
                    ("22", "Falafel-Bowl vegetarisch", "Reis, Falafel, Hummus, Salat, Soße", ["9,50"]),
                ],
            },
        ],
    },
    {
        "id": "grill", "titel": "Burger & Wurst", "icon": "burger",
        "abschnitte": [
            {
                "titel": "Burger", "info": "Brioche-Brötchen, mit Pommes",
                "gerichte": [
                    ("30", "Grill-Burger", "Rindfleisch, Salat, Tomate, Zwiebel, Burgersoße, Pommes", ["10,50"]),
                    ("31", "Cheeseburger", "Rindfleisch, Käse, Salat, Tomate, Burgersoße, Pommes", ["11,00"]),
                    ("32", "Chicken-Burger", "Hähnchenbrust, Salat, Tomate, Burgersoße, Pommes", ["10,50"]),
                ],
            },
            {
                "titel": "Currywurst & Pommes",
                "gerichte": [
                    ("40", "Currywurst mit Pommes", "", ["7,50"]),
                    ("41", "Pommes, klein", "", ["3,00"]),
                    ("42", "Pommes, groß", "", ["4,00"]),
                ],
            },
        ],
    },
    {
        "id": "getraenke", "titel": "Getränke",
        "abschnitte": [
            {
                "titel": "Getränke", "info": "zzgl. 0,25 € Pfand",
                "gerichte": [
                    ("", "Cola, Fanta oder Wasser", "0,5 l", ["2,50"]),
                    ("", "Ayran", "0,25 l", ["2,00"]),
                ],
            },
        ],
    },
]

ALLERGENE = {"a": "Weizen (Gluten)", "b": "Milch", "c": "Ei", "d": "Senf", "e": "Sesam", "f": "Sellerie"}
ALLERGENE_EN = {"a": "Wheat (gluten)", "b": "Milk", "c": "Egg", "d": "Mustard", "e": "Sesame", "f": "Celery"}
ZUTATEN = {"1": ("Currywurst", "mit Konservierungsstoff (Nitritpökelsalz), Geschmacksverstärker.")}
KENNZEICHNUNG = {
    "Döner": ("", "a,b,c,d,e"), "Dürüm": ("", "a,b,c,d"), "Bowls": ("", "b,c,d,e"),
    "Burger": ("", "a,b,c,d,e,f"), "Currywurst & Pommes": ("1", "d,f"),
}
SOSSEN = ("Knoblauch, Kräuter, Scharf", "", "b,c,d", "garlic, herbs, hot")
GERICHT_ALLERGENE = {}

VEGETARISCH = {"5", "22", "41", "42"}
FISCH = set()
VEG_WAEHLBAR = set()
