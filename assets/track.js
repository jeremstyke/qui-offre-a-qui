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
  function hit(kind, target){
    if (bot || ls('aff_moi') === '1') return;
    var body = JSON.stringify({site: SITE, kind: kind, path: location.pathname.slice(0, 290), ref: ref.slice(0, 290), dev: dev, vid: vid, target: (target || '').slice(0, 290)});
    try { fetch(SB, {method: 'POST', keepalive: true, headers: {'apikey': KEY, 'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json', 'Prefer': 'return=minimal'}, body: body}); } catch(e){}
  }
  hit('view');
  window.qoaqHit = hit;
  // Temps passé : on envoie les secondes visibles à chaque fois que la page passe en arrière-plan ou se ferme
  var vu = document.visibilityState === 'visible' ? Date.now() : 0, cumul = 0;
  function envoyerDuree(){ if (vu) { cumul += (Date.now() - vu) / 1000; vu = 0; } var s = Math.round(cumul); if (s >= 2) { hit('duree', String(Math.min(s, 1800))); } cumul = 0; }
  document.addEventListener('visibilitychange', function(){ if (document.visibilityState === 'hidden') envoyerDuree(); else vu = Date.now(); });
  window.addEventListener('pagehide', envoyerDuree);
  document.addEventListener('click', function(e){
    var sh = e.target.closest && e.target.closest('#liens .act a, #liens .act button');
    if (sh) hit('partage', /wa\.me/.test(sh.href || '') ? 'whatsapp' : /^sms/.test(sh.href || '') ? 'sms' : 'copie');
    var a = e.target.closest && e.target.closest('a[href*="amazon.fr"]');
    if (a) { var m = a.href.match(/[?&]k=([^&]+)/); hit('amz', m ? decodeURIComponent(m[1].replace(/\+/g, ' ')) : a.href.split('?')[0]); }
  }, true);
})();
