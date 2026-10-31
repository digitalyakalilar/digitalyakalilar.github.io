import http.server,threading,functools
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
  def log_message(s,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(Q,directory='public'));threading.Thread(target=srv.serve_forever,daemon=True).start()
U="http://127.0.0.1:8765";D="shots/batch8/"
P={"egitim-tr":"/egitim-etkinligi-degerlendirme-eski-aliskanliklar/","training-en":"/en/how-to-measure-training-effectiveness-habit-hugging/",
   "robot-tr":"/sanayide-robot-kullanimi-turkiye-robot-yogunlugu-2026/","robot-en":"/en/industrial-robot-statistics-2026-turkey-robot-density/",
   "kargo-tr":"/kargo-hirsizligi-sahte-teslim-alma-nakliye-dolandiriciligi/","cargo-en":"/en/fictitious-pickup-cargo-theft-freight-fraud-prevention/",
   "aiops-tr":"/aiops-nedir-yapay-zeka-ajanlari-bt-operasyonlari/","aiops-en":"/en/agentic-aiops-ai-agents-it-operations/"}
with sync_playwright() as p:
  b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
  for n,u in P.items():
    for kind,w,h,mob in (("desktop",1280,900,False),("mobile",390,844,True)):
      c=b.new_context(viewport={"width":w,"height":h},device_scale_factor=2 if mob else 1,is_mobile=mob,has_touch=mob)
      c.add_init_script("try{localStorage.setItem(\"dy_consent\",\"denied\")}catch(e){}");pg=c.new_page();pg.goto(U+u);pg.wait_for_load_state("networkidle");pg.wait_for_timeout(300)
      pg.screenshot(path=f"{D}{n}-{kind}.png")
      if mob:
        t=pg.query_selector("article table")
        if t: t.scroll_into_view_if_needed();pg.evaluate("window.scrollBy(0,-90)");pg.wait_for_timeout(200);pg.screenshot(path=f"{D}{n}-table.png")
      c.close();print(n,kind)
  b.close()
