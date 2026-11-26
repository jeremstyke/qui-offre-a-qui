# Épingles Pinterest 1000x1500 pour Qui offre à qui. Usage : python3 pin.py (génère toutes les épingles de PINS)
import sys, html
sys.path.insert(0, '/home/claude/qui-offre-a-qui/tools/video')
from fonts import CSS
from playwright.sync_api import sync_playwright
OUT = '/home/claude/qui-offre-a-qui/media/pins/'
PINS = [
 ("idee-cadeau-20-euros", "15 idées cadeaux", "à 20 €", ["Plaid tout doux", "Jeu de société rapide", "Coffret thé ou café", "Lampe veilleuse"], "Secret Santa et Noël"),
 ("idee-cadeau-10-euros", "15 idées cadeaux", "à 10 €", ["Mug original", "Chaussettes de Noël", "Jeu de cartes apéro", "Bougie parfumée"], "Petit budget, vrai plaisir"),
 ("idee-cadeau-50-euros", "15 idées cadeaux", "à 50 €", ["Écouteurs sans fil", "Appareil à raclette", "Plaid chauffant", "Coffret LEGO adulte"], "Un vrai beau cadeau"),
 ("idee-cadeau-100-euros", "15 idées cadeaux", "à 100 €", ["Casque réduction de bruit", "Friteuse sans huile", "Liseuse", "Appareil photo instantané"], "Le cadeau qui marque"),
 ("idee-cadeau-5-euros", "15 petites idées", "à 5 €", ["Bonbons originaux", "Chaussettes fantaisie", "Baume à lèvres", "Mini plante grasse"], "Classe, club, grande équipe"),
 ("idee-cadeau-secret-santa-homme", "Secret Santa", "pour un homme", ["Mug isotherme", "Multi-outil de poche", "Coffret bières du monde", "Enceinte Bluetooth"], "15 idées par budget"),
 ("idee-cadeau-secret-santa-femme", "Secret Santa", "pour une femme", ["Bougie parfumée", "Plaid tout doux", "Coffret soin", "Bijou délicat"], "15 idées par budget"),
 ("jeu-ange-gardien", "Le jeu de", "l'ange gardien", ["Les règles en 4 étapes", "Idées d'attentions", "EVJF, colo, séminaire", "Tirage en ligne gratuit"], "Idées et tirage au sort"),
 ("qui-apporte-quoi", "Repas de Noël :", "qui apporte quoi ?", ["Un tableau partagé", "Chacun note ce qu'il apporte", "Fini les 3 bûches", "Gratuit, sans compte"], "Organiser le repas"),
 ("", "Tirage au sort", "Secret Santa", ["Prénoms et e-mails", "Exclusions entre couples", "Résultat secret par e-mail", "Gratuit, sans compte"], "Prêt en 2 minutes"),
]
def page(h1, big, items, sub):
    li = ''.join(f'<li>{html.escape(x)}</li>' for x in items)
    return f'''<html><head><style>{CSS}
*{{margin:0;box-sizing:border-box}}body{{width:1000px;height:1500px;background:#123d34;color:#fff;font-family:'Atkinson Hyperlegible';position:relative;overflow:hidden}}
.r{{position:absolute;left:0;right:0;height:22px;background:repeating-linear-gradient(-45deg,#b3263a 0 36px,#fff 36px 52px,#1f6b4f 52px 88px,#fff 88px 104px)}}
.t{{position:absolute;left:70px;right:70px;top:120px}}
.sub{{display:inline-block;font:700 40px/1 'Atkinson Hyperlegible';color:#e9b949;margin-bottom:26px}}
h1{{font:800 108px/1 'Bricolage Grotesque';letter-spacing:-.02em}}
.big{{display:inline-block;margin-top:22px;font:800 112px/1.02 'Bricolage Grotesque';color:#123d34;background:#e9b949;border-radius:28px;padding:14px 36px 22px;transform:rotate(-2deg)}}
ul{{list-style:none;position:absolute;left:70px;right:70px;top:720px}}
li{{background:#fffdf6;color:#1d2a26;font:700 46px/1.15 'Atkinson Hyperlegible';border-radius:22px;padding:26px 34px;margin-bottom:22px;display:flex;align-items:center;gap:22px}}
li:before{{content:"🎁";font-size:44px}}
.f{{position:absolute;left:0;right:0;bottom:70px;text-align:center;font:800 52px/1 'Bricolage Grotesque'}}
.f span{{display:block;font:700 34px/1 'Atkinson Hyperlegible';color:#cfe1d9;margin-bottom:18px}}
</style></head><body><div class="r" style="top:0"></div><div class="r" style="bottom:0"></div>
<div class="t"><div class="sub">{html.escape(sub)}</div><h1>{html.escape(h1)}</h1><div class="big">{html.escape(big)}</div></div>
<ul>{li}</ul><div class="f"><span>Tirage au sort gratuit et idées sur</span>qui-offre-a-qui.fr</div></body></html>'''
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1000, 'height': 1500})
    for slug, h1, big, items, sub in PINS:
        pg.set_content(page(h1, big, items, sub)); pg.wait_for_timeout(300)
        pg.screenshot(path=OUT + (slug or 'tirage-au-sort') + '.jpg', type='jpeg', quality=85)
    b.close()
print('ok', len(PINS))
