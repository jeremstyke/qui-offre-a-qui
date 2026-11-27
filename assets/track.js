// Mesure d'audience anonyme (pages vues et clics vers Amazon), partagée avec les autres sites.
(function(){
  var SITE = 'qoaq';
  var SB = 'https://txvrlvcxfnylnrpdrxtt.supabase.co/rest/v1/vcs_hits';
  var KEY = 'sb_publishable_7aA-njoU5fU2ialO0ExwQQ_REHjAEIe';
  function ls(k, v){ try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch(e){ return null; } }
  if (/[?&]moi=1/.test(location.search)) ls('aff_moi', '1');
  if (/[?&]moi=0/.test(location.search)) ls('aff_moi', '0');
  var bot = /bot|crawl|spider|slurp|lighthouse|headless|preview/i.test(navigator.userAgent);
  var vid = ls('aff_vid'); if (!vid) { vid = Math.random().toString(36).slice(2, 12); ls('aff_vid', vid); }
  var dev = /Mobi|Android|iPhone/i.test(navigator.userAgent) ? 'mobile' : 'desktop';
  var ref = document.referrer ? (document.referrer.indexOf(location.host) > -1 ? 'interne' : document.referrer.split('/')[2] || '') : '';
  // Source marquée dans le lien (?src=yt, fb, pin...) : gardée pour toute la visite et ajoutée à la provenance
  var sm = location.search.match(/[?&]src=([a-z0-9-]{1,30})/i); if (sm) { try { sessionStorage.setItem('qoaq_s', sm[1]); } catch(e){} }
  var srcv = sm ? sm[1] : (function(){ try { return sessionStorage.getItem('qoaq_s'); } catch(e){ return null; } })();
  if (srcv && ref !== 'interne') ref = 'src:' + srcv + (ref ? ' ' + ref : '');
  else if (srcv) ref = 'interne src:' + srcv;
  function hit(kind, target){
    if (bot || ls('aff_moi') === '1') return;
    var body = JSON.stringify({site: SITE, kind: kind, path: location.pathname.slice(0, 290), ref: ref.slice(0, 290), dev: dev, vid: vid, target: (target || '').slice(0, 290)});
    try { fetch(SB, {method: 'POST', keepalive: true, headers: {'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal'}, body: body}); } catch(e){}
  }
  var EMB = /[?&]e=1/.test(location.search);
  if (!EMB) hit('view');
  window.qoaqHit = hit;
  // Temps passé : on envoie les secondes visibles à chaque fois que la page passe en arrière-plan ou se ferme
  var vu = document.visibilityState === 'visible' ? Date.now() : 0, cumul = 0;
  function envoyerDuree(){ if (vu) { cumul += (Date.now() - vu) / 1000; vu = 0; } var s = Math.round(cumul); if (s >= 2) { hit('duree', String(Math.min(s, 1800))); } cumul = 0; }
  document.addEventListener('visibilitychange', function(){ if (document.visibilityState === 'hidden') envoyerDuree(); else vu = Date.now(); });
  window.addEventListener('pagehide', envoyerDuree);
  document.addEventListener('click', function(e){
    var sh = e.target.closest && e.target.closest('#liens .act a, #liens .act button');
    if (sh) hit('partage', /wa\.me/.test(sh.href || '') ? 'whatsapp' : /^sms/.test(sh.href || '') ? 'sms' : 'copie');
    var aw = e.target.closest && e.target.closest('a[href*="awin1.com"]');
    if (aw) { var mm = aw.href.match(/awinmid=(\d+)/); hit('awin', (mm ? mm[1] : '') + ' ' + location.pathname); }
    var a = e.target.closest && e.target.closest('a[href*="amazon.fr"]');
    if (a) { var m = a.href.match(/[?&]k=([^&]+)/); hit('amz', m ? decodeURIComponent(m[1].replace(/\+/g, ' ')) : a.href.split('?')[0]); }
  }, true);
})();

// Formulaires d'inscription à la newsletter (double opt-in : un e-mail de confirmation est envoyé)
(function(){
  var FN = 'https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/qoaq';
  document.addEventListener('submit', function(e){
    var f = e.target; if (!f.classList || !f.classList.contains('nlf')) return;
    e.preventDefault();
    var i = f.querySelector('input'), b = f.querySelector('button'), m = f.nextElementSibling;
    var v = (i.value || '').trim();
    if (!/^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v)) { m.textContent = 'Cette adresse ne semble pas valide.'; i.focus(); return; }
    b.disabled = true; b.textContent = 'Envoi...';
    fetch(FN, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({action: 'inscrire', email: v, src: f.getAttribute('data-src') || 'site'})})
      .then(function(r){ return r.json().then(function(j){ j._s = r.status; return j; }); })
      .then(function(j){
        if (j.ok) {
          f.style.display = 'none';
          m.textContent = j.deja ? 'Vous êtes déjà inscrit, merci !' : 'Presque fini : cliquez sur le lien que nous venons de vous envoyer par e-mail (pensez aux spams).';
          try { window.qoaqHit && window.qoaqHit('lead', 'form_' + (f.getAttribute('data-src') || 'site')); } catch(_){}
        } else {
          b.disabled = false; b.textContent = 'Je m\'inscris';
          m.textContent = j._s === 429 ? 'Trop de demandes, réessayez dans une heure.' : j.raison === 'email' ? 'Cette adresse ne semble pas valide.' : 'Ça n\'a pas marché, réessayez.';
        }
      }).catch(function(){ b.disabled = false; b.textContent = 'Je m\'inscris'; m.textContent = 'Pas de connexion, réessayez.'; });
  });
})();

// Vidéo YouTube chargée seulement au clic (pas de cookie avant)
document.addEventListener('click', function(e){
  var b = e.target.closest && e.target.closest('.vid button'); if (!b) return;
  var v = b.parentNode, id = v.getAttribute('data-yt'); if (!id) return;
  var f = document.createElement('iframe');
  f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
  f.title = b.getAttribute('aria-label') || 'Vidéo'; f.allow = 'autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen = true;
  v.innerHTML = ''; v.appendChild(f);
  try { window.qoaqHit && window.qoaqHit('video', id); } catch(_){}
});
