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

var L=null,id=null,minuteur=null,force=true,enregistre=null;
function confirmerSuppr(tr){if(tr.dataset.sur){return true}tr.dataset.sur="1";var b=tr.querySelector("[data-del]");b.textContent="Sûr ?";b.classList.add("sur");setTimeout(function(){delete tr.dataset.sur;b.textContent="×";b.classList.remove("sur")},2500);return false}
var dernierEnvoi={};
function sauver(iid,f,v){var k=iid+"|"+f;if(dernierEnvoi[k]===v)return;dernierEnvoi[k]=v;var o={action:"liste_maj",id:id,item:iid};o[f]=v;$("rp-maj").textContent="Enregistrement...";
  post(o).then(function(j){if(j.ok){L=j.liste;clearTimeout(enregistre);$("rp-maj").textContent="Enregistré pour tout le monde à "+new Date().toLocaleTimeString("fr-FR",{hour:"2-digit",minute:"2-digit"})+".";hit("liste_maj",f)}else $("rp-maj").textContent="Pas enregistré, réessayez."}).catch(function(){$("rp-maj").textContent="Pas de connexion : la modification n'est pas enregistrée."})}
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
  return post(Object.assign({id:id},o)).then(function(j){if(j.ok){L=j.liste;force=true;rendre();hit("liste_maj",o.action)}else if(el){el.disabled=false}}).catch(function(){if(el)el.disabled=false});
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
  if(!ordre.length)ordre=["Entrée","Plat","Dessert","Boissons"];
  var w=$("rp-liste"),actif=document.activeElement&&w.contains(document.activeElement)?document.activeElement:null;
  if(actif&&!force)return; force=false;
  w.innerHTML="";
  ordre.forEach(function(cat){
    var s=document.createElement("section");s.className="carte rp-bloc";
    s.innerHTML='<h2>'+esc(cat)+'</h2><table class="rp-tab"><thead><tr><th>Quoi</th><th>Qui l\'apporte</th><th>Note</th><th><span class="sr">Supprimer</span></th></tr></thead><tbody>'+(par[cat]||[]).map(function(i){
      return '<tr data-id="'+i.id+'" class="'+(i.qui?"pris":"")+'"><td><input data-f="label" value="'+esc(i.label)+'" placeholder="Ex. bûche" aria-label="Quoi"></td><td><input data-f="qui" value="'+esc(i.qui||"")+'" placeholder="Personne" aria-label="Qui l\'apporte"><button class="btn s mini" data-moi>Moi</button></td><td><input data-f="note" value="'+esc(i.note||"")+'" placeholder="Quantité, détail" aria-label="Note"></td><td><button class="x" data-del aria-label="Supprimer la ligne">×</button></td></tr>'}).join("")+'</tbody></table><button class="btn s petit rp-plus">Ajouter une ligne</button>';
    s.querySelectorAll("tr[data-id]").forEach(function(tr){
      var iid=+tr.dataset.id,t=null;
      tr.querySelectorAll("input").forEach(function(inp){
        inp.addEventListener("input",function(){clearTimeout(t);t=setTimeout(function(){sauver(iid,inp.dataset.f,inp.value)},700);if(inp.dataset.f==="qui")tr.classList.toggle("pris",!!inp.value.trim())});
        inp.addEventListener("blur",function(){clearTimeout(t);sauver(iid,inp.dataset.f,inp.value)});
      });
      tr.querySelector("[data-moi]").onclick=function(){var m=moi();if(!m){$("rp-moi").focus();$("rp-moi").classList.add("attention");setTimeout(function(){$("rp-moi").classList.remove("attention")},1500);return}var q=tr.querySelector('[data-f="qui"]');q.value=m;tr.classList.add("pris");sauver(iid,"qui",m)};
      tr.querySelector("[data-del]").onclick=function(){if(tr.querySelector('[data-f="label"]').value.trim()&&!confirmerSuppr(tr))return;force=true;act({action:"liste_suppr",item:iid})};
    });
    s.querySelector(".rp-plus").onclick=function(){force=true;post({id:id,action:"liste_ajouter",cat:cat,label:""}).then(function(j){if(j.ok){L=j.liste;force=true;rendre();var rows=w.querySelectorAll(".rp-bloc")[ordre.indexOf(cat)].querySelectorAll('tbody tr');var last=rows[rows.length-1];last&&last.querySelector("input").focus()}})};
    w.appendChild(s);
  });
  var nc=document.createElement("div");nc.className="rp-ajout";nc.innerHTML='<input placeholder="Nouvelle catégorie (ex. Fromages)" aria-label="Nouvelle catégorie"><button class="btn s petit">Ajouter la catégorie</button>';
  nc.querySelector("button").onclick=function(){var v=nc.querySelector("input").value.trim();if(!v)return;force=true;act({action:"liste_ajouter",cat:v,label:""})};
  w.appendChild(nc);
  var url=location.origin+location.pathname+"#l="+id;
  $("rp-wa").href="https://wa.me/?text="+encodeURIComponent("Pour « "+L.titre+" », dites ce que vous apportez ici : "+url);
  if(!/Enregistr/.test($("rp-maj").textContent))$("rp-maj").textContent="Tout le monde voit et modifie ce tableau. Il se met à jour tout seul.";
}
$("rp-copie").onclick=function(){var b=this;try{navigator.clipboard.writeText(location.origin+location.pathname+"#l="+id).then(function(){b.textContent="Lien copié";hit("partage","liste")})}catch(e){}};
$("rp-wa").addEventListener("click",function(){hit("partage","liste-whatsapp")});
function charger(f){post({action:"liste_lire",id:id}).then(function(j){if(j.ok){L=j.liste;if(f)force=true;rendre()}else{$("rp-vue").classList.add("cache");$("rp-creer").classList.remove("cache");$("rp-err").textContent="Cette liste n'existe pas ou a été supprimée. Créez-en une nouvelle."}}).catch(function(){})}
function route(){
  var m=location.hash.match(/l=([a-z0-9]{10})/),nm=location.hash.match(/[&]n=([^&]+)/);
  if(nm){try{var pn=decodeURIComponent(nm[1]).slice(0,30);$("rp-moi").value=pn;localStorage.setItem("qoaq_prenom",pn)}catch(e){}}
  if(m){id=m[1];$("rp-creer").classList.add("cache");$("rp-vue").classList.remove("cache");$("rp-h1").textContent="Qui apporte quoi ?";$("rp-intro").textContent="Écrivez directement dans le tableau : ce qu'il faut, qui l'apporte, une note. Tout le monde voit les changements.";charger(true);
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
