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
var EMB=/[?&]e=1/.test(location.search);
if(EMB){document.documentElement.classList.add("rp-embed");
  var envH=function(){try{parent.postMessage({qoaqH:document.documentElement.scrollHeight},location.origin)}catch(e){}};
  try{new ResizeObserver(envH).observe(document.body)}catch(e){setInterval(envH,1000)}window.addEventListener("load",envH);}
var choix="noel";
var boutonsM=document.querySelectorAll("#rp-modeles button");
boutonsM.forEach(function(b){b.onclick=function(){choix=b.dataset.m;boutonsM.forEach(function(x){x.setAttribute("aria-checked",x===b?"true":"false")});$("rp-titre").value=MODELES[choix].t}});

$("rp-go").onclick=function(){
  var bt=this,m=MODELES[choix],items=[];
  m.c.forEach(function(c){c[1].forEach(function(it){items.push({cat:c[0],label:it})})});
  bt.disabled=true;bt.textContent="Création...";
  var fin=function(){bt.disabled=false;bt.textContent="Créer mon tableau"};
  post({action:"liste_creer",titre:$("rp-titre").value,date:m.d,lieu:"",items:items}).then(function(j){
    if(!j.ok){fin();$("rp-err").textContent=j._s===429?"Trop de tableaux créés depuis votre connexion. Réessayez dans une heure.":"La création n'a pas marché. Réessayez.";return}
    var lid=j.liste.id,suite=Promise.resolve();
    if(!items.length)m.c.forEach(function(c){suite=suite.then(function(){return post({id:lid,action:"liste_ajouter",cat:c[0],label:""})})});
    suite.then(function(){fin();hit("liste",choix);memo(lid,j.liste.titre);nouveau=true;location.hash="l="+lid});
  }).catch(function(){fin();$("rp-err").textContent="Pas de connexion. Réessayez."});
};

var L=null,id=null,minuteur=null,nouveau=false,dernierEnvoi={},attente={};
function moi(){return $("rp-moi").value.trim()}
try{$("rp-moi").value=localStorage.getItem("qoaq_prenom")||""}catch(e){}
$("rp-moi").addEventListener("input",function(){try{localStorage.setItem("qoaq_prenom",moi())}catch(e){}majMoi()});
function etat(t,ok){var e=$("rp-maj");e.textContent=t;e.className=ok?"ok":""}
function heure(){return new Date().toLocaleTimeString("fr-FR",{hour:"2-digit",minute:"2-digit"})}
function compte(){if(!L)return;var v=L.items.filter(function(i){return (i.label||"").trim()}),p=v.filter(function(i){return i.qui}).length;$("rp-compte").innerHTML="<b>"+p+"/"+v.length+"</b> déjà pris";
  document.querySelectorAll("#rp-corps tr.cat").forEach(function(r){var c=r.dataset.c,a=v.filter(function(i){return i.cat===c});var sp=r.querySelector("span");if(sp)sp.textContent=a.filter(function(i){return i.qui}).length+"/"+a.length})}
function sauver(iid,f,v){var k=iid+"|"+f;if(dernierEnvoi[k]===v)return;dernierEnvoi[k]=v;var o={action:"liste_maj",id:id,item:iid};o[f]=v;etat("Enregistrement...");
  post(o).then(function(j){if(j.ok){L=j.liste;compte();etat("✓ Enregistré pour tout le monde à "+heure(),true);hit("liste_maj",f)}else{delete dernierEnvoi[k];etat("Pas enregistré, réessayez.")}}).catch(function(){delete dernierEnvoi[k];etat("Pas de connexion : la modification n'est pas enregistrée.")})}

function ligne(i,cat){
  var vide=!(i&&i.qui);
  return '<tr'+(i?' data-id="'+i.id+'"':' class="fantome"')+' data-cat="'+esc(cat)+'"'+(i&&i.qui?' data-pris="1"':'')+'>'
   +'<td><input data-f="label" value="'+esc(i?i.label:"")+'" placeholder="'+(i?"Quoi ?":"+ Ajouter")+'" aria-label="Quoi ('+esc(cat)+')" maxlength="60"></td>'
   +'<td class="qui"><input data-f="qui" value="'+esc(i?i.qui||"":"")+'" placeholder="Qui ?" aria-label="Qui l\'apporte" maxlength="30"><button type="button" class="moi'+(vide&&i?'':' cache')+'" tabindex="-1">Moi</button></td>'
   +'<td><input data-f="note" value="'+esc(i?i.note||"":"")+'" placeholder="…" aria-label="Note" maxlength="80"></td>'
   +'<td class="x">'+(i?'<button type="button" class="del" aria-label="Supprimer la ligne">×</button>':'')+'</td></tr>';
}
function rendre(forcer){
  if(!L)return;
  memo(id,L.titre);
  var g=$("rp-grille");
  if(!forcer&&document.activeElement&&g.contains(document.activeElement)){compte();return}
  if(document.activeElement!==$("rp-v-titre"))$("rp-v-titre").value=L.titre;
  if(document.activeElement!==$("rp-v-date"))$("rp-v-date").value=L.date_ev||"";
  if(document.activeElement!==$("rp-v-lieu"))$("rp-v-lieu").value=L.lieu||"";
  document.title=L.titre+" : qui apporte quoi ?";
  var ordre=[],par={};
  L.items.forEach(function(i){if(!par[i.cat]){par[i.cat]=[];ordre.push(i.cat)}par[i.cat].push(i)});
  var h="";
  ordre.forEach(function(cat){
    var its=par[cat],pl=its.filter(function(i){return (i.label||"").trim()}),pr=pl.filter(function(i){return i.qui}).length;
    h+='<tr class="cat" data-c="'+esc(cat)+'"><th colspan="4">'+esc(cat)+'<span>'+pr+'/'+pl.length+'</span></th></tr>';
    its.forEach(function(i){h+=ligne(i,cat)});
    if(!its.some(function(i){return !(i.label||"").trim()}))h+=ligne(null,cat);
  });
  $("rp-corps").innerHTML=h;
  majMoi();compte();
  var url=lien();
  $("rp-wa").href="https://wa.me/?text="+encodeURIComponent(texte()+" "+url);
}
function lien(){return location.origin+location.pathname+"#l="+id}
function texte(){return "Pour « "+(L?L.titre:"notre repas")+" », notez ce que vous apportez dans le tableau :"}
function majMoi(){var m=moi();document.querySelectorAll("#rp-corps .moi").forEach(function(b){b.textContent=m?"Moi":"Moi ?"})}

// Saisie façon tableur : enregistrement automatique, ligne fantôme qui devient une vraie ligne
var corps=$("rp-corps"),minut={};
corps.addEventListener("input",function(e){
  var inp=e.target;if(!inp.dataset.f)return;var tr=inp.closest("tr");
  if(inp.dataset.f==="qui"){tr.querySelector(".moi").classList.toggle("cache",!!inp.value.trim());tr.toggleAttribute("data-pris",!!inp.value.trim())}
  if(tr.dataset.id){var k=tr.dataset.id+"|"+inp.dataset.f;clearTimeout(minut[k]);minut[k]=setTimeout(function(){sauver(+tr.dataset.id,inp.dataset.f,inp.value)},600)}
  else if(!tr.dataset.cree)creer(tr);
});
corps.addEventListener("focusout",function(e){var inp=e.target,tr=inp.closest&&inp.closest("tr");if(!tr||!inp.dataset.f||!tr.dataset.id)return;var k=tr.dataset.id+"|"+inp.dataset.f;clearTimeout(minut[k]);sauver(+tr.dataset.id,inp.dataset.f,inp.value)});
function val(tr,f){return tr.querySelector('[data-f="'+f+'"]').value}
function creer(tr){
  tr.dataset.cree="1";tr.classList.remove("fantome");var cat=tr.dataset.cat;etat("Enregistrement...");
  var envoye={label:val(tr,"label"),qui:val(tr,"qui"),note:val(tr,"note")};
  post({id:id,action:"liste_ajouter",cat:cat,label:envoye.label,qui:envoye.qui,note:envoye.note}).then(function(j){
    if(!j.ok){delete tr.dataset.cree;tr.classList.add("fantome");etat(j.raison==="plein"?"Le tableau est plein (150 lignes).":"Pas enregistré, réessayez.");return}
    L=j.liste;var mx=0;L.items.forEach(function(i){if(i.cat===cat&&i.id>mx)mx=i.id});
    tr.dataset.id=mx;["label","qui","note"].forEach(function(f){dernierEnvoi[mx+"|"+f]=envoye[f];if(val(tr,f)!==envoye[f])sauver(mx,f,val(tr,f))});
    tr.querySelector("td.x").innerHTML='<button type="button" class="del" aria-label="Supprimer la ligne">×</button>';
    tr.querySelector('[data-f="label"]').placeholder="Quoi ?";tr.querySelector(".moi").classList.toggle("cache",!!val(tr,"qui").trim());
    var t=document.createElement("tbody");t.innerHTML=ligne(null,cat);tr.after(t.firstChild);majMoi();
    compte();etat("✓ Enregistré pour tout le monde à "+heure(),true);hit("liste_maj","ajout");
  }).catch(function(){delete tr.dataset.cree;tr.classList.add("fantome");etat("Pas de connexion : la ligne n'est pas enregistrée.")});
}
corps.addEventListener("click",function(e){
  var b=e.target;
  if(b.classList.contains("moi")){var tr=b.closest("tr"),m=moi();if(!m){var p=$("rp-moi");p.focus();p.classList.add("attention");setTimeout(function(){p.classList.remove("attention")},1500);return}
    var q=tr.querySelector('[data-f="qui"]');q.value=m;q.dispatchEvent(new Event("input",{bubbles:true}));if(tr.dataset.id)sauver(+tr.dataset.id,"qui",m);return}
  if(b.classList.contains("del")){var r=b.closest("tr");
    if(val(r,"label").trim()&&!r.dataset.sur){r.dataset.sur="1";b.textContent="Sûr ?";b.classList.add("sur");setTimeout(function(){delete r.dataset.sur;b.textContent="×";b.classList.remove("sur")},2500);return}
    post({id:id,action:"liste_suppr",item:+r.dataset.id}).then(function(j){if(j.ok){L=j.liste;rendre(true);etat("✓ Ligne supprimée à "+heure(),true)}})}
});
// Entrée : passer à la ligne du dessous, même colonne
corps.addEventListener("keydown",function(e){
  if(e.key!=="Enter"||!e.target.dataset.f)return;e.preventDefault();
  var f=e.target.dataset.f,tr=e.target.closest("tr"),n=tr.nextElementSibling;
  while(n&&n.classList.contains("cat"))n=n.nextElementSibling;
  if(n)n.querySelector('[data-f="'+f+'"]').focus();else e.target.blur();
});

// Titre, date, lieu
var tInfo=null;
function info(){clearTimeout(tInfo);tInfo=setTimeout(function(){etat("Enregistrement...");post({id:id,action:"liste_info",titre:$("rp-v-titre").value,date:$("rp-v-date").value,lieu:$("rp-v-lieu").value}).then(function(j){if(j.ok){L=j.liste;memo(id,L.titre);document.title=L.titre+" : qui apporte quoi ?";$("rp-wa").href="https://wa.me/?text="+encodeURIComponent(texte()+" "+lien());etat("✓ Enregistré pour tout le monde à "+heure(),true)}})},700)}
["rp-v-titre","rp-v-date","rp-v-lieu"].forEach(function(k){$(k).addEventListener("input",info)});
$("rp-ncat-ok").onclick=function(){var v=$("rp-ncat").value.trim();if(!v)return;post({id:id,action:"liste_ajouter",cat:v,label:""}).then(function(j){if(j.ok){L=j.liste;$("rp-ncat").value="";rendre(true);var r=corps.querySelectorAll('tr[data-cat="'+v.replace(/"/g,'\\"')+'"] [data-f="label"]');r.length&&r[0].focus()}})};

// Partage
$("rp-share").onclick=function(){
  var u=lien();
  if(navigator.share){navigator.share({title:L?L.titre:"Qui apporte quoi ?",text:texte(),url:u}).then(function(){hit("partage","liste-natif")}).catch(function(){})}
  else{window.open($("rp-wa").href,"_blank","noopener");hit("partage","liste-whatsapp")}
};
$("rp-hop").onclick=function(){this.href="https://hoplien.fr/?u="+encodeURIComponent(lien())+"&src=qoaq-repas";hit("partage","liste-hoplien")};
$("rp-copie").onclick=function(){var b=this;try{navigator.clipboard.writeText(lien()).then(function(){b.textContent="Lien copié ✓";hit("partage","liste");setTimeout(function(){b.textContent="Copier le lien"},2500)})}catch(e){}};
$("rp-wa").addEventListener("click",function(){hit("partage","liste-whatsapp")});

function mesListes(){var M=[];try{M=JSON.parse(localStorage.getItem("qoaq_listes")||"[]")}catch(e){}return M}
function memo(i,t){var M=mesListes().filter(function(x){return x.id!==i});M.unshift({id:i,t:t,ts:Date.now()});try{localStorage.setItem("qoaq_listes",JSON.stringify(M.slice(0,12)))}catch(e){}}
function rendreMes(){
  var M=mesListes(),c=$("rp-mes");if(!M.length){c.classList.add("cache");return}
  c.classList.remove("cache");var ul=$("rp-mes-l");ul.innerHTML="";
  M.forEach(function(x,k){var li=document.createElement("li");
    li.innerHTML='<span><b>'+esc(x.t||"Tableau")+'</b>'+(x.ts?'<small>ouvert le '+new Date(x.ts).toLocaleDateString("fr-FR",{day:"numeric",month:"long"})+'</small>':'')+'</span><span class="act"><a class="btn s petit" href="#l='+esc(x.id)+'">Ouvrir</a><button class="x" aria-label="Oublier ce tableau">×</button></span>';
    li.querySelector("button").onclick=function(){var M2=mesListes();M2.splice(k,1);try{localStorage.setItem("qoaq_listes",JSON.stringify(M2))}catch(e){}rendreMes()};
    ul.appendChild(li)});
}
function charger(f){post({action:"liste_lire",id:id}).then(function(j){if(j.ok){L=j.liste;rendre(f)}else if(j._s===404){$("rp-vue").classList.add("cache");$("rp-creer").classList.remove("cache");$("rp-err").textContent="Ce tableau n'existe pas ou a été supprimé. Créez-en un nouveau."}}).catch(function(){})}
function route(){
  var m=location.hash.match(/l=([a-z0-9]{10})/),nm=location.hash.match(/[&]n=([^&]+)/);
  if(nm){try{var pn=decodeURIComponent(nm[1]).slice(0,30);$("rp-moi").value=pn;localStorage.setItem("qoaq_prenom",pn)}catch(e){}}
  if(m){id=m[1];$("rp-creer").classList.add("cache");$("rp-vue").classList.remove("cache");$("rp-h1").textContent="Qui apporte quoi\u00a0?";document.body.classList.add("rp-mode-tab");charger(true);
    clearInterval(minuteur);minuteur=setInterval(function(){if(document.visibilityState==="visible")charger()},8000);window.scrollTo(0,0);
    if(nouveau){nouveau=false;var s=$("rp-share");s.classList.add("pulse");etat("✓ Tableau créé. Partagez-le avec le bouton ci-dessus.",true);setTimeout(function(){s.classList.remove("pulse")},6000)}}
  else{id=null;clearInterval(minuteur);document.body.classList.remove("rp-mode-tab");$("rp-creer").classList.remove("cache");$("rp-vue").classList.add("cache");$("rp-h1").textContent="Qui apporte quoi\u00a0? Le tableau du repas à partager";rendreMes()}
}
$("rp-mail-ok").onclick=function(){var bt=this,v=$("rp-mail").value.trim(),m=$("rp-mail-msg");if(!/^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v)){m.textContent="Cette adresse n'est pas valide.";return}
  bt.disabled=true;post({action:"liste_mail",id:id,email:v}).then(function(x){bt.disabled=false;m.textContent=x.ok?"C'est envoyé. Gardez cet e-mail pour retrouver le tableau.":x._s===429?"Trop de demandes, réessayez plus tard.":"L'envoi n'a pas marché, réessayez."}).catch(function(){bt.disabled=false;m.textContent="Pas de connexion."})};
document.addEventListener("visibilitychange",function(){if(document.visibilityState==="visible"&&id)charger()});
window.addEventListener("hashchange",route);
var IDEES=[["Nappe de fête","Pour une jolie table","nappe noel"],["Bougies de table","L'ambiance en un instant","bougies de table"],["Crackers de Noël","Pour rire à table","crackers de noel"],["Vaisselle jetable chic","Moins de vaisselle à faire","vaisselle jetable elegante"]];
$("rp-idees").innerHTML=IDEES.map(function(x){return '<div class="idee"><b>'+x[0]+'</b><span>'+x[1]+'</span><a class="btn s petit" target="_blank" rel="sponsored nofollow noopener" href="https://www.amazon.fr/s?k='+encodeURIComponent(x[2])+'&tag=quioffreaqui-21">Voir les modèles</a></div>'}).join("");
route();
})();
