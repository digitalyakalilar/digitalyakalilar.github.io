import http.server,threading,functools
from playwright.sync_api import sync_playwright
class Q(http.server.SimpleHTTPRequestHandler):
  def log_message(s,*a):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8765),functools.partial(Q,directory='public'));threading.Thread(target=srv.serve_forever,daemon=True).start()
U="http://127.0.0.1:8765";D="shots/batch7/"
P={"ilan-tr":"/is-ilani-metni-nasil-yazilir-sifir-basvuru/","jobad-en":"/en/job-posting-buzzwords-zero-applicants/",
   "ot-tr":"/endustriyel-kontrol-sistemleri-siber-guvenligi-yz-ajani/","ot-en":"/en/ot-vulnerability-management-best-practices/",
   "deniz-tr":"/denizcilikte-siber-guvenlik-gemi-liman-zafiyet/","maritime-en":"/en/maritime-cyber-risk-management-vulnerability-database/",
   "verim-tr":"/yapay-zeka-ve-verimlilik-kazanilan-zaman-olcumu/","prod-en":"/en/how-to-measure-ai-productivity-gains/"}
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
