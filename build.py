#!/usr/bin/env python3
"""Digital Yakalılar static site builder — Webrazzi-like magazine layout."""
import os, re, shutil, markdown, html, datetime

SITE = "https://digitalyakalilar.com"
NAME = "Digital Yakalılar"
B = os.path.dirname(os.path.abspath(__file__))
OUT = B + "/public"
# --- Palette switch (A | B | C) — one config value ---
from palette import PALETTES
PALETTE = "C"  # <-- switch web palette here: A | B | C
PALETTE = os.environ.get("DY_PALETTE", PALETTE)  # optional tooling override

if PALETTE not in PALETTES:
    raise SystemExit(f"Unknown PALETTE={PALETTE!r}; choose A, B, or C")
P = PALETTES[PALETTE]
G = P["grad"]  # kept for any residual f-string use
AY = "Ocak Şubat Mart Nisan Mayıs Haziran Temmuz Ağustos Eylül Ekim Kasım Aralık".split()
MO = "January February March April May June July August September October November December".split()

def build_css(p):
    return f"""@font-face{{font-family:M;src:url(/montserrat.ttf);font-weight:100 900;font-display:swap}}
:root{{
  --bg:{p['bg']};--surface:{p['surface']};--text:{p['text']};--body:{p['body']};
  --muted:{p['muted']};--muted2:{p['muted2']};--border:{p['border']};--border2:{p['border2']};
  --accent:{p['accent']};--accent2:{p['accent2']};--accent3:{p['accent3']};
  --soft:{p['soft']};--soft2:{p['soft2']};--ink:{p['ink']};--footer-link:{p['footer_link']};
  --grad:{p['grad']};--header-bg:{p['header_bg']};--mark:{p['mark']};
  --shadow:rgba({p['shadow_rgb']},.08);--shadow-md:rgba({p['shadow_rgb']},.12);--shadow-lg:rgba({p['shadow_rgb']},.16);
}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{margin:0;font-family:M,system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--body);line-height:1.7;-webkit-font-smoothing:antialiased}}
a{{color:var(--accent)}}img{{max-width:100%;height:auto;display:block}}
.w{{max-width:1180px;margin:0 auto;padding:0 22px}}
.ad-slot{{display:none}}

/* Sticky header */
.site-header{{position:sticky;top:0;z-index:50;background:var(--header-bg);backdrop-filter:saturate(1.4) blur(14px);-webkit-backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid var(--border)}}
.site-header .inner{{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 0;flex-wrap:wrap}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:800;font-size:18px;color:var(--text);text-decoration:none;margin:0!important;white-space:nowrap}}
.brand img{{width:38px;height:38px;border-radius:50%;border:2px solid var(--accent)}}
.nav-cats{{display:flex;flex-wrap:nowrap;gap:6px;overflow-x:auto;scrollbar-width:none;-ms-overflow-style:none;padding:2px 0;flex:1;min-width:0}}
.nav-cats::-webkit-scrollbar{{display:none}}
.nav-cats a{{flex:none;color:var(--muted);text-decoration:none;font-weight:700;font-size:13px;padding:7px 13px;border-radius:20px;background:var(--surface);border:1px solid var(--border2);white-space:nowrap;transition:.15s}}
.nav-cats a:hover,.nav-cats a.on{{background:var(--grad);color:#fff;border-color:transparent}}
.nav-right{{display:flex;align-items:center;gap:10px;flex:none}}
.nav-right a.plain{{color:var(--muted);text-decoration:none;font-weight:700;font-size:13px}}
.lang{{border:2px solid var(--accent);color:var(--accent)!important;border-radius:20px;padding:3px 11px;font-size:12px;font-weight:800;text-decoration:none}}

/* Home hero */
.feat{{display:grid;grid-template-columns:1.45fr 1fr;gap:0;align-items:center;margin:18px 0 10px;background:var(--surface);border-radius:22px;overflow:hidden;box-shadow:0 10px 36px var(--shadow-md);text-decoration:none;color:inherit;transition:.2s}}
.feat:hover{{transform:translateY(-3px);box-shadow:0 16px 44px var(--shadow-lg)}}
.feat-img{{position:relative;aspect-ratio:16/9;background:var(--ink);align-self:stretch}}
.feat-img img{{width:100%;height:100%;object-fit:cover;position:absolute;inset:0}}
.feat-body{{padding:32px 36px 36px;display:flex;flex-direction:column;justify-content:center}}
.feat-body .tag{{align-self:flex-start}}
.feat-body h1{{font-size:30px;line-height:1.18;font-weight:900;color:var(--text);margin:14px 0 12px;letter-spacing:-.4px}}
.feat-body p{{margin:0 0 18px;color:var(--muted);font-size:16px;line-height:1.55;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}}
.tagline{{display:flex;align-items:center;gap:12px;margin:18px 0 0;padding:12px 18px;background:var(--surface);border-radius:14px;border:1px solid var(--border);color:var(--text);font-size:15px;font-weight:600;line-height:1.45}}
.tagline::before{{content:'';flex:none;width:6px;align-self:stretch;border-radius:4px;background:var(--accent)}}
.tagline b{{font-weight:900;white-space:nowrap}}
.sec-h{{display:flex;align-items:center;gap:12px;margin:0 0 16px;font-size:20px;font-weight:900;color:var(--text)}}
.sec-h::after{{content:'';flex:1;height:2px;background:var(--border)}}
.sec-h::before{{content:'';width:14px;height:14px;border-radius:4px;background:var(--accent)}}
.tiles{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:34px}}
.tile{{display:block;background:var(--surface);border-radius:16px;overflow:hidden;text-decoration:none;color:var(--text);box-shadow:0 6px 22px var(--shadow);transition:.2s}}
.tile:hover{{transform:translateY(-3px)}}.tile img{{aspect-ratio:16/9;width:100%;object-fit:cover}}
.tile span{{display:flex;justify-content:space-between;gap:8px;padding:10px 14px;font-weight:800;font-size:14px}}.tile em{{font-style:normal;color:var(--accent);font-size:12px;white-space:nowrap}}

/* Cards grid */
.layout{{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:36px;align-items:start;margin:22px 0 40px}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}}
.card{{display:flex;flex-direction:column;background:var(--surface);border-radius:18px;overflow:hidden;text-decoration:none;color:inherit;box-shadow:0 6px 24px var(--shadow);transition:.2s;height:100%}}
.card:hover{{transform:translateY(-3px);box-shadow:0 14px 36px var(--shadow-md)}}
.card-img{{aspect-ratio:16/9;background:var(--soft2);overflow:hidden}}
.card-img img{{width:100%;height:100%;object-fit:cover}}
.card-body{{padding:16px 18px 20px;display:flex;flex-direction:column;gap:8px;flex:1}}
.card-body h2{{margin:0;font-size:18px;line-height:1.35;font-weight:800;color:var(--text)}}
.card-body p{{margin:0;color:var(--muted);font-size:14.5px;line-height:1.5;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}}
.meta{{font-size:13px;color:var(--muted2);font-weight:600;display:flex;flex-wrap:wrap;align-items:center;gap:6px}}
.tag{{display:inline-block;background:var(--accent);color:#fff;font-size:11px;font-weight:800;padding:3px 11px;border-radius:20px;letter-spacing:.2px}}
a.tag{{text-decoration:none}}
.dot{{opacity:.5}}

/* Sidebar */
.side{{position:sticky;top:78px}}
.side-box{{background:var(--surface);border-radius:18px;padding:20px 22px;box-shadow:0 6px 24px var(--shadow);margin-bottom:18px}}
.side-box h3{{margin:0 0 14px;font-size:15px;font-weight:900;color:var(--text);letter-spacing:.3px;text-transform:uppercase}}
.side-list{{list-style:none;margin:0;padding:0}}
.side-list li{{border-top:1px solid var(--border);padding:12px 0}}
.side-list li:first-child{{border-top:0;padding-top:0}}
.side-list a{{color:var(--text);text-decoration:none;font-weight:700;font-size:14.5px;line-height:1.4;display:block}}
.side-list a:hover{{color:var(--accent)}}
.side-list .sm{{display:block;margin-top:4px;font-size:12px;color:var(--muted2);font-weight:600}}
.side-cats{{display:flex;flex-direction:column;gap:8px}}
.side-cats a{{display:block;padding:10px 14px;border-radius:12px;background:var(--bg);color:var(--text);text-decoration:none;font-weight:700;font-size:14px;border:1px solid var(--border)}}
.side-cats a:hover,.side-cats a.on{{background:var(--accent);color:#fff;border-color:transparent}}

/* Article */
.cover-wrap{{max-width:920px;margin:22px auto 6px;border-radius:22px;overflow:hidden;background:var(--ink);box-shadow:0 14px 40px var(--shadow-lg)}}
.cover-wrap img{{width:100%;aspect-ratio:16/9;object-fit:cover}}
.lede{{font-size:19px;color:var(--muted);line-height:1.55;margin:0 0 6px;font-weight:500}}
.crumb{{font-size:13px;font-weight:700;color:var(--muted2);margin:14px 0 0}}.crumb a{{color:var(--muted2);text-decoration:none}}.crumb a:hover{{color:var(--accent)}}
.article-shell{{max-width:720px;margin:0 auto;padding:8px 22px 40px}}
article.story h1{{font-size:38px;line-height:1.18;font-weight:900;color:var(--text);margin:18px 0 10px;letter-spacing:-.4px}}
article.story{{font-size:18px}}
article.story h2{{font-size:24px;margin-top:34px;color:var(--text)}}
article.story h2::after{{content:'';display:block;width:56px;height:4px;border-radius:4px;background:var(--accent);margin-top:8px}}
article.story h3{{font-size:20px;color:var(--text);margin-top:26px}}
blockquote{{margin:20px 0;background:var(--surface);border-left:5px solid var(--accent);padding:12px 20px;border-radius:10px}}
.toc{{background:var(--surface);border-radius:14px;padding:14px 22px;margin:26px 0;box-shadow:0 4px 18px var(--shadow);font-size:16px}}
.toc strong{{color:var(--text)}}.toc ol{{margin:8px 0 0;padding-left:20px}}
.toc a{{color:var(--body);text-decoration:none}}.toc a:hover{{color:var(--accent)}}
sup.cite{{font-size:.68em;line-height:0;margin-left:1px}}
sup.cite a{{text-decoration:none;font-weight:700}}sup.cite a:hover{{text-decoration:underline}}
.tbl{{overflow-x:auto;margin:20px 0}}
table{{border-collapse:collapse;width:100%;font-size:16px;background:var(--surface);border-radius:12px;overflow:hidden}}
th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--border);vertical-align:top}}th{{background:var(--ink);color:#fff}}
li.check{{list-style:none;margin-left:-22px}}li.check::before{{content:'☐';color:var(--accent);font-weight:900;margin-right:8px}}
.refs{{margin-top:40px;padding-top:6px;border-top:2px solid var(--border)}}.refs h2{{font-size:20px}}
ol.sources{{font-size:14.5px;line-height:1.55;padding-left:24px;color:var(--muted)}}
ol.sources li{{margin:0 0 9px;word-break:break-word}}ol.sources li:target{{background:var(--mark);border-radius:6px}}
ol.sources a{{word-break:break-all}}
.updated{{display:block;margin-top:4px;font-weight:500}}
.share{{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:28px 0 8px}}.share.top{{margin:16px 0 4px}}.share b{{font-size:13px;color:var(--muted2);margin-right:2px}}
.share a{{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:22px;background:var(--surface);border:1px solid var(--border2);color:var(--text);text-decoration:none;font-weight:700;font-size:13px}}
.share a:hover{{border-color:var(--accent);color:var(--accent)}}
.related{{margin:48px auto 20px;max-width:1180px;padding:0 22px}}
.related>h2{{font-size:22px;font-weight:900;color:var(--text);margin:0 0 18px}}
.related .grid{{grid-template-columns:repeat(3,minmax(0,1fr))}}

/* Category / about pages */
.page-head{{padding:28px 0 8px}}
.page-head h1{{font-size:36px;font-weight:900;color:var(--text);margin:0 0 8px;letter-spacing:-.3px}}
.lead{{color:var(--muted);margin:0 0 18px;font-size:17px;max-width:720px}}
.empty{{background:var(--surface);border-radius:18px;padding:28px;color:var(--muted2);box-shadow:0 6px 24px var(--shadow)}}
.cat-hero{{display:grid;grid-template-columns:1fr 1.2fr;gap:24px;align-items:center;background:var(--surface);border-radius:22px;overflow:hidden;box-shadow:0 10px 36px var(--shadow-md);margin:18px 0 28px}}
.cat-hero img{{width:100%;height:100%;object-fit:cover;aspect-ratio:16/9;min-height:220px}}
.cat-hero .t{{padding:28px}}.cat-hero h1{{font-size:34px;line-height:1.15;font-weight:900;color:var(--text);margin:12px 0 10px}}.cat-hero .lead{{margin:0}}

footer{{background:var(--ink);color:#fff;padding:34px 0;margin-top:50px;font-size:14.5px}}
footer a{{color:var(--footer-link);font-weight:700}}
footer .w{{display:flex;flex-wrap:wrap;gap:12px 28px;justify-content:space-between;align-items:flex-start}}
footer .foot-brand{{font-weight:800;font-size:16px;margin-bottom:6px}}

@media(max-width:980px){{
  .layout{{grid-template-columns:1fr}}
  .side{{position:static}}
  .feat{{grid-template-columns:1fr}}
  .feat-body{{padding:22px}}
  .feat-body h1{{font-size:26px}}
  .related .grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}
  .cat-hero{{grid-template-columns:1fr}}
  .cat-hero h1{{font-size:26px}}.cat-hero .t{{padding:20px 22px 24px}}
}}
@media(max-width:640px){{
  .w{{padding:0 16px}}
  .site-header .inner{{padding:10px 0;gap:10px}}
  .brand span{{font-size:15px}}
  .nav-cats{{order:3;width:100%;flex-basis:100%}}
  .grid{{grid-template-columns:1fr}}
  .related .grid{{grid-template-columns:1fr}}
  article.story h1{{font-size:28px}}
  .page-head h1{{font-size:28px}}
  .cover-wrap{{margin:0 0 4px;border-radius:0 0 18px 18px;box-shadow:none}}
  .lede{{font-size:17px}}
  .tagline{{font-size:13.5px;padding:10px 14px;margin-top:12px}}
  .tagline b{{display:none}}
  .tiles{{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;margin-right:-16px;padding-right:16px}}
  .tile{{flex:0 0 72%;scroll-snap-align:start}}
  .nav-right a.plain{{display:none}}
  .feat{{margin-top:12px}}
  .article-shell{{padding:4px 16px 32px}}
}}"""

CSS = build_css(P)

UI = {
    "tr": dict(
        pre="",
        posts="Yazılar",
        about="Hakkında",
        aboutslug="hakkinda",
        loc="tr_TR",
        foot="İK, endüstri, lojistik ve daha fazlasının dijitalleşme ürünleri; haberler ve kaynaklı rehberler.",
        other="EN",
        otherlabel="English",
        read="dk okuma",
        upd="Son güncelleme",
        toc="İçindekiler",
        empty="Bu kategoride yakında yazılar yayımlanacak.",
        cat="Kategori",
        popular="En çok okunanlar",
        cats="Kategoriler",
        latest="Son yazılar",
        related="İlgini çekebilir",
        share="Paylaş",
        home_title=NAME + " | Sektörlerin dijitalleşme haberleri ve rehberleri",
        home_desc="İK, endüstri, lojistik ve daha fazlasının dijitalleşme ürünleri; haberler ve kaynaklı rehberler. Digital Yakalılar.",
        home_lead="İK, endüstri, lojistik ve daha fazlasının dijitalleşme ürünleri; haberler ve kaynaklı rehberler.",
        all_posts="Tüm yazılar",
    ),
    "en": dict(
        pre="/en",
        posts="Posts",
        about="About",
        aboutslug="about",
        loc="en_US",
        foot="Digitalization products across HR, industry, logistics and beyond — news and sourced guides.",
        other="TR",
        otherlabel="Türkçe",
        read="min read",
        upd="Last updated",
        toc="Contents",
        empty="Posts in this category are coming soon.",
        cat="Category",
        popular="Most read",
        cats="Categories",
        latest="Latest",
        related="You may also like",
        share="Share",
        home_title=NAME + " | Sector digitalization news and guides",
        home_desc="Digitalization products across HR, industry, logistics and beyond — news and sourced guides. Digital Yakalılar.",
        home_lead="Digitalization products across HR, industry, logistics and beyond — news and sourced guides.",
        all_posts="All posts",
    ),
}

CATS = [
    ("ik-teknolojileri", "İK Teknolojileri", "hr-tech", "HR Tech"),
    ("endustri-4-0", "Endüstri 4.0 / Üretim", "industry-4-0", "Industry 4.0 & Manufacturing"),
    ("lojistik-nakliyat", "Lojistik & Nakliyat", "logistics", "Logistics & Freight"),
    ("yapay-zeka-verimlilik", "Yapay Zekâ & Verimlilik", "ai-productivity", "AI & Productivity"),
    ("dijital-guvenlik", "Dijital Güvenlik", "digital-security", "Digital Security"),
]
CAT = {
    k: dict(tr=(tn, "/kategori/" + k + "/"), en=(en, "/en/category/" + es + "/"))
    for k, tn, es, en in CATS
}
CATDESC = {
    "ik-teknolojileri": (
        "İşe alım, yetenek yönetimi ve İK yazılımlarında dijitalleşme.",
        "Digitalization in recruiting, talent management and HR software.",
    ),
    "endustri-4-0": (
        "Üretimde otomasyon, IoT, veri ve dijital fabrika uygulamaları.",
        "Automation, IoT, data and digital factory practices in manufacturing.",
    ),
    "lojistik-nakliyat": (
        "Taşımacılık, depo ve tedarik zincirinde dijital çözümler.",
        "Digital solutions in transport, warehousing and the supply chain.",
    ),
    "yapay-zeka-verimlilik": (
        "İş hayatında yapay zekâ araçları ve verimlilik yöntemleri.",
        "AI tools and productivity methods at work.",
    ),
    "dijital-guvenlik": (
        "Hesap, cihaz ve kurumsal veri güvenliği için pratik rehberler.",
        "Practical guides to account, device and corporate data security.",
    ),
}


def catname(k, lang):
    return CAT[k][lang][0] if k in CAT else k


def caturl(k, lang):
    return CAT[k][lang][1]


def ad(slot):
    return f'<div class="ad-slot" id="ad-{slot}" data-ad-slot="{slot}" aria-hidden="true"></div>'


def mins(text):
    wc = len(re.sub(r"<[^>]+>", " ", text).split())
    return max(1, round(wc / 200))


def cover_url(slug, size="full"):
    if size == "card":
        return f"/covers/{slug}-800.webp"
    return f"/covers/{slug}.jpg"


def cover_exists(slug):
    for d in (f"/static/covers-{PALETTE}", "/static/covers"):
        if os.path.isfile(B + d + f"/{slug}.jpg"):
            return True
    return False


def enrich(h, lang):
    label = "Kaynaklar" if lang == "tr" else "References"
    pre = "kaynak" if lang == "tr" else "ref"
    m = re.search(r"<h2[^>]*>" + label + r"</h2>", h)
    body, src = (h[: m.start()], h[m.end() :]) if m else (h, "")
    body = re.sub(
        r"\[(\d+)\]",
        lambda x: f'<sup class="cite"><a href="#{pre}-{x.group(1)}" aria-label="{label} {x.group(1)}">[{x.group(1)}]</a></sup>',
        body,
    )
    body = re.sub(r"<input [^>]*>", "", body)
    body = (
        body.replace("<li>[ ] ", '<li class="check">')
        .replace("<table>", '<div class="tbl"><table>')
        .replace("</table>", "</table></div>")
    )
    toc = []
    n = [0]

    def hid(x):
        n[0] += 1
        t = re.sub(r"<[^>]+>", "", x.group(1))
        toc.append((n[0], t))
        return f'<h2 id="b{n[0]}">{x.group(1)}</h2>'

    body = re.sub(r"<h2>(.*?)</h2>", hid, body)
    if src:
        i = [0]

        def lid(x):
            i[0] += 1
            return f'<li id="{pre}-{i[0]}">'

        src = re.sub(r"<li>", lid, src).replace("<ol>", '<ol class="sources">', 1)
        src = re.sub(
            r'<a href="(http[^"]+)">',
            r'<a href="\1" target="_blank" rel="noopener">',
            src,
        )
        src = f'<section class="refs"><h2 id="{pre}lar">{label}</h2>{src}</section>'
    return body, src, toc


def header(lang, url, alt=None):
    u = UI[lang]
    o = "en" if lang == "tr" else "tr"
    sw = f'<a class="lang" href="{alt or UI[o]["pre"]+"/"}" hreflang="{o}" lang="{o}" title="{u["otherlabel"]}">{u["other"]}</a>'
    cats = "".join(
        f'<a href="{caturl(k,lang)}"{" class=on" if url==caturl(k,lang) else ""}>{catname(k,lang)}</a>'
        for k, *_ in CATS
    )
    return f"""<header class="site-header"><div class="w"><div class="inner">
<a class="brand" href="{u['pre']}/"><img src="/logo.png" alt="{NAME} logo" width="38" height="38"><span>{NAME}</span></a>
<nav class="nav-cats" aria-label="{u['cats']}">{cats}</nav>
<div class="nav-right"><a class="plain" href="{u['pre']}/{u['aboutslug']}/">{u['about']}</a>{sw}</div>
</div></div></header>"""


def footer(lang):
    u = UI[lang]
    return f"""<footer><div class="w"><div><div class="foot-brand">{NAME}</div>{u['foot']}<br>© {datetime.date.today().year} {NAME}</div>
<div><a href="https://www.instagram.com/digitalyakalilar/">Instagram @digitalyakalilar</a><br>
<a href="https://x.com/digiyakalilar">X @digiyakalilar</a></div></div></footer>"""


def page(title, desc, body, url, typ="website", lang="tr", alt=None, og=None, extra_head=""):
    t = html.escape(title)
    d = html.escape(desc)
    u = UI[lang]
    ogi = og or f"{SITE}/og.png"
    hl = ""
    if alt:
        tr_u, en_u = (url, alt) if lang == "tr" else (alt, url)
        hl = (
            f'<link rel="alternate" hreflang="tr" href="{SITE}{tr_u}">'
            f'<link rel="alternate" hreflang="en" href="{SITE}{en_u}">'
            f'<link rel="alternate" hreflang="x-default" href="{SITE}{tr_u}">'
        )
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{SITE}{url}">{hl}
<meta property="og:type" content="{typ}"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{SITE}{url}"><meta property="og:image" content="{ogi}"><meta property="og:locale" content="{u['loc']}"><meta property="og:site_name" content="{NAME}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@digiyakalilar"><meta name="twitter:image" content="{ogi}">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="stylesheet" href="/style.css">{extra_head}</head><body>
{header(lang,url,alt)}
{body}
{footer(lang)}</body></html>"""


def fd(s, lang="tr"):
    y, m, d = map(int, s.split("-"))
    return f"{d} {AY[m-1]} {y}" if lang == "tr" else f"{MO[m-1]} {d}, {y}"


def card(p, lang, pre, size="card"):
    u = UI[lang]
    k = p.get("category", "")
    slug = p["slug"]
    img = cover_url(slug, size) if cover_exists(slug) else "/og.png"
    return f"""<a class="card" href="{pre}/{slug}/">
<div class="card-img"><img src="{img}" alt="" width="800" height="450" loading="lazy" decoding="async"></div>
<div class="card-body"><div class="meta"><span class="tag">{catname(k,lang)}</span></div>
<h2>{html.escape(p["title"])}</h2>
<p>{html.escape(p["description"])}</p>
<div class="meta">{fd(p["date"],lang)}<span class="dot">·</span>{p["mins"]} {u["read"]}</div>
</div></a>"""


def featured(p, lang, pre):
    u = UI[lang]
    k = p.get("category", "")
    slug = p["slug"]
    img = cover_url(slug) if cover_exists(slug) else "/og.png"
    return f"""<a class="feat" href="{pre}/{slug}/">
<div class="feat-img"><img src="{img}" alt="" width="1600" height="900" fetchpriority="high" decoding="async"></div>
<div class="feat-body"><span class="tag">{catname(k,lang)}</span>
<h1>{html.escape(p["title"])}</h1>
<p>{html.escape(p["description"])}</p>
<div class="meta">{fd(p["date"],lang)}<span class="dot">·</span>{p["mins"]} {u["read"]}</div>
</div></a>"""


def sidebar(ps, lang, current_cat=None):
    u = UI[lang]
    pop = "".join(
        f'<li><a href="{UI[lang]["pre"]}/{p["slug"]}/">{html.escape(p["title"])}</a>'
        f'<span class="sm">{fd(p["date"],lang)} · {p["mins"]} {u["read"]}</span></li>'
        for p in ps[:5]
    )
    cats = "".join(
        f'<a href="{caturl(k,lang)}"{" class=on" if current_cat==k else ""}>{catname(k,lang)}</a>'
        for k, *_ in CATS
    )
    return f"""<aside class="side">
<div class="side-box"><h3>{u["popular"]}</h3><ol class="side-list">{pop}</ol></div>
<div class="side-box"><h3>{u["cats"]}</h3><div class="side-cats">{cats}</div></div>
{ad("sidebar")}
</aside>"""


def share_btns(url, title, lang, cls=""):
    from urllib.parse import quote
    u = UI[lang]
    f = quote(SITE + url, safe="")
    t = quote(title, safe="")
    links = [
        ("X", f"https://x.com/intent/post?url={f}&text={t}"),
        ("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={f}"),
        ("WhatsApp", f"https://wa.me/?text={t}%20{f}"),
        ("Facebook", f"https://www.facebook.com/sharer/sharer.php?u={f}"),
        ("Telegram", f"https://t.me/share/url?url={f}&text={t}"),
        ("E-posta" if lang == "tr" else "Email", f"mailto:?subject={t}&body={f}"),
    ]
    a = "".join(
        f'<a href="{h}"{"" if h.startswith("mailto") else " target=_blank rel=noopener"}>{n}</a>' for n, h in links
    )
    return f'<div class="share {cls}" aria-label="{u["share"]}"><b>{u["share"]}:</b>{a}</div>'


def related_block(ps, current, lang, pre):
    u = UI[lang]
    k = current.get("category")
    others = [p for p in ps if p["slug"] != current["slug"]]
    others = sorted(others, key=lambda p: p.get("category") != k)[:3]
    if not others:
        return ""
    cards = "".join(card(p, lang, pre) for p in others)
    return f'<section class="related"><h2>{u["related"]}</h2><div class="grid">{cards}</div></section>'


# --- Build ---
shutil.rmtree(OUT, ignore_errors=True)
shutil.copytree(B + "/static", OUT, ignore=shutil.ignore_patterns("covers-*"))
# Prefer palette-specific covers when present (from tools/covers.py A|B|C)
_pc = B + f"/static/covers-{PALETTE}"
if os.path.isdir(_pc):
    if os.path.isdir(OUT + "/covers"):
        shutil.rmtree(OUT + "/covers")
    shutil.copytree(_pc, OUT + "/covers")
open(OUT + "/style.css", "w").write(CSS)
print("palette", PALETTE, P["label"])
open(OUT + "/CNAME", "w").write("digitalyakalilar.com\n")
open(OUT + "/.nojekyll", "w").write("")


def load(d):
    ps = []
    for f in os.listdir(d):
        if not f.endswith(".md"):
            continue
        fm, body = open(d + "/" + f).read().split("---", 2)[1:]
        m = dict(l.split(":", 1) for l in fm.strip().splitlines())
        m = {k.strip(): v.strip() for k, v in m.items()}
        m["slug"] = f[:-3]
        m["html"] = markdown.markdown(body, extensions=["extra"])
        ps.append(m)
    return sorted(ps, key=lambda p: p["date"], reverse=True)


posts = load(B + "/posts")
en = load(B + "/posts/en")
tr2en = {p["tr"]: p["slug"] for p in en}


def w(path, s):
    os.makedirs(os.path.dirname(OUT + path), exist_ok=True)
    open(OUT + path, "w").write(s)


pairs = [("/", "/en/"), ("/hakkinda/", "/en/about/")]


def build(ps, lang, pre, link):
    u = UI[lang]
    for p in ps:
        me = f'{pre}/{p["slug"]}/'
        alt = link(p)
        k = p.get("category", "")
        body, src, toc = enrich(p["html"], lang)
        p["mins"] = mins(body)
        upd = f'<span class="updated">{u["upd"]}: {fd(p.get("updated",p["date"]),lang)}</span>'
        tc = (
            f'<div class="toc" role="navigation" aria-label="{u["toc"]}"><strong>{u["toc"]}</strong><ol>'
            + "".join(f'<li><a href="#b{i}">{t}</a></li>' for i, t in toc)
            + "</ol></div>"
            if len(toc) > 2
            else ""
        )
        j = body.find("</p>")
        body = body[: j + 4] + tc + ad("article-top") + body[j + 4 :] if j >= 0 else tc + body
        img = cover_url(p["slug"]) if cover_exists(p["slug"]) else "/og.png"
        og = SITE + img
        cover = f'<div class="cover-wrap"><img src="{img}" alt="" width="1600" height="900" fetchpriority="high" decoding="async"></div>'
        share = share_btns(me, p["title"], lang)
        share_top = share_btns(me, p["title"], lang, "top")
        home_l = "Ana sayfa" if lang == "tr" else "Home"
        crumb = f'<div class="crumb"><a href="{pre}/">{home_l}</a> › <a href="{caturl(k,lang)}">{catname(k,lang)}</a></div>'
        import json
        ld = json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["description"],
            "image": [og], "datePublished": p["date"], "dateModified": p.get("updated", p["date"]), "inLanguage": lang,
            "mainEntityOfPage": SITE + me, "author": {"@type": "Organization", "name": NAME, "url": SITE},
            "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": SITE + "/logo.png"}}}, ensure_ascii=False)
        head_extra = f'<meta property="og:image:width" content="1600"><meta property="og:image:height" content="900"><meta property="article:published_time" content="{p["date"]}"><script type="application/ld+json">{ld}</script>' 
        rel = related_block(ps, p, lang, pre)
        story = f"""{cover}<div class="article-shell"><article class="story">
{crumb}<h1>{html.escape(p["title"])}</h1>
<p class="lede">{html.escape(p["description"])}</p>
<div class="meta"><a class="tag" href="{caturl(k,lang)}">{catname(k,lang)}</a>{fd(p["date"],lang)}<span class="dot">·</span>{p["mins"]} {u["read"]}{upd}</div>
{share_top}
{body}{ad("article-bottom")}{src}{share}
</article></div>{rel}"""
        w(
            me + "index.html",
            page(
                p["title"] + " | " + NAME,
                p["description"],
                story,
                me,
                "article",
                lang,
                alt,
                og=og,
                extra_head=head_extra,
            ),
        )


# Precompute mins for cards (rough from raw html)
for p in posts + en:
    p["mins"] = mins(p["html"])

build(posts, "tr", "", lambda p: f'/en/{tr2en[p["slug"]]}/' if p["slug"] in tr2en else None)
build(en, "en", "/en", lambda p: f'/{p["tr"]}/')
# Recompute mins after enrich isn't stored for home — rebuild mins from rendered? Use existing.
# Actually build() overwrites p["mins"] with body-based count. Good.

pairs += [(f"/{k}/", f"/en/{v}/") for k, v in tr2en.items()]


def home(ps, lang, pre, alt):
    u = UI[lang]
    feat = featured(ps[0], lang, pre) if ps else ""
    rest = ps[1:]
    cards = "".join(card(p, lang, pre) for p in rest)
    if len(rest) >= 2:
        # inject ad after 2nd card visually — wrap mid
        parts = [card(p, lang, pre) for p in rest]
        mid = "".join(parts[:2]) + ad("list-inline") + "".join(parts[2:])
        cards = mid
    grid = f'<div class="grid">{cards}</div>' if rest else f'<div class="empty">{u["empty"]}</div>'
    def cnt(k):
        n = sum(1 for p in ps if p.get("category") == k)
        return f"{n} yazı" if lang == "tr" else f"{n} post" + ("" if n == 1 else "s")

    tiles = "".join(
        f'<a class="tile" href="{caturl(k,lang)}"><img src="/covers/cat-{k}-{lang}-800.webp" alt="" width="800" height="450" loading="lazy" decoding="async">'
        f'<span>{catname(k,lang)}<em>{cnt(k)}</em></span></a>'
        for k, *_ in CATS
    )
    brand_l = "Digital Yakalılar:"
    body = f"""<main class="w"><p class="tagline"><span><b>{brand_l}</b> {html.escape(u["home_lead"])}</span></p>
{feat}{ad("home-below-hero")}
<div class="layout"><div><h2 class="sec-h">{u["latest"]}</h2>{grid}<h2 class="sec-h" style="margin-top:38px">{u["cats"]}</h2><div class="tiles" style="margin-top:0">{tiles}</div></div>{sidebar(ps,lang)}</div></main>"""
    og = SITE + cover_url(ps[0]["slug"]) if ps and cover_exists(ps[0]["slug"]) else None
    w(
        (pre or "") + "/index.html" if pre else "/index.html",
        page(u["home_title"], u["home_desc"], body, pre + "/" if pre else "/", lang=lang, alt=alt, og=og),
    )


home(posts, "tr", "", "/en/")
home(en, "en", "/en", "/")

ab = f"""<main class="w"><div class="page-head"><h1>Hakkında</h1></div>
<article class="story" style="max-width:720px">
<p><strong>Digital Yakalılar</strong>, İK, endüstri, lojistik ve daha fazlasının dijitalleşme ürünlerini takip eden bir içerik platformu.</p>
<p>Burada sektörlerin dijitalleşme haberlerini ve kaynaklı rehberleri paylaşıyoruz: yapay zekâ ile verimlilik, telefon ve hesap güvenliği, LinkedIn ve İK teknolojileri ve daha fazlası.</p>
<p>Satış yok, e-ticaret yok; sadece işine yarayacak bilgi.</p>
<p>Günlük ipuçları için Instagram'da <a href="https://www.instagram.com/digitalyakalilar/">@digitalyakalilar</a> hesabını takip et.</p>
</article></main>"""
w(
    "/hakkinda/index.html",
    page(
        "Hakkında | " + NAME,
        "Digital Yakalılar: sektörlerin dijitalleşme haberleri ve kaynaklı rehberleri.",
        ab,
        "/hakkinda/",
        alt="/en/about/",
    ),
)
ab_en = f"""<main class="w"><div class="page-head"><h1>About</h1></div>
<article class="story" style="max-width:720px">
<p><strong>Digital Yakalılar</strong> is a content platform that follows digitalization products across HR, industry, logistics and beyond.</p>
<p>Here we share sector digitalization news and sourced guides: AI for productivity, phone and account security, LinkedIn and HR tech, and more.</p>
<p>No sales pitches, no e-commerce — just information you can use.</p>
<p>For daily tips, follow <a href="https://www.instagram.com/digitalyakalilar/">@digitalyakalilar</a> on Instagram.</p>
</article></main>"""
w(
    "/en/about/index.html",
    page(
        "About | " + NAME,
        "Digital Yakalılar: sector digitalization news and sourced guides.",
        ab_en,
        "/en/about/",
        lang="en",
        alt="/hakkinda/",
    ),
)

for k, tn, es, en_ in CATS:
    for lang, ps, pre in (("tr", posts, ""), ("en", en, "/en")):
        u = UI[lang]
        me = caturl(k, lang)
        other = caturl(k, "en" if lang == "tr" else "tr")
        sel = [p for p in ps if p.get("category") == k]
        desc = CATDESC[k][0 if lang == "tr" else 1]
        cover_slug = f"cat-{k}-{'tr' if lang=='tr' else 'en'}"
        cimg = cover_url(cover_slug) if cover_exists(cover_slug) else "/og.png"
        hero = f"""<div class="cat-hero"><img src="{cimg}" alt="" width="1600" height="900" fetchpriority="high">
<div class="t"><div class="meta"><span class="tag">{u["cat"]}</span></div>
<h1>{catname(k,lang)}</h1><p class="lead">{html.escape(desc)}</p></div></div>"""
        lst_c = (
            f'<div class="grid">{"".join(card(p,lang,pre) for p in sel)}</div>'
            if sel
            else f'<div class="empty">{u["empty"]}</div>'
            + (f'<h2 class="sec-h" style="margin-top:30px">{u["latest"]}</h2><div class="grid">' + "".join(card(p, lang, pre) for p in ps[:4]) + "</div>" if ps else "")
        )
        body = f"""<main class="w">{hero}<div class="layout"><div>{lst_c}</div>{sidebar(ps,lang,current_cat=k)}</div></main>"""
        w(
            me + "index.html",
            page(
                catname(k, lang) + " | " + NAME,
                desc,
                body,
                me,
                lang=lang,
                alt=other,
                og=SITE + cimg,
            ),
        )
    pairs.append((caturl(k, "tr"), caturl(k, "en")))


def al(a, b):
    return f'<xhtml:link rel="alternate" hreflang="tr" href="{SITE}{a}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}{b}"/>'


w(
    "/sitemap.xml",
    '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
    + "".join(f"<url><loc>{SITE}{u}</loc>{al(a,b)}</url>" for a, b in pairs for u in (a, b))
    + "</urlset>",
)
w("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
w(
    "/404.html",
    page(
        "Sayfa bulunamadı | " + NAME,
        "Sayfa bulunamadı",
        "<main class='w'><article class='story'><h1>Sayfa bulunamadı / Page not found</h1><p><a href='/'>Ana sayfaya dön</a> · <a href='/en/'>Back to home</a></p></article></main>",
        "/404.html",
    ),
)
print("ok", len(posts), len(en), "covers", len([f for f in os.listdir(B+"/static/covers") if f.endswith(".jpg")]))
