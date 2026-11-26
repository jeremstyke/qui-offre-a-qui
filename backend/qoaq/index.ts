// Qui offre à qui : tirage au sort fait sur le serveur, résultat envoyé à chaque participant par e-mail (Resend).
// L'organisateur ne voit jamais les résultats. Il reçoit une confirmation et un lien de gestion pour renvoyer un e-mail.
import { createClient } from "npm:@supabase/supabase-js@2";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const ORIGINS = ["https://qui-offre-a-qui.fr", "https://www.qui-offre-a-qui.fr", "https://jeremstyke.github.io", "http://localhost:8000"];
const SITE = "https://qui-offre-a-qui.fr";
const FN = "https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/qoaq";
const FROM = "Qui offre à qui <tirage@qui-offre-a-qui.fr>";
const REPLY = "contact@cvlibre.com";
const EMAIL = /^[^\s@<>"]{1,64}@[^\s@<>"]{1,190}\.[a-z]{2,24}$/i;
const MAX_PARTS = 40, MAX_PAR_HEURE = 6, MAX_RENVOIS = 30;
const NOMS: Record<string, string> = { noel: "Père Noël secret", nouvelan: "Échange de cadeaux du Nouvel An", stnicolas: "Saint-Nicolas", anniv: "Échange de cadeaux d'anniversaire", collegues: "Échange de cadeaux entre collègues", amis: "Échange de cadeaux entre amis", classe: "Échange de cadeaux de fin d'année", autre: "Échange de cadeaux" };

function cors(req: Request) {
  const o = req.headers.get("origin") || "";
  return { "Access-Control-Allow-Origin": ORIGINS.includes(o) ? o : SITE, "Access-Control-Allow-Headers": "content-type", "Access-Control-Allow-Methods": "POST,GET,OPTIONS", "Vary": "Origin" };
}
const esc = (s: string) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));
const court = (s: unknown, n: number) => String(s ?? "").replace(/[\r\n\t]+/g, " ").trim().slice(0, n);
async function sha(s: string) {
  const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(b)].map((x) => x.toString(16).padStart(2, "0")).join("");
}
function rnd(n: number) { const a = new Uint32Array(1); crypto.getRandomValues(a); return a[0] % n; }
// Même encodage que le site (tool.js) pour que la page de résultat fonctionne sans serveur
function code(o: unknown) {
  const bytes = new TextEncoder().encode(JSON.stringify(o));
  let r = ""; for (const b of bytes) r += String.fromCharCode(b ^ 23);
  return btoa(r).replace(/=+$/, "");
}
const SECRET = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") || "x";
async function sig(tid: number, idx: number) { return (await sha(`abo|${tid}.${idx}|${SECRET}`)).slice(0, 16); }
async function jeton(tid: number, idx: number) { return `${tid}.${idx}.${await sig(tid, idx)}`; }
async function abonner(p: string, source: string) {
  const m = /^(\d+)\.(\d+)\.([a-f0-9]{16})$/.exec(p || "");
  if (!m || (await sig(+m[1], +m[2])) !== m[3]) return false;
  const { data: x } = await sb.from("qoaq_participants").select("nom,email").eq("tirage_id", +m[1]).eq("idx", +m[2]).maybeSingle();
  if (!x) return false;
  const { data: t } = await sb.from("qoaq_tirages").select("occasion").eq("id", +m[1]).maybeSingle();
  await sb.from("qoaq_abonnes").upsert({ email: x.email, prenom: x.nom, source, occasion: t?.occasion || null, actif: true, desabo_at: null }, { onConflict: "email" });
  return true;
}
let KEY = "";
async function cle() {
  if (KEY) return KEY;
  KEY = Deno.env.get("RESEND_QOAQ") || "";
  if (!KEY) { const { data } = await sb.from("tm_cfg").select("v").eq("k", "resend_qoaq").maybeSingle(); KEY = data?.v || ""; }
  return KEY;
}
function dateFr(d: string | null) {
  if (!d || !/^\d{4}-\d{2}-\d{2}$/.test(d)) return "";
  return new Date(d + "T12:00:00Z").toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Paris" });
}
function cadre(titre: string, corps: string, pied: string) {
  return `<!doctype html><html lang="fr"><body style="margin:0;background:#f3f6f4"><div style="font-family:Arial,Helvetica,sans-serif;max-width:520px;margin:0 auto;background:#fff;color:#1d2a26">
<div style="height:8px;background:repeating-linear-gradient(-45deg,#b3263a 0 12px,#ffffff 12px 18px,#1f6b4f 18px 30px,#ffffff 30px 36px)"></div>
<div style="padding:24px 24px 8px"><p style="margin:0 0 4px;font-size:13px;color:#5b6b66">Qui offre à qui</p><h1 style="font-size:22px;line-height:1.3;margin:0 0 16px">${titre}</h1>${corps}</div>
<div style="padding:16px 24px 24px;font-size:12px;line-height:1.5;color:#5b6b66;border-top:1px solid #e2e8e5">${pied}</div></div></body></html>`;
}
const bouton = (url: string, txt: string) => `<p style="margin:20px 0"><a href="${esc(url)}" style="display:inline-block;background:#b3263a;color:#fff;text-decoration:none;font-weight:bold;padding:14px 22px;border-radius:10px">${txt}</a></p>`;

async function envoyerLot(mails: unknown[]) {
  const k = await cle();
  if (!k) return mails.map(() => false);
  const res: boolean[] = [];
  for (let i = 0; i < mails.length; i += 100) {
    const lot = mails.slice(i, i + 100);
    let ok = false;
    try {
      const r = await fetch("https://api.resend.com/emails/batch", { method: "POST", headers: { Authorization: `Bearer ${k}`, "Content-Type": "application/json" }, body: JSON.stringify(lot) });
      ok = r.ok; if (!ok) console.log("resend", (await r.text()).slice(0, 300));
    } catch (e) { console.log("resend", String(e).slice(0, 200)); }
    lot.forEach(() => res.push(ok));
  }
  return res;
}

type T = { ev: string; budget: string; date_ech: string | null; orga_email?: string | null; liste?: string | null };
const lienListe = (l: string, nom?: string) => `${SITE}/qui-apporte-quoi/#l=${l}${nom ? "&n=" + encodeURIComponent(nom) : ""}`;
function infos(t: T) {
  const quand = dateFr(t.date_ech);
  return `<p style="margin:0 0 8px;font-size:15px;line-height:1.5">${esc(t.ev)}${quand ? `, échange le ${esc(quand)}` : ""}${t.budget ? `. Budget : ${esc(t.budget)} € environ.` : "."}</p>`;
}
function idees(b: string) { return /^(5|10|15|20|30|50)$/.test(b) ? `${SITE}/idee-cadeau-${b}-euros/?utm_source=email` : `${SITE}/guides/?utm_source=email`; }
function mailParticipant(t: T, p: { nom: string; email: string; url: string; jeton?: string }) {
  const quand = dateFr(t.date_ech);
  return {
    from: FROM, reply_to: REPLY, to: [p.email],
    subject: `${p.nom}, votre tirage pour « ${t.ev} » est prêt`,
    html: cadre(`Bonjour ${esc(p.nom)}, votre tirage est prêt`,
      `${infos(t)}<p style="margin:0;font-size:15px;line-height:1.5">Le tirage au sort a été fait. Le nom de la personne à qui vous offrez un cadeau vous attend derrière ce bouton. Vous êtes le seul à le voir : même l'organisateur ne le connaît pas. Gardez le secret !</p>${bouton(p.url, "Découvrir à qui j'offre")}<div style="background:#f3f6f4;border-radius:12px;padding:14px 16px;margin:0 0 16px"><p style="margin:0 0 6px;font-size:15px;font-weight:bold">Besoin d'une idée de cadeau ?</p><p style="margin:0;font-size:15px;line-height:1.5"><a href="${esc(idees(t.budget))}" style="color:#1f6b4f;font-weight:bold">${/^(5|10|15|20|30|50)$/.test(t.budget) ? `Voir 15 idées cadeaux à ${esc(t.budget)} €` : "Voir nos idées cadeaux par budget"}</a>, classées par goût et faciles à commander.</p></div>${t.liste ? `<div style="background:#fdf6e3;border-radius:12px;padding:14px 16px;margin:0 0 16px"><p style="margin:0 0 6px;font-size:15px;font-weight:bold">Et pour le repas, qui apporte quoi ?</p><p style="margin:0 0 10px;font-size:15px;line-height:1.5">Une liste commune est prête pour tous les participants : dites ce que vous apportez.</p><a href="${esc(lienListe(t.liste, p.nom))}" style="color:#1f6b4f;font-weight:bold">Voir la liste du repas</a></div>` : ""}<p style="margin:0 0 8px;font-size:14px;color:#5b6b66">Gardez ce message : le bouton vous permet de revoir votre résultat à tout moment.</p>${p.jeton ? `<div style="border:1px solid #e2e8e5;border-radius:12px;padding:14px 16px;margin:16px 0 8px"><p style="margin:0 0 6px;font-size:15px;font-weight:bold">Recevoir la newsletter ?</p><p style="margin:0 0 10px;font-size:14px;line-height:1.5;color:#5b6b66">Des idées cadeaux de temps en temps et un rappel pour le tirage de l'an prochain. Désinscription en un clic.</p><a href="${FN}?abo=${esc(p.jeton)}" style="display:inline-block;background:#1f6b4f;color:#fff;text-decoration:none;font-weight:bold;padding:10px 16px;border-radius:10px;font-size:14px">Oui, je m'inscris</a></div>` : ""}`,
      `Vous recevez ce message parce que l'organisateur de « ${esc(t.ev)} » vous a inscrit au tirage au sort sur <a href="${SITE}/" style="color:#5b6b66">qui-offre-a-qui.fr</a>. Votre adresse sert à vous envoyer ce résultat ; vous ne recevrez rien d'autre sans votre accord.`),
    text: `Bonjour ${p.nom},\n\nLe tirage au sort pour « ${t.ev} » est fait${quand ? ` (échange le ${quand})` : ""}.\nDécouvrez à qui vous offrez un cadeau (vous êtes le seul à le voir) : ${p.url}\n\nBesoin d'une idée de cadeau ? ${idees(t.budget)}\n\nGardez ce message pour revoir votre résultat.\n\nQui offre à qui, ${SITE}/`,
  };
}

function tirer(n: number, ex: Set<string>) {
  const interdit = (a: number, b: number) => a === b || ex.has(a + "-" + b) || ex.has(b + "-" + a);
  for (let essai = 0; essai < 2000; essai++) {
    const ordre: number[] = [], pris = new Set<number>(); let ok = true;
    const idx = [...Array(n).keys()].sort(() => rnd(3) - 1);
    const res: number[] = new Array(n);
    for (const i of idx) {
      const c: number[] = []; for (let j = 0; j < n; j++) if (!pris.has(j) && !interdit(i, j)) c.push(j);
      if (!c.length) { ok = false; break; }
      const k = c[rnd(c.length)]; res[i] = k; pris.add(k); ordre.push(k);
    }
    if (ok) return res;
  }
  return null;
}

async function etat(id: number) {
  const { data } = await sb.from("qoaq_participants").select("idx,nom,email,envois,statut,last_sent").eq("tirage_id", id).order("idx");
  return (data || []).map((p) => ({ i: p.idx, nom: p.nom, email: p.email, envois: p.envois, statut: p.statut, le: p.last_sent }));
}

// Listes de repas partagées « qui apporte quoi » : toute personne qui a le lien peut modifier
const LID = /^[a-z0-9]{10}$/;
function rid() { const a = new Uint8Array(10); crypto.getRandomValues(a); return [...a].map((x) => "abcdefghijkmnpqrstuvwxyz23456789"[x % 32]).join(""); }
const MODELES: Record<string, [string, string[]][]> = {
  noel: [["Apéritif", ["Biscuits apéro", "Toasts et tartinades"]], ["Entrée", ["Entrée"]], ["Plat", ["Plat principal", "Accompagnement"]], ["Fromage", ["Plateau de fromages"]], ["Dessert", ["Bûche de Noël", "Chocolats"]], ["Boissons", ["Champagne", "Vin", "Jus de fruits et sodas"]], ["Pain et divers", ["Pain", "Glaçons"]]],
  nouvelan: [["Apéritif", ["Biscuits apéro", "Verrines"]], ["Plat", ["Plat principal"]], ["Dessert", ["Dessert"]], ["Boissons", ["Champagne pour minuit", "Vin", "Softs"]], ["Fête", ["Cotillons", "Glaçons"]]],
  anniv: [["Salé", ["Chips", "Quiches ou pizzas"]], ["Sucré", ["Gâteau d'anniversaire", "Bonbons"]], ["Boissons", ["Jus de fruits", "Sodas"]], ["Fête", ["Bougies", "Décoration"]]],
  autre: [["Salé", ["Plat salé", "Plat salé"]], ["Sucré", ["Dessert", "Dessert"]], ["Boissons", ["Boissons", "Boissons"]], ["Divers", ["Pain", "Gobelets et serviettes"]]],
};
async function creerListe(titre: string, date_ev: string | null, occ: string, ipH: string) {
  const id = rid();
  const { error } = await sb.from("qoaq_listes").insert({ id, titre: titre.slice(0, 80), date_ev, ip_hash: ipH });
  if (error) return null;
  const m = MODELES[occ === "stnicolas" ? "noel" : occ] || MODELES.autre;
  const items: any[] = []; m.forEach(([cat, l]) => l.forEach((label) => items.push({ liste_id: id, cat, label, pos: items.length })));
  await sb.from("qoaq_liste_items").insert(items);
  return id;
}
async function lireListe(id: string) {
  const { data: l } = await sb.from("qoaq_listes").select("id,titre,date_ev,lieu,updated_at").eq("id", id).maybeSingle();
  if (!l) return null;
  const { data: it } = await sb.from("qoaq_liste_items").select("id,cat,label,qui,pos").eq("liste_id", id).order("pos").order("id");
  return { ...l, items: it || [] };
}

Deno.serve(async (req) => {
  const H = cors(req);
  const J = (o: unknown, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { ...H, "Content-Type": "application/json", "Cache-Control": "no-store" } });
  if (req.method === "OPTIONS") return new Response(null, { headers: H });
  const u = new URL(req.url);

  if (req.method === "GET") {
    const go = (r: string) => new Response(null, { status: 302, headers: { Location: `${SITE}/newsletter/?r=${r}` } });
    const abo = u.searchParams.get("abo");
    if (abo) return go((await abonner(abo, "email")) ? "ok" : "lien");
    const t = u.searchParams.get("stop") || "";
    if (/^[a-f0-9]{24}$/.test(t)) {
      const { data } = await sb.from("qoaq_tirages").select("orga_email").eq("unsub", t).maybeSingle();
      if (data?.orga_email) {
        await sb.from("qoaq_tirages").update({ rappel: false }).eq("orga_email", data.orga_email);
        await sb.from("qoaq_abonnes").update({ actif: false, desabo_at: new Date().toISOString() }).eq("email", data.orga_email);
        return go("stop");
      }
      const { data: ab } = await sb.from("qoaq_abonnes").select("email").eq("unsub", t).maybeSingle();
      if (ab) { await sb.from("qoaq_abonnes").update({ actif: false, desabo_at: new Date().toISOString() }).eq("email", ab.email); return go("stop"); }
    }
    return go("lien");
  }
  if (req.method !== "POST") return J({ ok: false }, 405);

  let b: any;
  try { b = await req.json(); } catch { return J({ ok: false, raison: "format" }, 400); }


  if (typeof b.action === "string" && b.action.startsWith("liste_")) {
    const ip0 = req.headers.get("cf-connecting-ip") || req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() || "?";
    if (b.action === "liste_creer") {
      const ipH0 = await sha("qoaq|" + ip0);
      const { count } = await sb.from("qoaq_listes").select("id", { count: "exact", head: true }).eq("ip_hash", ipH0).gte("created_at", new Date(Date.now() - 3600e3).toISOString());
      if ((count || 0) >= 10) return J({ ok: false, raison: "limite" }, 429);
      const titre = court(b.titre, 80) || "Notre repas";
      const date_ev = /^\d{4}-\d{2}-\d{2}$/.test(String(b.date || "")) ? b.date : null;
      const id = rid();
      const { error } = await sb.from("qoaq_listes").insert({ id, titre, date_ev, lieu: court(b.lieu, 80) || null, ip_hash: ipH0 });
      if (error) return J({ ok: false, raison: "serveur" }, 500);
      const items = (Array.isArray(b.items) ? b.items.slice(0, 80) : []).map((x: any, i: number) => ({ liste_id: id, cat: court(x?.cat, 30) || "Autre", label: court(x?.label, 60), pos: i })).filter((x: any) => x.label);
      if (items.length) await sb.from("qoaq_liste_items").insert(items);
      return J({ ok: true, liste: await lireListe(id) });
    }
    const id = String(b.id || "");
    if (!LID.test(id)) return J({ ok: false, raison: "lien" }, 400);
    const l = await lireListe(id);
    if (!l) return J({ ok: false, raison: "introuvable" }, 404);
    const item = parseInt(b.item);
    if (b.action === "liste_prendre" && item) {
      await sb.from("qoaq_liste_items").update({ qui: court(b.qui, 30) || null }).eq("id", item).eq("liste_id", id);
    } else if (b.action === "liste_ajouter") {
      if (l.items.length >= 150) return J({ ok: false, raison: "plein" }, 400);
      const label = court(b.label, 60);
      if (label) await sb.from("qoaq_liste_items").insert({ liste_id: id, cat: court(b.cat, 30) || "Autre", label, qui: court(b.qui, 30) || null, pos: 1000 + l.items.length });
    } else if (b.action === "liste_suppr" && item) {
      await sb.from("qoaq_liste_items").delete().eq("id", item).eq("liste_id", id);
    } else if (b.action === "liste_info") {
      await sb.from("qoaq_listes").update({ titre: court(b.titre, 80) || l.titre, date_ev: /^\d{4}-\d{2}-\d{2}$/.test(String(b.date || "")) ? b.date : l.date_ev, lieu: court(b.lieu, 80) || null }).eq("id", id);
    } else if (b.action === "liste_mail") {
      const em = court(b.email, 254).toLowerCase();
      if (!EMAIL.test(em)) return J({ ok: false, raison: "email" }, 400);
      const ipH1 = await sha("qoaq|" + ip0);
      const { count: nm } = await sb.from("qoaq_retrouver").select("id", { count: "exact", head: true }).eq("ip_hash", ipH1).gte("at", new Date(Date.now() - 3600e3).toISOString());
      if ((nm || 0) >= 10) return J({ ok: false, raison: "limite" }, 429);
      await sb.from("qoaq_retrouver").insert({ email_hash: await sha(em), ip_hash: ipH1 });
      const url = `${SITE}/qui-apporte-quoi/#l=${id}`;
      const quand = dateFr(l.date_ev);
      const [ok] = await envoyerLot([{ from: FROM, reply_to: REPLY, to: [em], subject: `Votre liste « ${l.titre} » : qui apporte quoi`,
        html: cadre(`Votre liste « ${esc(l.titre)} »`, `<p style="margin:0 0 8px;font-size:15px;line-height:1.5">${quand ? `Repas du ${esc(quand)}. ` : ""}Voici le lien de votre liste : gardez cet e-mail pour la retrouver et suivre qui apporte quoi, depuis n'importe quel appareil.</p>${bouton(url, "Ouvrir la liste")}<p style="margin:0;font-size:14px;color:#5b6b66">Partagez ce même lien avec les invités pour qu'ils choisissent ce qu'ils apportent.</p>`, `Vous recevez ce message parce que vous avez demandé le lien de cette liste sur <a href="${SITE}/qui-apporte-quoi/" style="color:#5b6b66">qui-offre-a-qui.fr</a>. Votre adresse n'est pas conservée.`),
        text: `Votre liste « ${l.titre} » : ${url}\nGardez cet e-mail pour la retrouver.\n\nQui offre à qui, ${SITE}/` }]);
      return J({ ok });
    } else if (b.action !== "liste_lire") return J({ ok: false }, 400);
    if (b.action !== "liste_lire" && b.action !== "liste_mail") await sb.from("qoaq_listes").update({ updated_at: new Date().toISOString() }).eq("id", id);
    return J({ ok: true, liste: b.action === "liste_lire" ? l : await lireListe(id) });
  }

  // Nettoyage : les adresses des participants sont supprimées 8 mois après le tirage (les abonnés à la newsletter sont gardés à part)
  try {
    await sb.from("qoaq_participants").delete().lt("created_at", new Date(Date.now() - 240 * 864e5).toISOString());
  } catch (_) { /* ignore */ }

  if (b.action === "abo") return J({ ok: await abonner(String(b.p || ""), "resultat") });

  // Gestion par l'organisateur : voir l'état ou renvoyer un e-mail (sans jamais voir les résultats)
  if (b.action === "etat" || b.action === "renvoyer") {
    const id = parseInt(b.id), g = String(b.g || "");
    if (!id || !/^[a-f0-9]{24}$/.test(g)) return J({ ok: false, raison: "lien" }, 400);
    const { data: t } = await sb.from("qoaq_tirages").select("id,ev,budget,date_ech,gestion,renvois,created_at,liste_id").eq("id", id).maybeSingle();
    if (!t || t.gestion !== g) return J({ ok: false, raison: "lien" }, 404);
    if (b.action === "renvoyer") {
      if (t.renvois >= MAX_RENVOIS) return J({ ok: false, raison: "limite" }, 429);
      const i = parseInt(b.i);
      const { data: p } = await sb.from("qoaq_participants").select("id,nom,email,url,envois").eq("tirage_id", id).eq("idx", i).maybeSingle();
      if (!p) return J({ ok: false, raison: "inconnu" }, 404);
      let email = p.email;
      const nouv = court(b.email, 254).toLowerCase();
      if (nouv) { if (!EMAIL.test(nouv)) return J({ ok: false, raison: "email" }, 400); email = nouv; }
      const [ok] = await envoyerLot([mailParticipant({ ...(t as any), liste: t.liste_id } as T, { nom: p.nom, email, url: p.url, jeton: await jeton(id, i) })]);
      await sb.from("qoaq_participants").update({ email, envois: p.envois + 1, statut: ok ? "envoye" : "echec", last_sent: new Date().toISOString() }).eq("id", p.id);
      await sb.from("qoaq_tirages").update({ renvois: t.renvois + 1 }).eq("id", id);
      return J({ ok, participants: await etat(id) });
    }
    return J({ ok: true, ev: t.ev, budget: t.budget, date: t.date_ech, cree: t.created_at, liste: t.liste_id, participants: await etat(id) });
  }

  // Nouveau tirage
  const occ = court(b.t, 20);
  const ev = court(b.ev, 80) || NOMS[occ] || "Échange de cadeaux";
  const budget = court(b.b, 4), d = court(b.d, 10);
  const parts = Array.isArray(b.parts) ? b.parts.slice(0, MAX_PARTS + 1) : [];
  if (parts.length < 3 || parts.length > MAX_PARTS) return J({ ok: false, raison: "participants" }, 400);
  const P = parts.map((p: any) => ({ nom: court(p?.nom, 40), email: court(p?.email, 254).toLowerCase() }));
  const bad = P.findIndex((p) => !p.nom || !EMAIL.test(p.email));
  if (bad > -1) return J({ ok: false, raison: "email", i: bad }, 400);
  const orga = court(b.orga, 254).toLowerCase();
  if (orga && !EMAIL.test(orga)) return J({ ok: false, raison: "orga" }, 400);
  const rappel = !!b.rappel && !!orga;
  const ex = new Set<string>();
  for (const e of Array.isArray(b.excl) ? b.excl.slice(0, 60) : []) { const x = +e?.[0], y = +e?.[1]; if (x >= 0 && y >= 0 && x < P.length && y < P.length && x !== y) ex.add(x + "-" + y); }

  const ip = req.headers.get("cf-connecting-ip") || req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() || "?";
  const ipH = await sha("qoaq|" + ip);
  const { count } = await sb.from("qoaq_tirages").select("id", { count: "exact", head: true }).eq("ip_hash", ipH).gte("created_at", new Date(Date.now() - 3600e3).toISOString());
  if ((count || 0) >= MAX_PAR_HEURE) return J({ ok: false, raison: "limite" }, 429);

  const res = tirer(P.length, ex);
  if (!res) return J({ ok: false, raison: "exclusions" }, 400);

  const date_ech = /^\d{4}-\d{2}-\d{2}$/.test(d) ? d : null;
  const { data: row, error } = await sb.from("qoaq_tirages").insert({
    ev, occasion: occ, budget, date_ech, nb: P.length,
    orga_email: rappel ? orga : null, rappel, rappel_at: rappel ? new Date().toISOString() : null, ip_hash: ipH,
  }).select("id,unsub,gestion").single();
  if (error || !row) return J({ ok: false, raison: "serveur" }, 500);

  const listeId = await creerListe(ev, date_ech, occ, ipH);
  if (listeId) await sb.from("qoaq_tirages").update({ liste_id: listeId }).eq("id", row.id);
  const t: T = { ev, budget, date_ech, liste: listeId };
  const jetons = await Promise.all(P.map((_, i) => jeton(row.id, i)));
  const lignes = P.map((p, i) => ({ tirage_id: row.id, idx: i, nom: p.nom, email: p.email, url: `${SITE}/#r=${code({ e: ev, t: occ, b: budget, d, de: p.nom, a: P[res[i]].nom, l: listeId || undefined })}&p=${jetons[i]}` }));
  const mails: unknown[] = lignes.map((l, i) => mailParticipant(t, { ...l, jeton: jetons[i] }));
  const gestion = `${SITE}/#g=${row.id}.${row.gestion}`;
  if (orga) {
    const stop = `${FN}?stop=${row.unsub}`;
    const liste = P.map((p) => `<li style="margin:0 0 6px"><b>${esc(p.nom)}</b> <span style="color:#5b6b66">${esc(p.email)}</span></li>`).join("");
    mails.push({
      from: FROM, reply_to: REPLY, to: [orga],
      subject: `Tirage « ${ev} » fait : ${P.length} participants prévenus`,
      html: cadre(`Votre tirage « ${esc(ev)} » est fait`,
        `${infos(t)}<p style="margin:0 0 12px;font-size:15px;line-height:1.5">Chaque participant a reçu son résultat par e-mail. Personne d'autre ne le connaît, pas même vous : vous pouvez donc participer sans tricher.</p><ul style="padding-left:18px;margin:0 0 8px;font-size:15px">${liste}</ul><p style="margin:12px 0 0;font-size:15px;line-height:1.5">Quelqu'un n'a rien reçu ou s'est trompé d'adresse ? Renvoyez-lui son e-mail depuis la page de suivi, sans voir son résultat.</p>${bouton(gestion, "Suivre mon tirage")}${listeId ? `<p style="margin:0;font-size:15px;line-height:1.5">Une liste commune « qui apporte quoi » a été créée pour le repas : <a href="${esc(lienListe(listeId))}" style="color:#1f6b4f;font-weight:bold">voir la liste</a>. Les participants la retrouvent sous leur résultat.</p>` : ""}`,
        rappel ? `Vous avez accepté qu'on vous rappelle l'an prochain de refaire un tirage (un seul e-mail par an). <a href="${esc(stop)}" style="color:#5b6b66">Ne plus recevoir de rappel</a>.` : `Votre adresse sert uniquement à vous envoyer cette confirmation.`),
      text: `Votre tirage « ${ev} » est fait. Chaque participant a reçu son résultat par e-mail, personne d'autre ne le connaît.\n\n` + P.map((p) => `${p.nom} : ${p.email}`).join("\n") + `\n\nSuivre le tirage et renvoyer un e-mail : ${gestion}\n\nQui offre à qui, ${SITE}/` + (rappel ? `\nNe plus recevoir de rappel : ${stop}` : ""),
      headers: rappel ? { "List-Unsubscribe": `<${stop}>` } : undefined,
    });
  }
  if (rappel) await sb.from("qoaq_abonnes").upsert({ email: orga, source: "organisateur", occasion: occ, actif: true, desabo_at: null }, { onConflict: "email" });
  const oks = await envoyerLot(mails);
  const now = new Date().toISOString();
  await sb.from("qoaq_participants").insert(lignes.map((l, i) => ({ ...l, envois: 1, statut: oks[i] ? "envoye" : "echec", last_sent: now })));
  const nOk = oks.slice(0, lignes.length).filter(Boolean).length;
  await sb.from("qoaq_tirages").update({ envoyes: oks.filter(Boolean).length, echecs: oks.filter((x) => !x).length }).eq("id", row.id);
  return J({ ok: nOk === lignes.length, envoyes: nOk, id: row.id, g: row.gestion, liste: listeId, participants: await etat(row.id) });
});
