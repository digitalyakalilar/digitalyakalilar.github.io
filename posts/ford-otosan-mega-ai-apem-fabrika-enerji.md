---
title: Fabrikada yapay zekâ ile enerji yönetimi: Ford Otosan'ın MEGA AI APEM örneği
date: 2026-10-16
updated: 2026-10-16
description: Ford Otosan, Kocaeli'deki Gölcük ve Yeniköy fabrikalarında MEGA AI APEM ile 1.000'den fazla noktadan enerji tüketimini izliyor. Fabrikada yapay zekâ ile enerji yönetimi Türkiye üretimi için ne vaat ediyor?
cover_title: Fabrikada YZ ile enerji yönetimi
cover_icon: factory
category: endustri-4-0
seo_title: Fabrikada yapay zekâ ile enerji yönetimi: Ford Otosan APEM
meta_description: Fabrikada yapay zekâ ile enerji yönetimi: Ford Otosan MEGA AI APEM 1.000+ noktayı izliyor; hedef 2.560 ton CO₂ ve araç başına 19,66 kWh. Kaynaklı rehber.
focus_kw: fabrikada yapay zekâ ile enerji yönetimi
keywords: fabrikada yapay zekâ ile enerji yönetimi, endüstriyel enerji izleme, akıllı bakım, fabrika CO2 azaltma, üretimde yapay zekâ, MEGA AI APEM
cover_alt: Fabrikada yapay zekâ ile enerji yönetimi: Ford Otosan MEGA AI APEM kapak görseli
---
Üretimde dijitalleşme çoğu zaman MES, kalite veya robotik üzerinden anlatılır. Enerji katmanı ise sıkça raporlama ekranında kalır. Ford Otosan'ın 2026'da Kocaeli fabrikalarında devreye aldığını duyurduğu MEGA AI APEM (Yapay Zekâ Destekli Enerji Yönetimi), izlemeyi saha aksiyonuna bağlayan bir örnek sunuyor [1]. Bu yazıda **fabrikada yapay zekâ ile enerji yönetimi** yaklaşımını kaynaklarıyla inceliyor, ISA-95 / MES tartışmasıyla ilişkilendiriyor ve diğer üreticiler için bir kontrol listesi çıkarıyoruz.

## MEGA AI APEM ne yapıyor?

Şirketin Ekonomigazetesi'nde yayımlanan açıklamasına göre sistem Gölcük ve Yeniköy fabrikalarında çalışıyor. Elektrik, doğalgaz, su ve basınçlı hava tüketimini **1.000'in üzerinde noktadan** izliyor; beklenen tüketimden sapmaları anlık belirliyor ve saha ekiplerini **otomatik iş emirleriyle** harekete geçiriyor [1]. Böylece enerji yönetimi, geriye dönük raporlamadan "izleme + aksiyon" kapalı döngüsüne taşınıyor.

Kocaeli fabrikalarının toplam üretim kapasitesi açıklamada **612 bin adet/yıl** olarak geçiyor [1]. APEM hazır bir paket yazılım olarak değil, Ford Otosan'ın üretim, enerji, bakım ve veri ekiplerinin birlikte geliştirdiği endüstriyel yapay zekâ katmanı olarak tanımlanıyor [1].

## Paylaşılan hedefler ve örnek olay

| Gösterge | Açıklamadaki rakam |
|---|---|
| Yıllık CO₂ azaltım hedefi | 2.560 ton [1] |
| Araç başına enerji tasarrufu | 19,66 kWh [1] |
| Yeniköy Boyahane örneği | Tek olayda ~180 bin kWh/yıl kaybın önüne geçilmesi [1] |
| Ölçüm noktası | 1.000+ [1] |

Ford Otosan Yeni Projeler & Yatırımlar Lideri Müjdat Tiryaki, Yeniköy Boyahane örneğini yapay zekâ destekli çözümlerin sahadaki somut değeri olarak aktarıyor [1]. Aynı açıklamada APEM'in, şirketin **2034'e kadar Kapsam 1 ve 2 mutlak emisyonlarını 2017 baz yılına göre %77 azaltma** ve **2050 net sıfır** hedeflerine hizmet eden uygulamalardan biri olduğu belirtiliyor [1].

## Teknik omurga: Veriden iş emrine

Açıklamaya göre APEM'in temelinde saha enerji ekipmanlarından gelen verilerin üretim ve çevresel verilerle birleştirilmesi var. Yapay zekâ ve makine öğrenmesi modelleri farklı üretim koşullarında test edilerek geliştiriliyor; **Akıllı Bakım entegrasyonu** sayesinde tespit edilen sapmalar doğrudan saha aksiyonuna dönüşüyor [1].

Bu mimari, klasik "dashboard'da kırmızı çizgi" yaklaşımından farklı: Model sapmayı görüyor, bakım/enerji ekibine iş emri açılıyor, müdahale kayda giriyor. İnsan hâlâ döngüde; ajan (veya model) kararın tetikleyicisi.

## Endüstri 4.0 bağlamı: MES ile enerji katmanı

Türkiye'de büyük üreticiler üretim yönetimini ISA-95 Seviye 3 MES katmanıyla güçlendiriyor. [KARDEMİR'in 27 tesiste Seviye 3 MES hedefi](/kardemir-seviye-3-mes-isa-95/) ERP ile saha otomasyonu arasını dolduruyor. APEM ise aynı dijital omurgada **enerji ve sürdürülebilirlik** katmanını kapatıyor: Üretim verisi olmadan "beklenen tüketim" modeli zayıf kalır; enerji verisi olmadan MES OEE'si maliyet ve karbon gerçeğini kaçırır.

KOBİ'ler için yol haritası arayanlar [TÜBİTAK DDX dijital olgunluk rehberimize](/tubitak-ddx-dijital-olgunluk-kobi-rehberi/) de bakabilir. Depo ve tedarik zinciri tarafındaki ajan örnekleri için [tedarik zincirinde yapay zekâ ajanları yazımız](/tedarik-zinciri-yapay-zeka-ajanlari-depo-dijital-isci/) tamamlayıcı.

## Karşılaştırma: Enerji YZ olgunluk basamakları

| Seviye | Ne yapılır? | Tipik çıktı |
|---|---|---|
| 1. Sayacın dijitalleşmesi | Aylık fatura / manuel okuma | Gecikmeli rapor |
| 2. Gerçek zamanlı izleme | SCADA / IoT dashboard | Alarm, ama aksiyon ayrı sistemde |
| 3. Sapma + iş emri (APEM tipi) | Model + bakım entegrasyonu [1] | Otomatik saha görevi |
| 4. Üretim-enerji ortak optimizasyon | MES + enerji + planlama | Vardiya/plan kararlarına bağlı enerji |

Ford Otosan örneği seviye 3'e oturuyor: İzleme ile aksiyon aynı yapıda [1].

## Kontrol listesi: Fabrikada yapay zekâ ile enerji yönetimi

- [ ] Elektrik, gaz, su, basınçlı hava için kritik tüketim noktaları haritalandı mı?
- [ ] "Beklenen tüketim" modeli ürün, vardiya ve çevre koşullarını kapsıyor mu?
- [ ] Sapma alarmı otomatik iş emrine dönüşüyor mu, yoksa yalnızca e-posta mı gidiyor?
- [ ] Bakım CMMS / Akıllı Bakım ile entegrasyon var mı?
- [ ] CO₂ ve kWh hedefleri baz yıl ve sınır (Kapsam 1–2) ile yazılı mı?
- [ ] Sahte pozitif oranını düşürmek için model yeniden eğitiliyor mu?
- [ ] Veri sahipliği (enerji, üretim, IT) net mi?

## Sıkça sorulan sorular

### Fabrikada yapay zekâ ile enerji yönetimi nedir?

Tüketim verisini üretim bağlamıyla birleştirip sapmaları tespit eden ve bakım/enerji ekiplerini aksiyona yönlendiren yapay zekâ katmanı. Ford Otosan APEM örneğinde 1.000+ noktadan izleme ve otomatik iş emirleri kullanılıyor [1].

### APEM hazır bir ürün mü?

Açıklamada Ford Otosan'ın fabrika ihtiyaçlarına göre kurguladığı endüstriyel yapay zekâ katmanı olarak tanımlanıyor; raftan alınan tek bir paket olarak sunulmuyor [1].

### 2.560 ton CO₂ ve 19,66 kWh rakamları nedir?

Şirket açıklamasındaki hedeflenen / sağlanan tasarruf göstergeleri [1]. Bağımsız üçüncü taraf denetim raporu bu haberde yer almıyor.

### Küçük bir fabrika bunu kopyalayabilir mi?

Ölçüm noktası sayısını ve model karmaşıklığını ölçeklemek mümkün. Önce kritik 20–50 noktayı dijitalleştirmek, sonra sapma→iş emri döngüsünü kurmak daha gerçekçi bir yol.

### Bu yazı e-ticaret veya tüketici elektroniği içeriyor mu?

Hayır. Konu üretim tesisinde enerji yönetimi ve endüstriyel yapay zekâ.

## Kaynaklar

1. Ekonomigazetesi, "'MEGA AI APEM ile enerji kayıplarını henüz oluşmadan tespit ederek önlem alabiliyoruz'" (Ford Otosan açıklaması), güncelleme 8 Ekim 2026. <https://www.ekonomigazetesi.com/sirket-haberleri/ford-otosan-kocaeli-fabrikalarinda-enerji-yonetimini-yapay-zekayla-donusturuyor-89288> (Erişim: 16 Ekim 2026)
