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
        "karte_alt": "Stadtplan Freital-Potschappel: Saray Döner an der Dresdner Straße, Ecke Turnerstraße",   # bilder/karte_<id>.webp
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
        "karte_alt": "Stadtplan Altenberg: Saray Döner an der Dresdner Straße am Bahnhof",
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


# ---------- Texte (Deutsch, Englisch); weitere Sprachen: laeden/<id>/sprachen/<code>.json (Englisch -> Sprache) ----------
KURZNAME = "Saray"                    # kurz: App-Name auf dem Handy, „Saray auf den Home-Bildschirm“
UNTERZEILE = ("Döner & Pizza seit 1997", "Döner & pizza since 1997")       # unter dem Namen im Kopf
TITEL = "Saray Döner Freital & Altenberg – Döner, Pizza und Salate seit 1997"   # Titel im Browser und bei Google
BESCHREIBUNG = ("Saray Döner in Freital (Dresdner Str. 87) und Altenberg (Dresdner Str. 23): Döner, Dürüm, Pizza, Lahmacun und Salate. "
                "Speisekarte mit Preisen, Öffnungszeiten und Telefonnummern.")
OG_TITEL = "Saray Döner – Freital & Altenberg"                              # Vorschau beim Teilen (WhatsApp, Facebook)
OG_TEXT = "Döner, Dürüm, Pizza und Salate seit 1997. Speisekarte, Öffnungszeiten und Telefon."
OG_ALT = "Saray Döner: Laden in Freital mit dem Koch-Maskottchen – Frisch vom Spieß seit 1997"
HELD = ("Frisch vom Spieß.<br> Seit 1997.", "Fresh off the skewer.<br> Since 1997.")   # große Überschrift oben (HTML erlaubt: <br>)
EINLEITUNG = ("Döner, Dürüm, Pizza und Salate – in Freital an der Dresdner Straße und in Altenberg direkt am Bahnhof.",
              "Döner, dürüm, pizza and salads – in Freital on Dresdner Straße and in Altenberg right by the station.")
KARTE_INFO = ("Alle Preise in Euro inkl. MwSt. Nur Abholung, keine Liefer- oder Versandkosten. Zu jedem Gericht gibt es Soße nach Wahl: Knoblauch, Kräuter oder Chili.",
              "All prices in euros incl. VAT. Pickup only, no delivery or shipping costs. Every dish comes with your choice of sauce: garlic, herb or chili.")
KARTE_GILT = ("Die Karte gilt in Freital und Altenberg.", "The menu applies in Freital and Altenberg.")   # nur bei mehreren Standorten; None = weglassen
ORTE_INTRO = ("Zweimal Saray: in Freital und in Altenberg.", "Two Saray shops: in Freital and in Altenberg.")   # über den Standorten; None = weglassen
GUTSCHEIN_TEXT = ("zum Geburtstag, zu Weihnachten oder als Dankeschön – an der Theke in beiden Läden.",
                  "for birthdays, Christmas or as a thank-you – available at the counter in both shops.")   # None = kein Hinweis
MOTTO = ("Qualität ist kein Zufall.", "Quality is no accident.")              # im Fuß; None = weglassen
GRUSS = '<span lang="tr">Afiyet olsun</span> – <span data-en="enjoy your meal!">guten Appetit!</span>'   # im Fuß (HTML); "" = weglassen
STICKER = ("Döner Kebap", "1")        # runder Aufkleber am Foto: Beschriftung und Nummer des Gerichts, dessen Preis er zeigt; None = keiner

# ---------- Bilder (laeden/<id>/bilder/ und laeden/<id>/maskottchen/) ----------
LOGO = "saray-koch-kopf.svg"          # rundes Logo (Kopf, Fuß, Druck) – in maskottchen/
FIGUR = "saray-koch.svg"              # ganze Figur neben der Überschrift; None = keine
FOTO = ("laden_web.webp", "laden_480.webp", "Der Laden von außen: Eckhaus mit grünen Schildern, davor Tische und bunte Stühle.")   # None = kein Foto
FARBEN = {}                           # z. B. {"gelb": "#FFD21F", "tinte": "#3A1531", "paprika": "#C8371A"} – leer = Saray-Farben

# ---------- Wintersaison (Kasten oben, nur in diesen Monaten bzw. per Chef-App) ----------
WINTER = {
    "laden": "altenberg",
    "titel": ("Nach der Piste in Altenberg", "After the slopes in Altenberg"),
    "text": ("Vorbestellen und warm abholen – direkt am Bahnhof. Mit dem Zug zurück? Wir richten die Abholung nach der Abfahrt.",
             "Pre-order and pick up hot – right by the station. Taking the train back? We time your pickup to the departure."),
    "knopf": ("In Altenberg vorbestellen", "Pre-order in Altenberg"),
}

# ---------- Rechtliches (HTML) ----------
IMPRESSUM = """<p><b>Saray Döner Freital</b><br><span class="platzhalter">[Inhaber Khan – vollständiger Name, Anschrift, E-Mail, ggf. Firmenform und USt-IdNr.]</span><br>Dresdner Str. 87<br>01705 Freital<br>
        Telefon: <a href="tel:+4935127676660">0351 27676660</a></p>
        <p><b>Saray Döner Altenberg</b><br>Ahmet Saglam<br>Bahnhof 3<br>01773 Altenberg</p>
        <p>Telefon: <a href="tel:+493505623674">035056 23674</a><br>
        Telefax: 035056 23676<br>
        E-Mail: <a href="mailto:solino1@hotmail.de">solino1@hotmail.de</a></p>"""
VERANTWORTLICH = """<p>Für Saray Döner Freital: <span class="platzhalter">[Khan – Name, Anschrift, E-Mail]</span>, Dresdner Str. 87, 01705 Freital, Telefon 0351 27676660.
        Für Saray Döner Altenberg: Ahmet Saglam, Bahnhof 3, 01773 Altenberg, Telefon 035056 23674, E-Mail solino1@hotmail.de.
        <span class="platzhalter">[Klären: Betreiben beide die Website gemeinsam (dann gemeinsam Verantwortliche nach Art. 26 DSGVO mit Vereinbarung) oder jeder für seinen Laden?]</span></p>"""


# ---------- Chef-App ----------
# Google-Unternehmensprofil: Beschreibung nach „<Name> in <Ort> – “
GOOGLE_TEXT = ("seit 1997 Döner, Dürüm, Pizza, Lahmacun, Salate und Teller. "
               "Dönerfleisch aus Kalb und Pute, Hähnchen-Döner, viele vegetarische Gerichte mit Falafel und Halloumi.")
# Reihenfolge der Kärtchen „Was gibt es heute nicht?“ (Kennungen aus den Sperrgruppen); leer = alle Kategorien
SPERR_REIHENFOLGE = ["huhn", "nuggets", "falafel", "halloumi", "schnitzel-fleisch", "fisch",
                     "doener", "duerum", "teller", "pizza", "lahmacun", "baguette", "salate", "kinder"]
# Zutaten, die der Inhaber einzeln ausschalten kann (Namen wie auf der Seite; „Zwiebel“ gilt auch für „Zwiebeln“).
# Pommes/Reis: Gerichte gibt es dann ohne diese Beilage, je 0,50 € günstiger (BEILAGEN in build.py)
ZUTATEN_SCHALTER = [
    ["Soßen", ["Knoblauch", "Kräuter", "Chili"]],
    ["Salat und Gemüse", ["Eisbergsalat", "Tomate", "Gurken", "Zwiebel", "Rotkohl", "Weißkohl", "Paprika", "Champignon",
                          "Peperoni", "Ananas", "Oliven", "Brokkoli", "Mais"]],
    ["Beilagen", ["Pommes", "Reis"]],
    ["Käse", ["Käse", "Halloumikäse", "Fetakäse", "Mozzarella"]],
    ["Fleisch, Fisch, Ei", ["Dönerfleisch", "Hähnchen-Dönerfleisch", "Schinken", "Salami", "Thunfisch", "Ei"]],
]


# Offene Punkte vor dem Freischalten: [Gruppe, [[id, Text, Hinweis, muss]]]
CHECKLISTE = [
    ["Freischalten", [
        ["domain", "Domain saraydöner.de", "Wer hat Zugang zu Domain und DNS? Wo liegt die alte Seite?", 1],
        ["wa-freital", "WhatsApp Freital", "Vorerst gehen Bestellungen an Khans privates Handy (01573 3729521). Später durch das Laden-Handy ersetzen – welche Nummer?", 1],
        ["wa-altenberg", "WhatsApp Altenberg", "Welche Nummer nimmt Bestellungen an?", 1],
        ["wa-wer", "Wer bestätigt die Bestellungen?", "Wer schaut während der Öffnungszeiten aufs Handy und antwortet?", 1],
        ["impressum", "Impressum Altenberg (Ahmet)", "Anschrift (Bahnhof 3 oder Dresdner Str. 23?), Firmenform, USt-IdNr. (falls vorhanden), E-Mail. Mehr als 10 Beschäftigte? Dann Hinweis zur Verbraucherschlichtung (§ 36 VSBG) nötig.", 1],
        ["impressum-freital", "Impressum Freital (Khan)", "Vollständiger Name, Anschrift, E-Mail, Firmenform, USt-IdNr. (falls vorhanden), Beschäftigtenzahl (§ 36 VSBG).", 1],
        ["betreiber", "Wer betreibt die Website?", "Beide gemeinsam (dann Vereinbarung als gemeinsam Verantwortliche, Art. 26 DSGVO) oder jeder für seinen Laden?", 1],
        ["eine-oder-zwei", "Eine Website oder zwei?", "Eine gemeinsame Seite für Freital und Altenberg (so wie jetzt) oder je Laden eine eigene Seite mit eigener Adresse, eigenem Impressum und eigener Chef-App?", 1],
        ["uebersetzungen", "Übersetzungen gegenlesen lassen", "Tschechisch, Türkisch, Russisch und Arabisch sind maschinennah übersetzt. Je eine Person mit der Muttersprache kurz drüberschauen lassen (Seite → Sprache wählen).", 0],
        ["allergene", "Allergene ergänzen und bestätigen", "Neu: h = Fisch (Nr. 71, 87, 97, 136, 154) und i = Ei in der Soße. Es fehlen noch Angaben für Extra-Portion, Fladenbrot und die Milchgetränke (Kaffee mit Milch, Kakao).", 1],
        ["goatcounter-av", "Besucherzählung: Auftragsverarbeitung", "Mit GoatCounter einen Vertrag zur Auftragsverarbeitung klären (oder Zählung abschalten).", 0],
        ["zeiten-altenberg", "Öffnungszeiten Altenberg samstags", "Ab 10 oder ab 11 Uhr? Google zeigt 11 Uhr.", 0],
        ["feiertage", "Feiertage", "Freital 11–22 Uhr, Altenberg? Reformationstag 31.10., Buß- und Bettag 18.11.", 0],
        ["preise", "Preise der Karte", "Gilt die Karte vom 01.02.2024 noch? In beiden Läden gleich?", 0],
        ["datenschutz", "Datenschutzerklärung vom Anwalt prüfen lassen", "Entwurf steht. Vor dem Freischalten von einem Anwalt prüfen lassen – mit Impressum und gemeinsamer Verantwortung beider Inhaber.", 1],
        ["logo", "Echtes Logo", "Original-Logo von Saray Döner als Datei (am besten SVG oder PDF, sonst großes PNG) – auch für Flyer und Aufsteller", 1],
        ["maskottchen", "Original-Maskottchen", "Den echten Saray-Koch als Datei; ersetzt die nachgezeichnete Figur auf Seite, App-Symbol und Druck", 1],
    ]],
    ["Chef-App und Abläufe", [
        ["einweisung", "Einweisung", "Heute aus, Zutaten, Wartezeit, besondere Tage, Aktionen, Hinweis, Drucken, Rückgängig", 0],
        ["gruppen-vorlauf", "Größere Bestellungen", "Ab wie vielen Portionen wie viel Vorlauf? Zum Beispiel „ab 10 Portionen am Vortag bestellen“. Kommt auf die Seite und den Gruppen-Flyer.", 0],
        ["vorbestellung", "Vorbestellung", "Bis 14 Tage im Voraus, frühestens 20 Minuten nach der Bestellung – passt das?", 0],
        ["beilage", "Pommes oder Reis aus = 0,50 € weniger", "So in Ordnung?", 0],
        ["zahlung", "Nur Barzahlung", "Kommt irgendwann Kartenzahlung dazu?", 0],
        ["aktion", "Erste Sonderaktion", "Zum Beispiel Mittagsangebot oder „Döner 5 €“", 0],
        ["druck", "Flyer und Aufsteller", "Probedruck ansehen, Anzahl, selbst drucken oder Druckerei?", 0],
        ["bildschirm", "Bildschirm im Laden", "Fernseher mit HDMI und Fire-TV-Stick (ca. 40 €), Adresse unter Mehr → Bildschirm im Laden als Startseite einstellen.", 0],
        ["kueche", "Küchenansicht", "Auf welchem Gerät im Laden öffnen wir die Bestellungen? Bondrucker gewünscht (ca. 40 €)?", 0],
        ["gutscheine", "Geschenkgutscheine", "Welche Werte? Restbetrag als neuer Gutschein? Gültig 3 Jahre bis Jahresende (gesetzlich).", 0],
        ["whatsapp-business", "WhatsApp Business einrichten", "Begrüßung, Abwesenheitsnachricht und Schnellantworten auf dem Laden-Handy – fertige Texte (Deutsch und Türkisch) unter Mehr → WhatsApp-Antworten zum Kopieren.", 0],
        ["slots", "Vorbestellungen je Viertelstunde", "Wie viele Vorbestellungen schafft die Küche pro Viertelstunde? Eingestellt sind 5 je Laden (Zeiten → Vorbestellungen je Viertelstunde). Ist die Zahl erreicht, sperrt die Küchenansicht die Zeit online – dafür braucht das Küchen-Gerät den Chef-App-Zugang.", 0],
        ["ton", "„Abholbereit per Ton“", "Drückt die Küche „Fertig ✓“, hört der Gast einen Ton, wenn die Seite offen ist. Läuft über den Dienst ntfy.sh – mit in die Prüfung der Datenschutzerklärung nehmen. Später auch auf eigenem Server möglich.", 0],
        ["fahrplan", "Zugzeiten Altenberg", "Die Abfahrten gelten bis 12.12.2026. Danach trägt Michael den neuen Fahrplan ein.", 0],
    ]],
    ["Google und Fotos", [
        ["google", "Google-Unternehmensprofil", "Verwaltungszugriff, Link zur Seite, Zeiten angleichen, Barzahlung eintragen", 0],
        ["fotos", "Fotos der Gerichte", "Dürfen wir Fotos machen? Wann passt es?", 0],
    ]],
    ["Ideen für später", [
        ["stammkarte", "Stammkarte digital", "Nach 10 Bestellungen über die Seite ein Getränk gratis – ohne Konto, gezählt auf dem Handy des Gastes; die Küchenansicht zeigt „10. Bestellung – Getränk gratis“. Machen wir das?", 0],
        ["gericht-des-tages", "Gericht des Tages automatisch", "Jeden Tag ein anderes Gericht aus einer festen Liste oben auf der Seite, mit kleinem Rabatt – ohne tägliches Einstellen.", 0],
        ["ohne-besteck", "Ohne Besteck, ohne Tüte", "Zwei Häkchen im Bestellzettel; spart Material, die Küche sieht es auf dem Bon.", 0],
        ["vorlauf-auto", "Vorlauf bei großen Bestellungen automatisch", "Ab z. B. 10 Gerichten bietet der Bestellzettel nur Abholzeiten mit genug Vorlauf an (z. B. 1 Stunde).", 0],
        ["firmen-codes", "Firmen-Rabattcodes", "Vorerst abgeschaltet. Falls sie wiederkommen: als fester Firmenpreis pro Gericht (z. B. Döner 6 €, Dürüm 7 €) statt Prozent – für Barzahlung am einfachsten. Nur mit Kontrolle an der Theke (Bestellung auf Firmennamen oder Firmenausweis).", 0],
    ]],
    ["Laufende Kosten", [
        ["domain-kosten", "Domain", "Wer zahlt die Domain, auf wen läuft sie?", 0],
        ["github-pro", "GitHub Pro", "Rund 4 US-$ im Monat. Nötig, damit Seite und Chef-Daten in einem privaten Repository liegen können. Wer zahlt?", 0],
    ]],
]

# ---------- Druck (Flyer, Aufsteller, Aushänge) ----------
SEIT = "1997"                                   # „seit 1997“ auf dem Flyer; "" = weglassen
DRUCK_UNTERZEILE = "Döner · Pizza · Lahmacun"  # unter dem Namen auf dem Flyer
DRUCK_FUSS = "Alle Gerichte mit Soße nach Wahl: Knoblauch, Kräuter, Chili."   # Aushang A3 unten
FLYER = {"innen": [["doener", "duerum"], ["teller", "schnitzel", "kinder"], ["pizza", "lahmacun"]],   # Gruppen-Kennungen
         "klappe": ["salate", "baguette"], "rueck": ["getraenke"]}
ANGEBOT = {   # kurze Zeile „was es gibt“ auf dem Aushang „Hier vorbestellen“, je Sprache
    "de": "Döner, Dürüm, Pizza und Salate", "en": "Döner, dürüm, pizza and salads", "cs": "Döner, dürüm, pizza a saláty",
    "tr": "Döner, dürüm, pizza ve salatalar", "ru": "Дёнер, дюрюм, пицца и салаты", "ar": "دونر، دوروم، بيتزا وسلطات",
}
