---
title: Otonom mobil robot (AMR) güvenliği: ISO 3691-4, yeni Makine Emniyeti Yönetmeliği ve simülasyonla sertifikasyon
date: 2026-10-22
updated: 2026-10-22
description: TÜV SÜD ve Accenture, otonom mobil robotların güvenlik sertifikasyonunu dijital ikiz ve simülasyonla hızlandıran bir konsept tanıttı. Türkiye'de ise 2023/1230 uyumlu Makine Emniyeti Yönetmeliği 20 Ocak 2027'de yürürlüğe giriyor. Fabrika ve depolar neye hazırlanmalı?
cover_title: Otonom mobil robot güvenliği
cover_icon: amr
category: endustri-4-0
seo_title: Otonom mobil robot (AMR) güvenliği ve ISO 3691-4 rehberi
meta_description: Otonom mobil robot (AMR) kurarken ISO 3691-4'ü ve 20 Ocak 2027'de yürürlüğe girecek Makine Emniyeti Yönetmeliği'ni bilin. AGV-AMR farkı ve kontrol listesi.
focus_kw: otonom mobil robot
keywords: otonom mobil robot, AMR nedir, AGV AMR farkı, ISO 3691-4, fiziksel yapay zekâ, Makine Emniyeti Yönetmeliği 2023/1230, robot güvenlik sertifikasyonu
cover_alt: Otonom mobil robot (AMR) güvenliği: ISO 3691-4 ve simülasyonla sertifikasyon kapak görseli
---
Fabrikada ve depoda insanlarla aynı koridoru paylaşan bir **otonom mobil robot** (AMR) devreye almak, robotu satın almaktan çok daha uzun sürebiliyor; asıl zaman güvenlik konseptinin onaylanmasına gidiyor. TÜV SÜD ve Accenture 21 Ekim 2026'da bu süreci dijital ikiz ve simülasyonla kısaltmayı hedefleyen "Physical AI Safety Suite" konseptini tanıttı [1]. Aynı hafta Türkiye'de AB'nin 2023/1230 sayılı Makine Tüzüğü'ne uyumlu yeni Makine Emniyeti Yönetmeliği Resmî Gazete'de yayımlandı [6]. Bu yazıda AMR güvenliğinin standart, mevzuat ve uygulama tarafını bir arada derledik.

## Otonom mobil robot (AMR) nedir? AGV ile farkı

Uluslararası Robotik Federasyonu'nun (IFR) ISO 8373'e dayanan tanımlarına göre otomatik yönlendirmeli araç (AGV), işaretçilerle veya dış yönlendirme komutlarıyla belirlenmiş bir yolu izleyen mobil platform; kendi yolunu belirleme özerkliği olmadığı için IFR onu "robot" değil "robotik cihaz" sayıyor [4]. AMR ise endüstriyel ortamlarda sık kullanılsa da IFR tarafından profesyonel hizmet robotu olarak sınıflandırılıyor; üzerine robot kol takılırsa kol ayrıca endüstriyel robot olarak sayılıyor [4].

| | AGV | Otonom mobil robot (AMR) |
|---|---|---|
| Yol belirleme | Önceden belirlenmiş yol, işaretçi veya dış komut [4] | Kendi kontrolüyle hareket eden mobil robot [4] |
| IFR sınıflandırması | Robotik cihaz (robot değil) [4] | Profesyonel hizmet robotu [4] |
| Güvenlik standardı | ISO 3691-4 kapsamında [3] | ISO 3691-4 kapsamında [3] |
| İstatistikte görünürlük | Endüstriyel robot sayımına girmez [4] | Endüstriyel robot sayımına girmez; hizmet robotu olarak sayılır [4] |
| Tipik risk | Sabit güzergâhta engel ve çarpışma | Değişen güzergâhta insanla karşılaşma, sıkıştırma [1] |

Bu ayrım Türkiye verisini okurken önemli: Aşağıdaki IFR endüstriyel robot rakamları AMR'leri içermiyor.

## ISO 3691-4 neyi kapsıyor?

ISO 3691-4:2023, sürücüsüz endüstriyel araçlar ve sistemleri için güvenlik gerekliliklerini ve bunların doğrulama yöntemlerini tanımlıyor. Standart örnek olarak açıkça "otomatik yönlendirmeli araç", "otonom mobil robot", "bot", "otomatik yönlendirmeli araba" (automated guided cart), "tünel çekici" (tunnel tugger) ve "araba altı araç" (under cart) gibi tipleri sayıyor [3]. Raylar gibi yalnızca mekanik yönlendirmeli araçlar ve uzaktan kumandalı araçlar kapsam dışında [3].

Standardın kritik bir vurgusu var: Çalışma alanının durumu, aracın güvenli çalışmasını önemli ölçüde etkiliyor; çalışma alanının hazırlanması ayrı bir ekte (Ek A) düzenleniyor [3]. Yani güvenlik yalnızca robotun özelliği değil, zemin, koridor genişliği, karma kullanım alanları ve işaretlemeyle birlikte değerlendiriliyor. ISO sayfasına göre 2023 sürümünün yakında ISO/DIS 3691-4 ile değiştirilmesi bekleniyor [3].

## TÜV SÜD ve Accenture'ın modeli: Robot gelmeden önce test

Accenture'ın duyurusuna göre orta ölçekli bir üretim tesisinde güvenlik konseptlerinin tekrarlı koordinasyonu, doğrulanması ve kabulü birkaç hafta sürebiliyor [1]. Physical AI Safety Suite, tesis ve ekipmanın manuel değerlendirmesini ve sertifikasyon paketinin hazırlanmasını dijital ikiz ve yapay zekâ destekli simülasyonlarla kısmen dijitalleştiriyor. TÜV SÜD, bu dijital sürecin üretimi %30'a kadar daha erken devreye alabileceğini tahmin ediyor [1][2].

Konsept üç katmanda çalışıyor; bağımsız değerlendirme ve sertifikasyon sorumluluğu TÜV SÜD'de kalıyor [1]:

| Katman | Sorduğu soru | Ne yapılıyor? |
|---|---|---|
| 1. Tesis yerleşimi | Fiziksel yapay zekâ nerede güvenle çalışabilir? | Güzergâhlar, açıklıklar, karma kullanım ve iş birliği alanları robotlar gelmeden sanal olarak değerlendiriliyor; TÜV SÜD incelemesi için kanıt paketi üretiliyor [1] |
| 2. Robot filosu | Filo nasıl güvenle çalışır? | Filo davranışı simüle edilip çalışanın AMR'ler arasında sıkışması gibi tehlikeler önceden aranıyor; işletmede tesis kameralarıyla robotun göremediği riskler izleniyor [1] |
| 3. Tek robot | Robotun neye izni var? | Yük, hız, zemin ve aydınlatma gibi sahaya özgü koşullarda gerçek testte kapsanamayacak senaryolar simülasyonla test ediliyor [1] |

Accenture'dan Sarat Maitin'in tespiti birçok şirket için tanıdık: Otomasyon konseptleri çoğu zaman ekipman, yerleşim ve iş akışları kurulduktan sonra standartlara karşı test ediliyor [1]. Bu da sonradan pahalı tadilat demek.

Not: Physical AI Safety Suite NVIDIA GTC Berlin 2026'da bir "konsept" olarak sunuldu; %30 rakamı TÜV SÜD'ün tahmini [1].

## Türkiye: Yeni Makine Emniyeti Yönetmeliği ve robot verisi

Sanayi ve Teknoloji Bakanlığı'nın 16 Ekim 2026 tarihli ve 33402 sayılı Resmî Gazete'de yayımladığı Makine Emniyeti Yönetmeliği (2023/1230/AB), 2006/42/AT'ye dayanan eski yönetmeliği yürürlükten kaldırıyor; hükümlerin büyük kısmı 20 Ocak 2027'de yürürlüğe giriyor [6]. Yönetmelik yüksek riskli yapay zekâ sistemlerine ve siber güvenlik belgelendirmesine de atıf yapıyor [6]. AB tarafında EU-OSHA, yeni tüzüğün otonom mobil makineler (robotlar), bağlantılı ekipman ve güvenlik işlevini öğrenen yapay zekâ modüllerini daha iyi kapsamayı amaçladığını belirtiyor [5].

IFR verisini aktaran AA haberine göre Türkiye'nin endüstriyel robot tablosu şöyle [7]:

| Gösterge (2025) | Türkiye |
|---|---|
| Yeni endüstriyel robot kurulumu | 3.194 (yıllık %9 düşüş) |
| Fabrikalardaki aktif robot stoku | 30.990 (tüm zamanların en yükseği, dünyada 15. sıra) |
| Robot yoğunluğu (imalat, 10 bin çalışan başına) | 52 (otomotivde 374) |
| Yeni robotların uygulama alanı | %59 taşıma ve yerleştirme, %16 kaynak |
| En büyük alıcı sektör | Metal (%31 pay, 990 kurulum) |

Alıntılanabilir istatistik: **Türkiye'de 2025'te kurulan yeni endüstriyel robotların %59'u taşıma ve yerleştirme işinde; imalatta 10 bin çalışana yalnızca 52 robot düşüyor** [7]. Malzeme akışının otomasyonu büyüdükçe, robot kolların arasındaki yükü taşıyan AMR'lerin güvenlik onayı da daha sık gündeme gelecek.

## Güvenlik yalnızca fiziksel değil

Kaspersky'nin depo güvenliği makalesi, AGV ve AMR'lerin de saldırı hedefi olabileceğini, örneğin navigasyonlarının etkilenerek hedefe ulaşmalarının engellenebileceğini yazıyor; kontrol kanalını kaybeden bir AGV'nin güvenli tepkisi yerinde durmak olabilir ve duran bir makine bütün bir güzergâhı kapatabilir [8]. Bu yüzden AMR projelerinde iş güvenliği ve siber güvenlik ekiplerinin aynı masada olması gerekiyor.

Simülasyon ve dijital ikiz yaklaşımını [Unilever'in 40 fabrikaya yayılan dijital ikiz örneğinde](/uretimde-dijital-ikiz-unilever-40-fabrika/), fabrika verisinin yapay zekâyla yönetimini [Ford Otosan APEM yazımızda](/ford-otosan-mega-ai-apem-fabrika-enerji/), depoda robot ve yazılımın birlikte çalışmasını da [tedarik zincirinde yapay zekâ ajanları yazımızda](/tedarik-zinciri-yapay-zeka-ajanlari-depo-dijital-isci/) incelemiştik. Depo cihazlarının siber riskleri için [barkod okuyucu güvenliği yazımıza](/barkod-okuyucu-guvenligi-depo-siber-saldiri/) bakabilirsiniz.

## Kontrol listesi: Otonom mobil robot projesine başlamadan önce

- [ ] Araç tipi netleşti mi: sabit güzergâhlı AGV mi, kendi yolunu bulan AMR mi?
- [ ] Tedarikçi ISO 3691-4 uygunluğunu ve doğrulama kayıtlarını sunuyor mu?
- [ ] Çalışma alanı (zemin, koridor genişliği, karma kullanım ve yaya alanları) robot gelmeden değerlendirildi mi?
- [ ] Yerleşim ve filo davranışı simülasyonla veya dijital ikizle test edildi mi?
- [ ] Çalışanların AMR'ler arasında sıkışma senaryosu risk analizinde var mı?
- [ ] Sahaya özgü koşullar (yük, hız, zemin, aydınlatma) kabul testine yazıldı mı?
- [ ] 20 Ocak 2027 sonrası piyasaya arz edilecek makineler için yeni yönetmelik takvimi planlandı mı?
- [ ] Robot filosunun ağ bağlantısı OT güvenliği kapsamında mı; kontrol kanalı kesilirse ne olacağı tanımlı mı?
- [ ] İş güvenliği uzmanı, bakım ve BT güvenliği ekipleri proje ekibinde mi?

## Sıkça sorulan sorular

### Otonom mobil robot (AMR) nedir?

Kendi kontrolüyle hareket edebilen, sabit bir güzergâha bağlı olmayan mobil robottur. IFR, AMR'leri endüstriyel ortamda kullanılsalar da profesyonel hizmet robotu olarak sınıflandırıyor [4].

### AGV ile AMR arasındaki fark nedir?

AGV işaretçi veya dış komutla belirlenmiş yolu izler ve IFR'ye göre robot değil robotik cihazdır; AMR ise kendi kontrolüyle hareket eder [4]. İkisi de ISO 3691-4 kapsamındadır [3].

### AMR'ler için hangi güvenlik standardı geçerli?

Sürücüsüz endüstriyel araçlar ve sistemleri için güvenlik gereklilikleri ve doğrulama yöntemlerini tanımlayan ISO 3691-4:2023 [3].

### Türkiye'de yeni Makine Emniyeti Yönetmeliği ne zaman yürürlüğe giriyor?

16 Ekim 2026'da Resmî Gazete'de yayımlanan 2023/1230/AB uyumlu yönetmeliğin hükümlerinin büyük kısmı 20 Ocak 2027'de yürürlüğe giriyor [6].

### Simülasyonla sertifikasyon ne kazandırır?

TÜV SÜD, Physical AI Safety Suite konseptindeki dijital sürecin üretimi %30'a kadar daha erken devreye alabileceğini tahmin ediyor; sertifikasyon sorumluluğu yine bağımsız kuruluşta kalıyor [1].

## Kaynaklar

1. Accenture Newsroom, "TÜV SÜD and Accenture Accelerate Certification of Physical AI in Automated Factories and Warehouses with NVIDIA Technologies to Drive Manufacturing Productivity", 21 Ekim 2026. <https://newsroom.accenture.com/news/2026/tuv-sud-and-accenture-accelerate-certification-of-physical-ai-in-automated-factories-and-warehouses-with-nvidia-technologies-to-drive-manufacturing-productivity> (Erişim: 22 Ekim 2026)
2. DC Velocity, "Accenture collaboration will speed up rollout of AMRs in factories and warehouses", 21 Ekim 2026. <https://www.dcvelocity.com/material-handling/robotics/accenture-collaboration-will-speed-up-rollout-of-amrs-in-factories-and-warehouses> (Erişim: 22 Ekim 2026)
3. ISO, "ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems". <https://www.iso.org/standard/83545.html> (Erişim: 22 Ekim 2026)
4. International Federation of Robotics, "Introduction into service robotics: Definitions" (World Robotics Service Robots 2021). <https://ifr.org/img/worldrobotics/Definitions_WR_Service_Robots_2021.pdf> (Erişim: 22 Ekim 2026)
5. EU-OSHA, "Regulation 2023/1230/EU - machinery". <https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery> (Erişim: 22 Ekim 2026)
6. Resmî Gazete, Sanayi ve Teknoloji Bakanlığı, "Makine Emniyeti Yönetmeliği (2023/1230/AB)", 16 Ekim 2026, Sayı: 33402. <https://www.resmigazete.gov.tr/eskiler/2026/10/20261016-12.htm> (Erişim: 22 Ekim 2026)
7. Dünya Gazetesi (Kaynak: AA), "Türkiye'nin fabrikalarında tarihi rekor: Sayıları 30 bini aştı" (IFR World Robotics verisi), 2 Ekim 2026. <https://www.dunya.com/sektorler/bilim-ve-teknoloji/turkiyenin-fabrikalarinda-tarihi-rekor-sayilari-30-bini-asti-haberi-842311> (Erişim: 22 Ekim 2026)
8. Securelist (Kaspersky), Sergey Sidorov, Haidar Kabibo ve Victor Zvarykin, "The journey of a paper unicorn: adventures inside a modern warehouse", 20 Ekim 2026. <https://securelist.com/paper-unicorn-warehouse-security/121537/> (Erişim: 22 Ekim 2026)
