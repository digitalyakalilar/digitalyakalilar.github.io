"""Generate 1600x900 cover JPGs (+ 800px WebP) into static/covers/.
Needs Chrome + playwright. Frontmatter: cover_title, cover_icon (ai|profile|phone|factory|logistics|hragents|maturity|mes|warehouse|agentshield).

Usage:
  python3 tools/covers.py              # uses build.py PALETTE / DY_PALETTE
  python3 tools/covers.py A            # force palette A|B|C
  python3 tools/covers.py B slug-one   # palette + only these names
"""
import os, sys, math, html

from PIL import Image

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = B + "/static/covers"
sys.path.insert(0, B)
from palette import PALETTES  # noqa: E402

CATS = {
    "ik-teknolojileri": ("İK Teknolojileri", "HR Tech", "profile"),
    "endustri-4-0": ("Endüstri 4.0 / Üretim", "Industry 4.0 & Manufacturing", "factory"),
    "lojistik-nakliyat": ("Lojistik & Nakliyat", "Logistics & Freight", "logistics"),
    "yapay-zeka-verimlilik": ("Yapay Zekâ & Verimlilik", "AI & Productivity", "ai"),
    "dijital-guvenlik": ("Dijital Güvenlik", "Digital Security", "phone"),
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


def chk(cx, cy, s=1, c="#fff", w=6):
    return (
        f'<path d="M{cx-9*s} {cy} L{cx-3*s} {cy+7*s} L{cx+10*s} {cy-7*s}" '
        f'stroke="{c}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def gear(cx, cy, r, teeth, depth, fill):
    pts = []
    n = teeth * 4
    for i in range(n):
        a = 2 * math.pi * i / n
        rr = r if (i % 4) in (0, 1) else r - depth
        a += math.pi / n / 2
        pts.append(f"{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{fill}" stroke-width="10" stroke-linejoin="round"/>'


def pin(x, y, c, s=1):
    return (
        f'<g transform="translate({x},{y}) scale({s})">'
        f'<path d="M0 0 C-30 -38 -40 -52 -40 -72 A40 40 0 0 1 40 -72 C40 -52 30 -38 0 0Z" '
        f'fill="{c}" stroke="#fff" stroke-width="6"/><circle cx="0" cy="-72" r="15" fill="#fff"/></g>'
    )


def make_icons(C):
    P, PK, LG, MU = C["ink"], C["pk"], C["lg"], C["mu"]
    ACC, ACC2, CHIP, SOFT, LINE = C["g3"], C["g2"], C["chip"], C["softc"], C["line"]
    DEFS = f"""<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{C['g1']}"/><stop offset=".5" stop-color="{C['g2']}"/><stop offset="1" stop-color="{C['g3']}"/></linearGradient>
<linearGradient id="g2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{C['g2a']}"/><stop offset="1" stop-color="{C['g2b']}"/></linearGradient>
<filter id="s" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="22" stdDeviation="22" flood-color="{C['cover_shadow']}" flood-opacity=".28"/></filter></defs>
<circle cx="350" cy="350" r="320" fill="#fff" opacity=".08"/><circle cx="350" cy="350" r="230" fill="#fff" opacity=".08"/>"""

    def icon_ai():
        chips = "".join(
            f'<rect x="{504+i*34}" y="52" width="14" height="22" rx="5" fill="{CHIP}"/>'
            f'<rect x="{504+i*34}" y="240" width="14" height="22" rx="5" fill="{CHIP}"/>'
            f'<rect x="458" y="{98+i*34}" width="22" height="14" rx="5" fill="{CHIP}"/>'
            f'<rect x="646" y="{98+i*34}" width="22" height="14" rx="5" fill="{CHIP}"/>'
            for i in range(4)
        )
        return f"""<g filter="url(#s)"><rect x="80" y="150" width="470" height="390" rx="30" fill="#fff"/></g>
<circle cx="118" cy="186" r="8" fill="{SOFT}"/><circle cx="144" cy="186" r="8" fill="{SOFT}"/><circle cx="170" cy="186" r="8" fill="{SOFT}"/><rect x="80" y="212" width="470" height="3" fill="{LINE}"/>
<rect x="112" y="240" width="260" height="70" rx="22" fill="{LG}"/><rect x="136" y="260" width="190" height="11" rx="5.5" fill="{MU}"/><rect x="136" y="281" width="130" height="11" rx="5.5" fill="{MU}"/>
<rect x="238" y="330" width="280" height="88" rx="22" fill="url(#g)"/><rect x="262" y="350" width="214" height="11" rx="5.5" fill="#fff" opacity=".92"/><rect x="262" y="369" width="180" height="11" rx="5.5" fill="#fff" opacity=".92"/><rect x="262" y="388" width="120" height="11" rx="5.5" fill="#fff" opacity=".92"/>
<rect x="112" y="440" width="190" height="60" rx="22" fill="{LG}"/><circle cx="152" cy="470" r="9" fill="{ACC}" opacity=".45"/><circle cx="180" cy="470" r="9" fill="{ACC}" opacity=".7"/><circle cx="208" cy="470" r="9" fill="{ACC}"/>
<g filter="url(#s)"><rect x="478" y="72" width="170" height="170" rx="36" fill="{P}"/></g>
{chips}
<path d="M563 104 C569 140 578 150 614 157 C578 164 569 174 563 210 C557 174 548 164 512 157 C548 150 557 140 563 104Z" fill="url(#g)"/><path d="M612 96 C614 108 617 111 629 113 C617 115 614 118 612 130 C610 118 607 115 595 113 C607 111 610 108 612 96Z" fill="#fff"/>
<g filter="url(#s)"><rect x="30" y="480" width="190" height="130" rx="26" fill="#fff"/></g>
<rect x="62" y="556" width="22" height="28" rx="5" fill="url(#g)" opacity=".55"/><rect x="96" y="536" width="22" height="48" rx="5" fill="url(#g)" opacity=".7"/><rect x="130" y="516" width="22" height="68" rx="5" fill="url(#g)" opacity=".85"/><rect x="164" y="500" width="22" height="84" rx="5" fill="url(#g)"/>
<g filter="url(#s)"><circle cx="560" cy="540" r="56" fill="#fff"/></g><path d="M570 504 L532 548 H557 L547 578 L588 528 H563 Z" fill="{ACC}"/>"""

    def icon_profile():
        return f"""<g filter="url(#s)"><rect x="120" y="110" width="420" height="500" rx="32" fill="#fff"/></g>
<path d="M120 142 A32 32 0 0 1 152 110 H508 A32 32 0 0 1 540 142 V230 H120Z" fill="url(#g2)"/>
<circle cx="245" cy="235" r="70" fill="#fff"/><circle cx="245" cy="235" r="58" fill="{P}"/>
<rect x="217" y="226" width="56" height="40" rx="8" fill="#fff"/><rect x="235" y="212" width="20" height="18" rx="5" fill="none" stroke="#fff" stroke-width="6"/><rect x="217" y="241" width="56" height="4" fill="{P}"/>
<circle cx="296" cy="285" r="21" fill="{ACC}" stroke="#fff" stroke-width="6"/>{chk(296, 285, 0.85, w=5)}
<rect x="165" y="330" width="230" height="20" rx="10" fill="{P}"/><rect x="165" y="362" width="160" height="13" rx="6.5" fill="{MU}"/>
<rect x="165" y="400" width="135" height="40" rx="20" fill="{PK}"/><circle cx="187" cy="420" r="11" fill="{ACC}"/>{chk(187, 420, 0.55, w=4)}<rect x="206" y="415" width="76" height="10" rx="5" fill="{ACC2}" opacity=".55"/>
<rect x="312" y="400" width="118" height="40" rx="20" fill="{PK}"/><circle cx="334" cy="420" r="11" fill="{ACC}"/>{chk(334, 420, 0.55, w=4)}<rect x="353" y="415" width="60" height="10" rx="5" fill="{ACC2}" opacity=".55"/>
<rect x="165" y="452" width="160" height="40" rx="20" fill="{PK}"/><circle cx="187" cy="472" r="11" fill="{ACC}"/>{chk(187, 472, 0.55, w=4)}<rect x="206" y="467" width="100" height="10" rx="5" fill="{ACC2}" opacity=".55"/>
<rect x="165" y="525" width="300" height="11" rx="5.5" fill="{LINE}"/><rect x="165" y="548" width="240" height="11" rx="5.5" fill="{LINE}"/><rect x="165" y="571" width="270" height="11" rx="5.5" fill="{LINE}"/>
<g filter="url(#s)"><circle cx="548" cy="440" r="92" fill="#fff"/></g><circle cx="535" cy="427" r="42" fill="{PK}" stroke="{P}" stroke-width="15"/><line x1="567" y1="459" x2="600" y2="492" stroke="{P}" stroke-width="20" stroke-linecap="round"/>
<g filter="url(#s)"><rect x="440" y="58" width="200" height="76" rx="38" fill="#fff"/></g><circle cx="478" cy="96" r="22" fill="url(#g)"/>{chk(478, 96, 0.9, w=5)}<rect x="512" y="83" width="100" height="12" rx="6" fill="{P}"/><rect x="512" y="103" width="70" height="10" rx="5" fill="{MU}"/>"""

    def icon_phone():
        keys = "".join(
            f'<rect x="{240+i*38}" y="432" width="30" height="42" rx="9" fill="{LG}"/>'
            + (f'<circle cx="{255+i*38}" cy="453" r="6.5" fill="{P}"/>' if i < 4 else "")
            for i in range(6)
        )
        return f"""<g filter="url(#s)"><rect x="205" y="60" width="290" height="560" rx="46" fill="{P}"/></g><rect x="221" y="76" width="258" height="528" rx="34" fill="#fff"/><rect x="305" y="90" width="90" height="20" rx="10" fill="{P}"/>
<path d="M350 150 L445 186 V268 C445 336 404 378 350 400 C296 378 255 336 255 268 V186 Z" fill="url(#g)"/>
<rect x="316" y="262" width="68" height="56" rx="11" fill="#fff"/><path d="M329 262 V246 A21 21 0 0 1 371 246 V262" stroke="#fff" stroke-width="11" fill="none"/><circle cx="350" cy="285" r="8" fill="{ACC}"/><rect x="346" y="287" width="8" height="16" rx="3" fill="{ACC}"/>
{keys}
<rect x="268" y="508" width="164" height="46" rx="23" fill="url(#g)"/><rect x="318" y="527" width="64" height="9" rx="4.5" fill="#fff"/>
<g filter="url(#s)"><rect x="40" y="290" width="200" height="104" rx="26" fill="#fff"/></g><circle cx="94" cy="342" r="23" stroke="{ACC}" stroke-width="11" fill="none"/><line x1="118" y1="342" x2="206" y2="342" stroke="{P}" stroke-width="11" stroke-linecap="round"/><line x1="188" y1="342" x2="188" y2="366" stroke="{P}" stroke-width="11" stroke-linecap="round"/><line x1="166" y1="342" x2="166" y2="360" stroke="{P}" stroke-width="11" stroke-linecap="round"/>
<g filter="url(#s)"><circle cx="530" cy="190" r="62" fill="#fff"/></g><circle cx="530" cy="190" r="42" fill="url(#g)"/>{chk(530, 190, 1.5, w=9)}
<g filter="url(#s)"><rect x="452" y="460" width="200" height="92" rx="24" fill="#fff"/></g><path d="M480 530 L503 490 L526 530Z" fill="{C['g1']}" stroke="{C['g1']}" stroke-width="8" stroke-linejoin="round"/><rect x="500" y="503" width="6" height="13" rx="3" fill="#fff"/><circle cx="503" cy="523" r="3.5" fill="#fff"/><rect x="544" y="492" width="80" height="11" rx="5.5" fill="{P}"/><rect x="544" y="514" width="56" height="10" rx="5" fill="{MU}"/>"""

    def icon_factory():
        return f"""<g filter="url(#s)">{gear(300, 330, 165, 10, 32, "#fff")}</g><circle cx="300" cy="330" r="78" fill="{P}"/><circle cx="300" cy="330" r="30" fill="url(#g)"/>
<g filter="url(#s)">{gear(530, 165, 82, 8, 20, P)}</g><circle cx="530" cy="165" r="30" fill="#fff"/>
<path d="M90 140 A80 80 0 0 1 170 60" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".9"/><path d="M118 140 A52 52 0 0 1 170 88" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".9"/><circle cx="160" cy="132" r="12" fill="#fff"/>
<g filter="url(#s)"><rect x="400" y="430" width="250" height="180" rx="26" fill="#fff"/></g><polyline points="430,570 480,530 520,550 570,490 620,470" fill="none" stroke="url(#g)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="570" cy="490" r="10" fill="#fff" stroke="{ACC}" stroke-width="6"/><rect x="430" y="455" width="90" height="12" rx="6" fill="{P}"/><rect x="580" y="455" width="40" height="12" rx="6" fill="{PK}"/>
<g filter="url(#s)"><rect x="60" y="500" width="210" height="96" rx="24" fill="#fff"/></g><circle cx="108" cy="548" r="24" fill="url(#g)"/>{chk(108, 548, 1, w=6)}<rect x="146" y="532" width="96" height="12" rx="6" fill="{P}"/><rect x="146" y="554" width="66" height="10" rx="5" fill="{MU}"/>"""

    def icon_logistics():
        return f"""<path d="M120 560 C220 470 160 360 300 330 S520 260 560 170" stroke="#fff" stroke-width="9" fill="none" stroke-dasharray="2 22" stroke-linecap="round" opacity=".95"/>
<g filter="url(#s)"><rect x="130" y="300" width="300" height="180" rx="20" fill="#fff"/><path d="M430 346 H510 L568 404 V480 H430Z" fill="{P}" stroke="{P}" stroke-width="14" stroke-linejoin="round"/></g>
<path d="M452 366 H502 L540 404 H452Z" fill="{PK}"/><rect x="130" y="432" width="300" height="16" fill="url(#g)"/>
<rect x="245" y="330" width="76" height="76" rx="10" fill="{PK}"/><rect x="276" y="330" width="14" height="76" fill="{ACC2}"/>
<circle cx="210" cy="490" r="40" fill="{P}" stroke="#fff" stroke-width="8"/><circle cx="210" cy="490" r="14" fill="#fff"/><circle cx="490" cy="490" r="40" fill="{P}" stroke="#fff" stroke-width="8"/><circle cx="490" cy="490" r="14" fill="#fff"/>
<g filter="url(#s)">{pin(560, 190, "url(#g)", 1.15)}</g>
<g filter="url(#s)"><polygon points="180,120 250,90 320,120 250,150" fill="#fff"/><polygon points="180,120 250,150 250,235 180,205" fill="{PK}"/><polygon points="320,120 250,150 250,235 320,205" fill="{SOFT}"/></g><polygon points="215,105 285,135 285,160 215,130" fill="{ACC2}" opacity=".8"/>
<g filter="url(#s)"><rect x="380" y="560" width="260" height="84" rx="24" fill="#fff"/></g><circle cx="424" cy="602" r="22" fill="url(#g)"/>{chk(424, 602, 0.9, w=5)}<rect x="460" y="586" width="120" height="12" rx="6" fill="{P}"/><rect x="460" y="607" width="150" height="10" rx="5" fill="{LINE}"/>"""


    def icon_hragents():
        cards = ""
        for i, (y, sc) in enumerate(((150, 1), (290, 1), (430, 1))):
            on = i == 1
            cards += (f'<g filter="url(#s)"><rect x="70" y="{y}" width="300" height="110" rx="26" fill="#fff"/></g>'
                f'<circle cx="125" cy="{y+55}" r="30" fill="{"url(#g)" if on else PK}"/>'
                f'<circle cx="125" cy="{y+46}" r="11" fill="#fff"/><path d="M104 {y+75} A21 17 0 0 1 146 {y+75}Z" fill="#fff"/>'
                f'<rect x="172" y="{y+34}" width="150" height="13" rx="6.5" fill="{P}"/>'
                f'<rect x="172" y="{y+60}" width="{110 if on else 90}" height="11" rx="5.5" fill="{MU}"/>')
        return f"""<path d="M370 205 C430 205 430 345 470 345 M370 345 H470 M370 485 C430 485 430 345 470 345" stroke="#fff" stroke-width="6" fill="none" stroke-dasharray="3 14" stroke-linecap="round" opacity=".85"/>
{cards}
<g filter="url(#s)"><rect x="460" y="255" width="180" height="180" rx="40" fill="{P}"/></g>
<path d="M550 290 C556 326 565 336 601 343 C565 350 556 360 550 396 C544 360 535 350 499 343 C535 336 544 326 550 290Z" fill="url(#g)"/>
<path d="M603 280 C605 292 608 295 620 297 C608 299 605 302 603 314 C601 302 598 299 586 297 C598 295 601 292 603 280Z" fill="#fff"/>
<g filter="url(#s)"><rect x="440" y="80" width="210" height="120" rx="26" fill="#fff"/></g>
<rect x="440" y="80" width="210" height="34" rx="17" fill="url(#g2)"/><rect x="440" y="98" width="210" height="16" fill="url(#g2)"/>
<rect x="468" y="134" width="30" height="24" rx="6" fill="{PK}"/><rect x="510" y="134" width="30" height="24" rx="6" fill="{ACC}"/><rect x="552" y="134" width="30" height="24" rx="6" fill="{PK}"/><rect x="594" y="134" width="30" height="24" rx="6" fill="{PK}"/>
<rect x="468" y="166" width="30" height="20" rx="6" fill="{LG}"/><rect x="510" y="166" width="30" height="20" rx="6" fill="{LG}"/><rect x="552" y="166" width="30" height="20" rx="6" fill="{LG}"/>
<g filter="url(#s)"><rect x="430" y="500" width="230" height="96" rx="48" fill="#fff"/></g><circle cx="478" cy="548" r="28" fill="url(#g)"/>{chk(478, 548, 1.1, w=6)}<rect x="520" y="532" width="110" height="13" rx="6.5" fill="{P}"/><rect x="520" y="555" width="76" height="11" rx="5.5" fill="{MU}"/>"""

    def icon_maturity():
        bars = "".join(
            f'<rect x="{120+i*70}" y="{520-h}" width="52" height="{h}" rx="12" fill="{"url(#g)" if i==4 else (ACC2 if i==3 else SOFT)}" opacity="{1 if i>2 else .9}"/>'
            for i, h in enumerate((70, 120, 175, 235, 300)))
        return f"""<g filter="url(#s)"><rect x="80" y="170" width="420" height="400" rx="32" fill="#fff"/></g>
<rect x="116" y="204" width="170" height="16" rx="8" fill="{P}"/><rect x="116" y="232" width="110" height="12" rx="6" fill="{MU}"/>
{bars}<rect x="110" y="528" width="360" height="6" rx="3" fill="{LINE}"/>
<path d="M146 430 L216 382 L286 330 L356 270 L426 205" stroke="{P}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 16"/>
<g filter="url(#s)"><circle cx="545" cy="215" r="105" fill="#fff"/></g>
<path d="M470 245 A78 78 0 0 1 620 245" stroke="{LG}" stroke-width="26" fill="none" stroke-linecap="round"/>
<path d="M470 245 A78 78 0 0 1 598 186" stroke="url(#g)" stroke-width="26" fill="none" stroke-linecap="round"/>
<line x1="545" y1="245" x2="590" y2="196" stroke="{P}" stroke-width="10" stroke-linecap="round"/><circle cx="545" cy="245" r="14" fill="{P}"/>
<rect x="505" y="272" width="80" height="12" rx="6" fill="{MU}"/>
<g filter="url(#s)"><rect x="440" y="450" width="220" height="150" rx="28" fill="#fff"/></g>
<line x1="482" y1="478" x2="482" y2="575" stroke="{P}" stroke-width="9" stroke-linecap="round"/><path d="M486 480 H560 L540 505 L560 530 H486Z" fill="url(#g)"/>
<rect x="580" y="490" width="56" height="11" rx="5.5" fill="{P}"/><rect x="580" y="512" width="40" height="10" rx="5" fill="{MU}"/><rect x="505" y="555" width="130" height="10" rx="5" fill="{LINE}"/>"""

    def icon_mes():
        lv = ""
        labels = ("ERP", "MES", "PLC", "I/O", "")
        for i in range(5):
            y = 190 + i * 84
            half = 112 + i * 44
            fill = "url(#g)" if i == 1 else ("#fff" if i % 2 == 0 else PK)
            tc = "#fff" if i == 1 else P
            lv += f'<g filter="url(#s)"><path d="M{340-half} {y+76} L{340-half+26} {y} H{340+half-26} L{340+half} {y+76}Z" fill="{fill}"/></g>'
            lv += f'<text x="340" y="{y+50}" text-anchor="middle" font-family="M" font-weight="900" font-size="30" fill="{tc}">L{4-i}{" · " + labels[i] if labels[i] else ""}</text>'
        return f"""{lv}
<g filter="url(#s)"><rect x="500" y="40" width="160" height="110" rx="26" fill="{P}"/></g>
<rect x="528" y="68" width="70" height="54" rx="12" fill="#fff"/><circle cx="563" cy="95" r="18" fill="url(#g)"/><circle cx="563" cy="95" r="7" fill="#fff"/><path d="M604 80 L636 64 V126 L604 110Z" fill="#fff"/>
<path d="M560 156 C560 250 520 280 470 290" stroke="#fff" stroke-width="6" fill="none" stroke-dasharray="3 13" stroke-linecap="round"/>
<g filter="url(#s)"><rect x="40" y="40" width="190" height="96" rx="26" fill="#fff"/></g><circle cx="88" cy="88" r="24" fill="url(#g)"/>{chk(88, 88, 1, w=6)}<rect x="126" y="72" width="80" height="12" rx="6" fill="{P}"/><rect x="126" y="94" width="56" height="10" rx="5" fill="{MU}"/>"""

    def icon_warehouse():
        boxes = ""
        for r in range(3):
            for c in range(3):
                x, y = 112 + c * 92, 196 + r * 120
                hot = (r, c) == (1, 1)
                boxes += f'<rect x="{x}" y="{y}" width="72" height="80" rx="10" fill="{"url(#g)" if hot else (PK if (r+c)%2 else SOFT)}"/><rect x="{x+28}" y="{y}" width="16" height="30" fill="{"#fff" if hot else ACC2}" opacity=".55"/>'
        return f"""<g filter="url(#s)"><rect x="80" y="150" width="320" height="440" rx="26" fill="#fff"/></g>
<rect x="96" y="280" width="288" height="8" rx="4" fill="{P}"/><rect x="96" y="400" width="288" height="8" rx="4" fill="{P}"/><rect x="96" y="520" width="288" height="8" rx="4" fill="{P}"/>
{boxes}
<g filter="url(#s)"><rect x="470" y="500" width="150" height="70" rx="20" fill="{P}"/></g>
<path d="M545 500 L520 395 L600 310" stroke="{P}" stroke-width="30" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M545 500 L520 395 L600 310" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".25"/>
<circle cx="520" cy="395" r="24" fill="url(#g)" stroke="#fff" stroke-width="6"/><circle cx="600" cy="310" r="20" fill="#fff" stroke="{P}" stroke-width="8"/>
<path d="M600 330 L580 362 M600 330 L622 360" stroke="{P}" stroke-width="12" stroke-linecap="round"/>
<g filter="url(#s)"><rect x="440" y="70" width="220" height="150" rx="28" fill="#fff"/></g>
<circle cx="490" cy="145" r="20" fill="url(#g)"/><circle cx="610" cy="110" r="14" fill="{SOFT}"/><circle cx="610" cy="180" r="14" fill="{SOFT}"/><circle cx="550" cy="145" r="14" fill="{PK}"/>
<path d="M510 145 H536 M562 138 L598 116 M562 152 L598 174" stroke="{P}" stroke-width="6" stroke-linecap="round"/>"""

    def icon_agentshield():
        return f"""<g filter="url(#s)"><path d="M330 90 L520 160 V320 C520 450 440 530 330 580 C220 530 140 450 140 320 V160 Z" fill="#fff"/></g>
<path d="M330 128 L486 186 V320 C486 428 420 496 330 540 C240 496 174 428 174 320 V186 Z" fill="url(#g)"/>
<circle cx="330" cy="250" r="30" fill="#fff"/><circle cx="250" cy="380" r="24" fill="#fff"/><circle cx="410" cy="380" r="24" fill="#fff"/><circle cx="330" cy="470" r="20" fill="#fff" opacity=".9"/>
<path d="M314 274 L262 358 M346 274 L398 358 M274 386 H386 M330 280 V448" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".8"/>
<circle cx="330" cy="250" r="12" fill="{P}"/>
<g filter="url(#s)"><rect x="470" y="420" width="200" height="104" rx="26" fill="#fff"/></g>
<path d="M500 492 L524 450 L548 492Z" fill="{C['g1']}" stroke="{C['g1']}" stroke-width="8" stroke-linejoin="round"/><rect x="521" y="463" width="6" height="14" rx="3" fill="#fff"/><circle cx="524" cy="485" r="3.5" fill="#fff"/>
<rect x="566" y="452" width="80" height="12" rx="6" fill="{P}"/><rect x="566" y="474" width="58" height="10" rx="5" fill="{MU}"/>
<g filter="url(#s)"><rect x="30" y="470" width="170" height="120" rx="26" fill="#fff"/></g>
<path d="M70 510 H96 A12 12 0 0 1 120 510 H146 V536 A12 12 0 0 1 146 560 V576 H70 Z" fill="{P}"/>
<g filter="url(#s)"><circle cx="560" cy="150" r="62" fill="#fff"/></g>
<rect x="530" y="148" width="60" height="46" rx="10" fill="{P}"/><path d="M542 148 V134 A18 18 0 0 1 578 134 V148" stroke="{P}" stroke-width="10" fill="none"/><circle cx="560" cy="170" r="7" fill="#fff"/>"""

    icons = {
        "ai": icon_ai,
        "profile": icon_profile,
        "phone": icon_phone,
        "factory": icon_factory,
        "logistics": icon_logistics,
        "hragents": icon_hragents,
        "maturity": icon_maturity,
        "mes": icon_mes,
        "warehouse": icon_warehouse,
        "agentshield": icon_agentshield,
    }
    return DEFS, icons


def htmldoc(pill, title, icon, C, icons, defs, small=None):
    font = "file://" + B + "/static/montserrat.ttf"
    logo = "file://" + B + "/static/logo.png"
    fs = 78 if len(title) < 34 else (68 if len(title) < 52 else 60)
    sm = f'<div class="sm">{html.escape(small)}</div>' if small else ""
    glow = ".10" if "bg1" in C else ".22"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:M;src:url({font});font-weight:100 900}}
*{{margin:0;box-sizing:border-box}}
body{{width:1600px;height:900px;overflow:hidden;font-family:M;color:#fff;position:relative;
background:radial-gradient(circle at 78% 30%,rgba(255,255,255,{glow}),transparent 45%),
radial-gradient(circle at 10% 100%,{C['radial']},transparent 55%),
linear-gradient(135deg,{C.get('bg1',C['g1'])} 0%,{C.get('bg2',C['g2'])} 50%,{C.get('bg3',C['g3'])} 100%)}}
.dots{{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.22) 1.6px,transparent 1.8px);
background-size:30px 30px;-webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 60%,#000 100%)}}
.t{{position:absolute;left:96px;top:0;bottom:0;width:780px;display:flex;flex-direction:column;justify-content:center;padding-bottom:40px}}
.pill{{align-self:flex-start;background:rgba(255,255,255,.2);border:2px solid rgba(255,255,255,.55);padding:10px 24px;border-radius:40px;font-weight:800;font-size:24px;letter-spacing:.4px;margin-bottom:34px}}
h1{{font-size:{fs}px;line-height:1.08;font-weight:900;letter-spacing:-1px;text-wrap:balance;text-shadow:0 4px 30px {C['tshadow']}}}
.sm{{font-size:28px;font-weight:600;margin-top:24px;opacity:.95;line-height:1.35;max-width:700px}}
.br{{position:absolute;left:96px;bottom:70px;display:flex;align-items:center;gap:20px}}
.br img{{width:76px;height:76px;border-radius:20px;border:3px solid #fff}}
.br b{{display:block;font-size:30px;font-weight:800}}.br span{{font-size:21px;font-weight:600;opacity:.88}}
svg{{position:absolute;right:70px;top:100px;width:700px;height:700px}}
</style></head><body><div class="dots"></div>
<div class="t"><div class="pill">{html.escape(pill)}</div><h1>{html.escape(title)}</h1>{sm}</div>
<div class="br"><img src="{logo}"><div><b>Digital Yakalılar</b><span>digitalyakalilar.com</span></div></div>
<svg viewBox="0 0 700 700" xmlns="http://www.w3.org/2000/svg">{defs}{icons[icon]()}</svg></body></html>"""


def fm(path):
    fmt = open(path).read().split("---", 2)[1]
    m = {}
    for line in fmt.strip().splitlines():
        k, v = line.split(":", 1)
        m[k.strip()] = v.strip()
    return m


def jobs(C, icons, defs):
    for k, (tn, en, ic) in CATS.items():
        yield f"cat-{k}-tr", htmldoc("Kategori", tn, ic, C, icons, defs, CATDESC[k][0])
        yield f"cat-{k}-en", htmldoc("Category", en, ic, C, icons, defs, CATDESC[k][1])
    for d, lang in ((B + "/posts", "tr"), (B + "/posts/en", "en")):
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md"):
                continue
            m = fm(d + "/" + f)
            k = m.get("category", "")
            c = CATS.get(k, ("Digital Yakalılar", "Digital Yakalılar", "ai"))
            yield f[:-3], htmldoc(
                c[0] if lang == "tr" else c[1],
                m.get("cover_title", m["title"]),
                m.get("cover_icon", c[2]),
                C,
                icons,
                defs,
            )


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright

    args = sys.argv[1:]
    pal = None
    only = []
    for a in args:
        if a.upper() in PALETTES and pal is None and len(a) == 1:
            pal = a.upper()
        else:
            only.append(a)
    if not pal:
        pal = os.environ.get("DY_PALETTE", "A")
    pal = pal.upper()
    if pal not in PALETTES:
        raise SystemExit(f"Unknown palette {pal!r}; choose A, B, or C")
    C = PALETTES[pal]
    defs, icons = make_icons(C)
    out = OUT
    # also write palette archive
    archive = B + f"/static/covers-{pal}"
    os.makedirs(out, exist_ok=True)
    os.makedirs(archive, exist_ok=True)
    print(f"palette {pal}: {C['label']}")
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = br.new_page(viewport={"width": 1600, "height": 900})
        for name, doc in jobs(C, icons, defs):
            if only and name not in only:
                continue
            tmp = f"/tmp/cover-{pal}-{name}.html"
            open(tmp, "w").write(doc)
            pg.goto("file://" + tmp)
            pg.wait_for_timeout(120)
            png = f"/tmp/cover-{pal}-{name}.png"
            pg.screenshot(path=png)
            im = Image.open(png).convert("RGB")
            for dest in (out, archive):
                im.save(f"{dest}/{name}.jpg", quality=86, optimize=True, progressive=True)
                im.resize((800, 450), Image.LANCZOS).save(
                    f"{dest}/{name}-800.webp", quality=82, method=6
                )
            print("ok", pal, name)
        br.close()
