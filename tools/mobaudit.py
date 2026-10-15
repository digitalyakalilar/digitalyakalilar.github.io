import sys,json,http.server,threading,functools,os
from playwright.sync_api import sync_playwright
tag=sys.argv[1]
class Q(http.server.SimpleHTTPRequestHandler):
  def log_message(s,*a):pass
H=functools.partial(Q,directory='public')
s=http.server.ThreadingHTTPServer(('127.0.0.1',8765),H);threading.Thread(target=s.serve_forever,daemon=True).start()
cat=sorted(os.listdir('public/kategori'))[0]
pages={'home':'/','cat':f'/kategori/{cat}/','a1':'/telefon-ve-hesap-guvenligi/','a2':'/ucretsiz-yapay-zeka-araclari/','a3':'/linkedin-profil-ipuclari/','enhome':'/en/','enart':'/en/'+[d for d in sorted(os.listdir('public/en')) if os.path.isdir('public/en/'+d) and d not in('kategori','category','about')][0]+'/'}
JS='''()=>{const W=document.documentElement.clientWidth;const r={sw:document.documentElement.scrollWidth,W,vp:(document.querySelector('meta[name=viewport]')||{}).content};
r.over=[...document.querySelectorAll('body *')].filter(e=>{const b=e.getBoundingClientRect();return b.width>0&&b.right>W+1&&getComputedStyle(e).position!='fixed'&&!e.closest('.table-wrap,pre,.pills,nav ul,[data-scroll]')}).slice(0,6).map(e=>e.tagName+'.'+e.className+' r='+Math.round(e.getBoundingClientRect().right));
r.body=getComputedStyle(document.querySelector('article p, main p')||document.body).fontSize;
r.small=[...document.querySelectorAll('a,button')].filter(e=>{const b=e.getBoundingClientRect();return b.width>0&&b.height>0&&b.height<24&&!e.closest('p,li,.prose')}).slice(0,5).map(e=>e.tagName+'.'+e.className+':'+e.textContent.trim().slice(0,15)+' h'+Math.round(e.getBoundingClientRect().height));
r.tables=[...document.querySelectorAll('table')].map(t=>t.parentElement.className+' '+getComputedStyle(t.parentElement).overflowX);
const h=document.querySelector('header');r.hdr=h?Math.round(h.getBoundingClientRect().height):0;
const sb=document.querySelector('aside');r.aside=sb?Math.round(sb.getBoundingClientRect().top):null;return r}'''
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
  for w in [360,375,390,414,768]:
    pg=b.new_page(viewport={'width':w,'height':844},device_scale_factor=2)
    for k,u in pages.items():
      pg.goto('http://127.0.0.1:8765'+u);pg.wait_for_timeout(150)
      r=pg.evaluate(JS);print(w,k,json.dumps(r,ensure_ascii=False))
      if w==390 and k in('home','a1'):pg.screenshot(path=f'shots/mobile-fix/{"home" if k=="home" else "article"}-{tag}.png')
      if w==390 and k=='a1':
        for sel,n in[('table','table'),('#kaynaklar, .sources, ol.refs','sources'),('.toc','toc')]:
          e=pg.query_selector(sel)
          if e: e.scroll_into_view_if_needed();pg.screenshot(path=f'shots/mobile-fix/{n}-{tag}.png')
  b.close()
