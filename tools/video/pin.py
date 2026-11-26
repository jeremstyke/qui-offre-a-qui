# Épingles Pinterest 1000x1500 pour Qui offre à qui. Usage : python3 pin.py (génère toutes les épingles de PINS)
import sys, html
sys.path.insert(0, '/home/claude/qui-offre-a-qui/tools/video')
from fonts import CSS
from playwright.sync_api import sync_playwright
OUT = '/home/claude/qui-offre-a-qui/media/pins/'
PINS = [
 ("idee-cadeau-20-euros", "15 idées cadeaux", "à 20 €", ["Plaid tout doux", "Jeu de société rapide", "Coffret thé ou café", "Lampe veilleuse"], "Secret Santa et Noël", "baie", "grand"),
 ("idee-cadeau-10-euros", "15 idées cadeaux", "à 10 €", ["Mug original", "Chaussettes de Noël", "Jeu de cartes apéro", "Bougie parfumée"], "Petit budget, vrai plaisir", "sapin", "liste"),
 ("idee-cadeau-50-euros", "15 idées cadeaux", "à 50 €", ["Écouteurs sans fil", "Appareil à raclette", "Plaid chauffant", "Coffret LEGO adulte"], "Un vrai beau cadeau", "nuit", "etiquette"),
 ("idee-cadeau-100-euros", "15 idées cadeaux", "à 100 €", ["Casque réduction de bruit", "Friteuse sans huile", "Liseuse", "Appareil photo instantané"], "Le cadeau qui marque", "creme", "grand"),
 ("idee-cadeau-5-euros", "15 petites idées", "à 5 €", ["Bonbons originaux", "Chaussettes fantaisie", "Baume à lèvres", "Mini plante grasse"], "Classe, club, grande équipe", "baie", "etiquette"),
 ("idee-cadeau-secret-santa-homme", "Secret Santa", "pour un homme", ["Mug isotherme", "Multi-outil de poche", "Coffret bières du monde", "Enceinte Bluetooth"], "15 idées par budget", "sapin", "liste"),
 ("idee-cadeau-secret-santa-femme", "Secret Santa", "pour une femme", ["Bougie parfumée", "Plaid tout doux", "Coffret soin", "Bijou délicat"], "15 idées par budget", "creme", "etiquette"),
 ("jeu-ange-gardien", "Le jeu de", "l'ange gardien", ["Les règles en 4 étapes", "Idées d'attentions", "EVJF, colo, séminaire", "Tirage en ligne gratuit"], "Idées et tirage au sort", "sapin", "liste"),
 ("qui-apporte-quoi", "Repas de Noël :", "qui apporte quoi ?", ["Un tableau partagé", "Chacun note ce qu'il apporte", "Fini les 3 bûches", "Gratuit, sans compte"], "Organiser le repas", "sapin", "liste"),
 ("", "Tirage au sort", "Secret Santa", ["Prénoms et e-mails", "Exclusions entre couples", "Résultat secret par e-mail", "Gratuit, sans compte"], "Prêt en 2 minutes", "sapin", "liste"),
]
THEMES = {
 "sapin": dict(bg="#123d34", fg="#ffffff", acc="#e9b949", accfg="#123d34", card="#fffdf6", cardfg="#1d2a26", soft="#cfe1d9"),
 "baie": dict(bg="#b3263a", fg="#ffffff", acc="#fffdf6", accfg="#b3263a", card="#ffffff", cardfg="#1d2a26", soft="#f6d3d8"),
 "creme": dict(bg="#fbf3e2", fg="#123d34", acc="#b3263a", accfg="#ffffff", card="#ffffff", cardfg="#1d2a26", soft="#5b6b66"),
 "nuit": dict(bg="#1d2440", fg="#ffffff", acc="#e9b949", accfg="#1d2440", card="#2c355c", cardfg="#ffffff", soft="#c9cfe6"),
}
LAYOUTS = ["liste", "grand", "etiquette"]
def page(h1, big, items, sub, theme="sapin", layout="liste"):
    t = THEMES[theme]
    li = ''.join(f'<li>{html.escape(x)}</li>' for x in items)
    base = f"""*{{margin:0;box-sizing:border-box}}body{{width:1000px;height:1500px;background:{t['bg']};color:{t['fg']};font-family:'Atkinson Hyperlegible';position:relative;overflow:hidden}}
.r{{position:absolute;left:0;right:0;height:22px;background:repeating-linear-gradient(-45deg,#b3263a 0 36px,#fff 36px 52px,#1f6b4f 52px 88px,#fff 88px 104px)}}
.f{{position:absolute;left:0;right:0;bottom:70px;text-align:center;font:800 52px/1 'Bricolage Grotesque'}}
.f span{{display:block;font:700 34px/1 'Atkinson Hyperlegible';color:{t['soft']};margin-bottom:18px}}
.sub{{font:700 40px/1.1 'Atkinson Hyperlegible';color:{t['acc'] if theme!='creme' else t['acc']}}}"""
    foot = '<div class="f"><span>Tirage au sort gratuit et idées sur</span>qui-offre-a-qui.fr</div>'
    if layout == "grand":
        css = base + f"""
.t{{position:absolute;left:70px;right:70px;top:110px;text-align:center}}
h1{{font:800 96px/1 'Bricolage Grotesque';margin-top:24px}}
.big{{font:800 170px/1 'Bricolage Grotesque';color:{t['acc']};margin-top:18px;letter-spacing:-.03em}}
ul{{list-style:none;position:absolute;left:60px;right:60px;top:760px;display:grid;grid-template-columns:1fr 1fr;gap:22px}}
li{{background:{t['card']};color:{t['cardfg']};font:700 38px/1.15 'Atkinson Hyperlegible';border-radius:999px;padding:26px 28px;text-align:center}}"""
        body = f'<div class="t"><div class="sub">{html.escape(sub)}</div><h1>{html.escape(h1)}</h1><div class="big">{html.escape(big)}</div></div><ul>{li}</ul>{foot}'
    elif layout == "etiquette":
        css = base + f"""
.tag{{position:absolute;left:110px;right:110px;top:150px;height:560px;background:{t['card']};color:{t['cardfg']};border-radius:40px 40px 40px 40px;transform:rotate(-3deg);box-shadow:0 30px 60px rgba(0,0,0,.25);padding:90px 60px 0;text-align:center}}
.tag:before{{content:"";position:absolute;top:34px;left:50%;width:44px;height:44px;margin-left:-22px;border-radius:50%;background:{t['bg']}}}
.tag .sub{{color:#b3263a}}
.tag h1{{font:800 92px/1 'Bricolage Grotesque';margin-top:22px;color:{t['cardfg']}}}
.tag .big{{display:inline-block;margin-top:24px;font:800 96px/1 'Bricolage Grotesque';color:#fff;background:#b3263a;border-radius:24px;padding:10px 32px 18px}}
ul{{list-style:none;position:absolute;left:90px;right:90px;top:820px}}
li{{font:700 44px/1.2 'Atkinson Hyperlegible';padding:16px 0 16px 64px;border-bottom:2px solid {t['soft']}55;position:relative}}
li:before{{content:"✓";position:absolute;left:0;top:14px;width:46px;height:46px;border-radius:50%;background:{t['acc']};color:{t['accfg']};font-size:30px;line-height:46px;text-align:center}}"""
        body = f'<div class="tag"><div class="sub">{html.escape(sub)}</div><h1>{html.escape(h1)}</h1><div class="big">{html.escape(big)}</div></div><ul>{li}</ul>{foot}'
    else:
        css = base + f"""
.t{{position:absolute;left:70px;right:70px;top:120px}}
.sub{{display:inline-block;margin-bottom:26px}}
h1{{font:800 108px/1 'Bricolage Grotesque';letter-spacing:-.02em}}
.big{{display:inline-block;margin-top:22px;font:800 112px/1.02 'Bricolage Grotesque';color:{t['accfg']};background:{t['acc']};border-radius:28px;padding:14px 36px 22px;transform:rotate(-2deg)}}
ul{{list-style:none;position:absolute;left:70px;right:70px;top:720px}}
li{{background:{t['card']};color:{t['cardfg']};font:700 46px/1.15 'Atkinson Hyperlegible';border-radius:22px;padding:26px 34px;margin-bottom:22px;display:flex;align-items:center;gap:22px}}
li:before{{content:"🎁";font-size:44px}}"""
        body = f'<div class="t"><div class="sub">{html.escape(sub)}</div><h1>{html.escape(h1)}</h1><div class="big">{html.escape(big)}</div></div><ul>{li}</ul>{foot}'
    rubans = '<div class="r" style="top:0"></div><div class="r" style="bottom:0"></div>' if theme != "baie" else ''
    return f"<html><head><style>{CSS}\n{css}</style></head><body>{rubans}{body}</body></html>"
# Chaque épingle peut préciser theme et layout (6e et 7e éléments) ; sinon rotation automatique pour varier.
THEME_ORDER = ["sapin", "baie", "creme", "nuit"]
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1000, 'height': 1500})
    seul = sys.argv[1:]
    for n, pin in enumerate(PINS):
        slug, h1, big, items, sub = pin[:5]
        theme = pin[5] if len(pin) > 5 else THEME_ORDER[n % 4]
        layout = pin[6] if len(pin) > 6 else LAYOUTS[n % 3]
        if seul and (slug or 'tirage-au-sort') not in seul: continue
        pg.set_content(page(h1, big, items, sub, theme, layout)); pg.wait_for_timeout(300)
        pg.screenshot(path=OUT + (slug or 'tirage-au-sort') + '.jpg', type='jpeg', quality=85)
    b.close()
print('ok', len(PINS))
