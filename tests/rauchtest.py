#!/usr/bin/env python3
"""Rauchtest für alle gebauten Läden (docs/<id>/): Seite, Bestellung, Küche, Chef-App und Bildschirm laden ohne Fehler.

    python3 alle_bauen.py && python3 tests/rauchtest.py [laden …]

Die ausführlichen Abläufe prüft tests/test_seite.py am Referenz-Laden „saray“.
"""
import base64
import functools
import http.server
import json
import pathlib
import sys
import threading
import traceback
import urllib.parse

from playwright.sync_api import sync_playwright

HIER = pathlib.Path(__file__).resolve().parent.parent
DOCS = HIER / "docs"
ZEIT = "2026-10-21T17:45:00+02:00"   # Mittwoch, alle Beispiel-Läden geöffnet


class Leise(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def pruefen(b, url, laden):
    std = json.loads((DOCS / laden / "chef" / "standard.json").read_text())
    namen = [l["name"] for l in std["laeden"]]
    ctx = b.new_context(viewport={"width": 390, "height": 844}, locale="de-DE", timezone_id="Europe/Berlin", is_mobile=True, has_touch=True)
    fehler = []
    ctx.on("weberror", lambda e: fehler.append(str(e.error)))
    p = ctx.new_page()
    p.on("pageerror", lambda e: fehler.append(str(e)))
    p.clock.set_fixed_time(ZEIT)
    p.goto(url + laden + "/")
    p.wait_for_timeout(500)
    titel = p.title()
    # erstes Gericht mit einem Preis bestellen
    p.locator("li[data-k]:not([data-p*='|']) .plus:visible").first.click()
    p.wait_for_timeout(300)
    if p.is_visible("#zettel-leiste"):
        p.click("#zettel-leiste")
    if len(namen) > 1:
        p.click("[data-laden] >> nth=0")
    p.evaluate("document.getElementById('zettel-whatsapp').addEventListener('click',e=>e.preventDefault())")
    href = p.get_attribute("#zettel-whatsapp", "href") or ""
    text = urllib.parse.parse_qs(urllib.parse.urlparse(href).query).get("text", [""])[0]
    assert "Summe:" in text and "1×" in text, f"{laden}: Bestelltext {text[:200]!r}"
    assert any(n in text for n in namen), f"{laden}: Laden fehlt im Bestelltext"
    link = [z for z in text.split("\n") if z.startswith("Für die Küche: ")][0].split(": ", 1)[1]
    assert f"/{laden}/kueche/#b=" in link, link
    # Küche
    k = ctx.new_page()
    k.on("pageerror", lambda e: fehler.append("Küche: " + str(e)))
    k.goto(link)
    k.wait_for_selector("#offen .bon")
    # Chef-App mit nachgebildeter GitHub-API
    c = ctx.new_page()
    c.on("pageerror", lambda e: fehler.append("Chef: " + str(e)))
    c.route("https://api.github.com/**", lambda r: r.fulfill(status=200, json={"sha": "x", "content": base64.b64encode(b"{}").decode()}))
    c.add_init_script("try{localStorage.setItem('" + std.get("praefix", "") + "-chef-tour','1')}catch(e){}")
    c.goto(url + laden + "/chef/#token=TEST")
    c.wait_for_selector("nav.tabs:not([hidden])")
    if c.locator("#tour").count():
        c.click("#tour-ende")
    for tab in ("karte", "preise", "zeiten", "mehr"):
        c.click(f'nav.tabs [data-tab="{tab}"]')
    c.click('[data-seite="drucken"]')
    # Bildschirm im Laden
    t = ctx.new_page()
    t.on("pageerror", lambda e: fehler.append("TV: " + str(e)))
    t.goto(url + laden + "/tv/")
    t.wait_for_timeout(500)
    ctx.close()
    assert not fehler, f"{laden}: {fehler}"
    return titel


def main():
    auswahl = sys.argv[1:] or sorted(p.name for p in DOCS.iterdir() if (p / "index.html").exists() and (p / "chef").exists())
    handler = functools.partial(Leise, directory=str(DOCS))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{srv.server_address[1]}/"
    ok = 0
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for laden in auswahl:
            try:
                titel = pruefen(b, url, laden)
                ok += 1
                print(f"  ok      {laden}  ({titel})")
            except Exception:
                print(f"  FEHLER  {laden}")
                traceback.print_exc()
        b.close()
    srv.shutdown()
    print(f"{ok} von {len(auswahl)} Läden in Ordnung")
    return 0 if ok == len(auswahl) else 1


if __name__ == "__main__":
    sys.exit(main())
