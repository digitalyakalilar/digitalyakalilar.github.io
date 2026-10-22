---
title: Barkod okuyucu güvenliği: Depoda kablosuz okuyucu, el terminali ve yazıcı nasıl giriş kapısı olur?
date: 2026-10-22
updated: 2026-10-22
description: Kaspersky, kablosuz barkod okuyucuların baz istasyonu üzerinden depo bilgisayarına sahte tuş vuruşu gönderilebildiğini gösterdi. Barkod okuyucu güvenliği neden WMS güvenliğinin ilk halkası ve depo yöneticileri neyi kontrol etmeli?
cover_title: Barkod okuyucu güvenliği
cover_icon: scanner
category: lojistik-nakliyat
seo_title: Barkod okuyucu güvenliği: Depoda Bluetooth saldırı riski
meta_description: Barkod okuyucu güvenliği depo için kritik: Kaspersky, kablosuz okuyucuyla WMS bilgisayarına sahte tuş vuruşu gönderilebildiğini gösterdi. Tablo ve 10 adım.
focus_kw: barkod okuyucu güvenliği
keywords: barkod okuyucu güvenliği, kablosuz barkod okuyucu, el terminali güvenliği, depo siber güvenliği, WMS güvenliği, Bluetooth saldırısı, CVE-2026-4272
cover_alt: Barkod okuyucu güvenliği: Depoda kablosuz barkod okuyucu, el terminali ve WMS siber saldırı riski kapak görseli
---
Depoda her gün binlerce kez tetiğe basılan el tipi okuyucu, çoğu şirketin güvenlik envanterinde yer almıyor bile. Kaspersky'nin 20 Ekim 2026'da paylaştığı araştırma bu körlüğün bedelini gösteriyor: Kablosuz bir barkod okuyucunun baz istasyonu, Bluetooth menzilindeki bir saldırganın bağlı bilgisayara sahte klavye girişi göndermesine izin verebiliyor [1][3]. Bu yazıda **barkod okuyucu güvenliği** konusunu, aynı araştırmadaki el terminali, termal yazıcı ve WMS bulgularıyla birlikte depo ve lojistik ekipleri için derledik.

## Barkod okuyucu güvenliği neden gündemde?

Kaspersky Security Services ekibi, bir deponun dijital ekosistemine yönelik güvenlik denetimi sırasında büyük bir üreticinin barkod okuyucu modelinde yeni bir saldırı yolu buldu; bulgular Bali'deki Security Analyst Summit 2026'da paylaşıldı [1]. Tipik kurulumda el tipi okuyucu bir baz istasyonuyla konuşuyor, baz istasyonu da bir iş istasyonuna veya iş sistemine bağlanıyor. Temel zayıflık, baz istasyonu ile okuyucular arasında kimlik doğrulama olmaması [1].

Saldırı senaryosu şöyle: Çalışan okuyucuyla normal işini yaparken saldırgan, örneğin Bluetooth trafiğini pasif olarak dinleyerek baz istasyonunun Bluetooth adresini öğreniyor. Ardından baz istasyonuna klavye tuş vuruşlarını taklit eden bir veri yükü gönderiyor; baz istasyonu bunları bilgisayara iletiyor, bilgisayar da meşru kullanıcı girişi sanıyor [1]. Kaspersky'ye göre bu yol kullanıcı müdahalesi gerekmeden uzaktan kod çalıştırmaya varabiliyor ve aynı saldırı deseni birden fazla üreticinin cihazında gözlendi [1].

Kaspersky'nin teknik makalesi bir örneği adıyla veriyor: CVE-2026-4272 açığından etkilenen Honeywell cihazları [3]. ABD Ulusal Güvenlik Açığı Veritabanı'na (NVD) göre açık 5 Nisan 2026'da yayımlandı, Honeywell tarafından CVSS 3.1 ölçeğinde 8,1 (yüksek) puanlandı ve baz istasyonuna Bluetooth menzilindeki bir saldırganın bağlı bilgisayarda kimlik doğrulama olmadan sistem komutu çalıştırabilmesine yol açıyor [4]. Honeywell, düzeltilmiş ürün yazılımı sürümlerine güncellemeyi öneriyor [4].

## Okuyucu yalnızca giriş kapısı: Asıl hedef WMS

Kaspersky Endüstriyel Güvenlik Hizmetleri Başkanı Sergey Sidorov'a göre modern lojistikte kurumsal yönetim platformlarından çalışanın elindeki cihaza kadar her katman bir saldırı giriş noktası olabilir; araştırma bunun tek bir barkod okuyucu bile olabileceğini gösteriyor [2][5]. Önemli olan okuyucunun kendisi değil, bağlandığı bilgisayarın depo içindeki güvenilir konumu [1].

Securelist'teki makaleye göre depo yönetim sistemi (WMS), mal kabulden sevkiyata sekiz aşamanın tamamını koordine ediyor ve bu yüzden "deponun işletim sistemine" daha yakın [3]. WMS'teki bir kaydı değiştirebilen saldırgan stok miktarlarını, raf adreslerini, toplama görevlerini veya sevkiyat bilgisini bozabiliyor; ilk aşamadaki sahte bir kayıt sonraki tüm aşamalara miras kalıyor [3]. Makale, siber olayların depo operasyonlarını gerçekten durdurduğunu hatırlatmak için Morrisons'taki WMS kesintisini, UNFI'nin sipariş karşılamayı etkileyen olayını ve Avrupa'da sekiz CEVA Logistics deposunu etkilediği bildirilen saldırıyı örnek veriyor [3].

## Depodaki cihazlar ve saldırı yolları

Aşağıdaki tablo Kaspersky'nin depo denetiminde tarif ettiği giriş noktalarını ve ilgili kontrolleri özetliyor:

| Cihaz / alan | Tarif edilen saldırı yolu | Öne çıkan kontrol |
|---|---|---|
| Kablosuz barkod okuyucu + baz istasyonu | Bluetooth üzerinden sahte tuş vuruşu; bağlı bilgisayarda komut [1][3] | Ürün yazılımı güncellemesi, kullanılmayan Bluetooth'u kapatma [2][4] |
| Okutulan barkod / QR kod | Okuyucu klavye gibi davrandığı için kötü amaçlı barkodla tuş vuruşu enjeksiyonu [3] | Okuyucunun bağlı olduğu bilgisayarda en az yetki [2] |
| El terminali (Android, kiosk modu) | Kiosk modundan kaçış; Wi-Fi şifresinin açığa çıkması veya zararlı yazılım kurulumu [3] | Cihaz yönetimi, cihazın düzenli güvenlik değerlendirmesi [3] |
| Mobil termal yazıcı | Securelist örneğinde (Zebra ZQ630) eşleştirme yapılandırma hatasıyla Bluetooth üzerinden uygulama yükleme [3] | Eşleştirme ayarlarının sıkılaştırılması, uç nokta güvenliğine dahil etme [3] |
| Raf arkasındaki ağ prizleri, kameralar | Sökülen bir kameranın bıraktığı aktif port; kullanılmayan prizler [3] | Port güvenliği, IEEE 802.1X ve EAP-TLS ile cihaz kimlik doğrulama [3] |
| WMS (web tabanlı) | Yetki atlatma ve web açıklarıyla stok, görev ve sevkiyat kayıtlarının değiştirilmesi [3] | Ağ segmentasyonu, yama yönetimi, en az yetki [2][3] |

Alıntılanabilir bulgu: **Kaspersky'ye göre baz istasyonu ile kablosuz barkod okuyucu arasında kimlik doğrulama yok; menzildeki bir saldırgan bağlı bilgisayara kullanıcı müdahalesi olmadan tuş vuruşu gönderebiliyor** [1].

## Saldırgan nerede durur? Otopark da depo ağına dahil

Securelist makalesi tehdit aktörlerini ikiye ayırıyor: Depoyla meşru ilişkisi olmayan dış aktörler ve çalışan, yüklenici veya geçici personel gibi meşru erişimi olan iç aktörler. Dış aktörlerin bir alt türü "yakındaki" saldırgan: Otoparkta, komşu bir birimde veya yükleme rampasında durup Wi-Fi, Bluetooth gibi kısa menzilli arayüzlere hesap ya da kart olmadan ulaşabilen kişi [3]. Makaleye göre radyo dalgaları pencerelerden, kapılardan ve ince dış panellerden geçtiği için yönlü bir antenle depo ağına çok daha uzaktan da erişilebiliyor [3].

Makale bir İK notu da düşüyor: Ayıklama, paketleme ve kurye rolleri hızlı ve toplu işe alımla dolduruluyor; dışarıdan gelen biri birkaç gün içinde tesise meşru fiziksel erişim kazanabiliyor. Bu nedenle hassas alanlara erişen roller için daha risk odaklı bir işe alım yaklaşımı öneriliyor [3].

## Ne yapmalı? Kaspersky'nin önerileri

Kaspersky depo ortamları için şu adımları öneriyor: Her yeni cihazı ağa bağlanmadan önce doğrulamak, kullanılmayan Bluetooth arayüzlerini kapatmak ve güçlü kimlik doğrulama uygulamak, depo ağlarını yalnızca gerekli bağlantılara izin verecek şekilde bölümlere ayırmak, hem cihazlara hem WMS'e güncellemeleri hızla uygulamak, hesap yetkilerini gereken en aza indirmek ve meşru kimlik bilgilerine sahip iç aktör senaryolarını içeren düzenli saldırı yolu tatbikatları yapmak [2][5]. Teknik makale bunlara radyo frekansı taraması ve depo cihazlarının uç nokta güvenliği ve açık yönetimi süreçlerine dahil edilmesini ekliyor [3].

Bluetooth'un kurumsal kullanımına dair genel çerçeve için ABD standart kurumu NIST'in Bluetooth güvenliği rehberi (SP 800-121 Rev. 2), Bluetooth'un güvenlik yeteneklerini ve kuruluşlar için önerileri bir arada sunuyor [6].

Depo operasyonunda yapay zekâ ve otomasyonun nereye gittiğini [tedarik zincirinde yapay zekâ ajanları yazımızda](/tedarik-zinciri-yapay-zeka-ajanlari-depo-dijital-isci/), taşımacılıkta yazılım tarafını [lojistikte yapay zekâ uygulamaları yazımızda](/lojistikte-yapay-zeka-uygulamalari-fatura-denetimi/) inceledik. Üretim tarafında BT ile OT'nin buluştuğu katmanı [Kardemir Seviye 3 MES örneğinde](/kardemir-seviye-3-mes-isa-95/), çalışanı kendi eliyle komut çalıştırmaya ikna eden saldırıları da [ClickFix saldırısı rehberimizde](/clickfix-saldirisi-sahte-captcha-korunma/) ele aldık.

## Kontrol listesi: Depo için barkod okuyucu güvenliği

- [ ] Depodaki tüm kablosuz okuyucuların baz istasyonu modeli ve ürün yazılımı sürümü envanterde var mı? (Yalnızca el cihazı değil, baz istasyonu da)
- [ ] Honeywell baz istasyonları kullanılıyorsa sürümler CVE-2026-4272 düzeltmesini içeriyor mu? [4]
- [ ] Kullanılmayan Bluetooth arayüzleri okuyucu, yazıcı ve terminallerde kapatıldı mı?
- [ ] Okuyucunun bağlı olduğu bilgisayar standart kullanıcı yetkisiyle mi çalışıyor?
- [ ] Depo OT ağı, kurumsal BT ağından ve misafir Wi-Fi'dan ayrılmış mı?
- [ ] Yeni cihazlar ağa bağlanmadan önce onay sürecinden geçiyor mu?
- [ ] Kullanılmayan ağ prizleri ve kamera portları kapatıldı, 802.1X değerlendirildi mi?
- [ ] El terminallerinin kiosk modu ve cihaz yönetimi düzenli test ediliyor mu?
- [ ] WMS ve entegrasyonları yama takvimine dahil mi?
- [ ] Yılda en az bir kez otopark senaryosunu da içeren saldırı yolu tatbikatı yapılıyor mu?

## Sıkça sorulan sorular

### Barkod okuyucu hacklenebilir mi?

Kaspersky'nin araştırmasına göre bazı kablosuz modellerde baz istasyonu ile okuyucu arasında kimlik doğrulama olmadığı için Bluetooth menzilindeki bir saldırgan bağlı bilgisayara sahte tuş vuruşu gönderebiliyor [1].

### CVE-2026-4272 nedir?

Honeywell el tipi okuyucuların bazı baz istasyonlarını etkileyen, kritik bir işlev için kimlik doğrulama eksikliği açığıdır. NVD'ye göre Bluetooth menzilindeki bir saldırgan bağlı bilgisayarda komut çalıştırabilir; Honeywell düzeltilmiş sürüme güncellemeyi öneriyor [4].

### Saldırganın depoya girmesi gerekiyor mu?

Hayır. Kaspersky'nin tehdit modelinde otoparkta veya yükleme rampasında duran "yakındaki" bir saldırgan Bluetooth ve Wi-Fi gibi kısa menzilli arayüzlere ulaşabiliyor [3].

### Depoda en kritik sistem hangisi?

Kaspersky'ye göre WMS; tüm aşamaları koordine ettiği için ele geçirilmesi stok, görev ve sevkiyat kayıtlarının bozulmasına ve operasyonun durmasına yol açabilir [3].

### İlk adım ne olmalı?

Baz istasyonları dahil tüm okuyucu, terminal ve yazıcıların model ve ürün yazılımı envanterini çıkarmak, ardından güncelleme ve kullanılmayan Bluetooth'u kapatma adımlarını uygulamak [2][4].

## Kaynaklar

1. Kaspersky Türkiye, "Kaspersky, barkod okuyuculardaki güvenlik açıklarını tespit etti: Depo sektörü siber saldırı riskiyle karşı karşıya", 20 Ekim 2026. <https://www.kaspersky.com.tr/about/press-releases/kaspersky-barkod-okuyuculardaki-guvenlik-aciklarini-tespit-etti-depo-sektoru-siber-saldiri-riskiyle-karsi-karsiya> (Erişim: 22 Ekim 2026)
2. Kaspersky, "Your order is delayed: Kaspersky identifies vulnerabilities in barcode scanners, posing potential threat for the warehouse industry", 20 Ekim 2026. <https://www.kaspersky.com/about/press-releases/your-order-is-delayed-kaspersky-identifies-vulnerabilities-in-barcode-scanners-posing-potential-threat-for-the-warehouse-industry> (Erişim: 22 Ekim 2026)
3. Securelist (Kaspersky), Sergey Sidorov, Haidar Kabibo ve Victor Zvarykin, "The journey of a paper unicorn: adventures inside a modern warehouse", 20 Ekim 2026. <https://securelist.com/paper-unicorn-warehouse-security/121537/> (Erişim: 22 Ekim 2026)
4. NIST National Vulnerability Database, "CVE-2026-4272". <https://nvd.nist.gov/vuln/detail/CVE-2026-4272> (Erişim: 22 Ekim 2026)
5. DC Velocity, "Kaspersky: Hackers could access warehouse software through wireless barcode scanners", 20 Ekim 2026. <https://www.dcvelocity.com/technology/warehouse-it/kaspersky-hackers-could-access-warehouse-software-through-wireless-barcode-scanners> (Erişim: 22 Ekim 2026)
6. NIST, John Padgette vd., "SP 800-121 Rev. 2, Guide to Bluetooth Security" (Ocak 2022 güncellemesi dahil). <https://csrc.nist.gov/pubs/sp/800/121/r2/upd1/final> (Erişim: 22 Ekim 2026)
