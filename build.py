import os,re,shutil,markdown,html,datetime
SITE="https://digitalyakalilar.com";NAME="Digital Yakalılar"
B=os.path.dirname(os.path.abspath(__file__));OUT=B+"/public"
G="linear-gradient(135deg,#FF7A5C 0%,#F7577A 50%,#E8378E 100%)"
AY="Ocak Şubat Mart Nisan Mayıs Haziran Temmuz Ağustos Eylül Ekim Kasım Aralık".split()
CSS=f"""@font-face{{font-family:M;src:url(/montserrat.ttf);font-weight:100 900;font-display:swap}}
*{{box-sizing:border-box}}body{{margin:0;font-family:M,system-ui,sans-serif;background:#FFF8F5;color:#2B2B33;line-height:1.7}}
a{{color:#E8378E}}header{{background:{G};color:#fff}}.w{{max-width:820px;margin:0 auto;padding:0 22px}}
nav{{display:flex;align-items:center;justify-content:space-between;padding:16px 0}}nav a{{color:#fff;text-decoration:none;font-weight:700;margin-left:18px}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;font-size:20px;margin:0!important}}.brand img{{width:42px;height:42px;border-radius:50%;border:2px solid #fff}}
.hero{{padding:40px 0 56px}}.hero h1{{font-size:44px;line-height:1.1;font-weight:900;margin:0 0 12px}}.hero p{{font-size:19px;opacity:.95;margin:0}}
.card{{display:block;background:#fff;border-radius:20px;padding:24px 26px;margin:22px 0;text-decoration:none;color:inherit;box-shadow:0 6px 24px rgba(232,55,142,.08);transition:.2s}}.card:hover{{transform:translateY(-3px)}}
.card h2{{margin:6px 0;font-size:24px;line-height:1.3;color:#2A1630}}.meta{{font-size:14px;color:#8a7380;font-weight:600}}.tag{{display:inline-block;background:{G};color:#fff;font-size:12px;font-weight:800;padding:3px 12px;border-radius:20px;margin-right:8px}}
article h1{{font-size:38px;line-height:1.15;font-weight:900;color:#2A1630;margin:40px 0 8px}}article h2{{font-size:24px;margin-top:34px;color:#2A1630}}article h2::after{{content:'';display:block;width:60px;height:5px;border-radius:4px;background:{G};margin-top:8px}}
article{{font-size:18px;padding-bottom:30px}}blockquote{{margin:20px 0;background:#fff;border-left:5px solid #F7577A;padding:12px 20px;border-radius:10px}}
footer{{background:#2A1630;color:#fff;padding:30px 0;margin-top:50px;font-size:15px}}footer a{{color:#FF9AB5;font-weight:700}}
.lang{{border:2px solid #fff;border-radius:20px;padding:2px 10px;font-size:13px}}@media(max-width:600px){{.hero h1{{font-size:32px}}article h1{{font-size:30px}}nav a{{margin-left:10px}}}}"""
MO="January February March April May June July August September October November December".split()
UI={"tr":dict(pre="",posts="Yazılar",about="Hakkında",aboutslug="hakkinda",loc="tr_TR",foot="Beyaz yakalılar için yapay zekâ, verimlilik, güvenlik ve kariyer.",other="EN",otherlabel="English"),
    "en":dict(pre="/en",posts="Posts",about="About",aboutslug="about",loc="en_US",foot="AI, productivity, security and career tips for white-collar professionals.",other="TR",otherlabel="Türkçe")}
def page(title,desc,body,url,typ="website",lang="tr",alt=None):
  t=html.escape(title);d=html.escape(desc);u=UI[lang];o="en" if lang=="tr" else "tr"
  hl=""
  if alt:
    tr_u,en_u=(url,alt) if lang=="tr" else (alt,url)
    hl=f'<link rel="alternate" hreflang="tr" href="{SITE}{tr_u}"><link rel="alternate" hreflang="en" href="{SITE}{en_u}"><link rel="alternate" hreflang="x-default" href="{SITE}{tr_u}">'
  sw=f'<a class="lang" href="{alt or UI[o]["pre"]+"/"}" hreflang="{o}" lang="{o}" title="{u["otherlabel"]}">{u["other"]}</a>'
  return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{SITE}{url}">{hl}
<meta property="og:type" content="{typ}"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{SITE}{url}"><meta property="og:image" content="{SITE}/og.png"><meta property="og:locale" content="{u['loc']}"><meta property="og:site_name" content="{NAME}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@digiyakalilar"><meta name="twitter:image" content="{SITE}/og.png">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="stylesheet" href="/style.css"></head><body>
<header><div class="w"><nav><a class="brand" href="{u['pre']}/"><img src="/logo.png" alt="{NAME} logo">{NAME}</a><div><a href="{u['pre']}/">{u['posts']}</a><a href="{u['pre']}/{u['aboutslug']}/">{u['about']}</a>{sw}</div></nav>{{HERO}}</div></header>
<main class="w">{body}</main><footer><div class="w">© {datetime.date.today().year} {NAME} · <a href="https://www.instagram.com/digitalyakalilar/">Instagram @digitalyakalilar</a> · <a href="https://x.com/digiyakalilar">X @digiyakalilar</a><br>{u['foot']}</div></footer></body></html>"""
def fd(s,lang="tr"):
  y,m,d=map(int,s.split("-"));return f"{d} {AY[m-1]} {y}" if lang=="tr" else f"{MO[m-1]} {d}, {y}"
shutil.rmtree(OUT,ignore_errors=True);shutil.copytree(B+"/static",OUT)
open(OUT+"/style.css","w").write(CSS);open(OUT+"/CNAME","w").write("digitalyakalilar.com\n");open(OUT+"/.nojekyll","w").write("")
def load(d):
  ps=[]
  for f in os.listdir(d):
    if not f.endswith(".md"):continue
    fm,body=open(d+"/"+f).read().split("---",2)[1:]
    m=dict(l.split(":",1) for l in fm.strip().splitlines());m={k.strip():v.strip() for k,v in m.items()};m["slug"]=f[:-3];m["html"]=markdown.markdown(body,extensions=["extra"]);ps.append(m)
  return sorted(ps,key=lambda p:p["date"],reverse=True)
posts=load(B+"/posts");en=load(B+"/posts/en")
tr2en={p["tr"]:p["slug"] for p in en}
def w(path,s):os.makedirs(os.path.dirname(OUT+path),exist_ok=True);open(OUT+path,"w").write(s)
pairs=[("/","/en/"),("/hakkinda/","/en/about/")]
def build(ps,lang,pre,link):
  for p in ps:
    me=f'{pre}/{p["slug"]}/';alt=link(p)
    b=f'<article><h1>{html.escape(p["title"])}</h1><div class="meta"><span class="tag">{p["tag"]}</span>{fd(p["date"],lang)}</div>{p["html"]}</article>'
    w(me+"index.html",page(p["title"]+" | "+NAME,p["description"],b,me,"article",lang,alt).replace("{HERO}",""))
  return "".join(f'<a class="card" href="{pre}/{p["slug"]}/"><div class="meta"><span class="tag">{p["tag"]}</span>{fd(p["date"],lang)}</div><h2>{html.escape(p["title"])}</h2><p>{html.escape(p["description"])}</p></a>' for p in ps)
lst=build(posts,"tr","",lambda p:f'/en/{tr2en[p["slug"]]}/' if p["slug"] in tr2en else None)
lst_en=build(en,"en","/en",lambda p:f'/{p["tr"]}/')
pairs+=[(f'/{k}/',f'/en/{v}/') for k,v in tr2en.items()]
w("/index.html",page(NAME+" | Beyaz yakalılar için dijital ipuçları","Beyaz yakalılar için yapay zekâ araçları, verimlilik, telefon ve hesap güvenliği, LinkedIn ve kariyer ipuçları.",lst,"/",alt="/en/").replace("{HERO}",'<div class="hero"><h1>Dijital dünyada bir adım önde ol.</h1><p>Beyaz yakalılar için yapay zekâ, verimlilik, güvenlik ve kariyer ipuçları.</p></div>'))
w("/en/index.html",page(NAME+" | Digital tips for white-collar professionals","AI tools, productivity, phone and account security, LinkedIn and career tips for white-collar professionals.",lst_en,"/en/",lang="en",alt="/").replace("{HERO}",'<div class="hero"><h1>Stay one step ahead in the digital world.</h1><p>AI, productivity, security and career tips for white-collar professionals.</p></div>'))
ab='<article><h1>Hakkında</h1><p><strong>Digital Yakalılar</strong>, yoğun tempoda çalışan beyaz yakalılar için dijital dünyayı sadeleştiren bir içerik platformu.</p><p>Burada yapay zekâ araçlarıyla işini hızlandırmanın yollarını, telefonunu ve hesaplarını korumanın pratik adımlarını, LinkedIn ve kariyer ipuçlarını kısa ve uygulanabilir şekilde paylaşıyoruz.</p><p>Satış yok, reklam kokan tavsiye yok; sadece işine yarayacak bilgi.</p><p>Günlük ipuçları için Instagram\'da <a href="https://www.instagram.com/digitalyakalilar/">@digitalyakalilar</a> hesabını takip et.</p></article>'
w("/hakkinda/index.html",page("Hakkında | "+NAME,"Digital Yakalılar: beyaz yakalılar için dijital ipuçları platformu.",ab,"/hakkinda/",alt="/en/about/").replace("{HERO}",""))
ab_en='<article><h1>About</h1><p><strong>Digital Yakalılar</strong> is a content platform that makes the digital world simpler for busy white-collar professionals.</p><p>Here we share short, practical tips on getting your work done faster with AI tools, protecting your phone and your accounts, and growing your career on LinkedIn and beyond.</p><p>No sales pitches, no ads disguised as advice; just information you can actually use.</p><p>For daily tips, follow <a href="https://www.instagram.com/digitalyakalilar/">@digitalyakalilar</a> on Instagram.</p></article>'
w("/en/about/index.html",page("About | "+NAME,"Digital Yakalılar: a digital tips platform for white-collar professionals.",ab_en,"/en/about/",lang="en",alt="/hakkinda/").replace("{HERO}",""))
def al(a,b):return f'<xhtml:link rel="alternate" hreflang="tr" href="{SITE}{a}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}{b}"/>'
w("/sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+"".join(f"<url><loc>{SITE}{u}</loc>{al(a,b)}</url>" for a,b in pairs for u in (a,b))+"</urlset>")
w("/robots.txt",f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
w("/404.html",page("Sayfa bulunamadı | "+NAME,"Sayfa bulunamadı","<article><h1>Sayfa bulunamadı / Page not found</h1><p><a href='/'>Ana sayfaya dön</a> · <a href='/en/'>Back to home</a></p></article>","/404.html").replace("{HERO}",""))
print("ok",len(posts),len(en))
