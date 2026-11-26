#!/usr/bin/env python3
# Génère le site Qui offre à qui (qui-offre-a-qui.fr) à la racine du dépôt, servi par GitHub Pages.
import os, re, html, json, datetime
from urllib.parse import quote_plus

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
BASE = 'https://qui-offre-a-qui.fr'
SITE = 'Qui offre à qui'
TAG = 'quioffreaqui-21'
INDEXNOW = 'da4540821acf4048569bad7fbedc3ee1'
CSS = open(os.path.join(HERE, 'tool.css')).read()
EXTRA_CSS = """
.vid{position:relative;aspect-ratio:16/9;border-radius:14px;overflow:hidden;background:#123d34;margin:10px 0 6px}
.vid button{all:unset;cursor:pointer;display:block;width:100%;height:100%;position:relative}
.vid img,.vid iframe{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border:0}
.vid .play{position:absolute;left:12px;right:auto;top:auto;bottom:10px;width:clamp(34px,9%,60px);height:auto;aspect-ratio:1;margin:0;border-radius:50%;background:#b3263a;box-shadow:0 8px 24px rgba(0,0,0,.35)}
.vid .play::after{content:"";position:absolute;left:38%;top:28%;border-left:solid #fff;border-width:0 0 0 0;width:0;height:0;border-left-width:clamp(12px,1.2vw + 8px,20px);border-top:clamp(8px,0.8vw + 5px,13px) solid transparent;border-bottom:clamp(8px,0.8vw + 5px,13px) solid transparent}
.vid button:focus-visible{outline:4px solid var(--or,#e9b949);outline-offset:-4px}
.vid-note{font-size:14px;color:#5b6b66;margin:0}
.nlbox{border:2px solid var(--or,#e8b04a);background:#fffaf0}
.nlcoche{background:#fffaf0;border:2px solid var(--or,#e8b04a);border-radius:12px;padding:12px 14px}
.nlf{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0 0}
.nlf input{flex:1 1 200px;min-width:0;font-size:16px;padding:12px 14px;border-radius:10px;border:1px solid #c9d6d0}
.nlf button{flex:0 0 auto;font:700 16px system-ui,sans-serif;padding:12px 18px;border:0;border-radius:10px;background:#b3263a;color:#fff;cursor:pointer}
.nlf button:disabled{opacity:.6}
.nlm{font-size:14px;margin:8px 0 0;min-height:1em}
.nlpied{background:rgba(255,255,255,.08);border-radius:14px;padding:18px 20px;margin:0 0 26px}
.nlpied h2{font:800 18px/1.3 "Bricolage Grotesque",sans-serif;color:#fff;margin:0 0 4px}
.nlpied p{margin:0}
.nlpied .nlm{color:#fff}
nav.top{background:var(--pin);border-bottom:1px solid rgba(255,255,255,.12)}
nav.top .wrap{display:flex;justify-content:space-between;align-items:center;padding-top:12px;padding-bottom:12px}
nav.top a{color:#fff;text-decoration:none;font:800 19px "Bricolage Grotesque",sans-serif}
nav.top a.cta{font:700 15px "Atkinson Hyperlegible",sans-serif;background:var(--baie);padding:8px 14px;border-radius:10px}
article h1{font:800 clamp(30px,6vw,44px)/1.1 "Bricolage Grotesque",sans-serif;margin:8px 0 12px;letter-spacing:-.01em}
article h2{font:800 24px/1.25 "Bricolage Grotesque",sans-serif;margin:32px 0 10px}
article h3{font-size:18px;margin:20px 0 6px}
article .meta{color:var(--gris);font-size:14px}
.encart{background:var(--pin);color:#fff;border-radius:14px;padding:20px;margin:28px 0}
.encart a.btn{background:var(--or);color:var(--encre)}
.voir{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px;margin:12px 0 0}
.voir a{display:block;background:#fff;border:1px solid var(--ligne);border-radius:12px;padding:12px 14px;text-decoration:none;color:var(--encre)}
.voir a:hover{border-color:var(--pin2)}
.voir b{display:block;font-size:16px;line-height:1.3}
.voir span{display:block;font-size:14px;color:var(--gris);margin-top:2px}
footer{background:var(--pin);color:#dfe9e4;text-align:left;margin-top:40px;padding:32px 0 36px}
footer a{color:#fff}
.pied{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.pied h2{font:800 16px/1.3 "Bricolage Grotesque",sans-serif;color:#fff;margin:0 0 10px}
.pastilles{display:flex;flex-wrap:wrap;gap:8px}
.pastilles.clair a{background:#eef3f0;color:var(--encre)}
.pastilles a{background:rgba(255,255,255,.12);border-radius:999px;padding:6px 12px;text-decoration:none;font-weight:700;font-size:15px}
.pied ul{list-style:none;padding:0;margin:0}
.pied li{margin:0 0 6px}
.pied li a{text-decoration:none}
.pied li a:hover,.pastilles a:hover{text-decoration:underline}
.bas{border-top:1px solid rgba(255,255,255,.18);margin-top:24px;padding-top:16px;font-size:14px}
.bas p{margin:4px 0}.soc{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:14px 0 6px}
.soc span{font-size:14px;opacity:.85}
.soc a{display:inline-flex;align-items:center;justify-content:center;width:46px;height:46px;border-radius:50%;background:rgba(255,255,255,.12);color:#fff;transition:background .2s,transform .2s}
.soc a:hover,.soc a:focus-visible{transform:translateY(-2px)}
.soc a.fb:hover,.soc a.fb:focus-visible{background:#1877f2}
.soc a.yt:hover,.soc a.yt:focus-visible{background:#f00}
.soc svg{width:24px;height:24px;fill:currentColor}
footer .amz{color:#b9cdc5}
@media(max-width:600px){.pied{grid-template-columns:1fr}}
.amz{font-size:13px;color:var(--gris)}
"""
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Atkinson+Hyperlegible:wght@400;700&display=swap" rel="stylesheet">'
FAVICON = '<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#123d34">'

from pages import PAGES
from pages_noel import PAGES_NOEL
PAGES = PAGES + PAGES_NOEL
def _k(p):
    m = re.search(r'(\d+)-euros', p['slug'])
    return (0, int(m.group(1))) if m else (1, 0)
PAGES = sorted(PAGES, key=_k)
POUR_QUI = ("homme", "femme", "ado", "collegue", "humour", "dernier-moment")
def groupe(p):
    if 'euros' in p['slug']: return 'budget'
    if any(k in p['slug'] for k in POUR_QUI): return 'pourqui'
    return 'organiser'
GROUPES = [('budget', 'Idées cadeaux par budget'), ('pourqui', 'Idées selon la personne'), ('organiser', 'Organiser son échange')]
def court_titre(p): return p['title'].split(' : ')[0]
def sous(t):
    x = t.split(" : ", 1)[1] if " : " in t else ""
    return x[:1].upper() + x[1:]
def cartes(liste):
    return '<div class="voir">' + ''.join(f'<a href="/{q["slug"]}/"><b>{esc(court_titre(q))}</b><span>{esc(sous(q["title"]))}</span></a>' for q in liste) + '</div>'

def amz(s):
    return re.sub(r'\{AMZ:([^}]+)\}', lambda m: 'https://www.amazon.fr/s?k=' + quote_plus(m.group(1).strip()) + '&tag=' + TAG, s)

def esc(s): return html.escape(s, quote=True)

def head(title, desc, path, schema=None, robots='index,follow'):
    _slug = path.strip('/')
    img = f'/og/{_slug}.png' if _slug and os.path.exists(os.path.join(OUT, 'og', _slug + '.png')) else '/og.png'
    sch = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in (schema or []))
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8638687738606649" crossorigin="anonymous"></script>
<meta name="google-site-verification" content="0tjo6Bj7KcNHJMLQKuavVd_d7pBDPoJX3TaLWRm1GA4">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{BASE}{path}"><meta property="og:type" content="website"><meta property="og:image" content="{BASE}{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(title)}"><meta property="og:site_name" content="Qui offre à qui"><meta name="twitter:image" content="{BASE}{img}"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:card" content="summary_large_image"><meta property="og:locale" content="fr_FR">
{FAVICON}
{FONTS}
<style>{CSS}{EXTRA_CSS}</style>
{sch}
<script src="/assets/track.js" defer></script>
</head>
<body>
'''

NAV = '<nav class="top"><div class="wrap"><a href="/">🎁 Qui offre à qui</a><span class="nav-d"><a class="nav-l" href="/qui-apporte-quoi/">Qui apporte quoi</a><a class="cta" href="/#outil">Faire un tirage</a></span></div></nav>'

def nlform(src, clair=False):
    return f'<form class="nlf" data-src="{src}" novalidate><input type="email" name="email" inputmode="email" autocomplete="email" placeholder="votre@email.fr" aria-label="Votre e-mail" required><button type="submit">Je m\'inscris</button></form><p class="nlm" role="status"></p>'
NLTXT = "Nos meilleures idées cadeaux avant les fêtes et un rappel pour le tirage de l'an prochain. Pas plus de 2 e-mails par mois, désinscription en un clic."
def nlencart(src):
    return f'<div class="carte nlbox" style="margin:24px 0"><h2>Recevez nos idées cadeaux</h2><p class="sous" style="margin:0">{NLTXT}</p>{nlform(src)}</div>'

def foot():
    bud = ''.join(f'<a href="/{p["slug"]}/">{p["slug"].split("-")[-2]} €</a>' for p in PAGES if groupe(p) == 'budget')
    cles = ["regles-pere-noel-secret", "pere-noel-secret-famille", "cadeau-secret-santa-collegue", "tirage-au-sort-secret-santa-whatsapp", "idee-cadeau-secret-santa-homme", "idee-cadeau-secret-santa-femme"]
    gd = ''.join(f'<li><a href="/{p["slug"]}/">{esc(court_titre(p))}</a></li>' for c in cles for p in PAGES if p["slug"] == c)
    return f'''<footer><div class="wrap">
<div class="nlpied"><h2>Ne ratez pas le tirage de l'an prochain</h2><p>{NLTXT}</p>{nlform("pied")}</div>
<div class="pied">
<div><h2>Idées cadeaux par budget</h2><div class="pastilles">{bud}</div>
<p style="margin-top:18px"><a class="btn" style="background:var(--or);color:var(--encre)" href="/#outil">Faire un tirage gratuit</a></p></div>
<div><h2>Guides</h2><ul>{gd}<li><a href="/qui-apporte-quoi/">Qui apporte quoi au repas</a></li><li><a href="/retrouver/">Retrouver mon tirage</a></li><li><a href="/guides/"><b>Tous les guides</b></a></li></ul></div>
</div>
<div class="bas">
<p>Tirage au sort de cadeaux en ligne, gratuit et sans compte. <a href="/mentions-legales/">Mentions légales et confidentialité</a></p><div class="soc"><span>Suivez-nous</span><a class="yt" href="https://www.youtube.com/channel/UCLPHpSiWZBkdT8f2UvPYF8w" rel="noopener" aria-label="Notre chaîne YouTube" title="YouTube"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3z"/></svg></a><a class="fb" href="https://www.facebook.com/122096271843567125" rel="noopener" aria-label="Notre page Facebook" title="Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-8.2h2.8l.5-3.3h-3.3V8.4c0-.9.4-1.7 1.8-1.7h1.6V3.8c-.3 0-1.3-.2-2.4-.2-2.5 0-4.1 1.5-4.1 4.2v2.7H7.6v3.3h2.8V22z"/></svg></a></div>
<p class="amz">En tant que Partenaire Amazon, Qui offre à qui réalise un bénéfice sur les achats remplissant les conditions requises.</p>
</div>
</div></footer>
</body>
</html>
'''

def w(rel, s):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(s)

def crumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": SITE, "item": BASE + "/"}] + items}

SEO_HOME = """<section class="carte"><h2>Comment faire un tirage au sort de cadeaux en ligne ?</h2>
<p>Qui offre à qui est un <strong>tirage au sort de cadeaux gratuit et sans compte</strong>. En 2 minutes, il remplace les papiers pliés dans un chapeau, même quand tout le monde n'est pas réuni.</p>
<ol>
<li><strong>Choisissez l'occasion et le budget</strong> : Noël, Nouvel An, anniversaire, collègues, amis, de 5 à 50 €.</li>
<li><strong>Ajoutez les prénoms</strong> des participants, et les exclusions si deux personnes ne doivent pas se tirer.</li>
<li><strong>Ajoutez l'e-mail de chacun</strong> : c'est là qu'il recevra son résultat.</li>
<li><strong>Lancez le tirage</strong> : chacun reçoit aussitôt un e-mail, ouvre son paquet et découvre à qui il offre un cadeau, avec des idées dans son budget.</li>
</ol>
<h3>Le tuto en vidéo (1 minute)</h3>
<div class="vid" data-yt="aLBfOgS4u3o"><button type="button" aria-label="Lire la vidéo : tirage au sort Père Noël secret en ligne, le tuto en 1 minute"><img src="/assets/video-tuto.jpg" alt="Tuto vidéo : faire un tirage au sort Père Noël secret en ligne avec Qui offre à qui" width="1280" height="720" loading="lazy"><span class="play" aria-hidden="true"></span></button></div>
<p class="vid-note">La vidéo YouTube ne se charge que si vous cliquez. <a href="https://www.youtube.com/watch?v=aLBfOgS4u3o" rel="noopener">La voir sur YouTube</a>.</p>
</section>
<section class="carte"><h2>Pourquoi utiliser Qui offre à qui ?</h2>
<ul>
<li><strong>Vraiment secret</strong> : le tirage est fait sur nos serveurs et chaque résultat part directement par e-mail. Personne ne sait qui offre à qui, pas même l'organisateur, qui peut donc participer.</li>
<li><strong>Sans compte</strong> : rien à créer, aucun mot de passe. Un lien de suivi permet de renvoyer un e-mail perdu, sans voir le résultat.</li>
<li><strong>100 % gratuit</strong>, sans limite de participants.</li>
<li><strong>Jamais son propre nom</strong> : le tirage exclut chaque personne d'elle-même et respecte vos exclusions.</li>
<li><strong>Idées cadeaux incluses</strong> : chacun voit des idées adaptées au budget, de <a href="/idee-cadeau-5-euros/">5 €</a> à <a href="/idee-cadeau-50-euros/">50 €</a>.</li>
<li><strong>Pour toutes les occasions</strong> : <a href="/regles-pere-noel-secret/">Père Noël secret</a> en famille, <a href="/cadeau-secret-santa-collegue/">Secret Santa entre collègues</a>, échange entre amis, classe ou club.</li>
</ul>
</section>
"""

# Accueil (outil)
tool = open(os.path.join(HERE, 'tool_body.html')).read()
tool = tool.replace('<main class="wrap">', '<main class="wrap" id="outil">', 1)
_pills = ''.join(f'<a href="/{p["slug"]}/">{p["slug"].split("-")[-2]} €</a>' for p in PAGES if groupe(p) == 'budget')
_top = [p for c in ["idee-cadeau-secret-santa-homme", "idee-cadeau-secret-santa-femme", "regles-pere-noel-secret", "cadeau-secret-santa-collegue"] for p in PAGES if p["slug"] == c]
guides = f'<p class="sous">Des idées par budget :</p><div class="pastilles clair">{_pills}</div><h3 style="margin-top:18px">Les guides les plus lus</h3>' + cartes(_top)
tool = tool.replace('</main>\n</div>\n\n<div id="vue-res"', f'<section class="carte"><h2>Idées et conseils</h2>{guides}<p style="margin-top:14px"><a href="/guides/">Voir tous les guides</a></p></section>\n</main>\n</div>\n\n<div id="vue-res"', 1)
faq = [("Le tirage au sort est-il vraiment gratuit ?", "Oui, entièrement gratuit, sans abonnement et sans option payante cachée."),
       ("Faut-il créer un compte ?", "Non. Vous entrez les prénoms et les e-mails des participants, et c'est tout : aucun compte, aucun mot de passe. Le tirage est prêt en 2 minutes."),
       ("Comment chaque participant reçoit-il son résultat ?", "Par e-mail, dès que le tirage est lancé. Il clique sur le bouton, ouvre son paquet et découvre à qui il offre un cadeau, avec des idées selon le budget."),
       ("L'organisateur peut-il voir qui offre à qui ?", "Non. Le tirage est fait sur nos serveurs et chaque résultat est envoyé directement au participant concerné. L'organisateur ne voit aucun résultat : il peut participer sans tricher."),
       ("J'ai perdu l'e-mail de mon tirage, comment le retrouver ?", "Allez sur la page Retrouver mon tirage et entrez votre adresse : vous recevez aussitôt un nouvel e-mail avec votre lien privé, la liste du repas et, si vous êtes l'organisateur, le suivi."),
       ("Et si quelqu'un ne reçoit pas son e-mail ?", "Demandez-lui de regarder dans ses spams. Sinon, la page de suivi du tirage (gardée sur votre appareil et envoyée par e-mail si vous laissez le vôtre) permet de renvoyer l'e-mail ou de corriger l'adresse, sans voir le résultat."),
       ("Peut-on empêcher deux personnes de se tirer ?", "Oui, avec les exclusions : par exemple deux conjoints ou deux frères et sœurs ne se tireront pas entre eux."),
       ("Combien de participants faut-il ?", "Au moins 3 personnes, et jusqu'à 40 : famille, classe, équipe ou club entier."),
       ("Peut-on l'utiliser pour autre chose que Noël ?", "Oui : Nouvel An, Saint-Nicolas, anniversaire, échange entre collègues ou entre amis, fin d'année d'une classe ou d'un club."),
       ("Quel budget choisir ?", "Le plus courant est de 10 à 20 €. Après le tirage, chacun voit des idées de cadeaux adaptées au budget choisi.")]

howto = {"@context": "https://schema.org", "@type": "HowTo", "name": "Faire un tirage au sort de cadeaux en ligne", "totalTime": "PT2M", "step": [{"@type": "HowToStep", "position": 1, "name": "Choisir l'occasion et le budget", "text": "Indiquez l'occasion, le nom de l'événement, le budget par cadeau et la date de l'échange."}, {"@type": "HowToStep", "position": 2, "name": "Ajouter les participants", "text": "Entrez le prénom et l'e-mail de chaque participant, au moins 3, et les éventuelles exclusions."}, {"@type": "HowToStep", "position": 3, "name": "Lancer le tirage", "text": "Cliquez sur Lancer le tirage et envoyer les e-mails : le tirage est fait en secret sur nos serveurs."}, {"@type": "HowToStep", "position": 4, "name": "Chacun reçoit son résultat", "text": "Chaque participant reçoit un e-mail et découvre à qui il offre un cadeau, avec des idées selon le budget. Personne d'autre ne connaît le tirage."}]}
sch_home = [howto, {"@context": "https://schema.org", "@type": "WebApplication", "name": SITE, "url": BASE + "/", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "inLanguage": "fr", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}},
            {"@context": "https://schema.org", "@type": "VideoObject", "name": "Tirage au sort Père Noël secret en ligne gratuit (Secret Santa) : le tuto en 1 minute", "description": "Comment faire un tirage au sort Père Noël secret en ligne, gratuit et sans compte : l'événement, les participants et leur e-mail, les exclusions, le lancement, puis ce que reçoit chaque participant.", "thumbnailUrl": BASE + "/assets/video-tuto.jpg", "uploadDate": "2026-11-26T12:55:00+01:00", "duration": "PT1M12S", "embedUrl": "https://www.youtube-nocookie.com/embed/aLBfOgS4u3o", "contentUrl": "https://www.youtube.com/watch?v=aLBfOgS4u3o", "inLanguage": "fr"},
            {"@context": "https://schema.org", "@type": "Organization", "name": SITE, "url": BASE + "/", "logo": BASE + "/assets/icon-512.png", "sameAs": ["https://www.youtube.com/channel/UCLPHpSiWZBkdT8f2UvPYF8w", "https://www.facebook.com/122096271843567125"]},
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
faq_html = '<section class="carte"><h2>Questions fréquentes</h2>' + ''.join(f'<h3>{esc(q)}</h3><p>{esc(a)}</p>' for q, a in faq) + '</section>'
tool = tool.replace('<section class="carte"><h2>Idées et conseils</h2>', SEO_HOME + faq_html + '<section class="carte"><h2>Idées et conseils</h2>', 1)
js = open(os.path.join(HERE, 'tool.js')).read()
home = head("Tirage au sort cadeau gratuit sans compte : Père Noël secret",
            "Tirage au sort Père Noël secret en ligne en 2 minutes : gratuit, sans compte, chacun reçoit son résultat par e-mail, même l'organisateur ne sait rien.",
            "/", sch_home) + NAV + tool + '<script>\n' + js + '\n</script>\n' + foot()
w('index.html', home)

# Guides
today = datetime.date.today().isoformat()
for p in PAGES:
    path = f'/{p["slug"]}/'
    body = amz(p["body"])
    qs = re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>', body.split('Questions fréquentes')[-1], re.S)
    sch = [{"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["desc"], "datePublished": p["date"], "dateModified": p.get("updated", p["date"]), "inLanguage": "fr", "mainEntityOfPage": BASE + path, "author": {"@type": "Organization", "name": SITE, "url": BASE + "/"}, "publisher": {"@type": "Organization", "name": SITE, "url": BASE + "/"}},
           crumb([{"@type": "ListItem", "position": 2, "name": p["title"], "item": BASE + path}])]
    if qs:
        sch.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub('<[^>]+>', '', q), "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in qs]})
    d = datetime.date.fromisoformat(p["date"])
    mois = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"][d.month-1]
    cta = '<div class="encart"><b>Faites votre tirage au sort en 2 minutes</b><p>Sans compte et 100 % gratuit : entrez les prénoms et les e-mails, chacun reçoit son résultat en secret.</p><a class="btn" href="' + p.get("outil", "/#outil") + '">' + p.get("outil_txt", "Faire mon tirage gratuit") + '</a></div>'
    promo = '<p class="encart" style="padding:14px 18px;margin:18px 0">🎁 <b>Pas encore fait le tirage ?</b> Sur <a href="/" style="color:#fff">Qui offre à qui</a>, il se fait en 2 minutes, sans compte et gratuitement.</p>'
    body = re.sub(r'(</p>)', r'\1' + promo, body, count=1)
    oth = [q for q in PAGES if q['slug'] != p['slug']]
    _g = [q for q in oth if 'euros' not in q['slug']]; _b = [q for q in oth if 'euros' in q['slug']]
    _i = PAGES.index(p)
    rel = (_g[_i % len(_g):] + _g[:_i % len(_g)])[:3] + (_b[_i % len(_b):] + _b[:_i % len(_b)])[:2]
    related = '<h2>À lire aussi</h2>' + cartes(rel)
    html_ = head(p["title"], p["desc"], path, sch) + NAV + f'<main class="wrap"><article><p class="meta"><a href="/">Accueil</a> › <a href="/guides/">Guides</a></p><h1>{esc(p["title"])}</h1><p class="meta">Publié le {d.day} {mois} {d.year}</p>{body}{cta}{nlencart('guide')}{related}</article></main>' + foot()
    w(f'{p["slug"]}/index.html', html_)

# Page hub des guides
hub = head("Tous les guides : idées cadeaux et Père Noël secret", "Tous nos guides : idées cadeaux par budget de 5 à 50 €, selon la personne, et conseils pour organiser un Père Noël secret ou un échange de cadeaux.", "/guides/", [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guides Qui offre à qui", "url": BASE + "/guides/"}]) + NAV + '<main class="wrap"><article><p class="meta"><a href="/">Accueil</a> › Guides</p><h1>Tous les guides</h1><p>Des idées de cadeaux pour chaque budget et chaque personne, et des conseils pour organiser votre échange. Le tirage au sort, lui, se fait en 2 minutes sur <a href="/">la page d\'accueil</a>, sans compte et gratuitement.</p>' + ''.join(f'<h2>{t}</h2>' + cartes([p for p in PAGES if groupe(p) == g]) for g, t in GROUPES) + '</article></main>' + foot()
w('guides/index.html', hub)

# Liste partagée « qui apporte quoi »
rbody = open(os.path.join(HERE, 'repas_body.html')).read()
rjs = open(os.path.join(HERE, 'repas.js')).read()
rfaq = [("Faut-il créer un compte ?", "Non. Vous créez la liste, vous partagez le lien, et chaque invité choisit ce qu'il apporte avec son prénom. Aucun compte, aucun mot de passe."),
        ("Comment les invités reçoivent-ils la liste ?", "Par un simple lien, à envoyer dans le groupe WhatsApp de la famille ou par SMS. Tout le monde voit la même liste, mise à jour en direct."),
        ("Peut-on ajouter des choses après coup ?", "Oui. Chaque invité peut ajouter une ligne dans une catégorie, ou libérer ce qu'il avait pris s'il change d'avis."),
        ("C'est seulement pour Noël ?", "Non : réveillon du Nouvel An, anniversaire, pique-nique, barbecue ou auberge espagnole. Choisissez un modèle ou partez d'une liste vide.")]
rseo = '<section class="carte"><h2>Organiser un repas où chacun apporte quelque chose</h2><p>Le repas de Noël en famille, le réveillon entre amis ou l\'auberge espagnole du bureau ont tous le même piège : sans liste, on se retrouve avec trois desserts et pas de pain. Une liste partagée règle le problème en quelques minutes.</p><ol><li><strong>Créez la liste</strong> à partir d\'un modèle (Noël, Nouvel An, anniversaire, pique-nique) et ajustez les lignes.</li><li><strong>Partagez le lien</strong> dans le groupe WhatsApp ou par SMS.</li><li><strong>Chacun choisit</strong> ce qu\'il apporte avec son prénom. La liste se met à jour pour tout le monde.</li></ol><p>Astuce : laissez les plats principaux à ceux qui reçoivent ou qui aiment cuisiner, et proposez les boissons, le pain et les fromages à ceux qui viennent de loin.</p></section>' + '<section class="carte"><h2>Questions fréquentes</h2>' + ''.join(f'<h3>{esc(q)}</h3><p>{esc(a)}</p>' for q, a in rfaq) + '</section>'
rbody = rbody.replace('<section class="carte">\n<h2>Pour la table</h2>', rseo + '\n<section class="carte">\n<h2>Pour la table</h2>', 1)
rsch = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "Qui apporte quoi : liste de repas partagée", "url": BASE + "/qui-apporte-quoi/", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "inLanguage": "fr", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in rfaq]}]
w('qui-apporte-quoi/index.html', head("Qui apporte quoi : liste de repas partagée gratuite", "Créez la liste du repas de Noël ou de la fête, partagez le lien, et chacun coche ce qu'il apporte. Gratuit, sans compte, mis à jour en direct pour tous.", "/qui-apporte-quoi/", rsch) + NAV + rbody + '<script>\n' + rjs + '\n</script>\n' + foot())

# Retrouver mon tirage (lien renvoyé par e-mail, jamais affiché sur le site)
rt = head("Retrouver mon tirage au sort", "Vous avez perdu l'e-mail de votre tirage ? Entrez votre adresse : vous recevez tout de suite vos liens (résultat, liste du repas, suivi). Gratuit.", "/retrouver/") + NAV + '''<header class="hero"><div class="ruban" aria-hidden="true"></div><div class="wrap"><h1>Retrouver mon tirage</h1><p>Vous ne trouvez plus l'e-mail de votre tirage ? Entrez votre adresse : nous vous renvoyons vos liens tout de suite.</p></div></header>
<main class="wrap"><section class="carte"><label for="rt-mail">Votre adresse e-mail</label><input id="rt-mail" type="email" inputmode="email" autocomplete="email" placeholder="vous@exemple.fr">
<button class="btn p" id="rt-go" style="margin-top:14px">Recevoir mes liens</button><p class="note" id="rt-msg" role="status" style="margin-top:12px"></p></section>
<section class="carte"><h2>Comment ça marche ?</h2><p>Vous recevez un e-mail avec un lien privé vers chacun de vos tirages : votre résultat si vous participez, la liste du repas, et le suivi si vous êtes l'organisateur. Pour garder le secret, rien ne s'affiche sur cette page : seule la personne qui lit cette boîte mail peut ouvrir les liens.</p><p>Rien reçu après quelques minutes ? Regardez dans les spams, ou essayez une autre adresse : c'est celle que l'organisateur a saisie qui compte.</p></section>
<div class="encart"><b>Pas encore de tirage ?</b><p>Le tirage au sort se fait en 2 minutes, sans compte : chacun reçoit son résultat par e-mail.</p><a class="btn" href="/#outil">Faire un tirage gratuit</a></div></main>
<script>(function(){var b=document.getElementById("rt-go"),i=document.getElementById("rt-mail"),m=document.getElementById("rt-msg");
function go(){var v=i.value.trim();if(!/^[^\\s@]+@[^\\s@]+\\.[a-z]{2,}$/i.test(v)){m.textContent="Cette adresse n'est pas valide.";return}b.disabled=true;b.textContent="Envoi...";
fetch("https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/qoaq",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({action:"retrouver",email:v})}).then(function(r){return r.json().then(function(j){j._s=r.status;return j})}).then(function(j){b.disabled=false;b.textContent="Recevoir mes liens";
m.textContent=j.ok?"C'est parti ! Si cette adresse a participé à un tirage, vous allez recevoir un e-mail avec vos liens dans quelques instants. Pensez aux spams.":j._s===429?"Trop de demandes. Réessayez dans une heure.":"Ça n'a pas marché, réessayez.";try{j.ok&&window.qoaqHit&&window.qoaqHit("mail","retrouver")}catch(e){}}).catch(function(){b.disabled=false;b.textContent="Recevoir mes liens";m.textContent="Pas de connexion, réessayez."})}
b.onclick=go;i.onkeydown=function(e){if(e.key==="Enter")go()};})();</script>''' + foot()
w('retrouver/index.html', rt)

# Page de retour newsletter (inscription, désinscription)
nl = head("Newsletter", "Inscription et désinscription à la newsletter de Qui offre à qui.", "/newsletter/", robots='noindex,follow') + NAV + '''<main class="wrap"><article><h1 id="t">Newsletter</h1><p id="m"></p><p><a class="btn p" style="width:auto;display:inline-block" href="/">Faire un tirage au sort</a></p><p><a href="/guides/">Voir les idées cadeaux</a></p></article></main>
<script>(function(){var r=new URLSearchParams(location.search).get("r"),t=document.getElementById("t"),m=document.getElementById("m");
if(r==="ok"){t.textContent="Merci, c'est noté !";m.textContent="Vous recevrez de temps en temps nos idées cadeaux et un rappel pour le tirage de l'an prochain. Chaque e-mail contient un lien pour vous désinscrire.";try{window.qoaqHit&&window.qoaqHit("lead","newsletter")}catch(e){}}
else if(r==="stop"){t.textContent="Vous êtes désinscrit";m.textContent="Nous ne vous écrirons plus. Vous pouvez toujours utiliser le tirage au sort gratuitement.";}
else{t.textContent="Ce lien n'est plus valable";m.textContent="Il a peut-être expiré. Rien de grave : vous pouvez faire un nouveau tirage quand vous voulez.";}})();</script>''' + foot()
w('newsletter/index.html', nl)

# Mentions légales
legal = head("Mentions légales et confidentialité", "Mentions légales, données personnelles et liens affiliés du site Qui offre à qui.", "/mentions-legales/", robots='noindex,follow') + NAV + '''<main class="wrap"><article><h1>Mentions légales et confidentialité</h1>
<h2>Éditeur</h2><p>Jérémy Dacier-Jury, 9 passage des Tisserands, 38790 Charantonnay. Contact : <a href="mailto:contact@cvlibre.com">contact@cvlibre.com</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Données personnelles</h2><p>Le tirage au sort est fait sur nos serveurs (Supabase, hébergé dans l'Union européenne) pour que personne, pas même l'organisateur, ne connaisse les résultats. Les prénoms et les adresses e-mail des participants servent uniquement à leur envoyer leur résultat (prestataire d'envoi : Resend) et à permettre à l'organisateur de renvoyer un e-mail. Ils sont supprimés automatiquement 8 mois après le tirage. Vos derniers tirages sont gardés sur votre appareil (stockage local du navigateur) ; vous pouvez les effacer à tout moment.</p><p><strong>Newsletter.</strong> Vous pouvez vous inscrire à notre newsletter (idées cadeaux, rappel du tirage de l'année suivante, 2 e-mails par mois au plus) en cliquant sur un bouton d'inscription, en cochant la case prévue lors du tirage ou en saisissant votre adresse dans un formulaire du site (vous confirmez alors par un clic dans un e-mail). Nous gardons votre prénom et votre adresse jusqu'à votre désinscription, possible en un clic dans chaque e-mail. Base légale : votre consentement. Sans cette inscription, nous n'écrivons jamais aux participants pour autre chose que leur tirage.</p><p><strong>E-mail de l'organisateur (facultatif).</strong> Il sert à envoyer la confirmation et le lien de suivi, et à retrouver vos tirages sur demande. Il est supprimé 8 mois après le tirage, sauf si vous vous inscrivez à la newsletter. Pour exercer vos droits (accès, suppression), écrivez à contact@cvlibre.com.</p><p>Nous mesurons l'audience de façon anonyme (pages vues, clics vers Amazon), sans donnée permettant de vous identifier.</p><p><strong>Vidéos.</strong> Les vidéos YouTube du site ne se chargent que si vous cliquez dessus, en mode « confidentialité renforcée » (youtube-nocookie.com). Une fois lancée, la vidéo est soumise aux règles de confidentialité de Google.</p><p><strong>Publicité.</strong> Le site affiche des annonces Google AdSense. Google et ses partenaires peuvent utiliser des cookies pour diffuser des annonces, personnalisées ou non selon votre choix dans le message de consentement. Vous pouvez modifier ce choix à tout moment et en savoir plus sur <a href="https://policies.google.com/technologies/ads?hl=fr" rel="noopener">la page de Google consacrée à la publicité</a>.</p>
<h2>Liens affiliés</h2><p>Certains liens vers Amazon sont des liens affiliés : en tant que Partenaire Amazon, Qui offre à qui réalise un bénéfice sur les achats remplissant les conditions requises, sans surcoût pour vous.</p>
</article></main>''' + foot()
w('mentions-legales/index.html', legal)

# 404
w('404.html', head("Page introuvable", "Cette page n'existe pas.", "/404.html", robots='noindex') + NAV + '<main class="wrap"><article><h1>Page introuvable</h1><p>Cette page n\'existe pas ou a été déplacée.</p><p><a class="btn p" href="/">Faire un tirage au sort</a></p></article></main>' + foot())

# Sitemap, robots, CNAME, IndexNow
urls = [("/", today, "1.0"), ("/qui-apporte-quoi/", today, "0.9"), ("/retrouver/", today, "0.5"), ("/guides/", today, "0.6")] + [(f'/{p["slug"]}/', p.get("updated", p["date"]), "0.8") for p in PAGES]
w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{BASE}{u}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>\n' for u, d, pr in urls) + '</urlset>\n')
BOTS = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckDuckBot", "YandexBot", "Qwantbot", "MistralAI-User", "CCBot"]
w('ads.txt', 'google.com, pub-8638687738606649, DIRECT, f08c47fec0942fa0\n')
w('robots.txt', 'User-agent: *\nAllow: /\nDisallow: /404.html\nDisallow: /media/\n\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in BOTS) + f'Sitemap: {BASE}/sitemap.xml\n')
# llms.txt : résumé du site pour les assistants IA (ChatGPT, Claude, Perplexity...)
budg = [p for p in PAGES if 'euros' in p['slug']]
autres = [p for p in PAGES if 'euros' not in p['slug']]
llms = f"""# {SITE}

> Qui offre à qui (qui-offre-a-qui.fr) est un outil gratuit de tirage au sort de cadeaux en ligne, en français : Père Noël secret, Secret Santa, échange de cadeaux du Nouvel An, de la Saint-Nicolas, d'anniversaire, entre collègues, entre amis ou dans une classe. Le tirage se fait en 2 minutes, sans compte et sans inscription, et chaque résultat est envoyé par e-mail.

## Ce que fait l'outil
- L'organisateur entre les prénoms (au moins 3), l'occasion, le budget par cadeau (5, 10, 15, 20, 30 ou 50 euros) et la date de l'échange.
- Il peut ajouter des exclusions : deux personnes qui ne doivent pas se tirer (par exemple un couple).
- L'organisateur entre aussi l'e-mail de chaque participant. Le tirage est fait en secret sur le serveur et chaque participant reçoit son résultat par e-mail : personne ne sait qui offre à qui, pas même l'organisateur.
- L'organisateur peut recevoir une confirmation et un lien de suivi pour renvoyer un e-mail ou corriger une adresse, sans voir les résultats.
- Les derniers tirages sont gardés sur l'appareil pour les retrouver.
- Après la révélation, chaque participant voit des idées de cadeaux adaptées au budget.
- Gratuit, sans publicité intrusive. Le site gagne de l'argent grâce aux liens affiliés Amazon des idées cadeaux.

## Outils
- [Faire un tirage au sort de cadeaux]({BASE}/): l'outil, avec la méthode et la FAQ.
- [Qui apporte quoi]({BASE}/qui-apporte-quoi/): liste de repas partagée par lien, chacun coche ce qu'il apporte, sans compte.

## Idées cadeaux par budget
""" + ''.join(f"- [{p['title']}]({BASE}/{p['slug']}/): {p['desc']}\n" for p in budg) + """
## Guides et conseils
""" + ''.join(f"- [{p['title']}]({BASE}/{p['slug']}/): {p['desc']}\n" for p in autres) + f"""
## Informations
- [Mentions légales et confidentialité]({BASE}/mentions-legales/)
- Contact : contact@cvlibre.com
"""
w('llms.txt', llms)
w('site.webmanifest', json.dumps({"name": "Qui offre à qui", "short_name": "Qui offre à qui", "start_url": "/", "display": "standalone", "background_color": "#123d34", "theme_color": "#123d34", "lang": "fr", "icons": [{"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}, {"src": "/assets/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, ensure_ascii=False))
w('CNAME', 'qui-offre-a-qui.fr\n')
w(f'{INDEXNOW}.txt', INDEXNOW)
w('.nojekyll', '')
bad = [f for f in os.listdir(OUT) if f.endswith('.html')]
for root, _, files in os.walk(OUT):
    if '.git' in root or root.startswith(HERE): continue
    for f in files:
        if f.endswith('.html') and re.search('[–—]', open(os.path.join(root, f), encoding='utf-8').read()):
            raise SystemExit('tiret long dans ' + os.path.join(root, f))
print('ok', len(PAGES), 'guides')
