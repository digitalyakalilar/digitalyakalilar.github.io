---
title: Endüstriyel kontrol sistemlerinin siber güvenliği: Bir YZ ajanı 4 saatte 4 ciddi açık buldu, fabrikalar ne yapmalı?
date: 2026-10-28
updated: 2026-10-28
description: Otonom bir yapay zekâ ajanı, parçacık hızlandırıcılarını yöneten EPICS yazılımında 3 saat 49 dakikada dört ciddi açık buldu. Endüstriyel kontrol sistemlerinin siber güvenliği için OT zafiyet yönetimi tablosu, Türkiye verisi ve kontrol listesi.
cover_title: Endüstriyel kontrol sistemlerinin siber güvenliği
cover_icon: ot
category: endustri-4-0
seo_title: Endüstriyel kontrol sistemlerinin siber güvenliği ve YZ
meta_description: Endüstriyel kontrol sistemlerinin siber güvenliği: YZ ajanı EPICS'te 4 saatte 4 açık buldu. OT zafiyet yönetimi tablosu, Türkiye verisi ve kontrol listesi.
focus_kw: endüstriyel kontrol sistemlerinin siber güvenliği
keywords: endüstriyel kontrol sistemlerinin siber güvenliği, OT güvenliği, SCADA güvenliği, OT zafiyet yönetimi, ağ segmentasyonu, CISA ICS bildirimi, EPICS, yapay zekâ ile zafiyet tespiti
cover_alt: Endüstriyel kontrol sistemlerinin siber güvenliği: ayrılmış ağ bölgeleri ve kalkanla korunan kontrol paneli kapak görseli
---
Yıllarca "kimse bu eski kontrol yazılımını incelemez" varsayımıyla korunan fabrika ve tesis sistemleri için kötü bir haber var. The Register'ın 27 Ekim'de aktardığına göre otonom bir yapay zekâ ajanı, dünyanın büyük bilim tesislerinde kullanılan açık kaynaklı EPICS kontrol yazılımında dört ciddi açığı yalnızca 3 saat 49 dakikada buldu ve doğruladı [1]. Aynı gün ABD Siber Güvenlik ve Altyapı Güvenliği Ajansı (CISA) bir endüstriyel kontrol sistemi bildirimi yayımladı [2]. Bu yazıda olayın **endüstriyel kontrol sistemlerinin siber güvenliği** için ne anlama geldiğini ve fabrikaların atabileceği somut adımları ele alıyoruz.

## Ne oldu? EPICS'te dört açık, düzeltme 7.0.11'de

EPICS (Experimental Physics and Industrial Control System), Los Alamos ve Argonne ulusal laboratuvarlarında geliştirilmiş, dağıtık SCADA sistemleri kurmak ve fiziksel cihazları uzaktan yönetmek için kullanılan bir yazılım çatısı. The Register'a göre dünya genelinde yaklaşık 90 büyük bilimsel, üniversite ve endüstriyel projede kullanılıyor [1].

| CVE | CVSS v3.1 | Tür | Olası etki |
|---|---|---|---|
| CVE-2026-114595 | 9,8 (kritik) | Tamsayı taşması → yığın dışı yazma | Uzaktan kod çalıştırma potansiyeli |
| CVE-2026-114596 | 8,2 (yüksek) | Mesaj uzunluğu doğrulama hatası | Bellek yazma, kontrol sürecinin çökmesi |
| CVE-2026-114597 | 7,5 (yüksek) | Yetersiz sınır kontrolü | Bellek okuma, süreç çökmesi |
| CVE-2026-114598 | 7,5 (yüksek) | Tür karışıklığı | Hizmet engelleme, bitişik bellek ifşası |

Kaynak: The Register [1], CISA ICSA-26-300-01 [2]. Etkilenen sürümler EPICS Base 7.0.10 ve öncesi; düzeltmeler 7.0.11 sürümünde [2][3].

CISA'ya göre açıkların başarılı istismarı hizmet engelleme, bellek bozulması, hassas bilgi ifşası ya da potansiyel olarak keyfi kod çalıştırma ile sonuçlanabilir [2]. Bildirim, sektör olarak "Kritik İmalat"ı işaretliyor [2].

Alıntılanabilir istatistik: **Causal Security'nin "Cipher" adlı YZ ajanı, daha önce tanımadığı EPICS sisteminde dört bilinmeyen açığı bulup istismar edilebilirliğini 3 saat 49 dakikada doğruladı** [1].

## Asıl ders: "Gizlilikle güvenlik" dönemi bitiyor

Causal Security kurucu ortağı Shubham Raj, ilk incelemenin insan müdahalesi olmadan yapıldığını; yalnızca derin istismar testleri için güvenli bir ortamda tek bir onay verildiğini söylüyor [1]. Raj'a göre bu açıkları istismar etmek için parçacık fiziği ya da derin OT bilgisi gerekmiyor; geleneksel istismar becerisi olan biri, giderek yetenekli YZ sistemlerinin yardımıyla bunu yapabilir [1].

The Register'ın değerlendirmesi de aynı yönde: Bu bulgular, YZ ajanlarının eskiden "bilinmezlik" sayesinde korunan endüstriyel ve operasyonel teknoloji (OT) sistemlerinde açık bulmakta ne kadar iyi olduğunu gösteriyor [1]. Yani saldırgan tarafında açık bulma maliyeti düşüyor; savunma tarafında yama ve segmentasyon temposu artmak zorunda.

İyi haber şu: Bu açıkları gerçek bir tesiste istismar etmenin ön koşulu, kontrol ağındaki EPICS servislerine ulaşabilmek. Bu da ağlar yeterince ayrılmamışsa ya da başka bir sistem bu ağa erişebiliyorsa mümkün oluyor [1]. Ağ segmentasyonu hâlâ en güçlü kalkan.

## Tek örnek değil: Aynı hafta başka ICS bildirimleri

CISA, EPICS bildirimiyle aynı gün Mitsubishi Electric'in GENESIS, ICONICS Suite ve MC Works64 gibi SCADA/HMI ürünleri için de ayrı bir bildirim (ICSA-26-300-02) yayımladı; bu bildirimde kimlik doğrulamanın atlatılması ve keyfi kod çalıştırma riskleri sayılıyor [4]. Fabrikalar için gerçek iş, tek bir açığı kapatmak değil, bu bildirim akışını düzenli bir süreçle yönetmek.

CISA'ya göre EPICS açıklarının kamuya açık şekilde istismar edildiğine dair bir bildirim henüz yok; ajans ayrıca savunma önlemlerini devreye almadan önce etki analizi ve risk değerlendirmesi yapılmasını hatırlatıyor [2]. OT'de aceleyle yapılan bir değişiklik de üretimi durdurabilir.

## Türkiye için okuma

Türkiye'ye özgü en güncel kamuya açık veri biraz eski: Kaspersky'nin 2023'ün ilk yarısına ait verilerine göre Türkiye'de ICS bilgisayarlarının %41,9'unda kötü amaçlı nesne engellendi; dünya ortalaması %34'tü [5]. Kaspersky ICS CERT'in 2026 ikinci çeyrek raporuna göre ise küresel oran 2022'den bu yana en düşük seviyeye inerken, fidye yazılımlarının hedef aldığı ICS bilgisayarlarının sayısı Orta Doğu'da çeyrekten çeyreğe %11 arttı [6]. Kaspersky uzmanları düzenli güvenlik değerlendirmesi, zafiyetlerin önceliklendirilmesi, kritik bileşenlerin zamanında güncellenmesi ve BT ile OT personelinin eğitimini öneriyor [6].

Fabrikada tarayıcı, robot ve MES gibi bileşenlerin güvenliğini daha önce [barkod okuyucu güvenliği](/barkod-okuyucu-guvenligi-depo-siber-saldiri/) ve [ISA-95 ile seviye 3 MES](/kardemir-seviye-3-mes-isa-95/) yazılarımızda ele almıştık. ISA-95'in seviye modeli, aşağıdaki segmentasyon adımları için de doğal bir harita sunuyor.

## OT zafiyet yönetimi: BT yaması ile farkı

| Boyut | Kurumsal BT | OT / endüstriyel kontrol |
|---|---|---|
| Öncelik | Gizlilik | Erişilebilirlik ve fiziksel güvenlik |
| Yama penceresi | Haftalık / aylık | Planlı duruşlar, bazen yılda birkaç kez |
| Test | Otomatik dağıtım yaygın | Üretici onayı ve test ortamı şart |
| Telafi edici kontrol | Daha az gerekli | Segmentasyon, erişim kısıtlama, izleme çoğu zaman ilk savunma |
| Envanter | Ajan tabanlı tarama | Pasif keşif; aktif tarama riskli olabilir |

Tablo, CISA'nın ağ maruziyetini azaltma ve izolasyon önerileri [2] ile Kaspersky'nin önerileri [6] temel alınarak tarafımızca derlenmiştir.

## Endüstriyel kontrol sistemlerinin siber güvenliği: 10 maddelik kontrol listesi

- [ ] Tüm kontrol sistemi cihaz ve yazılımlarının sürümlü envanterini çıkarın (EPICS, SCADA, HMI, PLC yazılımları)
- [ ] EPICS kullanıyorsanız 7.0.11'e yükseltin; kullanmıyorsanız CISA ICS bildirimlerini haftalık takip edin [2][3][4]
- [ ] Kontrol ağını internetten ve iş ağından ayırın, güvenlik duvarının arkasına alın [2]
- [ ] Uzaktan erişim gerekiyorsa VPN gibi güvenli yöntemler kullanın ve VPN'i en güncel sürümde tutun [2]
- [ ] Kontrol ağına erişebilen her BT sistemini listeleyin; gereksiz yolları kapatın [1]
- [ ] Yama yapılamayan sistemler için telafi edici kontrol tanımlayın (erişim listesi, izleme)
- [ ] Zafiyetleri CVSS'in yanında istismar edilebilirlik ve üretime etkiye göre önceliklendirin [6]
- [ ] Planlı duruş takvimine yama pencereleri ekleyin
- [ ] BT ve OT ekiplerine ortak eğitim ve tatbikat planlayın [6]
- [ ] Fidye yazılımı senaryosu için çevrimdışı yedek ve geri dönüş planı hazırlayın [6]

Eski Windows sunucuları da OT ağlarında sık görülen bir risk; bkz. [Windows Server 2016 destek sonu](/windows-server-2016-destek-sonu-gecis-rehberi/).

## Sıkça sorulan sorular

### Endüstriyel kontrol sistemlerinin siber güvenliği neden zor?

OT sistemlerinde öncelik kesintisiz çalışma ve fiziksel güvenlik; yama ancak planlı duruşlarda ve üretici onayıyla yapılabiliyor. Bu yüzden segmentasyon ve erişim kısıtlama genellikle ilk savunma hattı [2].

### EPICS açıkları hangi sürümü etkiliyor?

CISA'ya göre EPICS Base 7.0.10 ve öncesi etkileniyor; düzeltmeler 7.0.11'de [2][3].

### Yapay zekâ OT sistemlerinde açık bulabiliyor mu?

Evet. Causal Security'nin Cipher ajanı EPICS'te dört açığı 3 saat 49 dakikada buldu ve doğruladı [1].

### Açığı istismar etmek için ne gerekiyor?

The Register'a göre saldırganın kontrol ağındaki EPICS servislerine ulaşması gerekiyor; yetersiz segmentasyon bu yolu açabiliyor [1].

### Türkiye'de endüstriyel sistemler ne kadar hedefte?

Kaspersky'nin 2023 ilk yarı verisine göre Türkiye'de ICS bilgisayarlarının %41,9'unda kötü amaçlı nesne engellendi (dünya: %34) [5]. Daha güncel Türkiye'ye özgü kamuya açık veri bulamadık.

## Kaynaklar

1. The Register, Jessica Lyons, "AI 'hacker' finds 4 severe bugs in popular industrial control software in under 4 hours", 27 Ekim 2026. <https://www.theregister.com/security/2026/10/27/ai-hacker-finds-4-severe-bugs-in-popular-industrial-control-software-in-under-4-hours/5305811> (Erişim: 28 Ekim 2026)
2. CISA, "ICSA-26-300-01: EPICS Base", 27 Ekim 2026. <https://www.cisa.gov/news-events/ics-advisories/icsa-26-300-01> (Erişim: 28 Ekim 2026)
3. GitHub, epics-base/epics-base, sürüm notları (7.0.11). <https://github.com/epics-base/epics-base/releases> (Erişim: 28 Ekim 2026)
4. CISA, "ICSA-26-300-02: Mitsubishi Electric GENESIS, GENESIS64, ICONICS Suite ve diğerleri", 27 Ekim 2026. <https://www.cisa.gov/news-events/ics-advisories/icsa-26-300-02> (Erişim: 28 Ekim 2026)
5. Kaspersky Türkiye, "Türkiye, 2023'ün ilk yarısında endüstriyel kontrol sistemleri en fazla saldırıya uğrayan bölgeler arasında" (basın bülteni). <https://www.kaspersky.com.tr/about/press-releases/turkiye-2023un-ilk-yarisinda-endustriyel-kontrol-sistemleri-en-fazla-saldiriya-ugrayan-bolgeler-arasinda> (Erişim: 28 Ekim 2026)
6. Anadolu Ajansı, Sibel Morrow, "Kaspersky 'Endüstriyel Otomasyon Sistemlerine Yönelik Tehdit Ortamı' raporunu paylaştı", 26 Ağustos 2026. <https://www.aa.com.tr/tr/isdunyasi/bilisim/kaspersky-endustriyel-otomasyon-sistemlerine-yonelik-tehdit-ortami-raporunu-paylasti/704086> (Erişim: 28 Ekim 2026)
