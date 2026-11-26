import json,sys
sys.path.insert(0,'/tmp/t'); from fonts import route
from playwright.sync_api import sync_playwright
HIDE='ins,.adsbygoogle{display:none!important}'
S='/tmp/v2/s/'
P=[{"i":k,"nom":n,"email":n.lower().replace("é","e")+"@mail.fr","envois":1,"statut":"envoye","le":"2026-11-26T18:00:00Z"} for k,n in enumerate(["Léa","Tom","Mamie","Hugo","Papa"])]
ITEMS=[("Apéritif","Toasts et tartinades","Tom",""),("Apéritif","Biscuits apéro","",""),("Entrée","Saumon fumé","Mamie","pour 8"),("Plat","Chapon aux marrons","Papa",""),("Plat","Gratin dauphinois","",""),("Dessert","Bûche de Noël","Léa","chocolat"),("Dessert","Chocolats","Hugo",""),("Boissons","Champagne","Papa",""),("Boissons","Jus de fruits et sodas","","")]
def mk(n):
    its=[{"id":i+1,"cat":c,"label":l,"qui":(q if (i<n and q) else None),"note":nt or None,"pos":i} for i,(c,l,q,nt) in enumerate(ITEMS)]
    return {"ok":True,"liste":{"id":"abcdefgh23","titre":"Noël chez Mamie","date_ev":"2026-12-24","lieu":"Lyon","updated_at":"2026-11-26T18:00:00Z","items":its}}
state={'n':0}
def fn(r):
    try: b=json.loads(r.request.post_data or '{}')
    except: b={}
    a=b.get('action')
    if a=='etat': body={"ok":True,"ev":"Noël en famille 2026","budget":"20","date":"2026-12-24","cree":"2026-11-26T18:00:00Z","liste":"abcdefgh23","participants":P}
    elif a and a.startswith('liste_'): body=mk(state['n'])
    else: body={"ok":True}
    r.fulfill(status=200,content_type='application/json',body=json.dumps(body),headers={"Access-Control-Allow-Origin":"*","Access-Control-Allow-Headers":"content-type"})
def sh(pg,n): pg.screenshot(path=S+n,type='jpeg',quality=92)
with sync_playwright() as p:
    b=p.chromium.launch()
    c=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2.5,is_mobile=True,has_touch=True,locale='fr-FR'); route(c)
    c.route('**/functions/v1/qoaq**',fn)
    pg=c.new_page(); pg.add_init_script("localStorage.setItem('aff_moi','1')")
    pg.goto('http://localhost:8765/#g=12.0123456789abcdef01234567'); pg.wait_for_timeout(1800); pg.add_style_tag(content=HIDE)
    pg.evaluate("var s=document.getElementById('res-info');if(s){s.scrollIntoView({block:'start'});scrollBy(0,-160)}"); pg.wait_for_timeout(300)
    sh(pg,'suivi.jpg')
    Y={}
    for n in [0,9]:
        state['n']=n
        pg.goto('about:blank'); pg.goto('http://localhost:8765/qui-apporte-quoi/#l=abcdefgh23&n=L%C3%A9a'); pg.wait_for_timeout(1500); pg.add_style_tag(content=HIDE)
        Y['ap']=pg.evaluate('''document.evaluate("//*[normalize-space(text())='Apéritif']",document,null,9,null).singleNodeValue.getBoundingClientRect().top+scrollY''')
        Y['h']=pg.evaluate("document.documentElement.scrollHeight")
        pg.evaluate("scrollTo(0,0)"); pg.screenshot(path=S+f'full{n}.jpg',type='jpeg',quality=90,full_page=True)
    json.dump(Y,open(S+'y.json','w')); print(Y)
    b.close()
