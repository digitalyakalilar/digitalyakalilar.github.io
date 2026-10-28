---
title: Denizcilikte siber güvenlik: Gemi ve liman sistemleri için ücretsiz zafiyet veritabanı ve IMO/IACS uyum rehberi
date: 2026-10-28
updated: 2026-10-28
description: ClassNK, Bureau Veritas ve MTS-ISAC'in de yer aldığı Blue Initiative, gemi ve limanları etkileyen yaklaşık 30 bin zafiyeti ücretsiz bir veritabanında topladı. Denizcilikte siber güvenlik için IMO ve IACS E26/E27 tablosu, Türkiye liman verisi ve kontrol listesi.
cover_title: Denizcilikte siber güvenlik
cover_icon: ship
category: lojistik-nakliyat
seo_title: Denizcilikte siber güvenlik: zafiyet veritabanı ve uyum
meta_description: Denizcilikte siber güvenlik rehberi: Blue Initiative 29.552 zafiyeti gemi sistemlerine göre sınıflıyor. IMO ve IACS E26/E27 tablosu, Türkiye verisi ve liste.
focus_kw: denizcilikte siber güvenlik
keywords: denizcilikte siber güvenlik, gemi siber güvenliği, liman siber güvenliği, IACS E26 E27, IMO siber risk yönetimi, Blue Initiative, OT güvenliği, lojistik güvenlik
cover_alt: Denizcilikte siber güvenlik: kalkanla korunan konteyner gemisi ve liman vinci kapak görseli
---
Bir konteyner gemisinin seyir, makine dairesi ve yük yönetimi sistemleri artık birer bilgisayar ağı. Ancak bu sistemlerdeki açıkları takip etmek kolay değil: Ulusal zafiyet veritabanlarında denizcilik etiketi yok. SecurityWeek'in 27 Ekim'de duyurduğu Blue Initiative, bu boşluğu doldurmak için gemi ve limanları etkileyen zafiyetleri tek ve ücretsiz bir veritabanında topluyor [1][2]. Bu yazıda **denizcilikte siber güvenlik** için yeni aracı, uyulması gereken IMO ve IACS kurallarını ve lojistik şirketlerinin atabileceği adımları ele alıyoruz.

## Blue Initiative nedir, kim işletiyor?

Blue Initiative; siber güvenlik şirketi Cydome, Japon klas kuruluşu ClassNK, test ve sertifikasyon şirketi Bureau Veritas, denizcilik bilgi paylaşım merkezi MTS-ISAC ve Rakuten Maritime'ın ortak girişimi [1]. Site, Cydome tarafından ortaklarla birlikte işletiliyor [3]. ClassNK, dünya ticaret filosunun yaklaşık %20'sine denetim ve sertifikasyon hizmeti veriyor [3].

Projenin çıkış noktası şu tespit: CISA'nın endüstriyel kontrol sistemi bildirimlerinde denizcilik üreticileri yer alıyor, ama 200 başka üreticinin arasında; bir filo yöneticisine hangisinin kendi gemisinde olduğunu söyleyen bir filtre yok [3].

| Gösterge | Değer (28 Ekim 2026) | Kaynak |
|---|---|---|
| Veritabanındaki toplam kayıt | 29.552 | [2] |
| Kritik (CVSS 9,0-10,0) | 2.008 | [2] |
| CISA KEV'de (bilinen istismar) | 588 | [2] |
| Doğrudan gemi ve liman için üretilmiş ürünlerdeki zafiyet | 37 | [1][2] |
| Son 90 günde yayımlanan puanlı kayıt | 5.179 | [2] |
| Lisans | CC BY 4.0 (atıfla yeniden kullanılabilir) | [3] |

Alıntılanabilir istatistik: **Blue Initiative'e göre gemi ve limanlara ulaşabilen 29.552 zafiyetin 588'i CISA'nın "bilinen istismar edilen" kataloğunda yer alıyor** [2].

Dikkat edilmesi gereken bir nokta: Kayıtların çoğu CISA bildirimlerinden ve KEV kataloğundan otomatik seçilip sınıflandırılıyor; analist notu taşıyan kayıt sayısı az [1][3]. Yani veritabanı bir önceliklendirme filtresi; kendi envanterinizle eşleştirmeden tek başına risk değerlendirmesi değil. Sitenin bir güvenlik şirketi tarafından işletildiğini de not etmek gerekiyor [3].

## Denizcilikte siber güvenlik kuralları: IMO ve IACS ne istiyor?

Denizcilikte siber güvenlik artık yalnızca iyi uygulama değil, uyum konusu:

| Düzenleme | Kapsam | Ne istiyor? | Kaynak |
|---|---|---|---|
| IMO MSC.428(98) | Güvenlik yönetim sistemi (ISM Kodu) | Siber risklerin, 1 Ocak 2021 sonrasındaki ilk yıllık Uygunluk Belgesi doğrulamasına kadar güvenlik yönetim sistemlerinde ele alınması | [4] |
| IMO MSC-FAL.1/Circ.3/Rev.4 | Tüm denizcilik paydaşları | Siber risk yönetimi için üst düzey öneriler ve işlevsel unsurlar | [4] |
| IACS UR E26 | Geminin bütünü | Yeni gemilerin siber dayanıklılığı için asgari gereklilikler | [5] |
| IACS UR E27 | Gemideki sistem ve ekipman | Bilgisayar tabanlı sistemlerin siber dayanıklılığı | [5] |

ClassNK'ya göre IACS UR E26/E27 kuralları, 1 Temmuz 2024 ve sonrasında inşa sözleşmesi imzalanan gemilere uygulanıyor [5]. IMO ayrıca sektör birliklerinin gemide siber güvenlik rehberini, ISO/IEC 27001'i ve NIST çerçevesini başvuru kaynakları olarak gösteriyor [4].

## Türkiye için neden önemli?

Ulaştırma ve Altyapı Bakanlığı'nın paylaştığı verilere göre Türkiye limanlarında 2026'nın ilk 9 ayında 412,1 milyon ton yük elleçlendi; konteyner elleçleme %2,7 artışla 10,77 milyon TEU'ya ulaştı [6]. Bu hacimde bir liman veya gemi sisteminin birkaç saatlik durması bile ihracatçıdan nakliyeciye uzanan bir zinciri etkiler.

Türkiye'ye özgü kamuya açık bir denizcilik siber olay istatistiği bulamadık. Ancak sektörün kullandığı sistemlerin büyük kısmı küresel üreticilere ait; Blue Initiative'in topladığı açıklar Türk filoları ve terminalleri için de geçerli.

Depo ve tedarik zincirinde benzer riskleri [barkod okuyucu güvenliği](/barkod-okuyucu-guvenligi-depo-siber-saldiri/) ve [lojistikte yapay zekâ uygulamaları](/lojistikte-yapay-zeka-uygulamalari-fatura-denetimi/) yazılarımızda ele almıştık. Gemi ve terminallerdeki kontrol sistemleri için yaklaşım, [endüstriyel kontrol sistemlerinin siber güvenliği](/endustriyel-kontrol-sistemleri-siber-guvenligi-yz-ajani/) yazımızdaki OT ilkeleriyle aynı.

## Gemi ve terminal sistemleri: Nereden başlamalı?

| Sistem grubu | Örnek | Öncelikli kontrol |
|---|---|---|
| Köprüüstü ve seyir | ECDIS, radar, AIS | Yazılım sürümü, USB/harici medya kontrolü |
| Makine ve otomasyon | Alarm ve izleme, güç yönetimi | Ağ ayrımı, uzaktan servis erişimi |
| Yük ve terminal | Yük yönetimi, terminal işletim sistemi | Kimlik ve yetki yönetimi, yedekleme |
| Geminin iş BT'si | E-posta, ofis ağları | Kimlik avı farkındalığı, yama düzeni |
| Haberleşme | Uydu bağlantısı | Varsayılan parolalar, erişim kısıtlama |

Sistem grupları, Blue Initiative'in gemideki sisteme göre sınıflandırma yaklaşımından [2][3] hareketle tarafımızca örneklenmiştir.

## Denizcilikte siber güvenlik kontrol listesi (10 madde)

- [ ] Gemi ve terminaldeki bilgisayar tabanlı sistemlerin envanterini çıkarın (üretici, ürün, sürüm) [5]
- [ ] Envanteri Blue Initiative'de aratıp ilgili kayıtları işaretleyin [2]
- [ ] Önce CISA KEV'de olan, yani bilinen istismar edilen açıkları kapatın [2]
- [ ] Yeni kritik kayıtlar için Blue Initiative uyarılarına abone olun [2]
- [ ] Siber risklerin güvenlik yönetim sisteminde (ISM) ele alındığını doğrulayın [4]
- [ ] Yeni inşa sözleşmelerinde IACS UR E26/E27 uyumunu tersaneyle netleştirin [5]
- [ ] Ekipman tedarikçilerinden UR E27 kapsamındaki tip onay belgelerini isteyin [5]
- [ ] Uzaktan servis erişimini kayıt altına alın ve gerektiğinde açın
- [ ] Mürettebat ve ofis ekibi için siber farkındalık eğitimi planlayın [5]
- [ ] Liman ve gemi için olay müdahale ve manuel işletim planı hazırlayın

## Sıkça sorulan sorular

### Denizcilikte siber güvenlik neden önemli?

Gemi ve liman sistemleri artık birbirine bağlı bilgisayar ağları. IMO, siber risklerin gemi güvenlik yönetim sistemlerinde ele alınmasını istiyor [4].

### Blue Initiative ücretsiz mi?

Evet. Site herkese açık; veriler CC BY 4.0 lisansıyla atıf yapılarak yeniden kullanılabiliyor [3].

### IACS E26 ve E27 hangi gemileri kapsıyor?

ClassNK'ya göre 1 Temmuz 2024 ve sonrasında inşa sözleşmesi imzalanan gemiler [5]. E26 geminin bütününü, E27 gemideki sistem ve ekipmanı kapsıyor [5].

### Blue Initiative'deki kayıtlar nereden geliyor?

Çoğu CISA'nın ICS bildirimlerinden ve KEV kataloğundan otomatik seçiliyor; az sayıda kayıt elle yazılıyor [1][3].

### Türk limanları ne kadar yük elleçliyor?

Bakanlığa göre 2026'nın ilk 9 ayında 412,1 milyon ton yük ve 10,77 milyon TEU konteyner [6].

## Kaynaklar

1. SecurityWeek, Eduard Kovacs, "Maritime Coalition Launches Free Vulnerability Database for Ship and Port Systems", 27 Ekim 2026. <https://www.securityweek.com/maritime-coalition-launches-free-vulnerability-database-for-ship-and-port-systems/> (Erişim: 28 Ekim 2026)
2. Blue Initiative, ana sayfa ve gösterge paneli. <https://www.blue-initiative.org/> (Erişim: 28 Ekim 2026)
3. Blue Initiative, "About Blue Initiative". <https://www.blue-initiative.org/about> (Erişim: 28 Ekim 2026)
4. IMO (Uluslararası Denizcilik Örgütü), "Maritime cyber risk". <https://www.imo.org/en/OurWork/Security/Pages/Cyber-security.aspx> (Erişim: 28 Ekim 2026)
5. ClassNK, "IACS UR E26/27". <https://www.classnk.com/hp/en/activities/cybersecurity/ur-e26e27.html> (Erişim: 28 Ekim 2026)
6. Anadolu Ajansı, Mertkan Oruç, "Deniz ticaretinde 9 ayda 412,1 milyon ton yük elleçlendi", 13 Ekim 2026. <https://aa.com.tr/tr/ekonomi/deniz-ticaretinde-9-ayda-412-1-milyon-ton-yuk-elleclendi/4087554> (Erişim: 28 Ekim 2026)
