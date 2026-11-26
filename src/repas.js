(function(){
var $=function(i){return document.getElementById(i)};
var API="https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/qoaq";
function esc(x){return String(x==null?"":x).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function post(o){return fetch(API,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(o)}).then(function(r){return r.json().then(function(j){j._s=r.status;return j})})}
function hit(k,t){try{window.qoaqHit&&window.qoaqHit(k,t)}catch(e){}}
var MODELES={
 noel:{t:"Repas de Noël en famille",d:"2026-12-25",c:[["Apéritif",["Biscuits apéro","Toasts et tartinades"]],["Entrée",["Foie gras","Saumon fumé"]],["Plat",["Plat principal","Accompagnement"]],["Fromage",["Plateau de fromages"]],["Dessert",["Bûche de Noël","Chocolats"]],["Boissons",["Champagne","Vin rouge","Vin blanc","Jus de fruits et sodas"]],["Pain et divers",["Pain","Glaçons","Serviettes de table"]]]},
 nouvelan:{t:"Réveillon du Nouvel An",d:"2026-12-31",c:[["Apéritif",["Biscuits apéro","Verrines","Chips"]],["Plat",["Plat principal","Accompagnement"]],["Dessert",["Dessert","Mignardises"]],["Boissons",["Champagne pour minuit","Vin","Softs"]],["Fête",["Cotillons","Musique","Glaçons","Gobelets"]]]},
 anniv:{t:"Anniversaire",d:"",c:[["Salé",["Chips","Pizzas ou quiches","Crudités"]],["Sucré",["Gâteau d'anniversaire","Bonbons"]],["Boissons",["Jus de fruits","Sodas","Eau"]],["Fête",["Bougies","Assiettes et gobelets","Décoration"]]]},
 pique:{t:"Pique-nique entre amis",d:"",c:[["Salé",["Sandwichs","Salade composée","Chips"]],["Barbecue",["Saucisses","Brochettes","Charbon"]],["Sucré",["Dessert","Fruits"]],["Boissons",["Eau","Boissons fraîches"]],["Matériel",["Nappe","Glacière","Gobelets","Sacs poubelle"]]]},
 auberge:{t:"Auberge espagnole",d:"",c:[["Salé",["Plat salé","Plat salé","Salade"]],["Sucré",["Dessert","Dessert"]],["Boissons",["Boissons","Boissons"]],["Divers",["Pain","Vaisselle jetable"]]]},
 vide:{t:"Notre repas",d:"",c:[["Entrée",[]],["Plat",[]],["Dessert",[]],["Boissons",[]]]}
};
var cats=[];
function modele(k){var m=MODELES[k];cats=m.c.map(function(x){return {nom:x[0],items:x[1].slice()}});rendreCats()}
function rendreCats(){
  var w=$("rp-cats");w.innerHTML="";
  cats.forEach(function(c,ci){
    var d=document.createElement("div");d.className="rp-cat";
    d.innerHTML='<h3>'+esc(c.nom)+'</h3>'+c.items.map(function(it,ii){return '<div class="pers"><input class="nom" aria-label="'+esc(c.nom)+' '+(ii+1)+'" value="'+esc(it)+'" data-i="'+ii+'"><button class="x" aria-label="Retirer" data-i="'+ii+'">×</button></div>'}).join("")+'<button class="btn s petit ajout">Ajouter une ligne</button>';
    d.querySelectorAll("input").forEach(function(inp){inp.oninput=function(){c.items[+inp.dataset.i]=inp.value}});
    d.querySelectorAll("button.x").forEach(function(b){b.onclick=function(){c.items.splice(+b.dataset.i,1);rendreCats()}});
    d.querySelector(".ajout").onclick=function(){c.items.push("");rendreCats();var ins=w.querySelectorAll(".rp-cat")[ci].querySelectorAll("input");ins[ins.length-1].focus()};
    w.appendChild(d);
  });
}
$("rp-modele").onchange=function(){var m=MODELES[this.value];$("rp-titre").value=m.t;if(m.d)$("rp-date").value=m.d;modele(this.value)};
$("rp-go").onclick=function(){
  var bt=this,items=[];
  cats.forEach(function(c){c.items.forEach(function(it){if(it.trim())items.push({cat:c.nom,label:it.trim()})})});
  if(!items.length){$("rp-err").textContent="Ajoutez au moins une chose à apporter.";return}
  bt.disabled=true;bt.textContent="Création...";
  post({action:"liste_creer",titre:$("rp-titre").value,date:$("rp-date").value,lieu:$("rp-lieu").value,items:items}).then(function(j){
    bt.disabled=false;bt.textContent="Créer la liste et la partager";
    if(j.ok){hit("liste",$("rp-modele").value);memo(j.liste.id,j.liste.titre);location.hash="l="+j.liste.id;}
    else $("rp-err").textContent=j._s===429?"Trop de listes créées depuis votre connexion. Réessayez dans une heure.":"La création n'a pas marché. Réessayez.";
  }).catch(function(){bt.disabled=false;bt.textContent="Créer la liste et la partager";$("rp-err").textContent="Pas de connexion. Réessayez."});
};

var L=null,id=null,minuteur=null;
function mesListes(){var M=[];try{M=JSON.parse(localStorage.getItem("qoaq_listes")||"[]")}catch(e){}return M}
function memo(i,t){var M=mesListes().filter(function(x){return x.id!==i});M.unshift({id:i,t:t,ts:Date.now()});try{localStorage.setItem("qoaq_listes",JSON.stringify(M.slice(0,12)))}catch(e){}}
function rendreMes(){
  var M=mesListes(),c=$("rp-mes");if(!M.length){c.classList.add("cache");return}
  c.classList.remove("cache");var ul=$("rp-mes-l");ul.innerHTML="";
  M.forEach(function(x,k){var li=document.createElement("li");
    li.innerHTML='<span><b>'+esc(x.t||"Liste")+'</b>'+(x.ts?'<small>ouverte le '+new Date(x.ts).toLocaleDateString("fr-FR",{day:"numeric",month:"long"})+'</small>':'')+'</span><span class="act"><a class="btn s petit" href="#l='+esc(x.id)+'">Suivre</a><button class="x" aria-label="Oublier cette liste">×</button></span>';
    li.querySelector("button").onclick=function(){var M2=mesListes();M2.splice(k,1);try{localStorage.setItem("qoaq_listes",JSON.stringify(M2))}catch(e){}rendreMes()};
    ul.appendChild(li)});
}
function moi(){return $("rp-moi").value.trim()}
try{$("rp-moi").value=localStorage.getItem("qoaq_prenom")||""}catch(e){}
$("rp-moi").oninput=function(){try{localStorage.setItem("qoaq_prenom",moi())}catch(e){}};
function act(o,el){
  if(el){el.disabled=true}
  return post(Object.assign({id:id},o)).then(function(j){if(j.ok){L=j.liste;rendre();hit("liste_maj",o.action)}else if(el){el.disabled=false}}).catch(function(){if(el)el.disabled=false});
}
function rendre(){
  memo(id,L.titre);
  $("rp-v-titre").textContent=L.titre;
  var dt=L.date_ev?new Date(L.date_ev+"T12:00").toLocaleDateString("fr-FR",{weekday:"long",day:"numeric",month:"long"}):"";
  $("rp-v-info").textContent=[dt,L.lieu].filter(Boolean).join(", ");
  document.title=L.titre+" : qui apporte quoi ?";
  var pris=L.items.filter(function(i){return i.qui}).length;
  $("rp-compte").innerHTML='<b>'+pris+'/'+L.items.length+'</b><span>pris</span>';
  var ordre=[],par={};
  L.items.forEach(function(i){if(!par[i.cat]){par[i.cat]=[];ordre.push(i.cat)}par[i.cat].push(i)});
  var w=$("rp-liste");w.innerHTML="";
  ordre.concat(ordre.length?[]:["Entrée"]).forEach(function(cat){
    var s=document.createElement("section");s.className="carte rp-bloc";
    s.innerHTML='<h2>'+esc(cat)+'</h2><ul class="rp-items">'+(par[cat]||[]).map(function(i){
      return '<li class="'+(i.qui?"pris":"")+'"><span class="lab">'+esc(i.label)+'</span>'+(i.qui?'<span class="qui">'+esc(i.qui)+'</span><button class="x" data-a="lib" data-id="'+i.id+'" aria-label="Libérer">×</button>':'<button class="btn s petit" data-a="prendre" data-id="'+i.id+'">Je m\'en occupe</button>')+'</li>'}).join("")+'</ul><div class="rp-ajout"><input placeholder="Ajouter dans '+esc(cat)+'" aria-label="Ajouter dans '+esc(cat)+'"><button class="btn s petit">Ajouter</button></div>';
    s.querySelectorAll("button[data-a]").forEach(function(b){b.onclick=function(){
      if(b.dataset.a==="prendre"){var m=moi();if(!m){$("rp-moi").focus();$("rp-moi").classList.add("attention");setTimeout(function(){$("rp-moi").classList.remove("attention")},1500);return}act({action:"liste_prendre",item:+b.dataset.id,qui:m},b)}
      else act({action:"liste_prendre",item:+b.dataset.id,qui:""},b)}});
    var inp=s.querySelector(".rp-ajout input"),ab=s.querySelector(".rp-ajout button");
    function ajouter(){var v=inp.value.trim();if(!v)return;act({action:"liste_ajouter",cat:cat,label:v,qui:moi()},ab)}
    ab.onclick=ajouter;inp.onkeydown=function(e){if(e.key==="Enter")ajouter()};
    w.appendChild(s);
  });
  var url=location.origin+location.pathname+"#l="+id;
  $("rp-wa").href="https://wa.me/?text="+encodeURIComponent("Pour « "+L.titre+" », dites ce que vous apportez ici : "+url);
  $("rp-maj").textContent="Mis à jour à "+new Date().toLocaleTimeString("fr-FR",{hour:"2-digit",minute:"2-digit"})+". La liste se rafraîchit toute seule.";
}
$("rp-copie").onclick=function(){var b=this;try{navigator.clipboard.writeText(location.origin+location.pathname+"#l="+id).then(function(){b.textContent="Lien copié";hit("partage","liste")})}catch(e){}};
$("rp-wa").addEventListener("click",function(){hit("partage","liste-whatsapp")});
function charger(){post({action:"liste_lire",id:id}).then(function(j){if(j.ok){L=j.liste;rendre()}else{$("rp-vue").classList.add("cache");$("rp-creer").classList.remove("cache");$("rp-err").textContent="Cette liste n'existe pas ou a été supprimée. Créez-en une nouvelle."}}).catch(function(){})}
function route(){
  var m=location.hash.match(/l=([a-z0-9]{10})/),nm=location.hash.match(/[&]n=([^&]+)/);
  if(nm){try{var pn=decodeURIComponent(nm[1]).slice(0,30);$("rp-moi").value=pn;localStorage.setItem("qoaq_prenom",pn)}catch(e){}}
  if(m){id=m[1];$("rp-creer").classList.add("cache");$("rp-vue").classList.remove("cache");$("rp-h1").textContent="Qui apporte quoi ?";$("rp-intro").textContent="Choisissez ce que vous apportez : la liste se met à jour pour tout le monde.";charger();
    clearInterval(minuteur);minuteur=setInterval(function(){if(document.visibilityState==="visible")charger()},15000);window.scrollTo(0,0)}
  else{id=null;clearInterval(minuteur);$("rp-creer").classList.remove("cache");$("rp-vue").classList.add("cache");$("rp-h1").textContent="Qui apporte quoi ? La liste du repas à partager";modele($("rp-modele").value);rendreMes()}
}
$("rp-mail-ok").onclick=function(){var bt=this,v=$("rp-mail").value.trim(),m=$("rp-mail-msg");if(!/^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v)){m.textContent="Cette adresse n'est pas valide.";return}
  bt.disabled=true;post({action:"liste_mail",id:id,email:v}).then(function(x){bt.disabled=false;m.textContent=x.ok?"C'est envoyé. Gardez cet e-mail pour retrouver la liste.":x._s===429?"Trop de demandes, réessayez plus tard.":"L'envoi n'a pas marché, réessayez."}).catch(function(){bt.disabled=false;m.textContent="Pas de connexion."})};
document.addEventListener("visibilitychange",function(){if(document.visibilityState==="visible"&&id)charger()});
window.addEventListener("hashchange",route);
var IDEES=[["Nappe de fête","Pour une jolie table","nappe noel"],["Bougies de table","L'ambiance en un instant","bougies de table"],["Crackers de Noël","Pour rire à table","crackers de noel"],["Vaisselle jetable chic","Moins de vaisselle à faire","vaisselle jetable elegante"]];
$("rp-idees").innerHTML=IDEES.map(function(x){return '<div class="idee"><b>'+x[0]+'</b><span>'+x[1]+'</span><a class="btn s petit" target="_blank" rel="sponsored nofollow noopener" href="https://www.amazon.fr/s?k='+encodeURIComponent(x[2])+'&tag=quioffreaqui-21">Voir les modèles</a></div>'}).join("");
route();
})();
