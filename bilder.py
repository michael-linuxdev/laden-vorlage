#!/usr/bin/env python3
"""Erzeugt die Bilder eines Ladens aus Logo, Figur, Farben und Texten seiner Konfiguration:

    python3 bilder.py pirna        -> laeden/pirna/maskottchen/favicon-96.png, app-180/192/512.png
                                      laeden/pirna/bilder/og-bild.jpg (1200 × 630, Vorschau beim Teilen)

Vorher in laeden/<id>/maskottchen/ ablegen: das Logo (LOGO, rund, SVG) und optional eine Figur (FIGUR, SVG).
Braucht Playwright mit Chromium. Bestehende Dateien werden überschrieben.
"""
import html
import os
import pathlib
import subprocess
import sys

HIER = pathlib.Path(__file__).parent


def main(laden):
    os.environ["LADEN"] = laden
    import konfig
    K = konfig.K
    farben = dict(konfig.STANDARD_FARBEN, **(getattr(K, "FARBEN", None) or {}))
    mask = konfig.BILDER.parent / "maskottchen"
    logo = (mask / K.LOGO).resolve().as_uri()
    figur = (mask / K.FIGUR).resolve().as_uri() if getattr(K, "FIGUR", None) else ""
    font = lambda n: (HIER / "assets" / n).resolve().as_uri()
    e = html.escape
    held = K.HELD[0].replace("<br>", "<br>")
    foto = getattr(K, "FOTO", None)
    foto_uri = (konfig.BILDER / foto[0]).resolve().as_uri() if foto else ""
    rechts = (f'<div class="r"><img class="f" src="{foto_uri}">' + (f'<img class="k" src="{figur}">' if figur else "") + "</div>") if foto else \
             (f'<div class="r leer"><img class="g" src="{figur or logo}"></div>')
    og = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Slab;src:url({font("Roboto-Slab-Bold.sub.woff")})}}
@font-face{{font-family:Text;src:url({font("lato-bold.sub.woff")})}}
html,body{{margin:0}}body{{width:1200px;height:630px;display:flex;background:{farben["gelb"]};color:{farben["tinte"]};font-family:Text}}
.l{{width:620px;padding:56px 0 48px 64px;box-sizing:border-box;display:flex;flex-direction:column}}
.m{{display:flex;align-items:center;gap:18px}}.m img{{width:96px}}.m b{{font:46px/1.05 Slab}}
h1{{font:62px/1.06 Slab;margin:40px 0 0}}p{{font-size:30px;margin:18px 0 0}}
.o{{margin-top:auto;font-size:25px;white-space:nowrap;background:{farben["tinte"]};color:{farben["gelb"]};align-self:flex-start;padding:12px 22px;border-radius:999px}}
.r{{width:580px;height:630px;position:relative}}.r .f{{width:100%;height:100%;object-fit:cover;display:block}}
.r .k{{position:absolute;left:-70px;bottom:-6px;width:230px;height:auto}}
.r.leer{{display:grid;place-items:center;background:{farben["gelb-blass"]}}}.r .g{{width:440px;height:440px;object-fit:contain}}
</style></head><body><div class="l"><div class="m"><img src="{logo}"><b>{e(K.NAME)}</b></div>
<h1>{held}</h1><p>{e(K.UNTERZEILE[0])}</p><div class="o">{e(" & ".join(s["name"] for s in K.STANDORTE))} · online vorbestellen</div></div>
{rechts}</body></html>"""
    icon = lambda g, rand: f"""<!doctype html><html><head><style>html,body{{margin:0}}body{{width:{g}px;height:{g}px;display:grid;place-items:center;
background:{farben["gelb"]}}}img{{width:{g - 2 * rand}px;height:{g - 2 * rand}px}}</style></head><body><img src="{logo}"></body></html>"""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        def bild(inhalt, breite, hoehe, ziel, typ="png"):
            tmp = HIER / f"_bild_{laden}.html"
            tmp.write_text(inhalt, encoding="utf-8")
            p = b.new_page(viewport={"width": breite, "height": hoehe})
            p.goto(tmp.as_uri())
            p.wait_for_timeout(400)
            ziel.parent.mkdir(parents=True, exist_ok=True)
            p.screenshot(path=str(ziel), type=typ, **({"quality": 85} if typ == "jpeg" else {}), omit_background=False)
            p.close()
            tmp.unlink()
            print(ziel.relative_to(HIER))
        bild(icon(96, 4), 96, 96, mask / "favicon-96.png")
        for g in (180, 192, 512):
            bild(icon(g, g // 8), g, g, mask / f"app-{g}.png")
        bild(og, 1200, 630, konfig.BILDER / "og-bild.jpg", "jpeg")
        b.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    # jeder Laden in einem eigenen Prozess (konfig lädt beim Import genau einen Laden)
    if os.environ.get("LADEN") != sys.argv[1]:
        raise SystemExit(subprocess.call([sys.executable, __file__, sys.argv[1]], env=dict(os.environ, LADEN=sys.argv[1])))
    main(sys.argv[1])
