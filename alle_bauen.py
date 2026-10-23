#!/usr/bin/env python3
"""Baut alle Läden (laeden/*/laden.py) nach docs/<id>/ und eine Übersichtsseite docs/index.html.

    python3 alle_bauen.py              alle Läden
    python3 alle_bauen.py pirna saray  nur diese (Übersicht trotzdem mit allen)
    python3 alle_bauen.py --druck      zusätzlich Druckvorlagen je Laden nach docs/<id>/druck/ (braucht Playwright)
"""
import html
import json
import os
import pathlib
import subprocess
import sys

HIER = pathlib.Path(__file__).parent
DOCS = HIER / "docs"


def laeden():
    ids = sorted(p.parent.name for p in (HIER / "laeden").glob("*/laden.py"))
    return sorted(ids, key=lambda i: (i != "saray", i))


def info(laden):
    """Name, Orte und Farben eines Ladens (eigener Prozess, weil konfig genau einen Laden lädt)."""
    code = ("import json,konfig;K=konfig.K;f=dict(konfig.STANDARD_FARBEN,**(getattr(K,'FARBEN',None) or {}));"
            "print(json.dumps({'name':K.NAME,'orte':[s['name'] for s in K.STANDORTE],'text':K.UNTERZEILE[0],"
            "'gelb':f['gelb'],'tinte':f['tinte'],'logo':K.LOGO,'beispiel':bool(getattr(K,'VORSCHAU_TEXT',None))}))")
    out = subprocess.run([sys.executable, "-c", code], cwd=HIER, env=dict(os.environ, LADEN=laden), capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def uebersicht(alle):
    e = html.escape
    karten = []
    for l in alle:
        i = info(l)
        karten.append(f'''<a class="k" href="{l}/" style="--g:{i["gelb"]};--t:{i["tinte"]}">
  <img src="{l}/img/{e(i["logo"])}" alt="" width="64" height="64">
  <span><b>{e(i["name"])}</b><small>{e(" · ".join(i["orte"]))} – {e(i["text"])}</small>{'<em>erfundenes Beispiel</em>' if i["beispiel"] else ''}</span>
</a>''')
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>Laden-Vorlage – Übersicht</title>
<style>
:root{{color-scheme:light}}body{{margin:0;font:16px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#F6F3EE;color:#222}}
main{{max-width:720px;margin:0 auto;padding:28px 16px 48px}}h1{{font-size:1.6rem;margin:0 0 6px}}p{{margin:0 0 20px;color:#555}}
.k{{display:flex;gap:14px;align-items:center;padding:14px 16px;margin:0 0 12px;border-radius:16px;background:var(--g);color:var(--t);text-decoration:none;
  box-shadow:0 2px 0 rgba(0,0,0,.08)}}.k:hover{{transform:translateY(-1px)}}.k img{{flex:none;border-radius:50%}}
.k b{{display:block;font-size:1.15rem}}.k small{{display:block;opacity:.85}}.k em{{display:inline-block;margin-top:4px;font-style:normal;font-size:.8rem;
  font-weight:700;padding:2px 8px;border-radius:99px;background:var(--t);color:var(--g)}}
code{{background:#fff;padding:1px 5px;border-radius:5px}}
</style></head><body><main>
<h1>Laden-Vorlage</h1>
<p>Eine Technik, mehrere Läden: jede Seite unten kommt aus derselben Vorlage – nur die Einstellungen in <code>laeden/&lt;laden&gt;/</code> sind verschieden.
Zu jeder Seite gehören die Chef-App (<code>…/chef/</code>), die Küchenansicht (<code>…/kueche/</code>) und der Bildschirm im Laden (<code>…/tv/</code>).</p>
{"".join(karten)}
</main></body></html>
"""


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    alle = laeden()
    auswahl = argv or alle
    for l in auswahl:
        print(f"== {l}")
        subprocess.run([sys.executable, "build.py"], cwd=HIER, env=dict(os.environ, LADEN=l), check=True)
        if "--druck" in sys.argv:
            r = subprocess.run([sys.executable, "druck.py", str(DOCS / l / "druck")], cwd=HIER, env=dict(os.environ, LADEN=l))
            if r.returncode:
                print(f"WARNUNG: Druckvorlagen für {l} fehlgeschlagen")
    DOCS.mkdir(exist_ok=True)
    (DOCS / "index.html").write_text(uebersicht(alle), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "robots.txt").write_text("User-agent: *\nDisallow: /\n")   # Vorlage und Beispiele: nicht in Suchmaschinen
    for alt in DOCS.iterdir():   # Ordner von gelöschten Läden entfernen
        if alt.is_dir() and alt.name not in alle:
            import shutil
            shutil.rmtree(alt)
    print("Übersicht: docs/index.html –", ", ".join(alle))


if __name__ == "__main__":
    main()
