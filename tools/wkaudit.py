import http.server,threading,functools
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
  def log_message(s,*a):pass
s=http.server.ThreadingHTTPServer(('127.0.0.1',8766),functools.partial(Q,directory='public'));threading.Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
  b=p.webkit.launch()
  for w in[360,390,414]:
    pg=b.new_page(viewport={'width':w,'height':844},device_scale_factor=3,is_mobile=True,has_touch=True)
    for u in['/','/kategori/dijital-guvenlik/','/telefon-ve-hesap-guvenligi/','/ucretsiz-yapay-zeka-araclari/','/linkedin-profil-ipuclari/','/en/','/en/free-ai-tools/']:
      pg.goto('http://127.0.0.1:8766'+u);pg.wait_for_timeout(200)
      print(w,u,pg.evaluate("()=>{document.documentElement.style.overflowX='visible';document.body.style.overflowX='visible';return document.documentElement.scrollWidth-innerWidth}"))
  pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=3,is_mobile=True)
  pg.goto('http://127.0.0.1:8766/');pg.wait_for_timeout(300);pg.screenshot(path='shots/mobile-fix/home-after-webkit.png')
