// Qui offre à qui : envoi des liens du tirage par e-mail (Resend), récapitulatif pour l'organisateur, rappel l'an prochain (avec accord), désinscription.
import { createClient } from "npm:@supabase/supabase-js@2";

const sb = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
const ORIGINS = ["https://qui-offre-a-qui.fr", "https://www.qui-offre-a-qui.fr", "https://jeremstyke.github.io", "http://localhost:8000"];
const SITE = "https://qui-offre-a-qui.fr";
const FROM = "Qui offre à qui <tirage@qui-offre-a-qui.fr>";
const REPLY = "contact@cvlibre.com";
const EMAIL = /^[^\s@<>"]{1,64}@[^\s@<>"]{1,190}\.[a-z]{2,24}$/i;
const MAX_PARTS = 40, MAX_PAR_HEURE = 6;

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
let KEY = "";
async function cle() {
  if (KEY) return KEY;
  KEY = Deno.env.get("RESEND_QOAQ") || "";
  if (!KEY) { const { data } = await sb.from("tm_cfg").select("v").eq("k", "resend_qoaq").maybeSingle(); KEY = data?.v || ""; }
  return KEY;
}
function dateFr(d: string) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(d)) return "";
  return new Date(d + "T12:00:00Z").toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Paris" });
}
function cadre(titre: string, corps: string, pied: string) {
  return `<!doctype html><html lang="fr"><body style="margin:0;background:#f3f6f4"><div style="font-family:Arial,Helvetica,sans-serif;max-width:520px;margin:0 auto;background:#fff;color:#1d2a26">
<div style="height:8px;background:repeating-linear-gradient(-45deg,#b3263a 0 12px,#ffffff 12px 18px,#1f6b4f 18px 30px,#ffffff 30px 36px)"></div>
<div style="padding:24px 24px 8px"><p style="margin:0 0 4px;font-size:13px;color:#5b6b66">Qui offre à qui</p><h1 style="font-size:22px;line-height:1.3;margin:0 0 16px">${titre}</h1>${corps}</div>
<div style="padding:16px 24px 24px;font-size:12px;line-height:1.5;color:#5b6b66;border-top:1px solid #e2e8e5">${pied}</div></div></body></html>`;
}
const bouton = (url: string, txt: string) => `<p style="margin:20px 0"><a href="${esc(url)}" style="display:inline-block;background:#b3263a;color:#fff;text-decoration:none;font-weight:bold;padding:14px 22px;border-radius:10px">${txt}</a></p>`;

async function envoyer(mails: unknown[]) {
  const k = await cle();
  if (!k) return { ok: 0, ko: mails.length, err: "cle" };
  let ok = 0, ko = 0, err = "";
  for (let i = 0; i < mails.length; i += 100) {
    const lot = mails.slice(i, i + 100);
    try {
      const r = await fetch("https://api.resend.com/emails/batch", { method: "POST", headers: { Authorization: `Bearer ${k}`, "Content-Type": "application/json" }, body: JSON.stringify(lot) });
      if (r.ok) ok += lot.length; else { ko += lot.length; err = (await r.text()).slice(0, 200); }
    } catch (e) { ko += lot.length; err = String(e).slice(0, 200); }
  }
  return { ok, ko, err };
}

function pageDesinscription(ok: boolean) {
  const t = ok ? "C'est noté : vous ne recevrez plus de rappel." : "Ce lien n'est plus valable.";
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Désinscription | Qui offre à qui</title></head><body style="font-family:Arial,sans-serif;max-width:520px;margin:60px auto;padding:0 20px;color:#1d2a26"><h1 style="font-size:22px">${t}</h1><p>Votre adresse ne sera plus utilisée pour vous écrire.</p><p><a href="${SITE}/" style="color:#b3263a">Retour sur Qui offre à qui</a></p></body></html>`;
}

Deno.serve(async (req) => {
  const H = cors(req);
  const J = (o: unknown, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { ...H, "Content-Type": "application/json", "Cache-Control": "no-store" } });
  if (req.method === "OPTIONS") return new Response(null, { headers: H });
  const u = new URL(req.url);

  if (req.method === "GET") {
    const t = u.searchParams.get("stop") || "";
    let ok = false;
    if (/^[a-f0-9]{24}$/.test(t)) {
      const { data } = await sb.from("qoaq_tirages").select("orga_email").eq("unsub", t).maybeSingle();
      if (data?.orga_email) { await sb.from("qoaq_tirages").update({ rappel: false }).eq("orga_email", data.orga_email); ok = true; }
    }
    return new Response(pageDesinscription(ok), { headers: { "Content-Type": "text/html; charset=utf-8" } });
  }
  if (req.method !== "POST") return J({ ok: false }, 405);

  let b: any;
  try { b = await req.json(); } catch { return J({ ok: false, raison: "format" }, 400); }
  const ev = court(b.ev, 80) || "Échange de cadeaux";
  const occ = court(b.t, 20), budget = court(b.b, 4), d = court(b.d, 10);
  const parts = Array.isArray(b.parts) ? b.parts.slice(0, MAX_PARTS + 1) : [];
  if (parts.length < 3 || parts.length > MAX_PARTS) return J({ ok: false, raison: "participants" }, 400);
  const lien = (x: string) => typeof x === "string" && ((x.startsWith(SITE + "/") || x.startsWith("https://www.qui-offre-a-qui.fr/")) || x.startsWith("https://jeremstyke.github.io/") || x.startsWith("http://localhost:8000/")) && x.length < 900;
  const P = parts.map((p: any) => ({ nom: court(p?.nom, 40), email: court(p?.email, 254).toLowerCase(), url: String(p?.url || "") }));
  if (P.some((p) => !p.nom || !lien(p.url) || (p.email && !EMAIL.test(p.email)))) return J({ ok: false, raison: "donnees" }, 400);
  const orga = court(b.orga, 254).toLowerCase();
  if (orga && !EMAIL.test(orga)) return J({ ok: false, raison: "orga" }, 400);
  const rappel = !!b.rappel && !!orga;
  const dest = P.filter((p) => p.email);
  if (!dest.length && !orga) return J({ ok: false, raison: "rien" }, 400);

  const ip = req.headers.get("cf-connecting-ip") || req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() || "?";
  const ipH = await sha("qoaq|" + ip);
  const depuis = new Date(Date.now() - 3600e3).toISOString();
  const { count } = await sb.from("qoaq_tirages").select("id", { count: "exact", head: true }).eq("ip_hash", ipH).gte("created_at", depuis);
  if ((count || 0) >= MAX_PAR_HEURE) return J({ ok: false, raison: "limite" }, 429);

  const { data: row } = await sb.from("qoaq_tirages").insert({
    ev, occasion: occ, budget, date_ech: /^\d{4}-\d{2}-\d{2}$/.test(d) ? d : null, nb: P.length,
    orga_email: rappel ? orga : null, rappel, rappel_at: rappel ? new Date().toISOString() : null, ip_hash: ipH,
  }).select("id,unsub").single();

  const quand = dateFr(d);
  const infos = `<p style="margin:0 0 8px;font-size:15px;line-height:1.5">${esc(ev)}${quand ? `, échange le ${esc(quand)}` : ""}${budget ? `. Budget : ${esc(budget)} € environ.` : "."}</p>`;
  const piedPart = `Vous recevez ce message parce que l'organisateur de « ${esc(ev)} » a saisi votre adresse pour vous envoyer votre tirage. Elle n'est pas conservée et ne servira plus. Le tirage a été fait sur <a href="${SITE}/" style="color:#5b6b66">qui-offre-a-qui.fr</a>, gratuit et sans compte.`;
  const mails: unknown[] = dest.map((p) => ({
    from: FROM, reply_to: REPLY, to: [p.email],
    subject: `${p.nom}, votre tirage pour « ${ev} » est prêt`,
    html: cadre(`Bonjour ${esc(p.nom)}, votre tirage est prêt`,
      `${infos}<p style="margin:0;font-size:15px;line-height:1.5">Le nom de la personne à qui vous offrez un cadeau vous attend derrière ce bouton. Gardez le secret !</p>${bouton(p.url, "Découvrir à qui j'offre")}<p style="margin:0 0 8px;font-size:14px;color:#5b6b66">Gardez ce message : le lien vous permet de revoir votre résultat à tout moment. Vous y trouverez aussi des idées cadeaux selon le budget.</p>`,
      piedPart),
    text: `Bonjour ${p.nom},\n\nVotre tirage pour « ${ev} » est prêt${quand ? ` (échange le ${quand})` : ""}.\nDécouvrez à qui vous offrez un cadeau : ${p.url}\n\nGardez ce message, le lien vous permet de revoir votre résultat.\n\nQui offre à qui, ${SITE}/`,
  }));

  if (orga) {
    const stop = `https://txvrlvcxfnylnrpdrxtt.supabase.co/functions/v1/qoaq?stop=${row?.unsub || ""}`;
    const liste = P.map((p) => `<li style="margin:0 0 10px"><b>${esc(p.nom)}</b>${p.email ? ` <span style="color:#5b6b66">(envoyé à ${esc(p.email)})</span>` : ""}<br><a href="${esc(p.url)}" style="color:#1f6b4f;font-size:13px;word-break:break-all">Lien privé de ${esc(p.nom)}</a></li>`).join("");
    const pied = rappel
      ? `Vous avez accepté qu'on vous rappelle l'an prochain de refaire un tirage (un seul e-mail par an). <a href="${esc(stop)}" style="color:#5b6b66">Ne plus recevoir de rappel</a>.`
      : `Votre adresse sert uniquement à vous envoyer ce récapitulatif.`;
    mails.push({
      from: FROM, reply_to: REPLY, to: [orga],
      subject: `Votre tirage « ${ev} » : les ${P.length} liens privés`,
      html: cadre(`Votre tirage « ${esc(ev)} » est fait`,
        `${infos}<p style="margin:0 0 12px;font-size:15px;line-height:1.5">Voici le lien privé de chaque participant, pour le renvoyer si quelqu'un le perd. N'ouvrez pas les liens des autres si vous voulez garder la surprise : chacun dévoile un résultat.</p><ul style="padding-left:18px;margin:0 0 8px;font-size:15px">${liste}</ul>${bouton(SITE + "/", "Organiser un autre tirage")}`,
        pied),
      text: `Votre tirage « ${ev} » est fait.\n\n` + P.map((p) => `${p.nom} : ${p.url}`).join("\n") + `\n\nQui offre à qui, ${SITE}/` + (rappel ? `\nNe plus recevoir de rappel : ${stop}` : ""),
      headers: rappel ? { "List-Unsubscribe": `<${stop}>` } : undefined,
    });
  }

  const r = await envoyer(mails);
  if (row?.id) await sb.from("qoaq_tirages").update({ envoyes: r.ok, echecs: r.ko }).eq("id", row.id);
  if (r.err) console.log("resend", r.err);
  return J({ ok: r.ok > 0 && r.ko === 0, envoyes: r.ok, echecs: r.ko });
});
