import base64,os,sys,json
from playwright.sync_api import sync_playwright
H='/home/claude/qui-offre-a-qui/tools/fonts/'
f=lambda n: base64.b64encode(open(H+n,'rb').read()).decode()
img=lambda n: 'data:image/jpeg;base64,'+base64.b64encode(open('/tmp/t/s/'+n,'rb').read()).decode()
B=json.load(open('/tmp/t/boxes.json'))
GIFT='<svg viewBox="0 0 64 64"><path d="M32 21c-3-7-11-10-14-6-2.5 3.4 2 7 14 6zm0 0c3-7 11-10 14-6 2.5 3.4-2 7-14 6z" fill="#e9b949"/><rect x="13" y="29" width="38" height="24" rx="3.5" fill="#b8344a"/><rect x="10" y="20" width="44" height="11" rx="3.5" fill="#d2485f"/><rect x="28.5" y="20" width="7" height="33" fill="#e9b949"/></svg>'
SH=['s1.jpg','s2.jpg','s3.jpg','s4.jpg','res0.jpg']+[f'resA{k}.jpg' for k in range(8)]+['res1.jpg','guide2.jpg','repas.jpg']
# chapitres : (début, numéro, titre, texte)
CH=[(6,'Étape 1','L\'événement','Choisissez l\'occasion, le nom, le budget par cadeau et la date de l\'échange.'),
    (14,'Étape 2','Les participants','Ajoutez le prénom et l\'e-mail de chacun. C\'est là qu\'il recevra son résultat.'),
    (24,'Étape 3','Les exclusions','Facultatif : deux conjoints ou deux frères et sœurs ne se tireront pas entre eux.'),
    (31,'Étape 4','Lancer le tirage','Laissez votre e-mail pour le suivi, puis un clic : le tirage est fait en secret.'),
    (39,'Résultat','Chacun reçoit un e-mail','Avec son lien privé, des idées cadeaux à son budget et la liste du repas.'),
    (49,'Résultat','Le paquet s\'ouvre','Chacun découvre à qui il offre. Personne d\'autre ne le sait, pas même l\'organisateur.'),
    (58,'Bonus','Idées cadeaux et repas','Des idées de 5 à 50 € et une liste « qui apporte quoi » partagée par tous.')]
HTML=f"""<html><style>
@font-face{{font-family:B;font-weight:800;src:url(data:font/woff2;base64,{f('bricolage-grotesque-latin-800-normal.woff2')})}}
@font-face{{font-family:A;font-weight:400;src:url(data:font/woff2;base64,{f('atkinson-hyperlegible-latin-400-normal.woff2')})}}
@font-face{{font-family:A;font-weight:700;src:url(data:font/woff2;base64,{f('atkinson-hyperlegible-latin-700-normal.woff2')})}}
*{{margin:0;box-sizing:border-box}}
body{{width:1920px;height:1080px;background:#123d34;color:#fff;font-family:A;overflow:hidden;position:relative}}
.ruban{{position:absolute;left:0;right:0;height:16px;background:repeating-linear-gradient(-45deg,#b3263a 0 26px,#fff 26px 38px,#1f6b4f 38px 64px,#fff 64px 76px)}}
#side{{position:absolute;left:96px;top:0;width:520px;height:1080px;display:flex;flex-direction:column;justify-content:center}}
#num{{display:inline-block;align-self:flex-start;font:700 30px A;color:#123d34;background:#e9b949;border-radius:999px;padding:10px 24px}}
#tt{{font:800 76px/1.02 B;margin-top:26px;text-wrap:balance}}
#tx{{font:400 34px/1.4 A;color:#d6e4de;margin-top:28px}}
#win{{position:absolute;left:690px;top:150px;width:1140px;height:760px;border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 40px 100px rgba(0,0,0,.45)}}
#bar{{height:48px;background:#e8eeeb;display:flex;align-items:center;gap:10px;padding:0 20px}}
#bar i{{width:14px;height:14px;border-radius:50%;background:#c7d3ce;display:block}}
#url{{margin-left:20px;flex:1;height:30px;border-radius:15px;background:#fff;font:700 17px/30px A;color:#3c4d47;padding-left:18px}}
#vp{{position:relative;width:1140px;height:712px;overflow:hidden}}
#vp img{{position:absolute;left:0;top:0;width:1140px;opacity:0}}
#mailw{{position:absolute;inset:48px 0 0 0;background:#eef2f0;opacity:0}}
#mailh{{height:96px;background:#fff;border-bottom:1px solid #dde5e1;padding:18px 34px;font:700 24px A;color:#1d2a26}}
#mailh span{{display:block;font:400 19px A;color:#5b6b66;margin-top:6px}}
#mailz{{position:absolute;left:0;right:0;top:96px;bottom:0;overflow:hidden}}
#mailc{{position:absolute;left:250px;top:24px;width:640px;border-radius:12px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,.12)}}
#mailc img{{width:640px;display:block}}
#hl{{position:absolute;border:6px solid #e9b949;border-radius:18px;box-shadow:0 0 0 2000px rgba(18,61,52,.28);opacity:0}}
#tap{{position:absolute;width:120px;height:120px;margin:-60px 0 0 -60px;border-radius:50%;border:10px solid #e9b949;opacity:0}}
#cur{{position:absolute;width:44px;height:44px;opacity:0}}
#intro,#outro{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;opacity:0}}
#intro svg,#outro svg{{width:220px;height:220px}}
#intro h1{{font:800 104px/1.02 B;margin-top:26px;max-width:1500px;text-wrap:balance}}
#intro p{{font:700 46px A;color:#e9b949;margin-top:30px}}
#outro h2{{font:800 96px/1 B;margin-top:20px}}
#outro .u{{font:800 64px/1 B;color:#123d34;background:#e9b949;border-radius:24px;padding:24px 40px;margin-top:44px}}
#outro p{{font:700 40px/1.3 A;color:#d6e4de;margin-top:36px}}
#chips{{position:absolute;left:690px;top:944px;display:flex;gap:10px;opacity:0}}
#chips span{{font:700 20px A;padding:8px 16px;border-radius:999px;background:rgba(255,255,255,.08);color:#9fc0b4}}
#chips span.on{{background:#e9b949;color:#123d34}}
#marque{{position:absolute;left:96px;bottom:60px;display:flex;align-items:center;gap:14px;font:700 26px A;opacity:0}}
#marque svg{{width:40px;height:40px}}
</style><body><div class="ruban" style="top:0"></div><div class="ruban" style="bottom:0"></div>
<div id="intro">{GIFT}<h1>Tirage au sort Père Noël secret en ligne</h1><p>Le tuto en 1 minute : gratuit et sans compte</p></div>
<div id="side"><span id="num"></span><h2 id="tt"></h2><p id="tx"></p></div>
<div id="win"><div id="bar"><i></i><i></i><i></i><div id="url">qui-offre-a-qui.fr</div></div>
<div id="vp">{''.join(f'<img id="i{i}" src="{img(s)}">' for i,s in enumerate(SH))}<div id="hl"></div><div id="tap"></div>
<svg id="cur" viewBox="0 0 24 24"><path d="M4 2l16 9-7 2-3 7z" fill="#fff" stroke="#123d34" stroke-width="1.6" stroke-linejoin="round"/></svg></div>
<div id="mailw"><div id="mailh">Léa, votre tirage pour « Noël en famille 2026 » est prêt<span>De : Qui offre à qui</span></div><div id="mailz"><div id="mailc"><img src="{img('mail.jpg')}"></div></div></div></div>
<div id="chips"><span>1. Événement</span><span>2. Participants</span><span>3. Exclusions</span><span>4. Lancer</span><span>Résultat</span><span>Bonus</span></div>
<div id="marque">{GIFT}qui-offre-a-qui.fr</div>
<div id="outro">{GIFT}<h2>Qui offre à qui</h2><div class="u">qui-offre-a-qui.fr</div><p>Gratuit, sans compte, prêt en 2 minutes</p></div>
<script>
const CH={json.dumps(CH,ensure_ascii=False)}, BX={json.dumps(B)};
const K=1140/1280;
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3), cl=x=>x<0?0:x>1?1:x, io=x=>x<0?0:x>1?1:(x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2);
const $=id=>document.getElementById(id);
function show(idx,op){{for(let i=0;i<{len(SH)};i++){{const e=$('i'+i);e.style.opacity=0;e.style.transform='none'}} if(idx!=null){{const e=$('i'+idx);e.style.opacity=op??1}}}}
function hl(b,k,pad=10){{const e=$('hl'); if(!b||k<=0){{e.style.opacity=0;return}} e.style.left=(b[0]*K-pad)+'px';e.style.top=(b[1]*K-pad)+'px';e.style.width=(b[2]*K+2*pad)+'px';e.style.height=(b[3]*K+2*pad)+'px';e.style.opacity=k}}
function setT(t){{
 const ik=t<6?ease(t/0.8)*(1-cl((t-5.5)/0.5)):0; $('intro').style.opacity=ik; $('intro').style.transform=`scale(${{0.94+0.06*ease(t/0.8)}})`;
 const main=t>=5.8&&t<66.2; const mk=cl((t-5.8)/0.5)*(1-cl((t-65.8)/0.4));
 ['side','win','chips','marque'].forEach(i=>$(i).style.opacity=mk);
 $('win').style.transform=`translateX(${{(1-ease((t-5.8)/0.7))*120}}px)`;
 let ci=-1; CH.forEach((c,i)=>{{if(t>=c[0])ci=i}});
 if(ci>=0){{ const c=CH[ci]; if($('tt').dataset.i!=ci){{$('num').textContent=c[1];$('tt').textContent=c[2];$('tx').textContent=c[3];$('tt').dataset.i=ci}}
   const k=ease((t-c[0])/0.5); $('side').style.transform=`translateY(${{(1-k)*30}}px)`; ['num','tt','tx'].forEach((i,j)=>$(i).style.opacity=mk*ease((t-c[0]-j*0.08)/0.4)); }}
 const chipOn=[0,1,2,3,4,4,5][ci]; document.querySelectorAll('#chips span').forEach((s,i)=>s.className=i===chipOn?'on':'');
 $('mailw').style.opacity=0; $('tap').style.opacity=0; $('cur').style.opacity=0; hl(null,0);
 // scènes
 if(t<14){{ show(0); hl(BX.s1,ease((t-7.2)/0.5)); }}
 else if(t<24){{ show(1); hl(BX.s2,ease((t-15)/0.5)); }}
 else if(t<31){{ show(2); hl(BX.s3,ease((t-25)/0.5)); }}
 else if(t<39.4){{ show(3); hl(BX.s4,ease((t-32)/0.5)*(1-cl((t-35.4)/0.3)));
   const tb=BX.tirer, tx=(tb[0]+tb[2]/2)*K, ty=(tb[1]+tb[3]/2)*K; const m=io((t-35.6)/1.4);
   const cx=900+(tx-900)*m, cy=650+(ty-650)*m; const cu=$('cur'); cu.style.opacity=t>35.5?1:0; cu.style.left=cx+'px'; cu.style.top=cy+'px';
   const tp=(t-37.3)/0.6; const T=$('tap'); T.style.left=tx+'px'; T.style.top=ty+'px'; T.style.opacity=tp>0&&tp<1?1-tp:0; T.style.transform=`scale(${{0.4+tp*1.4}})`;
   const pr=$('i3'); pr.style.transform=t>37.3&&t<37.5?'scale(.995)':'none'; }}
 else if(t<49){{ show(null); const w=$('mailw'); w.style.opacity=ease((t-39.2)/0.4); const s=io((t-42)/5)*(1067*0.98-560); $('mailc').style.transform=`translateY(${{-s}}px)`; }}
 else if(t<58){{ // résultat
   if(t<51.5){{ show(4); hl(BX.paquet,ease((t-50)/0.4),14); const pb=BX.paquet, px=(pb[0]+pb[2]/2)*K, py=(pb[1]+pb[3]/2)*K; const cu=$('cur'); cu.style.opacity=t>49.8?1:0; const m=io((t-49.8)/1.2); cu.style.left=(px+260-260*m)+'px'; cu.style.top=(py+200-200*m)+'px'; const tp=(t-51.1)/0.5; const T=$('tap'); T.style.left=px+'px';T.style.top=py+'px';T.style.opacity=tp>0&&tp<1?1-tp:0;T.style.transform=`scale(${{0.4+tp*1.4}})`; }}
   else {{ const fi=Math.min(7,Math.floor((t-51.5)/0.12)); if(t<52.5) show(5+fi); else {{ show(13); const sc=1+0.05*cl((t-52.5)/5); $('i13').style.transform=`scale(${{sc}})`; $('i13').style.transformOrigin='50% 55%'; }} }} }}
 else {{ if(t<62.2) {{ show(14); $('i14').style.transform=`translateY(${{-io((t-58.6)/3.2)*220}}px)`; }} else {{ show(15); $('i15').style.opacity=ease((t-62.2)/0.4); }} }}
 const ok=ease((t-66.2)/0.6); $('outro').style.opacity=t>=66.2?ok:0; $('outro').style.transform=`scale(${{0.94+0.06*ok}})`;
}}
</script></body></html>"""
open('/tmp/t/tuto.html','w').write(HTML)
args=sys.argv[1:]
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':1920,'height':1080}); pg.set_content(HTML); pg.wait_for_timeout(600)
    if args[0]=='test':
        for t in map(float,args[1:]):
            pg.evaluate(f'setT({t})'); pg.screenshot(path=f'/tmp/t/test_{t}.jpg',type='jpeg',quality=85)
    else:
        a,b=float(args[0]),float(args[1])
        for i in range(int(a*30),int(b*30)):
            pg.evaluate(f'setT({i/30})'); pg.screenshot(path=f'/tmp/t/f/{i:05d}.jpg',type='jpeg',quality=92)
    br.close()
