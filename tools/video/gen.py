import base64,sys,json,os
from playwright.sync_api import sync_playwright
H='/home/claude/qui-offre-a-qui/tools/fonts/'
f=lambda n: base64.b64encode(open(H+n,'rb').read()).decode()
cfg=json.load(open(sys.argv[1])); mode=sys.argv[2]
imgs=[]
for p in cfg['shots']: imgs.append('data:image/jpeg;base64,'+base64.b64encode(open(p,'rb').read()).decode())
GIFT='<svg viewBox="0 0 64 64"><path d="M32 21c-3-7-11-10-14-6-2.5 3.4 2 7 14 6zm0 0c3-7 11-10 14-6 2.5 3.4-2 7-14 6z" fill="#e9b949"/><rect x="13" y="29" width="38" height="24" rx="3.5" fill="#b8344a"/><rect x="10" y="20" width="44" height="11" rx="3.5" fill="#d2485f"/><rect x="28.5" y="20" width="7" height="33" fill="#e9b949"/></svg>'
HTML=f"""<html><style>
@font-face{{font-family:B;font-weight:800;src:url(data:font/woff2;base64,{f('bricolage-grotesque-latin-800-normal.woff2')})}}
@font-face{{font-family:A;font-weight:700;src:url(data:font/woff2;base64,{f('atkinson-hyperlegible-latin-700-normal.woff2')})}}
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:#123d34;color:#fff;font-family:A;overflow:hidden;position:relative}}
.ruban{{position:absolute;left:0;right:0;height:26px;background:repeating-linear-gradient(-45deg,#b3263a 0 40px,#fff 40px 58px,#1f6b4f 58px 98px,#fff 98px 116px)}}
#hook{{position:absolute;left:80px;right:80px;top:540px;text-align:center}}
#hook h1{{font:800 120px/1.02 B;letter-spacing:-.01em;text-wrap:balance}}
#hook p{{font:800 96px/1.05 B;color:#e9b949;margin-top:60px;text-wrap:balance}}
#cap{{position:absolute;left:70px;right:70px;top:150px;height:400px;display:flex;align-items:center;justify-content:center;text-align:center;font:800 82px/1.08 B}}
#cap span{{text-wrap:balance}}#cap b{{color:#e9b949;font-weight:800}}
#phone{{position:absolute;left:140px;top:600px;width:800px;height:1220px;border-radius:64px;background:#0b241f;padding:20px;box-shadow:0 40px 90px rgba(0,0,0,.45)}}
#scr{{position:relative;width:760px;height:1180px;border-radius:46px;overflow:hidden;background:#fff}}
#scr img{{position:absolute;left:0;top:0;width:760px;opacity:0}}
#cta{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;opacity:0}}
#cta svg{{width:360px;height:360px}}
#cta h2{{font:800 120px/1 B;margin-top:30px}}
#cta .u{{font:800 76px/1 B;color:#123d34;background:#e9b949;border-radius:28px;padding:26px 40px;margin-top:60px}}
#cta p{{font:700 54px/1.3 A;color:#d6e4de;margin-top:50px}}
</style><body><div class="ruban" style="top:0"></div><div class="ruban" style="bottom:0"></div>
<div id="hook"><h1>{cfg['h1']}</h1><p>{cfg['p']}</p></div>
<div id="cap"></div>
<div id="phone"><div id="scr">{''.join(f'<img id="i{i}" src="{s}">' for i,s in enumerate(imgs))}</div></div>
<div id="cta">{GIFT}<h2>Qui offre à qui</h2><div class="u">qui-offre-a-qui.fr</div><p>{cfg.get('cta','Gratuit, sans compte,<br>prêt en 2 minutes')}</p></div>
<script>
const SEG={json.dumps(cfg['seg'],ensure_ascii=False)}, CAPS={json.dumps(cfg['caps'],ensure_ascii=False)}, N={len(imgs)}, K=760/390;
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3), cl=x=>x<0?0:x>1?1:x, io=x=>x<0?0:x>1?1:(x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2);
const $=i=>document.getElementById(i);
function setT(t){{
 const hk=$('hook'); const a=ease(t/0.5); hk.style.opacity=t<2.6?a:cl(1-(t-2.6)/0.25); hk.style.transform=`scale(${{0.85+0.15*a}})`;
 const hp=hk.querySelector('p'); hp.style.opacity=cl((t-1.2)/0.2); hp.style.transform=`scale(${{1.3-0.3*ease((t-1.2)/0.3)}})`;
 const ph=$('phone'); const pin=ease((t-2.6)/0.45), pout=cl((t-12)/0.3);
 ph.style.opacity=t<12?cl((t-2.6)/0.2):1-pout; ph.style.transform=`translateY(${{(1-pin)*500}}px)`;
 let ci=-1; CAPS.forEach((c,i)=>{{if(t>=c[0])ci=i}}); const cap=$('cap');
 if(ci>=0&&t<12){{ if(cap.dataset.i!=ci){{cap.innerHTML='<span>'+CAPS[ci][1]+'</span>';cap.dataset.i=ci}} const k=ease((t-CAPS[ci][0])/0.3); cap.style.opacity=k; cap.style.transform=`translateY(${{(1-k)*40}}px)`; }} else cap.style.opacity=t>=12?1-pout:0;
 for(let i=0;i<N;i++){{$('i'+i).style.opacity=0}}
 let si=0; SEG.forEach((s,i)=>{{if(t>=s[0])si=i}}); const s=SEG[si];
 const e=$('i'+s[1]); e.style.opacity=1; const y=s[2]+(s[3]-s[2])*io((t-s[0]-(s[5]||0.3))/((s[4]-s[0])-(s[5]||0.3)-0.3)); e.style.transform=`translateY(${{-y*K}}px)`;
 if(si>0){{const p=SEG[si-1]; const fk=cl((t-s[0])/0.25); if(fk<1){{const pe=$('i'+p[1]); if(p[1]!==s[1]){{pe.style.opacity=1-fk; e.style.opacity=fk; pe.style.transform=`translateY(${{-p[3]*K}}px)`}} }} }}
 const ct=$('cta'); const ck=ease((t-12.2)/0.5); ct.style.opacity=ck; ct.style.transform=`scale(${{0.9+0.1*ck}})`;
}}
</script></body></html>"""
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':1080,'height':1920}); pg.set_content(HTML); pg.wait_for_timeout(800)
    out=cfg['out']
    if mode=='test':
        for t in cfg['tests']:
            pg.evaluate(f'setT({t})'); pg.screenshot(path=f'{out}_t{t}.jpg',type='jpeg',quality=80)
    else:
        os.makedirs(out+'_f',exist_ok=True)
        for i in range(450):
            pg.evaluate(f'setT({i/30})'); pg.screenshot(path=f'{out}_f/{i:04d}.jpg',type='jpeg',quality=92)
    br.close()
