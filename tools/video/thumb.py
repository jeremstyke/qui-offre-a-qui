import base64,sys
sys.path.insert(0,'/tmp/t')
from playwright.sync_api import sync_playwright
H='/home/claude/qui-offre-a-qui/tools/fonts/'
f=lambda n: base64.b64encode(open(H+n,'rb').read()).decode()
im='data:image/jpeg;base64,'+base64.b64encode(open('/tmp/t/s/m_res1.jpg','rb').read()).decode()
GIFT='<svg viewBox="0 0 64 64"><path d="M32 21c-3-7-11-10-14-6-2.5 3.4 2 7 14 6zm0 0c3-7 11-10 14-6 2.5 3.4-2 7-14 6z" fill="#e9b949"/><rect x="13" y="29" width="38" height="24" rx="3.5" fill="#b8344a"/><rect x="10" y="20" width="44" height="11" rx="3.5" fill="#d2485f"/><rect x="28.5" y="20" width="7" height="33" fill="#e9b949"/></svg>'
H_=f"""<html><style>@font-face{{font-family:B;font-weight:800;src:url(data:font/woff2;base64,{f('bricolage-grotesque-latin-800-normal.woff2')})}}
@font-face{{font-family:A;font-weight:700;src:url(data:font/woff2;base64,{f('atkinson-hyperlegible-latin-700-normal.woff2')})}}
*{{margin:0;box-sizing:border-box}}body{{width:1280px;height:720px;background:#123d34;color:#fff;font-family:A;position:relative;overflow:hidden}}
.r{{position:absolute;left:0;right:0;height:14px;background:repeating-linear-gradient(-45deg,#b3263a 0 22px,#fff 22px 32px,#1f6b4f 32px 54px,#fff 54px 64px)}}
.t{{position:absolute;left:64px;top:70px;width:720px}}
h1{{font:800 104px/0.98 B;letter-spacing:-.015em}}
.big{{display:inline-block;margin-top:26px;font:800 92px/1 B;color:#123d34;background:#e9b949;border-radius:22px;padding:14px 28px;transform:rotate(-2deg)}}
.s{{font:700 38px A;color:#d6e4de;margin-top:30px}}
.ph{{position:absolute;right:70px;top:46px;width:360px;height:700px;border-radius:44px;background:#0b241f;padding:14px;transform:rotate(4deg);box-shadow:0 30px 70px rgba(0,0,0,.5)}}
.ph div{{width:332px;height:672px;border-radius:32px;overflow:hidden;background:#fff}}.ph img{{width:332px;margin-top:-4px}}
.g{{position:absolute;right:360px;top:430px;width:170px;height:170px;transform:rotate(-10deg)}}
</style><body><div class="r" style="top:0"></div><div class="r" style="bottom:0"></div>
<div class="t"><h1>Tirage au sort Secret Santa</h1><div class="big">en 2 min</div><p class="s">Gratuit, sans compte, vraiment secret</p></div>
<div class="ph"><div><img src="{im}"></div></div><div class="g">{GIFT}</div></body></html>"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':720}); pg.set_content(H_); pg.wait_for_timeout(400)
    pg.screenshot(path='/tmp/t/qoaq-miniature-tuto.jpg',type='jpeg',quality=92); b.close()
