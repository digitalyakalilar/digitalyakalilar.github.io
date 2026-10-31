---
title: AIOps nedir? Yapay zekâ ajanları BT operasyonlarını nasıl değiştiriyor (2026 rehberi)
date: 2026-10-31
updated: 2026-10-31
description: AIOps nedir, ajan tabanlı BT operasyonları nasıl çalışır? Gartner'ın 2027 öngörüleri, Google SRE'nin otonomi seviyeleri tablosu, insan onayı ve token maliyeti için kontrol listesiyle 2026 rehberi.
cover_title: AIOps nedir?
cover_icon: aiops
category: yapay-zeka-verimlilik
seo_title: AIOps nedir? Yapay zekâ ajanları ve BT operasyonları
meta_description: AIOps nedir? Gartner'a göre 2030'da kurumların %50'si BT operasyonlarında asgari insan müdahalesiyle ajan kullanacak. Otonomi tablosu ve kontrol listesi.
focus_kw: AIOps nedir
keywords: AIOps nedir, AIOps, AIOps araçları, yapay zekâ ajanları BT operasyonları, BT operasyonları, olay yönetimi, human-on-the-loop, SRE, ITSM, Gartner I&O 2027
cover_alt: AIOps nedir: yapay zekâ ajanlarının BT operasyonlarında sunucu ve olay panelini izlediği kapak görseli
---
Ödeme sayfanız çöktüğünde ilk aranan kişi genellikle sistemi en iyi bilen kıdemli mühendistir. Parny'nin kurucu ortağı ve CEO'su Berkay Özuygur, 28 Ekim'de Webrazzi'de yayımlanan konuk yazısında bu bilginin birkaç kişinin kafasında kalmasının riskine dikkat çekiyor ve AIOps'u bu hafızayı sisteme taşıyan "20 yıllık kıdemli mimar"a benzetiyor [1]. Peki **AIOps nedir**, yapay zekâ ajanlarıyla nasıl değişiyor ve kurumlar nereden başlamalı? Gartner'ın 26 Ekim 2026'da açıkladığı 2027 öngörüleri [2] ve Google SRE ekibinin yayımladığı otonomi seviyeleri [4] bu soruya somut bir çerçeve sunuyor.

## AIOps nedir? Kısa tanım

AIOps, yapay zekâ destekli BT operasyonları demektir. Webrazzi'deki yazıya göre AIOps, erişebildiği güncel sistem verileri ve kayıtlı operasyon bilgisi üzerinden uygulamalar, servisler ve altyapı arasındaki ilişkileri öğrenir; tek bir hataya değil, sistemin bütününe bakar [1]. Klasik izleme araçları "bir şey bozuk" der; AIOps "neden bozuk, ne yapmalı?" sorusuna cevap aramaya çalışır.

Yazıdaki varsayımsal örnek şöyle: Yeni bir yazılım sürümünden sonra ödemeler hata vermeye başlar. AIOps hata kayıtlarını, servis yanıt sürelerini, veritabanı bağlantı yoğunluğunu ve son değişiklikleri birlikte inceler. Bulgular yeni sürümü işaret ediyorsa ve önceki sürüme dönmek güvenliyse, belirlenen politika ve yetkiler içinde geri alma (rollback) yapar; onay gereken durumlarda gerekçesiyle önerir ve onayla uygular [1]. Yazar, konuya taraf bir AIOps şirketinin yöneticisi; yazı da bir konuk yazısı. Bu yüzden aşağıda bağımsız verilerle destekliyoruz.

## Human-in-the-loop'tan human-on-the-loop'a

Gartner'ın 26 Ekim 2026'da yayımladığı altyapı ve operasyon (I&O) trendlerine göre yapay zekâ ajanları, reaktif ve "insanın döngünün içinde olduğu" (human-in-the-loop) operasyonlardan, proaktif ve "insanın döngüyü gözetlediği" (human-on-the-loop) operasyonlara geçişi hızlandırıyor [2]. Farkı şöyle özetleyebiliriz:

- **Human-in-the-loop:** Sistem çözümü önerir, insan onaylar, sonra uygulanır [1].
- **Human-on-the-loop:** Sistem belirlenen politika ve yetkiler içinde kendisi uygular; ekip süreci izler ve gerektiğinde müdahale eder [1].

Gartner'ın 2027 için öne çıkardığı veriler [2]:

| Gartner öngörüsü / bulgusu (26 Ekim 2026) | Değer |
|---|---|
| Yapay zekâ denemelerini I&O'da yaygın kullanıma taşımayı önümüzdeki 12 ayın önceliği sayan I&O liderleri | %58 (272 kişilik anket, Nisan-Mayıs 2026) |
| BT operasyonlarında asgari insan müdahalesiyle yapay zekâ ajanı kullanacak kurumlar (2030) | %50 (2026'da neredeyse %0) |
| Token kullanımına bağlı, üst sınırı olmayan fiyatlandırmayla BT operasyonlarında ajan kullanan kurumların başlangıç maliyet beklentisini aşma oranı (2027'ye kadar, abonelik modellerine kıyasla) | %50'den fazla |
| Yapay zekâ iş yüklerini en az üç ortamda çalıştıracak büyük kurumlar (2029) | %80 |
| Ağ ve güvenlik operasyon merkezlerini (NOC/SOC) birleştirecek kurumlar (2030) | %25 (2026'da %5); araç ve personel harcamasında %25'ten fazla azalma |

Kaynak: Gartner basın bülteni [2]; ITPro'nun haberi de aynı bulguları aktarıyor [3].

Alıntılanabilir istatistik: **Gartner'a göre 2030'a kadar kurumların %50'si BT operasyonlarında asgari insan müdahalesiyle çalışan yapay zekâ ajanları kullanacak; 2026'da bu oran neredeyse sıfır** [2].

## Gerçeklik kontrolü: AIOps projelerinin çoğu henüz yatırım getirisini görmüyor

Aynı Gartner, Nisan 2026'da daha temkinli bir tablo çizmişti. 782 I&O lideriyle Kasım-Aralık 2025'te yapılan ankete göre altyapı ve operasyonlarda yapay zekâ kullanım senaryolarının yalnızca %28'i tamamen başarılı olup yatırım getirisi beklentisini karşılıyor; %20'si tamamen başarısız oluyor [5]. Liderlerin %57'si en az bir başarısızlık bildirdi [5].

Başarısızlıkların en sık görüldüğü alanlar, tam da AIOps'un vaat ettiği yerler: otomatik düzeltme (auto-remediation), kendi kendini onaran altyapı ve sistemler arası iş akışlarını ajanların yönetmesi [5]. Başarıların %53'ü ise BT hizmet yönetiminde (ITSM) geliyor [5]. Ders açık: Küçük, olgun ve ölçülebilir senaryolarla başlamak gerekiyor.

## Google SRE'nin otonomi seviyeleri: Ajana ne kadar yetki?

Google SRE ekibinin "AI in SRE" yazısı, ajanlara verilecek yetkiyi beş seviyede tanımlıyor [4]. Bu tablo, AIOps araçları seçerken "bu ürün hangi seviyede çalışıyor?" sorusunu sormak için iyi bir referans:

| Seviye | İzleme | İnceleme | Müdahaleye karar (onay) | Uygulama | Kendi yönünü belirleme |
|---|---|---|---|---|---|
| L0 – Manuel | Otomasyon | İnsan | İnsan | İnsan | İnsan |
| L1 – Destekli | Otomasyon | Otomasyon | İnsan | İnsan | İnsan |
| L2 – Kısmi (insan onayı) | Otomasyon | Otomasyon | İnsan | Otomasyon | İnsan |
| L3 – Yüksek | Otomasyon | Otomasyon | Otomasyon | Otomasyon | İnsan |
| L4 – Tam | Otomasyon | Otomasyon | Otomasyon | Otomasyon | Otomasyon |

Kaynak: Google SRE, "AI in SRE: How Google is Engineering the Future of Reliable Operations", Tablo 1 [4]; Türkçeleştirme tarafımızca yapılmıştır.

Google'ın kendi ölçümleri, düşük seviyelerin bile değer ürettiğini gösteriyor. Yalnızca bilgi veren "Incident Hypothesis" özelliği (L1), olayı hafifletme süresini (MTTM) %10 kısalttı. İnceleme panoları (Investigation Dashboard) ise desteklenen olaylarda MTTM'yi yaklaşık %44 azalttı; bu panolardaki makine öğrenmesi tabanlı anomali tespiti, bulguları %195 artırdı [4]. Bunlar Google'ın kendi ortamına ait sonuçlar; her kurumda aynı oranlar beklenmemeli.

## Ajan tabanlı AIOps için korkuluklar

Google SRE, üretim sistemlerine dokunan her yapay zekâ ajanı için dört mimari korkuluk tanımlıyor [4]:

| Korkuluk [4] | Ne anlama geliyor? |
|---|---|
| Sürekli erişim yok, en az yetki | Ajan, geliştiricisinin kimlik bilgileriyle çalışmaz; ayrı kimliği vardır ve yetkiyi yalnızca gerektiğinde alır |
| Ajana özel devre kesiciler | Hız sınırları ve otomatik kesiciler kontrolden çıkan döngüleri durdurur; her eylem kesilebilir olmalı |
| Zorunlu "dry run" | Ajanın kullandığı her API, eylemin etkisini önceden gösteren deneme modunu desteklemeli |
| Sıfır güven ilkesiyle uygulama | Altyapı araçları, onları kim çağırırsa çağırsın üretimi tek başına çökertemeyecek şekilde tasarlanmalı |

Bu ilkeler, [Microsoft execution containers yazımızda](/microsoft-execution-containers-ajan-guvenligi/) ve [çalışanların kurduğu yapay zekâ ajanlarının güvenlik riski yazımızda](/calisan-yapay-zeka-ajanlari-guvenlik-riski/) ele aldığımız ajan güvenliği konularıyla birebir örtüşüyor.

## Token maliyeti: "Telemetri yoksa devreye alma yok"

Gartner'ın öngörülerinden biri doğrudan bütçeyle ilgili: 2027'ye kadar BT operasyonlarında token kullanımına bağlı, üst sınırı olmayan fiyatlandırmayla yapay zekâ ajanı kullanan kurumlar, başlangıçtaki maliyet beklentilerini abonelik modeli kullananlara kıyasla %50'den fazla aşacak. Gartner, I&O liderlerine "telemetri yoksa devreye alma yok" politikası öneriyor [2]. Yani kullanım ve maliyet ölçülemeyen hiçbir ajan canlıya alınmamalı. Bu konuyu [yapay zekâ maliyet yönetimi ve token FinOps yazımızda](/yapay-zeka-maliyet-yonetimi-token-finops/) ayrıntılı anlattık.

## Pazar hareketi: Yatırımlar BT operasyonu ajanlarına akıyor

Webrazzi'nin 30 Ekim 2026 tarihli haberine göre BT operasyonlarına odaklanan ABD merkezli Serval, Sequoia liderliğinde 3 milyar dolar değerleme üzerinden 150 milyon dolarlık C serisi yatırım aldı [6]. Şirketin yapay zekâ ajanları çalışanların erişim izinlerini yönetiyor, teknik sorunları çözüyor ve yazılım-donanım varlıklarını takip ediyor; ajanların erişebileceği bilgiler BT ve güvenlik ekiplerince belirleniyor, hassas işlemlerde insan onayı alınabiliyor [6]. Bu yaklaşım, yukarıdaki tablodaki L2 seviyesine karşılık geliyor.

Türkiye'den bir bağlam: TÜİK'in Yapay Zekâ İstatistikleri 2026 bültenine göre yapay zekâ kullanan girişimlerin oranı %7,5'ten %14'e çıktı; bu oran telekomünikasyon, programlama ve bilişim sektöründe %63,7 [7]. BT ekipleri, yapay zekâyı en yoğun kullanan kesim; AIOps kararlarının da en önce bu ekiplerde verilmesi bekleniyor.

## AIOps'a başlamak için kontrol listesi

- [ ] Başarının en kanıtlı olduğu yerden başlayın: BT hizmet yönetimi ve olay inceleme [5]
- [ ] Her senaryo için Google'ın L0-L4 tablosuna göre hedef seviyeyi yazın; ilk aşamada L1-L2 ile sınırlayın [4]
- [ ] Ajanlara ayrı kimlik verin; insan hesaplarının kimlik bilgilerini kullandırmayın [4]
- [ ] Rollback gibi eylemler için yazılı politika ve yetki sınırı tanımlayın; onay gereken durumları listeleyin [1]
- [ ] Ajanın kullanacağı her API'de dry run desteği ve devre kesici olsun [4]
- [ ] "Telemetri yoksa devreye alma yok": token kullanımı ve maliyeti ölçülmeden canlıya almayın [2]
- [ ] Başlangıç değeri olarak bugünkü MTTM'yi ölçün; aksi hâlde iyileşmeyi kanıtlayamazsınız [4]
- [ ] Olay sonrası öğrenilenleri kayıt altına alın; bilgi birkaç kişinin kafasında kalmasın [1]
- [ ] Otomatik düzeltme ve kendi kendini onaran altyapı gibi en sık başarısız olan alanlarda beklentiyi düşük tutun [5]
- [ ] Satıcı iddialarını kendi ortamınızda pilotla doğrulayın

## Sıkça sorulan sorular

### AIOps nedir?

AIOps, yapay zekâ destekli BT operasyonlarıdır. Sistem verileri ve kayıtlı operasyon bilgisi üzerinden uygulamalar, servisler ve altyapı arasındaki ilişkileri öğrenir; sorunun kaynağını bulmaya ve müdahale etmeye yardımcı olur [1].

### Human-on-the-loop ne demek?

Yapay zekâ sisteminin belirlenen politika ve yetkiler içinde müdahaleyi kendisinin uyguladığı, ekibin ise süreci izleyip gerektiğinde müdahale ettiği yaklaşımdır. Human-in-the-loop'ta ise uygulama öncesinde insan onayı gerekir [1][2].

### AIOps projeleri başarılı oluyor mu?

Gartner'ın 782 I&O lideriyle yaptığı ankete göre altyapı ve operasyonlarda yapay zekâ senaryolarının yalnızca %28'i tamamen başarılı olup yatırım getirisini karşılıyor; %20'si tamamen başarısız [5].

### Yapay zekâ ajanlarına BT operasyonlarında ne kadar yetki verilmeli?

Google SRE, L0'dan L4'e beş otonomi seviyesi tanımlıyor ve ajanların düşük seviyede, insan onayıyla başlatılıp kademeli olarak yükseltilmesini öneriyor [4].

### AIOps maliyeti nasıl kontrol edilir?

Gartner, token kullanımına bağlı üst sınırsız fiyatlandırmayla BT operasyonlarında ajan kullanan kurumların 2027'ye kadar başlangıç maliyet beklentilerini %50'den fazla aşacağını öngörüyor ve "telemetri yoksa devreye alma yok" politikası öneriyor [2].

## Kaynaklar

1. Webrazzi, Berkay Özuygur (konuk yazar, Parny kurucu ortağı ve CEO'su), "AIOps: Tech ekibinin 20 yıllık kıdemli mimarı", 28 Ekim 2026. <https://webrazzi.com/2026/10/28/aiops-tech-ekibinin-20-yillik-kidemli-mimari/> (Erişim: 31 Ekim 2026)
2. Gartner, "Gartner Identifies the Top AI Trends in Infrastructure and IT Operations for 2027", 26 Ekim 2026. <https://www.gartner.com/en/newsroom/press-releases/2026-10-26-gartner-identifies-the-top-ai-trends-in-infrastructure-and-it-operations-for-2027> (Erişim: 31 Ekim 2026)
3. ITPro, Emma Woollacott, "AI is crucial to infrastructure and IT operations but only if it's done right, Gartner report says", 26 Ekim 2026. <https://www.itpro.com/infrastructure/ai-is-crucial-to-infrastructure-and-it-operations-but-only-if-its-done-right-gartner-report-says> (Erişim: 31 Ekim 2026)
4. Google SRE, Ioannis Papapanagiotou, Stevan Malesevic, Chris Heiser ve Ruslan Meshenberg, "AI in SRE: How Google is Engineering the Future of Reliable Operations". <https://sre.google/resources/practices-and-processes/ai-engineering-reliable-operations/> (Erişim: 31 Ekim 2026)
5. Gartner, "Gartner Says AI Projects in I&O Stall Ahead of Meaningful ROI Returns", 7 Nisan 2026. <https://www.gartner.com/en/newsroom/press-releases/2026-04-07-gartner-says-artificial-intelligence-projects-in-infrastructure-and-operations-stall-ahead-of-meaningful-roi-returns> (Erişim: 31 Ekim 2026)
6. Webrazzi, Candeğer Muradoğlu, "Serval, 3 milyar değerleme üzerinden 150 milyon dolar yatırım aldı", 30 Ekim 2026. <https://webrazzi.com/2026/10/30/serval-3-milyar-degerleme-uzerinden-150-milyon-dolar-yatirim-aldi/> (Erişim: 31 Ekim 2026)
7. Anadolu Ajansı, Mertkan Oruç, "Türkiye yapay zekayı en çok bilişimde, en az inşaatta kullanıyor" (TÜİK Yapay Zeka İstatistikleri 2026), 3 Ekim 2026. <https://www.aa.com.tr/tr/bilim-teknoloji/turkiye-yapay-zekayi-en-cok-bilisimde-en-az-insaatta-kullaniyor/4076782> (Erişim: 31 Ekim 2026)
