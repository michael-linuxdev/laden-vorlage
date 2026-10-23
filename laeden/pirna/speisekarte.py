# Speisekarte Pizzeria Fiamma Pirna – ERFUNDENER Beispiel-Laden für die Vorlage (Preise und Gerichte ausgedacht)
GRUNDSTAND = "01.10.2026"   # Preisstand der gedruckten Karte; in der Chef-App „Stand 01.10.2026“
# Format je Gericht: (Nr, Name, Beschreibung, [Preise]) – Preise als Text mit Komma; bei "groessen" ein Preis je Größe.

GRUPPEN = [
    {
        "id": "pizza", "titel": "Pizza",
        "abschnitte": [
            {
                "titel": "Pizza", "groessen": ["26 cm", "32 cm"], "info": "Steinofen, Teig 48 Stunden gereift",
                "gerichte": [
                    ("1", "Pizza Margherita", "Tomate, Mozzarella, Basilikum", ["7,50", "9,50"]),
                    ("2", "Pizza Salami", "Tomate, Mozzarella, Salami", ["8,50", "10,50"]),
                    ("3", "Pizza Prosciutto", "Tomate, Mozzarella, Schinken", ["8,50", "10,50"]),
                    ("4", "Pizza Funghi", "Tomate, Mozzarella, Champignon", ["8,50", "10,50"]),
                    ("5", "Pizza Tonno", "Tomate, Mozzarella, Thunfisch, Zwiebel", ["9,50", "11,50"]),
                    ("6", "Pizza Diavola", "Tomate, Mozzarella, scharfe Salami, Peperoni", ["9,50", "11,50"]),
                    ("7", "Pizza Vegetariana", "Tomate, Mozzarella, Paprika, Champignon, Zwiebel, Oliven", ["9,00", "11,00"]),
                    ("8", "Pizza Hawaii", "Tomate, Mozzarella, Schinken, Ananas", ["9,00", "11,00"]),
                    ("9", "Pizza Quattro Formaggi", "mit 4 verschiedenen Käsesorten", ["10,00", "12,00"]),
                    ("10", "Pizza Fiamma", "mit 3 Zutaten Ihrer Wahl", ["10,00", "12,00"]),
                    ("11", "Pizza Sächsische Schweiz", "Tomate, Mozzarella, Schinken, Champignon, Ei", ["10,50", "12,50"]),
                    ("12", "Calzone", "gefüllt mit Schinken, Salami, Champignon", ["10,50", "12,50"]),
                ],
            },
            {
                "titel": "Extras auf die Pizza", "info": "je Zutat",
                "gerichte": [
                    ("", "Paprika, Zwiebel, Champignon, Tomate, Peperoni, Ananas, Oliven, Rucola oder Mais", "", ["1,50"]),
                    ("", "Schinken, Salami oder Thunfisch", "", ["2,00"]),
                    ("", "Mozzarella, Gorgonzola oder Parmesan", "", ["2,00"]),
                ],
            },
        ],
    },
    {
        "id": "pasta", "titel": "Pasta",
        "abschnitte": [
            {
                "titel": "Pasta", "info": "frisch gekocht, auf Wunsch mit Parmesan",
                "gerichte": [
                    ("20", "Spaghetti Napoli", "Tomatensoße, Basilikum", ["8,50"]),
                    ("21", "Spaghetti Bolognese", "Rinderhack, Tomatensoße", ["9,50"]),
                    ("22", "Spaghetti Carbonara", "Speck, Ei, Parmesan", ["10,00"]),
                    ("23", "Penne all’Arrabbiata", "scharfe Tomatensoße, Knoblauch", ["9,00"]),
                    ("24", "Penne Spinaci", "Spinat, Sahne, Gorgonzola", ["9,50"]),
                    ("25", "Lasagne al forno", "Rinderhack, Béchamel, überbacken", ["11,00"]),
                ],
            },
        ],
    },
    {
        "id": "salate", "titel": "Salate",
        "abschnitte": [
            {
                "titel": "Salate", "info": "mit Hausdressing und Pizzabrot",
                "gerichte": [
                    ("30", "Insalata Mista", "Blattsalat, Tomate, Gurke, Paprika", ["7,00"]),
                    ("31", "Insalata Caprese", "Tomate, Mozzarella, Basilikum", ["8,50"]),
                    ("32", "Insalata Tonno", "Blattsalat, Thunfisch, Zwiebel, Ei", ["9,00"]),
                ],
            },
        ],
    },
    {
        "id": "dessert", "titel": "Dessert",
        "abschnitte": [
            {
                "titel": "Dessert",
                "gerichte": [
                    ("40", "Tiramisu", "hausgemacht", ["4,50"]),
                    ("41", "Panna Cotta", "mit Beerensoße", ["4,00"]),
                ],
            },
        ],
    },
    {
        "id": "getraenke", "titel": "Getränke",
        "abschnitte": [
            {
                "titel": "Kalte Getränke", "info": "zzgl. 0,25 € Pfand",
                "gerichte": [
                    ("", "Cola, Limonade oder Wasser", "0,33 l", ["2,50"]),
                    ("", "Apfelschorle", "0,33 l", ["2,50"]),
                ],
            },
            {
                "titel": "Heiße Getränke",
                "gerichte": [
                    ("", "Espresso", "", ["2,00"]),
                    ("", "Cappuccino", "", ["3,00"]),
                ],
            },
        ],
    },
]

# ---------- Zutaten und Allergene (Beispiel – bei einem echten Laden von der Karte abschreiben und bestätigen lassen) ----------
ALLERGENE = {"a": "Glutenhaltiges Getreide (Weizen)", "b": "Milch und Milcherzeugnisse", "c": "Eier", "d": "Fisch", "e": "Senf", "f": "Sellerie"}
ALLERGENE_EN = {"a": "Cereals containing gluten (wheat)", "b": "Milk and milk products", "c": "Eggs", "d": "Fish", "e": "Mustard", "f": "Celery"}
ZUTATEN = {
    "1": ("Salami", "mit Konservierungsstoff (Nitritpökelsalz) und Antioxidationsmittel."),
    "2": ("Schinken", "mit Konservierungsstoff (Nitritpökelsalz), Phosphat."),
}
KENNZEICHNUNG = {   # je Abschnitt: (Inhaltsstoffe, Allergene)
    "Pizza": ("1,2", "a,b"),
    "Extras auf die Pizza": ("1,2", "a,b"),
    "Pasta": ("", "a,b,c,f"),
    "Salate": ("", "a,e"),
    "Dessert": ("", "a,b,c"),
}
SOSSEN = None                         # keine Soßenwahl wie beim Döner
GERICHT_ALLERGENE = {"5": "d", "32": "c,d", "11": "c", "22": "c"}

VEGETARISCH = {"1", "4", "7", "9", "10", "20", "23", "24", "30", "31", "40", "41",
               "Paprika, Zwiebel, Champignon, Tomate, Peperoni, Ananas, Oliven, Rucola oder Mais", "Mozzarella, Gorgonzola oder Parmesan"}
FISCH = {"5", "32"}
VEG_WAEHLBAR = {"10"}
