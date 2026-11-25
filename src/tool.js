(function(){
var $=function(i){return document.getElementById(i)};
var noms=["Marie","Thomas","Julie","Lucas","Emma"];
function rendreListe(){
  var l=$("liste");l.innerHTML="";
  noms.forEach(function(n,i){
    var d=document.createElement("div");d.className="pers";
    d.innerHTML='<input aria-label="Prénom '+(i+1)+'" value="'+n.replace(/"/g,"&quot;")+'"><button class="x" aria-label="Retirer">×</button>';
    d.querySelector("input").oninput=function(e){noms[i]=e.target.value;rendreExc()};
    d.querySelector("button").onclick=function(){noms.splice(i,1);rendreListe();rendreExc()};
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
$("ajout").onclick=function(){noms.push("");rendreListe();rendreExc();var ins=document.querySelectorAll("#liste input");ins[ins.length-1].focus()};
$("ajoutExc").onclick=function(){if(noms.length>1){excs.push([0,1]);rendreExc()}};

function interdit(a,b){return a===b||excs.some(function(p){return (p[0]===a&&p[1]===b)||(p[0]===b&&p[1]===a)})}
function tirage(n){
  for(var essai=0;essai<500;essai++){
    var ordre=[],pris={},ok=true;
    for(var i=0;i<n&&ok;i++){
      var c=[];for(var j=0;j<n;j++)if(!pris[j]&&!interdit(i,j))c.push(j);
      if(!c.length){ok=false;break}
      var k=c[Math.floor(Math.random()*c.length)];ordre.push(k);pris[k]=1;
    }
    if(ok)return ordre;
  }
  return null;
}
function code(o){var s=unescape(encodeURIComponent(JSON.stringify(o))),r="";for(var i=0;i<s.length;i++)r+=String.fromCharCode(s.charCodeAt(i)^23);return btoa(r).replace(/=+$/,"")}
function decode(t){var s=atob(t),r="";for(var i=0;i<s.length;i++)r+=String.fromCharCode(s.charCodeAt(i)^23);return JSON.parse(decodeURIComponent(escape(r)))}

$("tirer").onclick=function(){
  var liste=noms.map(function(n){return n.trim()});
  $("err").textContent="";
  if(liste.filter(Boolean).length<3||liste.some(function(n){return !n})){$("err").textContent="Il faut au moins 3 prénoms, sans ligne vide.";return}
  var t=tirage(liste.length);
  if(!t){$("err").textContent="Impossible avec ces exclusions. Retirez-en une et relancez.";return}
  var ty=$("type").value,ev=$("ev").value.trim()||NOMS[ty],b=$("budget").value,d=$("date").value;
  var ul=$("liens");ul.innerHTML="";
  liste.forEach(function(n,i){
    var url=location.href.split("#")[0]+"#r="+code({e:ev,t:ty,b:b,d:d,de:n,a:liste[t[i]]});
    var li=document.createElement("li");
    var msg=encodeURIComponent("Ton tirage pour « "+ev+" » est prêt : "+url);
    li.innerHTML='<b>'+n.replace(/</g,"&lt;")+'</b><span class="act"><button class="btn s petit">Copier le lien</button><a class="btn s petit" target="_blank" rel="noopener" href="https://wa.me/?text='+msg+'">WhatsApp</a><a class="btn s petit" href="sms:?&body='+msg+'">SMS</a></span>';
    li.querySelector("button").onclick=function(){var bt=this;navigator.clipboard&&navigator.clipboard.writeText(url).then(function(){bt.textContent="Copié"})};
    ul.appendChild(li);
  });
  $("res").classList.remove("cache");try{window.qoaqHit&&window.qoaqHit("tirage",ty+"|"+liste.length+"|"+b)}catch(e){}$("res").scrollIntoView({behavior:"smooth"});
};

var NOMS={noel:"Père Noël secret",nouvelan:"Échange de cadeaux du Nouvel An",stnicolas:"Saint-Nicolas",anniv:"Échange de cadeaux d'anniversaire",collegues:"Échange de cadeaux entre collègues",amis:"Échange de cadeaux entre amis",classe:"Échange de cadeaux de fin d'année",autre:"Échange de cadeaux"};
var DEF={noel:["Noël en famille 2026","2026-12-24"],nouvelan:["Nouvel An entre amis","2026-12-31"],stnicolas:["Saint-Nicolas en famille","2026-12-06"],anniv:["Anniversaire de Léa",""],collegues:["Cadeaux de l'équipe",""],amis:["Soirée cadeaux entre amis",""],classe:["Fin d'année du club",""],autre:["Échange de cadeaux",""]};
$("type").onchange=function(){var x=DEF[this.value];$("ev").value=x[0];$("date").value=x[1]};
var IDEES={
 "10":[["Mug original","Un classique qui fait toujours plaisir","mug cadeau original"],["Chaussettes de Noël","Drôles et douillettes","chaussettes noel fantaisie"],["Jeu de cartes d'apéro","Pour rire entre amis","jeu de cartes apero"],["Bougie parfumée","Une ambiance cocooning","bougie parfumee"]],
 "20":[["Plaid tout doux","Pour les soirées d'hiver","plaid polaire doux"],["Jeu de société rapide","Une partie en 15 minutes","jeu de societe ambiance"],["Coffret thé ou café","Pour les gourmands","coffret the cadeau"],["Lampe veilleuse","Jolie sur une table de nuit","lampe veilleuse deco"]],
 "30":[["Enceinte Bluetooth","Petite mais puissante","enceinte bluetooth portable"],["Coffret cocktail","Pour jouer au barman","coffret cocktail"],["Livre de recettes","Du nouveau en cuisine","livre de recettes"],["Gourde isotherme","Utile tous les jours","gourde isotherme inox"]],
 "15":[["Coffret de thés","Pour les pauses gourmandes","coffret the"],["Jeu de cartes rapide","Parfait pour les soirées","jeu de cartes ambiance"],["Bougie parfumée","Une ambiance cocooning","bougie parfumee"],["Chaussettes de Noël","Drôles et douillettes","chaussettes noel fantaisie"]],
 "50":[["Écouteurs sans fil","Un vrai cadeau plaisir","ecouteurs sans fil"],["Appareil à fondue ou raclette","Pour les repas à plusieurs","appareil raclette"],["Lampe de lecture","Pour les lecteurs du soir","lampe de lecture led"],["Coffret jeu de société expert","Des heures de jeu","jeu de societe strategie"]]
};
function afficherRes(o){
  $("vue-orga").classList.add("cache");$("vue-res").classList.remove("cache");
  $("r-titre").textContent="Bonjour "+o.de;
  var dt=o.d?new Date(o.d+"T12:00").toLocaleDateString("fr-FR",{day:"numeric",month:"long"}):"";
  $("r-ev").textContent=o.e+(dt?", échange le "+dt:"");
  if(o.t&&o.t!=="noel"){document.querySelector("#vue-res .hero h1").style.maxWidth="none"}
  $("r-pour").textContent=o.a;$("r-budget").textContent="Budget : "+o.b+" € environ";$("r-b").textContent=o.b;var gd={"10":"/idee-cadeau-10-euros/","15":"/idee-cadeau-15-euros/","20":"/idee-cadeau-20-euros/","30":"/idee-cadeau-30-euros/","50":"/idee-cadeau-50-euros/"};$("r-guide").href=$("r-guide2").href=gd[o.b]||"/idee-cadeau-20-euros/";$("r-b2").textContent=o.b;
  var g=$("grille");g.innerHTML="";
  (IDEES[o.b]||IDEES["20"]).forEach(function(x){
    var a=document.createElement("div");a.className="idee";
    a.innerHTML='<b>'+x[0]+'</b><span>'+x[1]+'</span><a class="btn s petit" target="_blank" rel="sponsored nofollow noopener" href="https://www.amazon.fr/s?k='+encodeURIComponent(x[2])+'&tag=quioffreaqui-21">Voir les idées</a>';
    g.appendChild(a);
  });
  function ouvrir(){$("paquet").classList.add("ouvert");$("nom").classList.remove("cache");$("r-idees").classList.remove("cache")}
  $("paquet").onclick=ouvrir;$("paquet").onkeydown=function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();ouvrir()}};
}
window.addEventListener("hashchange",function(){if(/r=/.test(location.hash))location.reload()});
var m=location.hash.match(/r=([^&]+)/);
if(m){try{afficherRes(decode(m[1]))}catch(e){rendreListe();rendreExc()}}else{rendreListe();rendreExc()}
})();