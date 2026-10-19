---
title: Lojistikte yapay zekâ uygulamaları: Fatura denetimi ve kayıp sevkiyat bulan yeni ajanlar
date: 2026-10-19
updated: 2026-10-19
description: Evos'un YZ operatörü iki ayda yaklaşık 3.500 nakliye faturası denetim kararı verdi; Carrier Logistics ve LSP44 takip numarası olmadan sevkiyat bulan bir API sundu. Lojistikte yapay zekâ uygulamaları KOBİ'ler için ne vaat ediyor?
cover_title: Lojistikte YZ: fatura denetimi
cover_icon: audit
category: lojistik-nakliyat
seo_title: Lojistikte yapay zekâ uygulamaları: Fatura denetimi ve takip
meta_description: Lojistikte yapay zekâ uygulamaları KOBİ'ye iniyor: Evos 3.500 fatura denetim kararı, LSP44 numarasız sevkiyat takibi. BCG: yalnız %13 finansal getiri görüyor.
focus_kw: lojistikte yapay zekâ uygulamaları
keywords: lojistikte yapay zekâ uygulamaları, lojistikte yapay zekâ kullanımı, nakliye fatura denetimi, YZ operatörü, sevkiyat takip API, lojistik KOBİ yapay zekâ
cover_alt: Lojistikte yapay zekâ uygulamaları: Nakliye fatura denetimi ve sevkiyat takibi kapak görseli
---
Lojistikte yapay zekâ denince akla genellikle rota optimizasyonu ve depo robotları gelir. Ekim 2026'nın ikinci haftasında duyurulan iki yenilik ise daha az görünür ama her gün para ve zaman kaybettiren işlere odaklanıyor: nakliye faturalarının denetimi ve takip numarası eksik olan sevkiyatın bulunması [1][3]. Bu yazıda bu iki örnek üzerinden **lojistikte yapay zekâ uygulamaları** konusunun küçük ve orta ölçekli taşımacılar için ne anlama geldiğini, BCG'nin getiri verisiyle birlikte inceliyoruz.

## Evos: Deneyimli çalışanın kararını öğrenen "YZ operatörü"

New York merkezli Evos, 14 Ekim 2026'da 9 milyon dolarlık tohum öncesi (pre-seed) yatırımla gizlilikten çıktı; turu Uncork Capital ve Field Ventures birlikte yönetti [1]. Şirketin iddiası, "operatör" adını verdiği yazılımın bir işi şirketin en deneyimli çalışanlarından öğrenip mevcut sistemlerin içinde kendisinin yapması [1].

Evos'a göre operatör bir işi ancak kararları ekibin kararlarıyla tutarlı biçimde örtüştüğünde tamamen otonom üstleniyor; işletme her adımı bir insanın onaylamasından tamamen otonom çalışmaya kadar seviyeyi kendisi seçiyor [1]. Yatırımcı Field Ventures, operatörün önce "gölge modda" çalıştığını, müşterinin önerileri onaylayıp reddettiğini ve otonominin "varsayılmak yerine kazanıldığını" anlatıyor [2].

Somut örnek bir nakliye brokeri: MyFreightWorld'de Evos operatörü her LTL (parsiyel) taşıyıcı faturasını TMS kayıtlarıyla karşılaştırıyor. Şirkete göre ilk iki ayda yaklaşık 3.500 denetim kararı %97 doğrulukla verildi [1][3]. FreightWaves, Evos'un bu doğruluk oranını nasıl hesapladığını ve örneklemi açıklamadığını, 600 bin doları aşan tutarın ise geri kazanılan para değil, tespit edilen fatura uyuşmazlıklarının değeri olduğunu not ediyor [3].

## Carrier Logistics + LSP44: Takip numarası olmadan sevkiyat bulmak

İkinci örnek "bot yorgunluğu" denen bir sorunu hedefliyor. Carrier Logistics (CLI) ve LSP44'ün 9 Ekim'de Chicago'daki CLI kullanıcı konferansında tanıttığı ve 14 Ekim'de basın bülteniyle duyurduğu API'ye göre 3PL'ler ve yük sahipleri, takip numarası (PRO) eksik veya yanlış olduğunda bile şirket adları, teslimat yeri, yük tanımı ve yaklaşık tarih gibi bilgilerle sevkiyatı sorgulayabiliyor [4][5].

FreightWaves'in aktardığına göre sistem yaklaşık bir haftalık sevkiyat kaydını tarıyor, olası eşleşmeleri buluyor ve yapay zekâ bunları tutarsızlıkları hesaba katarak sıralıyor; örneğin iki hanesi yanlış yazılmış bir numarayı olası eşleşme olarak tanıyabiliyor [5]. API hesaba özel kimlik bilgileriyle korunuyor ve yalnızca doğrulanmış hesaplara ait sevkiyatları dikkate alıyor [5].

CLI başkanı Ben Wiesen yaklaşımı şöyle özetliyor: Karşı taraftaki ses botlarına kendi ses botlarıyla cevap vermek yerine darboğazın kendisini çözmek [5]. Şirketler, kaç taşıyıcının katılacağını ve manuel işin ne kadar azalacağını henüz açıklamadı [5].

## Neden fatura denetimi?

FreightWaves'in aktardığı 2024 tarihli AFS Logistics analizi, sorunun büyüklüğüne dair fikir veriyor [3]:

| AFS Logistics incelemesi (2024) | Değer |
|---|---|
| İncelenen fatura | Yaklaşık 250.000 |
| Tespit edilen hata | 11.881 |
| Hatalı ek hizmet (accessorial) ücretleri | Hataların %42,8'i |
| Yakıt ek ücreti hataları | %14,4 |
| Yük sınıfı hatası | %12,3 |

Bu veri AFS'nin kendi incelemesini yansıtıyor, tüm pazarı değil [3]. Yine de tekrarlanan, kurala dayalı ama istisnası bol bir iş olduğu için fatura denetimi yapay zekâ operatörleri için doğal bir başlangıç noktası.

## Bir bakışta: İki yaklaşım

| | Evos operatörü | CLI + LSP44 API |
|---|---|---|
| Hedef kullanıcı | Fiziksel sektörlerde KOBİ'ler (taşıma, üretim) [1] | LTL taşıyıcılar, 3PL'ler ve yük sahipleri [4] |
| Çözdüğü iş | Fatura denetimi gibi bütün bir fonksiyon [1] | Takip numarası olmadan sevkiyat eşleştirme [4] |
| Çalışma şekli | Uzmanlardan öğrenir, mevcut sistemlerde çalışır, otonomi kademeli [1][2] | API seviyesinde eşleştirme ve YZ ile sıralama [5] |
| Kontrol | Onay seviyesi işletmece belirlenir [1] | Hesaba özel kimlik bilgisi, doğrulanmış hesaplar [5] |
| Paylaşılan sonuç | ~3.500 karar, %97 doğruluk (yöntem açıklanmadı) [1][3] | Henüz ölçülmedi; yaygınlaşma belirsiz [5] |

## Yatırım var, getiri neden gecikiyor?

BCG'nin 24 Ağustos 2026'da yayımladığı ve 30 büyük küresel lojistik şirketinin yöneticileriyle yapılan ankete dayanan analizi, tabloyu dengeliyor: Yöneticilerin %97'si yapay zekâyı stratejik öncelik sayıyor, %67'sinin ayrılmış bir YZ bütçesi var; ama yalnızca %13'ü yapay zekânın ölçülebilir finansal etki sağladığını söylüyor [6].

Alıntılanabilir istatistik: **Büyük lojistik şirketlerinin üçte ikisinin YZ bütçesi var, ama yalnızca %13'ü ölçülebilir finansal sonuç görüyor** [6].

BCG'ye göre nedenler parçalı veri, birbirine bağlanmayan nokta çözümler ve insan tarafına yetersiz yatırım. Katılımcıların %80'i en etkili YZ çözümü olarak tek başına çalışan bir aracı gösteriyor; %37'si en büyük engel olarak şirket içi YZ uzmanlığı eksikliğini işaret ediyor [6]. BCG'nin deneyim kuralı: Eforun %10'u algoritma, %20'si teknoloji ve veri, %70'i insan, süreç ve organizasyonel değişim [6].

## Türkiye'deki taşımacılar için ne anlama geliyor?

TÜİK'in 2026 verilerine göre Türkiye'de "ulaştırma ve depolama" faaliyetindeki girişimlerin yalnızca %9,7'si yapay zekâ kullanıyor; tüm girişimlerde bu oran %14 [7]. Yani sektör ortalamanın gerisinde.

Bu, bir fırsat da olabilir: Evos ve LSP44 örnekleri, yapay zekânın büyük bir dönüşüm projesiyle değil, **tek bir ölçülebilir işle** (fatura uyuşmazlığı, sevkiyat sorgusu) başlayabileceğini gösteriyor. Mevcut sistemi değiştirmeden üstüne ajan koyma yaklaşımını İK tarafında [Providence'ın RITA örneğinde](/providence-ibm-rita-ise-alim-ajanlari/), depo ve tedarik zincirinde de [yapay zekâ ajanları yazımızda](/tedarik-zinciri-yapay-zeka-ajanlari-depo-dijital-isci/) incelemiştik. Ajanlara hangi yetkinin verileceği konusunda [gölge ajan güvenliği yazımız](/calisan-yapay-zeka-ajanlari-guvenlik-riski/), dijital olgunluğunuzu ölçmek için de [TÜBİTAK DDX+ rehberimiz](/tubitak-ddx-dijital-olgunluk-kobi-rehberi/) yol gösterebilir.

## Kontrol listesi: Lojistikte yapay zekâ uygulamalarına başlamadan önce

- [ ] YZ'nin üstleneceği tek bir iş seçildi mi? (fatura denetimi, sevkiyat sorgusu, belge kontrolü)
- [ ] Bu işin bugünkü maliyeti ölçüldü mü? (fatura başına dakika, aylık hata tutarı, telefon/e-posta sayısı)
- [ ] TMS, ERP ve muhasebe verisi YZ'nin okuyabileceği biçimde erişilebilir mi?
- [ ] Deneyimli çalışanın karar kuralları yazıya döküldü mü veya gölge modda öğretilecek mi?
- [ ] İlk aşamada her karar insan onayından geçiyor mu; otonomi için eşik belirlendi mi?
- [ ] Ajanın erişim yetkileri hesap bazında sınırlandı ve loglanıyor mu?
- [ ] "Tespit edilen uyuşmazlık" ile "geri kazanılan tutar" ayrı raporlanıyor mu?
- [ ] Başarılı pilot diğer süreçlere bağlanacak şekilde planlandı mı? (BCG'nin "nokta çözüm" uyarısı)

## Sıkça sorulan sorular

### Lojistikte yapay zekâ nerelerde kullanılıyor?

BCG'ye göre yapay zekâ ağ planlaması, talep tahmini, fiyatlama, müşteri hizmetleri, faturalama otomasyonu ve depo robotiği dahil lojistik değer zincirinin neredeyse her parçasına dokunuyor [6]. Ekim 2026'daki yeni örnekler fatura denetimi ve sevkiyat eşleştirme [1][4].

### Yapay zekâ operatörü nedir?

Evos'un tanımıyla bir işi şirketin deneyimli çalışanlarından öğrenip mevcut sistemlerin içinde o işi yapan yazılım; kararları ekiple tutarlı hâle gelene kadar tam otonomiye geçmiyor [1].

### Nakliye faturalarında en sık hangi hatalar görülüyor?

AFS Logistics'in 2024 incelemesinde hataların %42,8'i ek hizmet ücretlerinden, %14,4'ü yakıt ek ücretinden, %12,3'ü yük sınıfı hatasından kaynaklanıyor [3].

### Lojistik şirketleri yapay zekâdan getiri alıyor mu?

BCG'nin 2026 anketinde yöneticilerin yalnızca %13'ü yapay zekânın ölçülebilir finansal etki sağladığını söylüyor [6].

### Türkiye'de lojistik şirketleri yapay zekâ kullanıyor mu?

TÜİK'e göre ulaştırma ve depolama girişimlerinin %9,7'si yapay zekâ kullanıyor; bu, tüm girişimlerdeki %14 ortalamasının altında [7].

## Kaynaklar

1. Evos, "Evos Raises $9M to Bring Autonomous Operators to Industrial Businesses of All Sizes", 14 Ekim 2026. <https://getevos.ai/resources/blog/evos-raises-9m> (Erişim: 19 Ekim 2026)
2. Field Ventures, "Why We Invested in Evos: Autonomous Operators for the Physical Economy". <https://fieldventures.substack.com/p/why-we-invested-in-evos-autonomous> (Erişim: 19 Ekim 2026)
3. FreightWaves, "Evos raises $9M to build AI operators for industrial businesses", 16 Ekim 2026. <https://www.freightwaves.com/news/evos-raises-9m-to-build-ai-operators-for-industrial-businesses> (Erişim: 19 Ekim 2026)
4. Carrier Logistics / PR Newswire, "Carrier Logistics and LSP44 Join Forces to Solve AI Bot Fatigue", 14 Ekim 2026. <https://www.prnewswire.com/news-releases/carrier-logistics-and-lsp44-join-forces-to-solve-ai-bot-fatigue-302908225.html> (Erişim: 19 Ekim 2026)
5. FreightWaves, "Carrier Logistics, LSP44 announce partnership to automate LTL shipment identification", 16 Ekim 2026. <https://www.freightwaves.com/news/carrier-logistics-lsp44-announce-partnership-to-automate-ltl-shipment-identification> (Erişim: 19 Ekim 2026)
6. BCG, Martin Fink vd., "AI Hasn't Fully Paid Off Yet in Logistics. But It Will.", 24 Ağustos 2026. <https://www.bcg.com/publications/2026/why-ai-isnt-delivering-roi-logistics> (Erişim: 19 Ekim 2026)
7. Anadolu Ajansı, Mertkan Oruç, "Türkiye yapay zekayı en çok bilişimde, en az inşaatta kullanıyor" (TÜİK Yapay Zekâ İstatistikleri 2026), 3 Ekim 2026. <https://www.aa.com.tr/tr/bilim-teknoloji/turkiye-yapay-zekayi-en-cok-bilisimde-en-az-insaatta-kullaniyor/4076782> (Erişim: 19 Ekim 2026)
