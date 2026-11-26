(function(){
var $=function(i){return document.getElementById(i)};
var noms=["Marie","Thomas","Julie","Lucas","Emma"],mails=["","","","",""];
var API="https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/qoaq";
var MSG="Pour votre Père Noël secret ou votre échange de cadeaux : le tirage au sort se fait en 2 minutes, gratuit et sans compte, et chacun reçoit son résultat par e-mail. https://qui-offre-a-qui.fr/";
function brancherPartage(){
  document.querySelectorAll("[data-wa]").forEach(function(a){a.href="https://wa.me/?text="+encodeURIComponent(MSG.replace("https://qui-offre-a-qui.fr/","https://qui-offre-a-qui.fr/?src=wa-"+a.dataset.wa));a.onclick=function(){try{window.qoaqHit&&window.qoaqHit("partage","site-wa-"+a.dataset.wa)}catch(e){}}});
  document.querySelectorAll("[data-partage]").forEach(function(b){b.onclick=function(){var u="https://qui-offre-a-qui.fr/?src=partage-"+b.dataset.partage;try{window.qoaqHit&&window.qoaqHit("partage","site-"+b.dataset.partage)}catch(e){}
    if(navigator.share){navigator.share({title:"Qui offre à qui",text:MSG.replace(/ https.*$/,""),url:u}).catch(function(){})}
    else if(navigator.clipboard){navigator.clipboard.writeText(MSG.replace("https://qui-offre-a-qui.fr/",u)).then(function(){b.textContent="Lien copié"})}}});
}
try{if(/[?&]src=participant/.test(location.search))localStorage.setItem("qoaq_src","participant");else if(/[?&]src=/.test(location.search)&&!localStorage.getItem("qoaq_src"))localStorage.setItem("qoaq_src",(location.search.match(/[?&]src=([a-z0-9-]{1,30})/)||[,""])[1])}catch(e){}
function escH(x){return String(x||"").replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function rendreListe(){
  var l=$("liste");l.innerHTML="";
  noms.forEach(function(n,i){
    var d=document.createElement("div");d.className="pers";
    d.innerHTML='<input class="nom" aria-label="Prénom '+(i+1)+'" placeholder="Prénom" value="'+escH(n)+'"><input class="mail" type="email" inputmode="email" autocomplete="off" aria-label="E-mail de la personne '+(i+1)+'" placeholder="E-mail de '+escH(n||"la personne")+'" value="'+escH(mails[i])+'"><button class="x" aria-label="Retirer">×</button>';
    var ins=d.querySelectorAll("input");
    ins[0].oninput=function(e){noms[i]=e.target.value;rendreExc()};
    ins[1].oninput=function(e){mails[i]=e.target.value.trim()};
    d.querySelector("button").onclick=function(){noms.splice(i,1);mails.splice(i,1);rendreListe();rendreExc()};
    l.appendChild(d);
  });
}
var excs=[[0,1]];
function opts(sel){return noms.map(function(n,i){return '<option value="'+i+'"'+(i==sel?" selected":"")+'>'+(n||"Personne "+(i+1))+'</option>'}).join("")}
function rendreExc(){
  var e=$("excs");e.innerHTML="";
  excs=excs.filter(function(p){return p[0]<noms.length&&p[1]<noms.length});
  excs.forEach(function(p,k){
    var d=document.createElement("div");d.className="exc";
    d.innerHTML='<select aria-label="Personne">'+opts(p[0])+'</select><span>et</span><select aria-label="Personne">'+opts(p[1])+'</select><button class="x" aria-label="Retirer">×</button>';
    var s=d.querySelectorAll("select");
    s[0].onchange=function(){p[0]=+this.value};s[1].onchange=function(){p[1]=+this.value};
    d.querySelector("button").onclick=function(){excs.splice(k,1);rendreExc()};
    e.appendChild(d);
  });
}
$("ajout").onclick=function(){noms.push("");mails.push("");rendreListe();rendreExc();var ins=document.querySelectorAll("#liste input.nom");ins[ins.length-1].focus()};
$("ajoutExc").onclick=function(){if(noms.length>1){excs.push([0,1]);rendreExc()}};

function decode(t){var s=atob(t),r="";for(var i=0;i<s.length;i++)r+=String.fromCharCode(s.charCodeAt(i)^23);return JSON.parse(decodeURIComponent(escape(r)))}
var EMAIL=/^[^\s@<>"]+@[^\s@<>"]+\.[a-z]{2,24}$/i;
var courant=null;
function post(o){return fetch(API,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(o)}).then(function(r){return r.json().then(function(j){j._s=r.status;return j})})}
function afficherSuivi(T,parts,neuf){
  courant=T;$("res").classList.remove("cache");
  var ok=parts.filter(function(p){return p.statut==="envoye"}).length;
  $("res-titre").textContent=neuf?"C'est tiré et envoyé !":"Suivi de votre tirage";
  $("res-info").textContent=(T.ev?"« "+T.ev+" » : ":"")+(ok>1?ok+" participants ont reçu leur résultat":ok+" participant a reçu son résultat")+" par e-mail. Personne ne connaît le tirage, pas même vous."+(ok<parts.length?" Certains envois ont échoué : vérifiez l'adresse et renvoyez.":"");
  var rr=$("res-repas");if(T.liste){rr.innerHTML='Liste commune du repas : <a href="/qui-apporte-quoi/#l='+escH(T.liste)+'">voir qui apporte quoi</a>. Les participants la retrouvent sous leur résultat.';rr.classList.remove("cache")}else rr.classList.add("cache");
  var ul=$("suivi");ul.innerHTML="";
  parts.forEach(function(p){
    var li=document.createElement("li");
    var st=p.statut==="envoye"?'<span class="ok">Envoyé</span>':'<span class="ko">Échec de l\'envoi</span>';
    li.innerHTML='<div class="l1"><b>'+escH(p.nom)+'</b>'+st+'</div><div class="l2"><span class="em">'+escH(p.email)+'</span><span class="act"><button class="btn s petit r1">Renvoyer</button><button class="btn s petit r2">Corriger l\'e-mail</button></span></div><div class="l3 cache"><input type="email" inputmode="email" aria-label="Nouvelle adresse de '+escH(p.nom)+'" value="'+escH(p.email)+'"><button class="btn s petit r3">Envoyer</button></div><p class="msg" role="status"></p>';
    var msg=li.querySelector(".msg");
    function renvoyer(email,bt){
      bt.disabled=true;var avant=bt.textContent;bt.textContent="Envoi...";msg.textContent="";
      post({action:"renvoyer",id:T.id,g:T.g,i:p.i,email:email||""}).then(function(j){
        if(j.ok){afficherSuivi(T,j.participants,false);}
        else{bt.disabled=false;bt.textContent=avant;msg.textContent=j._s===429?"Trop de renvois pour ce tirage.":j.raison==="email"?"Cette adresse n'est pas valide.":"L'envoi n'a pas marché, réessayez."}
      }).catch(function(){bt.disabled=false;bt.textContent=avant;msg.textContent="Pas de connexion, réessayez."});
    }
    li.querySelector(".r1").onclick=function(){renvoyer("",this)};
    li.querySelector(".r2").onclick=function(){li.querySelector(".l3").classList.toggle("cache");li.querySelector(".l3 input").focus()};
    li.querySelector(".r3").onclick=function(){var v=li.querySelector(".l3 input").value.trim();if(!EMAIL.test(v)){msg.textContent="Cette adresse n'est pas valide.";return}renvoyer(v,this)};
    ul.appendChild(li);
  });
}
function memoriser(T){
  try{var L=JSON.parse(localStorage.getItem("qoaq_suivis")||"[]");L.unshift(T);localStorage.setItem("qoaq_suivis",JSON.stringify(L.slice(0,8)))}catch(e){}
  rendreMes();
}
function suivre(T){
  $("res").classList.remove("cache");$("suivi").innerHTML="";$("res-titre").textContent="Suivi de votre tirage";$("res-info").textContent="Chargement...";
  post({action:"etat",id:T.id,g:T.g}).then(function(j){
    if(j.ok){T.ev=j.ev;T.liste=j.liste||T.liste;afficherSuivi(T,j.participants,false)}
    else $("res-info").textContent="Ce tirage n'est plus disponible : les adresses sont effacées 30 jours après l'échange.";
  }).catch(function(){$("res-info").textContent="Pas de connexion, réessayez."});
  $("res").scrollIntoView({behavior:"smooth"});
}
function rendreMes(){
  var L=[],R=[];try{L=JSON.parse(localStorage.getItem("qoaq_suivis")||"[]");R=JSON.parse(localStorage.getItem("qoaq_resultats")||"[]")}catch(e){}
  var c=$("mes");if(!c)return;
  if(!L.length&&!R.length){c.classList.add("cache");return}
  c.classList.remove("cache");var ul=$("mes-l");ul.innerHTML="";
  R.forEach(function(x){var li=document.createElement("li");li.innerHTML='<span><b>'+escH(x.ev)+'</b><small>Votre résultat ('+escH(x.de)+')</small></span><span class="act"><a class="btn s petit" href="'+escH(x.u)+'">Revoir</a></span>';ul.appendChild(li)});
  L.forEach(function(T,k){
    var li=document.createElement("li");
    var dt=new Date(T.ts).toLocaleDateString("fr-FR",{day:"numeric",month:"long"});
    li.innerHTML='<span><b>'+escH(T.ev)+'</b><small>'+T.n+' participants, tiré le '+dt+'</small></span><span class="act"><button class="btn s petit">Suivre</button><button class="x" aria-label="Oublier ce tirage">×</button></span>';
    var b=li.querySelectorAll("button");
    b[0].onclick=function(){suivre(T)};
    b[1].onclick=function(){L.splice(k,1);try{localStorage.setItem("qoaq_suivis",JSON.stringify(L))}catch(e){}rendreMes()};
    ul.appendChild(li);
  });
}

$("tirer").onclick=function(){
  var bt=this,err=$("err");err.textContent="";
  var liste=noms.map(function(n){return n.trim()});
  if(liste.length<3||liste.some(function(n){return !n})){err.textContent="Il faut au moins 3 prénoms, sans ligne vide.";return}
  for(var q=0;q<liste.length;q++){if(!EMAIL.test(mails[q]||"")){err.textContent=mails[q]?"L'e-mail de "+liste[q]+" n'est pas valide.":"Il manque l'e-mail de "+liste[q]+" : c'est là que son résultat sera envoyé.";var m=document.querySelectorAll("#liste input.mail")[q];m&&m.focus();return}}
  var o=$("m-orga").value.trim();
  if(o&&!EMAIL.test(o)){err.textContent="Votre e-mail n'est pas valide (ou laissez la case vide).";return}
  var ty=$("type").value,ev=$("ev").value.trim()||NOMS[ty],b=$("budget").value,d=$("date").value;
  bt.disabled=true;var avant=bt.textContent;bt.textContent="Tirage et envoi en cours...";
  post({t:ty,ev:ev,b:b,d:d,orga:o,rappel:$("m-rappel").checked,excl:excs,parts:liste.map(function(n,i){return {nom:n,email:mails[i]}})}).then(function(j){
    bt.disabled=false;bt.textContent=avant;
    if(j.id){
      var T={id:j.id,g:j.g,ev:ev,ts:Date.now(),n:liste.length,liste:j.liste||null};
      memoriser(T);afficherSuivi(T,j.participants,true);
      try{var src="";try{src=localStorage.getItem("qoaq_src")||""}catch(e){}if(window.qoaqHit){window.qoaqHit("tirage",ty+"|"+liste.length+"|"+b+"|"+src);window.qoaqHit("mail",String(j.envoyes))}}catch(e){}
      $("res").scrollIntoView({behavior:"smooth"});
    } else err.textContent=j.raison==="exclusions"?"Impossible avec ces exclusions. Retirez-en une et relancez.":j.raison==="email"?"Une adresse e-mail n'est pas valide : vérifiez la liste.":j._s===429?"Trop de tirages depuis votre connexion. Réessayez dans une heure.":"Le tirage n'a pas marché. Réessayez dans un instant.";
  }).catch(function(){bt.disabled=false;bt.textContent=avant;err.textContent="Pas de connexion. Vérifiez votre réseau et réessayez."});
};

var NOMS={noel:"Père Noël secret",nouvelan:"Échange de cadeaux du Nouvel An",stnicolas:"Saint-Nicolas",anniv:"Échange de cadeaux d'anniversaire",collegues:"Échange de cadeaux entre collègues",amis:"Échange de cadeaux entre amis",classe:"Échange de cadeaux de fin d'année",autre:"Échange de cadeaux"};
var DEF={noel:["Noël en famille 2026","2026-12-24"],nouvelan:["Nouvel An entre amis","2026-12-31"],stnicolas:["Saint-Nicolas en famille","2026-12-06"],anniv:["Anniversaire de Léa",""],collegues:["Cadeaux de l'équipe",""],amis:["Soirée cadeaux entre amis",""],classe:["Fin d'année du club",""],autre:["Échange de cadeaux",""]};
$("type").onchange=function(){var x=DEF[this.value];$("ev").value=x[0];$("date").value=x[1]};
var IDEES={
 "5":[["Bonbons originaux","Toujours un succès","bonbons originaux"],["Chaussettes fantaisie","Drôles et utiles","chaussettes fantaisie"],["Baume à lèvres","Indispensable en hiver","baume levres"],["Mini plante grasse","Un peu de vert","mini plante grasse"]],
 "10":[["Mug original","Un classique qui fait toujours plaisir","mug cadeau original"],["Chaussettes de Noël","Drôles et douillettes","chaussettes noel fantaisie"],["Jeu de cartes d'apéro","Pour rire entre amis","jeu de cartes apero"],["Bougie parfumée","Une ambiance cocooning","bougie parfumee"]],
 "20":[["Plaid tout doux","Pour les soirées d'hiver","plaid polaire doux"],["Jeu de société rapide","Une partie en 15 minutes","jeu de societe ambiance"],["Coffret thé ou café","Pour les gourmands","coffret the cadeau"],["Lampe veilleuse","Jolie sur une table de nuit","lampe veilleuse deco"]],
 "30":[["Enceinte Bluetooth","Petite mais puissante","enceinte bluetooth portable"],["Coffret cocktail","Pour jouer au barman","coffret cocktail"],["Livre de recettes","Du nouveau en cuisine","livre de recettes"],["Gourde isotherme","Utile tous les jours","gourde isotherme inox"]],
 "15":[["Coffret de thés","Pour les pauses gourmandes","coffret the"],["Jeu de cartes rapide","Parfait pour les soirées","jeu de cartes ambiance"],["Bougie parfumée","Une ambiance cocooning","bougie parfumee"],["Chaussettes de Noël","Drôles et douillettes","chaussettes noel fantaisie"]],
 "50":[["Écouteurs sans fil","Un vrai cadeau plaisir","ecouteurs sans fil"],["Appareil à fondue ou raclette","Pour les repas à plusieurs","appareil raclette"],["Lampe de lecture","Pour les lecteurs du soir","lampe de lecture led"],["Coffret jeu de société expert","Des heures de jeu","jeu de societe strategie"]]
};
function afficherRes(o){
  try{localStorage.setItem("qoaq_src","participant")}catch(e){}
  try{var R=JSON.parse(localStorage.getItem("qoaq_resultats")||"[]").filter(function(x){return x.u!==location.href});R.unshift({u:location.href,ev:o.e,de:o.de,ts:Date.now()});localStorage.setItem("qoaq_resultats",JSON.stringify(R.slice(0,8)))}catch(e){}
  $("vue-orga").classList.add("cache");$("vue-res").classList.remove("cache");
  $("r-titre").textContent="Bonjour "+o.de;
  var dt=o.d?new Date(o.d+"T12:00").toLocaleDateString("fr-FR",{day:"numeric",month:"long"}):"";
  $("r-ev").textContent=o.e+(dt?", échange le "+dt:"");
  if(o.t&&o.t!=="noel"){document.querySelector("#vue-res .hero h1").style.maxWidth="none"}
  $("r-pour").textContent=o.a;$("r-budget").textContent="Budget : "+o.b+" € environ";$("r-b").textContent=o.b;var gd={"5":"/idee-cadeau-5-euros/","10":"/idee-cadeau-10-euros/","15":"/idee-cadeau-15-euros/","20":"/idee-cadeau-20-euros/","30":"/idee-cadeau-30-euros/","50":"/idee-cadeau-50-euros/"};$("r-guide").href=$("r-guide2").href=gd[o.b]||"/idee-cadeau-20-euros/";$("r-b2").textContent=o.b;
  var g=$("grille");g.innerHTML="";
  (IDEES[o.b]||IDEES["20"]).forEach(function(x){
    var a=document.createElement("div");a.className="idee";
    a.innerHTML='<b>'+x[0]+'</b><span>'+x[1]+'</span><a class="btn s petit" target="_blank" rel="sponsored nofollow noopener" href="https://www.amazon.fr/s?k='+encodeURIComponent(x[2])+'&tag=quioffreaqui-21">Voir les idées</a>';
    g.appendChild(a);
  });
  var lienPerso=location.href;
  $("r-copie").onclick=function(){var bt=this;navigator.clipboard&&navigator.clipboard.writeText(lienPerso).then(function(){bt.textContent="Lien copié"})};
  var pm=location.hash.match(/[&#]p=(\d+\.\d+\.[a-f0-9]{16})/);
  if(pm){var dejaNl=false;try{dejaNl=localStorage.getItem("qoaq_nl")==="1"}catch(e){}
    if(!dejaNl){$("nl-ok").onclick=function(){var bt=this;bt.disabled=true;bt.textContent="Inscription...";
      post({action:"abo",p:pm[1]}).then(function(x){if(x.ok){bt.textContent="C'est noté, merci !";$("nl-msg").textContent="Vous recevrez nos idées cadeaux et le rappel de l'an prochain.";setTimeout(function(){$("nl").classList.add("cache")},4000);try{localStorage.setItem("qoaq_nl","1");window.qoaqHit&&window.qoaqHit("lead","newsletter")}catch(e){}}else{bt.disabled=false;bt.textContent="Réessayer"}}).catch(function(){bt.disabled=false;bt.textContent="Réessayer"})};}
  }
  if(o.l&&/^[a-z0-9]{10}$/.test(o.l)){
    var lien="/qui-apporte-quoi/#l="+o.l+"&n="+encodeURIComponent(o.de);$("r-repas-lien").href=lien;
    var rendreRepas=function(L){
      var ordre=[],par={};L.items.forEach(function(i){if(!par[i.cat]){par[i.cat]=[];ordre.push(i.cat)}par[i.cat].push(i)});
      var w=$("r-repas-l");w.innerHTML=ordre.map(function(c){return '<h3 class="rr-cat">'+escH(c)+'</h3><ul class="rp-items">'+par[c].map(function(i){return '<li class="'+(i.qui?"pris":"")+'"><span class="lab">'+escH(i.label)+'</span>'+(i.qui?'<span class="qui">'+escH(i.qui)+'</span>'+(i.qui===o.de?'<button class="x" data-l="'+i.id+'" aria-label="Libérer">×</button>':''):'<button class="btn s petit" data-p="'+i.id+'">Je m\'en occupe</button>')+'</li>'}).join("")+'</ul>'}).join("");
      w.querySelectorAll("button[data-p],button[data-l]").forEach(function(b){b.onclick=function(){b.disabled=true;post({action:"liste_prendre",id:o.l,item:+(b.dataset.p||b.dataset.l),qui:b.dataset.p?o.de:""}).then(function(x){if(x.ok){rendreRepas(x.liste);try{window.qoaqHit&&window.qoaqHit("liste_maj","tirage")}catch(e){}}else b.disabled=false}).catch(function(){b.disabled=false})}});
    };
    post({action:"liste_lire",id:o.l}).then(function(x){if(x.ok){rendreRepas(x.liste);$("r-repas").dataset.ok="1";if($("paquet").classList.contains("ouvert"))$("r-repas").classList.remove("cache")}}).catch(function(){});
    try{var M=JSON.parse(localStorage.getItem("qoaq_listes")||"[]").filter(function(x){return x.id!==o.l});M.unshift({id:o.l,t:o.e,ts:Date.now()});localStorage.setItem("qoaq_listes",JSON.stringify(M.slice(0,12)));localStorage.setItem("qoaq_prenom",o.de)}catch(e){}
  }
  function ouvrir(){if(!$("paquet").classList.contains("ouvert")){if(pm){var d0=false;try{d0=localStorage.getItem("qoaq_nl")==="1"}catch(e){}if(!d0)$("nl").classList.remove("cache")}try{window.qoaqHit&&window.qoaqHit("reveal",o.b)}catch(e){}}$("paquet").classList.add("ouvert");$("nom").classList.remove("cache");$("r-idees").classList.remove("cache");$("r-autre").classList.remove("cache");if($("r-repas").dataset.ok)$("r-repas").classList.remove("cache")}
  $("paquet").onclick=ouvrir;$("paquet").onkeydown=function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();ouvrir()}};
}
window.addEventListener("hashchange",function(){if(/r=/.test(location.hash))location.reload()});
var gm=location.hash.match(/g=(\d+)\.([a-f0-9]{24})/);
var m=location.hash.match(/r=([^&]+)/);
if(m){try{afficherRes(decode(m[1]))}catch(e){rendreListe();rendreExc();rendreMes()}}else{rendreListe();rendreExc();rendreMes();if(gm){var GT={id:+gm[1],g:gm[2],ev:"",ts:Date.now(),n:0};suivre(GT)}}
brancherPartage();
})();