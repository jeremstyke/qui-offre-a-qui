import base64,sys,json
from playwright.sync_api import sync_playwright
H='/home/claude/qui-offre-a-qui/tools/fonts/'
f=lambda n: base64.b64encode(open(H+n,'rb').read()).decode()
c=json.loads(sys.argv[1])
im='data:image/jpeg;base64,'+base64.b64encode(open(c['shot'],'rb').read()).decode()
GIFT='<svg viewBox="0 0 64 64"><path d="M32 21c-3-7-11-10-14-6-2.5 3.4 2 7 14 6zm0 0c3-7 11-10 14-6 2.5 3.4-2 7-14 6z" fill="#e9b949"/><rect x="13" y="29" width="38" height="24" rx="3.5" fill="#b8344a"/><rect x="10" y="20" width="44" height="11" rx="3.5" fill="#d2485f"/><rect x="28.5" y="20" width="7" height="33" fill="#e9b949"/></svg>'
HT=f"""<html><style>@font-face{{font-family:B;font-weight:800;src:url(data:font/woff2;base64,{f('bricolage-grotesque-latin-800-normal.woff2')})}}
@font-face{{font-family:A;font-weight:700;src:url(data:font/woff2;base64,{f('atkinson-hyperlegible-latin-700-normal.woff2')})}}
*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1920px;background:#123d34;color:#fff;font-family:A;position:relative;overflow:hidden}}
.r{{position:absolute;left:0;right:0;height:26px;background:repeating-linear-gradient(-45deg,#b3263a 0 40px,#fff 40px 58px,#1f6b4f 58px 98px,#fff 98px 116px)}}
.t{{position:absolute;left:70px;right:70px;top:150px;text-align:center}}
h1{{font:800 118px/1 B;letter-spacing:-.015em;text-wrap:balance}}
.big{{display:inline-block;margin-top:34px;font:800 84px/1.05 B;color:#123d34;background:#e9b949;border-radius:26px;padding:16px 34px;transform:rotate(-2deg);text-wrap:balance;max-width:940px}}
.ph{{position:absolute;left:250px;top:{c.get('phtop',860)}px;width:580px;height:1180px;border-radius:60px;background:#0b241f;padding:18px;transform:rotate(4deg);box-shadow:0 40px 90px rgba(0,0,0,.5)}}
.ph div{{width:544px;height:1144px;border-radius:44px;overflow:hidden;background:#fff}}.ph img{{width:544px;margin-top:-{c.get('y',0)*544/390}px}}
.g{{position:absolute;left:90px;top:{c.get('phtop',860)+380}px;width:230px;height:230px;transform:rotate(-12deg)}}
</style><body><div class="r" style="top:0"></div><div class="r" style="bottom:0"></div>
<div class="t"><h1>{c['h1']}</h1><div class="big">{c['big']}</div></div>
<div class="ph"><div><img src="{im}"></div></div><div class="g">{GIFT}</div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920}); pg.set_content(HT); pg.wait_for_timeout(500)
    pg.screenshot(path=c['out'],type='jpeg',quality=90); b.close()
