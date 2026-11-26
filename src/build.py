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
from pages_noel import PAGES_NOEL
PAGES = PAGES + PAGES_NOEL
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
<meta name="google-site-verification" content="0tjo6Bj7KcNHJMLQKuavVd_d7pBDPoJX3TaLWRm1GA4">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{BASE}{path}"><meta property="og:type" content="website"><meta property="og:image" content="{BASE}/og.png"><meta name="twitter:card" content="summary_large_image"><meta property="og:locale" content="fr_FR">
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

SEO_HOME = """<section class="carte"><h2>Comment faire un tirage au sort de cadeaux en ligne ?</h2>
<p>Qui offre à qui est un <strong>tirage au sort de cadeaux gratuit et sans compte</strong>. En 2 minutes, il remplace les papiers pliés dans un chapeau, même quand tout le monde n'est pas réuni.</p>
<ol>
<li><strong>Choisissez l'occasion et le budget</strong> : Noël, Nouvel An, anniversaire, collègues, amis, de 5 à 50 €.</li>
<li><strong>Ajoutez les prénoms</strong> des participants, et les exclusions si deux personnes ne doivent pas se tirer.</li>
<li><strong>Lancez le tirage</strong> : chaque participant reçoit un lien privé.</li>
<li><strong>Envoyez les liens</strong> par e-mail, WhatsApp, SMS ou messagerie. Chacun ouvre son paquet et découvre à qui il offre un cadeau, avec des idées dans son budget.</li>
</ol>
</section>
<section class="carte"><h2>Pourquoi utiliser Qui offre à qui ?</h2>
<ul>
<li><strong>Sans compte, e-mail facultatif</strong> : des prénoms suffisent. Si vous voulez, chacun reçoit son lien par e-mail et vous recevez le récapitulatif.</li>
<li><strong>100 % gratuit</strong>, sans limite de participants.</li>
<li><strong>Vraiment secret</strong> : chaque lien n'affiche qu'un seul résultat, et l'organisateur peut participer sans tricher.</li>
<li><strong>Jamais son propre nom</strong> : le tirage exclut chaque personne d'elle-même et respecte vos exclusions.</li>
<li><strong>Idées cadeaux incluses</strong> : chacun voit des idées adaptées au budget, de <a href="/idee-cadeau-5-euros/">5 €</a> à <a href="/idee-cadeau-50-euros/">50 €</a>.</li>
<li><strong>Pour toutes les occasions</strong> : <a href="/regles-pere-noel-secret/">Père Noël secret</a> en famille, <a href="/cadeau-secret-santa-collegue/">Secret Santa entre collègues</a>, échange entre amis, classe ou club.</li>
</ul>
</section>
"""

# Accueil (outil)
tool = open(os.path.join(HERE, 'tool_body.html')).read()
tool = tool.replace('<main class="wrap">', '<main class="wrap" id="outil">', 1)
guides = ''.join(f'<li><a href="/{p["slug"]}/">{esc(p["title"])}</a></li>' for p in PAGES)
tool = tool.replace('</main>\n</div>\n\n<div id="vue-res"', f'<section class="carte"><h2>Idées et conseils</h2><ul>{guides}</ul></section>\n</main>\n</div>\n\n<div id="vue-res"', 1)
faq = [("Le tirage au sort est-il vraiment gratuit ?", "Oui, entièrement gratuit, sans abonnement et sans option payante cachée."),
       ("Faut-il créer un compte ou donner son e-mail ?", "Non. Des prénoms suffisent : aucun compte, aucun mot de passe, et le tirage est prêt en 2 minutes. L'e-mail est facultatif, il sert seulement à envoyer les liens par e-mail."),
       ("Peut-on envoyer les résultats par e-mail ?", "Oui. Ajoutez l'e-mail des participants qui le souhaitent : chacun reçoit son lien privé. L'organisateur peut aussi recevoir un récapitulatif avec tous les liens, pour les renvoyer si quelqu'un perd le sien."),
       ("Comment retrouver un tirage déjà fait ?", "Le tirage est gardé sur votre appareil : revenez sur le site, il apparaît dans « Vos derniers tirages ». Si vous avez donné votre e-mail, le récapitulatif contient aussi tous les liens."),
       ("L'organisateur peut-il voir qui offre à qui ?", "Non. Chaque lien privé n'affiche que le résultat de la personne concernée. Tant qu'il n'ouvre pas les liens des autres, l'organisateur peut participer sans connaître le tirage."),
       ("Comment chaque participant reçoit-il son résultat ?", "Après le tirage, chacun reçoit son lien privé par e-mail, ou vous l'envoyez par WhatsApp, SMS ou n'importe quelle messagerie."),
       ("Peut-on empêcher deux personnes de se tirer ?", "Oui, avec les exclusions : par exemple deux conjoints ou deux frères et sœurs ne se tireront pas entre eux."),
       ("Combien de participants faut-il ?", "Au moins 3 personnes. Il n'y a pas de maximum : famille, classe, équipe ou club entier."),
       ("Peut-on l'utiliser pour autre chose que Noël ?", "Oui : Nouvel An, Saint-Nicolas, anniversaire, échange entre collègues ou entre amis, fin d'année d'une classe ou d'un club."),
       ("Quel budget choisir ?", "Le plus courant est de 10 à 20 €. Après le tirage, chacun voit des idées de cadeaux adaptées au budget choisi.")]
howto = {"@context": "https://schema.org", "@type": "HowTo", "name": "Faire un tirage au sort de cadeaux en ligne", "totalTime": "PT2M", "step": [{"@type": "HowToStep", "position": 1, "name": "Choisir l'occasion et le budget", "text": "Indiquez l'occasion, le nom de l'événement, le budget par cadeau et la date de l'échange."}, {"@type": "HowToStep", "position": 2, "name": "Ajouter les participants", "text": "Entrez les prénoms des participants, au moins 3, et les éventuelles exclusions."}, {"@type": "HowToStep", "position": 3, "name": "Lancer le tirage", "text": "Cliquez sur Lancer le tirage au sort : chaque participant obtient un lien privé."}, {"@type": "HowToStep", "position": 4, "name": "Envoyer les liens", "text": "Envoyez à chacun son lien par e-mail, WhatsApp, SMS ou messagerie. Il découvre à qui il offre un cadeau et des idées selon le budget."}]}
sch_home = [howto, {"@context": "https://schema.org", "@type": "WebApplication", "name": SITE, "url": BASE + "/", "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "inLanguage": "fr", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}},
            {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
faq_html = '<section class="carte"><h2>Questions fréquentes</h2>' + ''.join(f'<h3>{esc(q)}</h3><p>{esc(a)}</p>' for q, a in faq) + '</section>'
tool = tool.replace('<section class="carte"><h2>Idées et conseils</h2>', SEO_HOME + faq_html + '<section class="carte"><h2>Idées et conseils</h2>', 1)
js = open(os.path.join(HERE, 'tool.js')).read()
home = head("Tirage au sort cadeau gratuit sans compte : Père Noël secret",
            "Tirage au sort Père Noël secret en ligne en 2 minutes : gratuit, sans compte, liens privés par e-mail ou WhatsApp par participant et des idées cadeaux selon le budget.",
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
    cta = '<div class="encart"><b>Faites votre tirage au sort en 2 minutes</b><p>Sans compte et 100 % gratuit : entrez les prénoms et chacun reçoit son lien privé, par e-mail ou WhatsApp.</p><a class="btn" href="/#outil">Faire mon tirage gratuit</a></div>'
    promo = '<p class="encart" style="padding:14px 18px;margin:18px 0">🎁 <b>Pas encore fait le tirage ?</b> Sur <a href="/" style="color:#fff">Qui offre à qui</a>, il se fait en 2 minutes, sans compte et gratuitement.</p>'
    body = re.sub(r'(</p>)', r'\1' + promo, body, count=1)
    oth = [q for q in PAGES if q['slug'] != p['slug']]
    _g = [q for q in oth if 'euros' not in q['slug']]; _b = [q for q in oth if 'euros' in q['slug']]
    _i = PAGES.index(p)
    rel = (_g[_i % len(_g):] + _g[:_i % len(_g)])[:3] + (_b[_i % len(_b):] + _b[:_i % len(_b)])[:2]
    related = '<h2>À lire aussi</h2><ul>' + ''.join(f'<li><a href="/{q["slug"]}/">{esc(q["title"])}</a></li>' for q in rel) + '</ul>'
    html_ = head(p["title"], p["desc"], path, sch) + NAV + f'<main class="wrap"><article><p class="meta"><a href="/">Accueil</a> › Idées et conseils</p><h1>{esc(p["title"])}</h1><p class="meta">Publié le {d.day} {mois} {d.year}</p>{body}{cta}{related}</article></main>' + foot()
    w(f'{p["slug"]}/index.html', html_)

# Mentions légales
legal = head("Mentions légales et confidentialité", "Mentions légales, données personnelles et liens affiliés du site Qui offre à qui.", "/mentions-legales/", robots='noindex,follow') + NAV + '''<main class="wrap"><article><h1>Mentions légales et confidentialité</h1>
<h2>Éditeur</h2><p>Jérémy Dacier-Jury, 9 passage des Tisserands, 38790 Charantonnay. Contact : <a href="mailto:contact@cvlibre.com">contact@cvlibre.com</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Données personnelles</h2><p>Le tirage au sort est calculé dans votre navigateur. Les prénoms et les résultats ne sont pas enregistrés sur nos serveurs : ils sont contenus dans les liens privés que vous partagez. Vos derniers tirages sont gardés sur votre appareil (stockage local du navigateur) pour que vous puissiez les retrouver ; vous pouvez les effacer à tout moment.</p><p><strong>Envoi par e-mail (facultatif).</strong> Si vous saisissez des adresses e-mail, elles sont transmises à notre prestataire d'envoi Resend uniquement pour envoyer les liens. Les adresses des participants ne sont pas conservées. L'adresse de l'organisateur est conservée seulement s'il coche la case de rappel : elle sert alors à envoyer un e-mail par an pour proposer un nouveau tirage, jusqu'à sa désinscription (lien dans chaque e-mail). Base légale : votre consentement. Pour exercer vos droits (accès, suppression), écrivez à contact@cvlibre.com.</p><p>Nous mesurons l'audience de façon anonyme (pages vues, clics vers Amazon), sans cookie publicitaire et sans donnée permettant de vous identifier.</p>
<h2>Liens affiliés</h2><p>Certains liens vers Amazon sont des liens affiliés : en tant que Partenaire Amazon, Qui offre à qui réalise un bénéfice sur les achats remplissant les conditions requises, sans surcoût pour vous.</p>
</article></main>''' + foot()
w('mentions-legales/index.html', legal)

# 404
w('404.html', head("Page introuvable", "Cette page n'existe pas.", "/404.html", robots='noindex') + NAV + '<main class="wrap"><article><h1>Page introuvable</h1><p>Cette page n\'existe pas ou a été déplacée.</p><p><a class="btn p" href="/">Faire un tirage au sort</a></p></article></main>' + foot())

# Sitemap, robots, CNAME, IndexNow
urls = [("/", today, "1.0")] + [(f'/{p["slug"]}/', p.get("updated", p["date"]), "0.8") for p in PAGES]
w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{BASE}{u}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>\n' for u, d, pr in urls) + '</urlset>\n')
BOTS = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckDuckBot", "YandexBot", "Qwantbot", "MistralAI-User", "CCBot"]
w('robots.txt', 'User-agent: *\nAllow: /\nDisallow: /404.html\n\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in BOTS) + f'Sitemap: {BASE}/sitemap.xml\n')
# llms.txt : résumé du site pour les assistants IA (ChatGPT, Claude, Perplexity...)
budg = [p for p in PAGES if 'euros' in p['slug']]
autres = [p for p in PAGES if 'euros' not in p['slug']]
llms = f"""# {SITE}

> Qui offre à qui (qui-offre-a-qui.fr) est un outil gratuit de tirage au sort de cadeaux en ligne, en français : Père Noël secret, Secret Santa, échange de cadeaux du Nouvel An, de la Saint-Nicolas, d'anniversaire, entre collègues, entre amis ou dans une classe. Le tirage se fait en 2 minutes, sans compte et sans inscription. L'e-mail est facultatif.

## Ce que fait l'outil
- L'organisateur entre les prénoms (au moins 3), l'occasion, le budget par cadeau (5, 10, 15, 20, 30 ou 50 euros) et la date de l'échange.
- Il peut ajouter des exclusions : deux personnes qui ne doivent pas se tirer (par exemple un couple).
- Le tirage est calculé dans le navigateur. Chaque participant reçoit un lien privé qui n'affiche que son propre résultat : personne ne voit qui offre à qui, pas même l'organisateur.
- Les liens s'envoient par e-mail, WhatsApp, SMS ou n'importe quelle messagerie. L'organisateur peut recevoir un récapitulatif par e-mail.
- Les derniers tirages sont gardés sur l'appareil pour les retrouver.
- Après la révélation, chaque participant voit des idées de cadeaux adaptées au budget.
- Gratuit, sans publicité intrusive. Le site gagne de l'argent grâce aux liens affiliés Amazon des idées cadeaux.

## Outil
- [Faire un tirage au sort de cadeaux]({BASE}/): l'outil, avec la méthode et la FAQ.

## Idées cadeaux par budget
""" + ''.join(f"- [{p['title']}]({BASE}/{p['slug']}/): {p['desc']}\n" for p in budg) + """
## Guides et conseils
""" + ''.join(f"- [{p['title']}]({BASE}/{p['slug']}/): {p['desc']}\n" for p in autres) + f"""
## Informations
- [Mentions légales et confidentialité]({BASE}/mentions-legales/)
- Contact : contact@cvlibre.com
"""
w('llms.txt', llms)
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
