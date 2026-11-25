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
.liens{display:flex;flex-wrap:wrap;gap:8px 16px;margin:6px 0 0}
footer a{color:var(--gris)}
.amz{font-size:13px;color:var(--gris)}
"""
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,800&family=Atkinson+Hyperlegible:wght@400;700&display=swap" rel="stylesheet">'
FAVICON = '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22%3E%3Crect x=%2210%22 y=%2230%22 width=%2280%22 height=%2260%22 rx=%228%22 fill=%22%23b8344a%22/%3E%3Crect x=%2244%22 y=%2230%22 width=%2212%22 height=%2260%22 fill=%22%23e9b949%22/%3E%3Crect x=%224%22 y=%2222%22 width=%2292%22 height=%2216%22 rx=%224%22 fill=%22%23123d34%22/%3E%3C/svg%3E">'

from pages import PAGES
def _k(p):
    m = re.search(r'(\d+)-euros', p['slug'])
    return (0, int(m.group(1))) if m else (1, 0)
PAGES = sorted(PAGES, key=_k)

def amz(s):
    return re.sub(r'\{AMZ:([^}]+)\}', lambda m: 'https://www.amazon.fr/s?k=' + quote_plus(m.group(1).strip()) + '&tag=' + TAG, s)

def esc(s): return html.escape(s, quote=True)

def head(title, desc, path, schema=None, robots='index,follow'):
    sch = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in (schema or []))
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{BASE}{path}"><meta property="og:type" content="website"><meta property="og:locale" content="fr_FR">
{FAVICON}
{FONTS}
<style>{CSS}{EXTRA_CSS}</style>
{sch}
<script src="/assets/track.js" defer></script>
</head>
<body>
'''

NAV = '<nav class="top"><div class="wrap"><a href="/">🎁 Qui offre à qui</a><a class="cta" href="/#outil">Faire un tirage</a></div></nav>'

def foot():
    links = ''.join(f'<a href="/{p["slug"]}/">{esc(p["title"].split(":")[0])}</a>' for p in PAGES)
    return f'''<footer><div class="wrap">
<p class="liens" style="justify-content:center">{links}</p>
<p>Tirage au sort de cadeaux gratuit, sans inscription. <a href="/mentions-legales/">Mentions légales et confidentialité</a>.</p>
<p class="amz">En tant que Partenaire Amazon, Qui offre à qui réalise un bénéfice sur les achats remplissant les conditions requises.</p>
</div></footer>
</body>
</html>
'''

def w(rel, s):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(s)

def crumb(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": SITE, "item": BASE + "/"}] + items}

# Accueil (outil)
tool = open(os.path.join(HERE, 'tool_body.html')).read()
tool = tool.replace('<main class="wrap">', '<main class="wrap" id="outil">', 1)
guides = ''.join(f'<li><a href="/{p["slug"]}/">{esc(p["title"])}</a></li>' for p in PAGES)
tool = tool.replace('</main>\n</div>\n\n<div id="vue-res"', f'<section class="carte"><h2>Idées et conseils</h2><ul>{guides}</ul></section>\n</main>\n</div>\n\n<div id="vue-res"', 1)
faq = [("Le tirage au sort est-il gratuit ?", "Oui, entièrement gratuit et sans inscription."),
       ("L'organisateur peut-il voir qui offre à qui ?", "Non. Chaque lien privé n'affiche que le résultat de la personne concernée. Les résultats ne sont enregistrés nulle part."),
       ("Peut-on empêcher deux personnes de se tirer ?", "Oui, avec les exclusions : par exemple deux conjoints ou deux frères et sœurs.")]
sch_home = [{"@context": "https://schema.org", "@type": "WebApplication", "name": SITE, "url": BASE + "/", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "inLanguage": "fr", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}},
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
faq_html = '<section class="carte"><h2>Questions fréquentes</h2>' + ''.join(f'<h3>{esc(q)}</h3><p>{esc(a)}</p>' for q, a in faq) + '</section>'
tool = tool.replace('<section class="carte"><h2>Idées et conseils</h2>', faq_html + '<section class="carte"><h2>Idées et conseils</h2>', 1)
js = open(os.path.join(HERE, 'tool.js')).read()
home = head("Tirage au sort cadeaux gratuit : Père Noël secret, Secret Santa",
            "Organisez votre Père Noël secret ou un échange de cadeaux en 1 minute : tirage au sort gratuit, sans inscription, un lien privé pour chaque participant.",
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
    cta = '<div class="encart"><b>Organisez votre tirage au sort en 1 minute</b><p>Gratuit, sans inscription, avec un lien privé pour chaque participant.</p><a class="btn" href="/#outil">Faire mon tirage</a></div>'
    html_ = head(p["title"], p["desc"], path, sch) + NAV + f'<main class="wrap"><article><p class="meta"><a href="/">Accueil</a> › Idées et conseils</p><h1>{esc(p["title"])}</h1><p class="meta">Publié le {d.day} {mois} {d.year}</p>{body}{cta}</article></main>' + foot()
    w(f'{p["slug"]}/index.html', html_)

# Mentions légales
legal = head("Mentions légales et confidentialité", "Mentions légales, données personnelles et liens affiliés du site Qui offre à qui.", "/mentions-legales/", robots='noindex,follow') + NAV + '''<main class="wrap"><article><h1>Mentions légales et confidentialité</h1>
<h2>Éditeur</h2><p>Jérémy Dacier-Jury, 9 passage des Tisserands, 38790 Charantonnay. Contact : <a href="mailto:contact@cvlibre.com">contact@cvlibre.com</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Données personnelles</h2><p>Le tirage au sort est calculé dans votre navigateur. Les prénoms et les résultats ne sont pas envoyés ni enregistrés sur nos serveurs : ils sont seulement contenus dans les liens privés que vous partagez. Nous mesurons l'audience de façon anonyme (pages vues, clics vers Amazon), sans cookie publicitaire et sans donnée permettant de vous identifier.</p>
<h2>Liens affiliés</h2><p>Certains liens vers Amazon sont des liens affiliés : en tant que Partenaire Amazon, Qui offre à qui réalise un bénéfice sur les achats remplissant les conditions requises, sans surcoût pour vous.</p>
</article></main>''' + foot()
w('mentions-legales/index.html', legal)

# 404
w('404.html', head("Page introuvable", "Cette page n'existe pas.", "/404.html", robots='noindex') + NAV + '<main class="wrap"><article><h1>Page introuvable</h1><p>Cette page n\'existe pas ou a été déplacée.</p><p><a class="btn p" href="/">Faire un tirage au sort</a></p></article></main>' + foot())

# Sitemap, robots, CNAME, IndexNow
urls = [("/", today, "1.0")] + [(f'/{p["slug"]}/', p.get("updated", p["date"]), "0.8") for p in PAGES]
w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{BASE}{u}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>\n' for u, d, pr in urls) + '</urlset>\n')
w('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n')
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
