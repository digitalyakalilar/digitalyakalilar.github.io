import sys
from playwright.sync_api import sync_playwright
U="http://localhost:8765";D="/workspace/blog/shots/"
J=[("home-desktop.png","/",1280,900,0,False),("home-desktop-2.png","/",1280,900,620,False),
   ("home-mobile.png","/",390,844,0,True),("article-desktop.png","/ucretsiz-yapay-zeka-araclari/",1280,900,0,False),
   ("article-mobile.png","/ucretsiz-yapay-zeka-araclari/",390,844,0,True)]
extra=[("x-home-en.png","/en/",1280,900,0,False),("x-cat.png","/kategori/dijital-guvenlik/",1280,900,0,False),
   ("x-cat-empty-m.png","/en/category/logistics/",390,844,0,True),("x-article-bottom.png","/ucretsiz-yapay-zeka-araclari/",1280,900,-1,False),
   ("x-home-mobile-2.png","/",390,844,800,True),("x-article-mobile-2.png","/ucretsiz-yapay-zeka-araclari/",390,844,700,True),("x-article-mobile-end.png","/en/free-ai-tools/",390,844,-1,True)]
with sync_playwright() as p:
  b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
  for n,path,wd,h,sc,mob in J+extra:
    c=b.new_context(viewport={"width":wd,"height":h},device_scale_factor=2 if mob else 1,is_mobile=mob,has_touch=mob)
    pg=c.new_page();pg.goto(U+path);pg.wait_for_load_state("networkidle")
    if sc==-1: pg.evaluate("window.scrollTo(0,document.body.scrollHeight-%d-400)"%h)
    elif sc: pg.evaluate(f"window.scrollTo(0,{sc})")
    pg.wait_for_timeout(300);pg.screenshot(path=D+n);c.close();print(n)
  b.close()
