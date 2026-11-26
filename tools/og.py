# Génère le favicon (PNG, ICO, apple-touch) et une image de partage 1200x630 par page (og/<slug>.png).
# Usage : python3 tools/og.py   (nécessite playwright + chromium). Les images existantes sont régénérées.
import os, sys, base64, html, io
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'src'))
from pages import PAGES
from pages_noel import PAGES_NOEL
from playwright.sync_api import sync_playwright
from PIL import Image
PAGES = PAGES + PAGES_NOEL
def f64(n): return base64.b64encode(open(os.path.join(HERE, 'fonts', n), 'rb').read()).decode()
SVG = open(os.path.join(ROOT, 'assets', 'favicon.svg')).read()
FONTS = f"""@font-face{{font-family:B;font-weight:800;src:url(data:font/woff2;base64,{f64('bricolage-grotesque-latin-800-normal.woff2')}) format('woff2')}}
@font-face{{font-family:A;font-weight:400;src:url(data:font/woff2;base64,{f64('atkinson-hyperlegible-latin-400-normal.woff2')}) format('woff2')}}
@font-face{{font-family:A;font-weight:700;src:url(data:font/woff2;base64,{f64('atkinson-hyperlegible-latin-700-normal.woff2')}) format('woff2')}}"""
ICON = 'data:image/svg+xml;base64,' + base64.b64encode(SVG.encode()).decode()

def page(kicker, titre, sous, gros=None):
    big = f'<div class="gros">{html.escape(gros)}</div>' if gros else ''
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#123d34;color:#fff;font-family:A;position:relative;overflow:hidden}}
.ruban{{position:absolute;right:-70px;top:-20px;bottom:-20px;width:230px;background:#b8344a;transform:skewX(-12deg)}}
.ruban:after{{content:"";position:absolute;left:92px;top:0;bottom:0;width:26px;background:#e9b949}}
.noeud{{position:absolute;right:58px;top:46px;width:150px}}
.c{{position:absolute;left:72px;top:64px;right:{470 if gros else 300}px;bottom:60px;display:flex;flex-direction:column}}
.k{{font:700 26px A;color:#e9b949;margin-bottom:18px}}
h1{{font:800 {64 if len(titre) < 48 else 56}px/1.04 B;letter-spacing:-.01em;text-wrap:balance}}
p{{font:400 28px/1.35 A;color:#d6e4de;margin-top:22px;max-width:760px}}
.pied{{margin-top:auto;display:flex;align-items:center;gap:16px;font:700 28px A}}
.pied img{{width:54px;height:54px}}
.pied span{{color:#9fc0b4;font-weight:400;margin-left:6px}}
.pills{{display:flex;gap:12px;margin-top:34px;flex-wrap:wrap}}
.pills span{{font:700 24px A;background:rgba(255,255,255,.1);border:2px solid rgba(255,255,255,.16);border-radius:999px;padding:9px 20px}}
.gros{{position:absolute;right:280px;top:200px;font:800 190px/1 B;color:#e9b949;letter-spacing:-.03em}}
</style></head><body><div class="ruban"></div>
<svg class="noeud" viewBox="0 0 150 90"><path d="M75 80C62 50 22 30 12 52 4 70 40 82 75 80zm0 0c13-30 53-50 63-28 8 18-28 30-63 28z" fill="#e9b949"/><circle cx="75" cy="78" r="11" fill="#f3d27a"/></svg>
<div class="c"><div class="k">{html.escape(kicker)}</div><h1>{html.escape(titre).replace(' €', '&nbsp;€').replace(' ?', '&nbsp;?').replace(' :', '&nbsp;:')}</h1><p>{html.escape(sous).replace(' :', '&nbsp;:').replace(' ?', '&nbsp;?').replace('e-mail', 'e&#8209;mail')}</p><div class="pills"><span>Gratuit</span><span>Sans compte</span><span>2 minutes</span></div>
<div class="pied"><img src="{ICON}">Qui offre à qui<span>qui-offre-a-qui.fr</span></div></div>{big}</body></html>"""

def main():
    os.makedirs(os.path.join(ROOT, 'og'), exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1200, 'height': 630})
        def shot(htmls, out):
            pg.set_content(htmls); pg.wait_for_timeout(150); pg.screenshot(path=out)
        # Accueil
        shot(page("Père Noël secret, Secret Santa", "Le tirage au sort de cadeaux, en 2 minutes", "Chacun reçoit son résultat par e-mail. Même l'organisateur ne sait pas qui offre à qui."), os.path.join(ROOT, 'og.png'))
        shot(page("Idées et conseils", "Tous nos guides cadeaux", "Des idées par budget, de 5 à 50 €, et des conseils pour organiser votre Père Noël secret."), os.path.join(ROOT, 'og', 'guides.png'))
        shot(page("Repas de Noël, Nouvel An, anniversaire", "Qui apporte quoi ? La liste du repas", "Partagez un lien, chacun coche ce qu'il apporte. Fini les trois bûches et zéro pain."), os.path.join(ROOT, 'og', 'qui-apporte-quoi.png'))
        for q in PAGES:
            t = q['title']; titre, _, reste = t.partition(' : ')
            if 'euros' in q['slug']:
                b_ = q['slug'].split('-')[-2]
                shot(page("Idées cadeaux par budget", f"Idée cadeau à {b_} €", reste[:1].upper() + reste[1:] + "."), os.path.join(ROOT, 'og', q['slug'] + '.png'))
            else:
                shot(page("Guide Qui offre à qui", titre, ((reste[:1].upper() + reste[1:] + ".") if reste else "Le tirage au sort de cadeaux en ligne.")), os.path.join(ROOT, 'og', q['slug'] + '.png'))
        # Favicons
        for n in (16, 32, 48, 180, 192, 512):
            pg.set_viewport_size({'width': n, 'height': n})
            pg.set_content(f'<html><body style="margin:0;background:transparent">{SVG.replace("<svg ", f"<svg width={n} height={n} ", 1)}</body></html>')
            pg.screenshot(path=os.path.join(ROOT, 'assets', f'icon-{n}.png'), omit_background=True)
        b.close()
    ims = [Image.open(os.path.join(ROOT, 'assets', f'icon-{n}.png')) for n in (16, 32, 48)]
    ims[2].save(os.path.join(ROOT, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)], append_images=ims[:2])
    # Apple : fond plein (pas de transparence)
    a = Image.open(os.path.join(ROOT, 'assets', 'icon-180.png')).convert('RGBA'); bg = Image.new('RGBA', a.size, (18, 61, 52, 255)); bg.alpha_composite(a); bg.convert('RGB').save(os.path.join(ROOT, 'assets', 'apple-touch-icon.png'))
    # Compression des images de partage
    for root in (ROOT, os.path.join(ROOT, 'og')):
        for f in os.listdir(root):
            if f.endswith('.png') and (root.endswith('og') or f == 'og.png'):
                pth = os.path.join(root, f); Image.open(pth).convert('RGB').quantize(colors=128, method=Image.Quantize.MEDIANCUT).save(pth, optimize=True)
    print('ok', len(PAGES) + 2, 'images')
main()
