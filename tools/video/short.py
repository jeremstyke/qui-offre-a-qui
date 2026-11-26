import base64,os,sys
from playwright.sync_api import sync_playwright
H='/home/claude/qui-offre-a-qui/tools/fonts'
f=lambda n: base64.b64encode(open(os.path.join(H,n),'rb').read()).decode()
img=lambda n: 'data:image/jpeg;base64,'+base64.b64encode(open('/tmp/v/s/'+n,'rb').read()).decode()
GIFT='<svg viewBox="0 0 64 64"><path d="M32 21c-3-7-11-10-14-6-2.5 3.4 2 7 14 6zm0 0c3-7 11-10 14-6 2.5 3.4-2 7-14 6z" fill="#e9b949"/><rect x="13" y="29" width="38" height="24" rx="3.5" fill="#b8344a"/><rect x="10" y="20" width="44" height="11" rx="3.5" fill="#d2485f"/><rect x="28.5" y="20" width="7" height="33" fill="#e9b949"/></svg>'
shots=['liste0.jpg','liste1.jpg','liste2.jpg','liste3.jpg','liste4.jpg','bouton.jpg','res0.jpg','res1.jpg']
HTML=f"""<html><style>
@font-face{{font-family:B;font-weight:800;src:url(data:font/woff2;base64,{f('bricolage-grotesque-latin-800-normal.woff2')})}}
@font-face{{font-family:A;font-weight:700;src:url(data:font/woff2;base64,{f('atkinson-hyperlegible-latin-700-normal.woff2')})}}
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:#123d34;color:#fff;font-family:A;overflow:hidden;position:relative}}
.ruban{{position:absolute;left:0;right:0;height:26px;background:repeating-linear-gradient(-45deg,#b3263a 0 40px,#fff 40px 58px,#1f6b4f 58px 98px,#fff 98px 116px)}}
#hook{{position:absolute;left:80px;right:80px;top:560px;text-align:center}}
#hook h1{{font:800 124px/1.02 B;letter-spacing:-.01em}}
#hook p{{font:800 150px/1 B;color:#e9b949;margin-top:60px}}
#cap{{position:absolute;left:70px;right:70px;top:150px;height:400px;display:flex;align-items:center;justify-content:center;text-align:center;font:800 84px/1.08 B;text-wrap:balance}}
#cap b{{color:#e9b949;font-weight:800}}
#phone{{position:absolute;left:140px;top:600px;width:800px;height:1220px;border-radius:64px;background:#0b241f;padding:20px;box-shadow:0 40px 90px rgba(0,0,0,.45)}}
#scr{{position:relative;width:760px;height:1180px;border-radius:46px;overflow:hidden;background:#fff}}
#scr img{{position:absolute;left:0;top:0;width:760px;opacity:0}}
#tap{{position:absolute;width:220px;height:220px;margin:-110px 0 0 -110px;border-radius:50%;border:14px solid #e9b949;opacity:0}}
#cta{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;opacity:0}}
#cta svg{{width:360px;height:360px}}
#cta h2{{font:800 120px/1 B;margin-top:30px}}
#cta .u{{font:800 76px/1 B;color:#123d34;background:#e9b949;border-radius:28px;padding:26px 40px;margin-top:60px}}
#cta p{{font:700 54px/1.3 A;color:#d6e4de;margin-top:50px}}
</style><body><div class="ruban" style="top:0"></div><div class="ruban" style="bottom:0"></div>
<div id="hook"><h1>Encore les petits papiers dans un chapeau ?</h1><p>Stop.</p></div>
<div id="cap"></div>
<div id="phone"><div id="scr">{''.join(f'<img id="i{i}" src="{img(s)}">' for i,s in enumerate(shots))}<div id="tap"></div></div></div>
<div id="cta">{GIFT}<h2>Qui offre à qui</h2><div class="u">qui-offre-a-qui.fr</div><p>Gratuit, sans compte,<br>prêt en 2 minutes</p></div>
<script>
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
const cl=x=>x<0?0:x>1?1:x;
const caps=[[2.6,'Ajoutez les <b>prénoms</b> et les <b>e-mails</b>'],[6.4,'Un clic, et le tirage est fait'],[8.4,'Chacun reçoit <b>son</b> résultat par e-mail'],[10.6,'Même l\\'organisateur <b>ne sait rien</b>']];
function setT(t){{
 const hk=document.getElementById('hook');
 const a=ease(t/0.5); hk.style.opacity=t<2.6?a:cl(1-(t-2.6)/0.25);
 hk.style.transform=`scale(${{0.85+0.15*a}})`;
 hk.querySelector('p').style.opacity=cl((t-1.4)/0.15); hk.querySelector('p').style.transform=`scale(${{1.6-0.6*ease((t-1.4)/0.25)}})`;
 const ph=document.getElementById('phone');
 const pin=ease((t-2.6)/0.45), pout=cl((t-12)/0.3);
 ph.style.opacity=t<12?cl((t-2.6)/0.2):1-pout; ph.style.transform=`translateY(${{(1-pin)*500}}px)`;
 const cap=document.getElementById('cap'); let ci=-1; caps.forEach((c,i)=>{{if(t>=c[0])ci=i}});
 if(ci>=0&&t<12){{ if(cap.dataset.i!=ci){{cap.innerHTML='<span>'+caps[ci][1]+'</span>';cap.dataset.i=ci}} const k=ease((t-caps[ci][0])/0.3); cap.style.opacity=k; cap.style.transform=`translateY(${{(1-k)*40}}px)`; }} else {{cap.style.opacity=t>=12?1-pout:0}}
 // screens
 let on=0; if(t>=3.3)on=1; if(t>=4.0)on=2; if(t>=4.7)on=3; if(t>=5.4)on=4; if(t>=6.4)on=5; if(t>=8.4)on=6; if(t>=10.4)on=7;
 for(let i=0;i<8;i++){{const e=document.getElementById('i'+i); e.style.opacity=i===on?1:0; e.style.transform='none'}}
 if(on===7){{const e=document.getElementById('i7'); const k=ease((t-10.4)/0.35); e.style.opacity=k; document.getElementById('i6').style.opacity=1; }}
 if(on===6||on===7){{ /* zoom léger */ const z=1+0.04*cl((t-8.4)/3.6); document.getElementById('i6').style.transform=`scale(${{z}})`; const sy=-400*ease((t-10.5)/0.6); document.getElementById('i7').style.transform=`translateY(${{sy}}px) scale(${{z}})`; document.getElementById('i6').style.transformOrigin=document.getElementById('i7').style.transformOrigin='50% 40%';}}
 const tp=document.getElementById('tap'); const tt=(t-7.2)/0.6; tp.style.left='380px'; tp.style.top='{int(0.488*1645)}px';
 tp.style.opacity=tt>0&&tt<1?1-tt:0; tp.style.transform=`scale(${{0.4+tt*1.2}})`;
 const ct=document.getElementById('cta'); const ck=ease((t-12.2)/0.5); ct.style.opacity=ck; ct.style.transform=`scale(${{0.9+0.1*ck}})`;
}}
</script></body></html>"""
a,bf=float(sys.argv[1]),float(sys.argv[2]) if len(sys.argv)>2 else None
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':1080,'height':1920}); pg.set_content(HTML); pg.wait_for_timeout(500)
    if bf is None:
        for t in [1.8,4.6,7.3,9.0,11.2,13.5]:
            pg.evaluate(f'setT({t})'); pg.screenshot(path=f'/tmp/v/test_{t}.jpg',type='jpeg',quality=80)
    else:
        n=0; fps=30
        for i in range(int(a*fps),int(bf*fps)):
            pg.evaluate(f'setT({i/fps})'); pg.screenshot(path=f'/tmp/v/f/{i:04d}.jpg',type='jpeg',quality=92)
    br.close()
