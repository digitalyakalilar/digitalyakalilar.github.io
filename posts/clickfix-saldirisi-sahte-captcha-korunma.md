---
title: ClickFix saldırısı nedir? Sahte CAPTCHA tuzağına karşı kurumsal korunma rehberi
date: 2026-10-22
updated: 2026-10-22
description: Sahte bir "Ben robot değilim" kutusu, çalışana komutu kendi eliyle çalıştırtıyor. Google Chrome'a ClickFix koruması geldi, Huntress yeni bir kampanyayı belgeledi. ClickFix saldırısı nasıl işliyor, şirketler neyi kapatmalı?
cover_title: ClickFix saldırısı: sahte CAPTCHA
cover_icon: captcha
category: dijital-guvenlik
seo_title: ClickFix saldırısı nedir? Sahte CAPTCHA'ya karşı korunma
meta_description: ClickFix saldırısı sahte CAPTCHA ile çalışana komut çalıştırtıyor; ESET'e göre %517 arttı. Chrome'un yeni koruması, Huntress vakası ve kurumsal kontrol listesi.
focus_kw: ClickFix saldırısı
keywords: ClickFix saldırısı, ClickFix nedir, sahte CAPTCHA, Win+R komutu, PowerShell, Lumma Stealer, bilgi hırsızı zararlı yazılım, Chrome Gelişmiş Koruma
cover_alt: ClickFix saldırısı: Sahte CAPTCHA ile çalıştırılan zararlı komuta karşı kurumsal korunma kapak görseli
---
Bir web sitesinde "Ben robot değilim" kutusunu işaretliyorsunuz, ardından ekranda kısa bir talimat beliriyor: Windows tuşu ile R'ye basın, Ctrl+V ile yapıştırın, Enter'a basın. İşte **ClickFix saldırısı** budur: Zararlı yazılımı indiren, saldırgan değil çalışanın kendisidir [6]. Google 20 Ekim 2026'da Chrome'a ClickFix komutlarını yakalayan bir koruma ekledi [1], güvenlik şirketi Huntress ise bir gün sonra sponsorlu Google reklamıyla başlayan yeni bir kampanyayı belgeledi [3][4]. Bu yazıda ClickFix saldırısının nasıl işlediğini, rakamlarını ve şirketlerin hangi ayarları kapatması gerektiğini kaynaklarıyla derledik.

## ClickFix saldırısı nedir?

Microsoft'un tanımıyla ClickFix, kullanıcıların küçük teknik sorunları kendi başına çözme eğiliminden ve CAPTCHA gibi zararsız görünen doğrulama adımlarından yararlanan bir sosyal mühendislik tekniği. Kullanıcıya komutu Windows Çalıştır penceresine, Windows Terminal'e veya PowerShell'e yapıştırıp çalıştırması söyleniyor [6]. Microsoft tekniği ilk kez Mart–Haziran 2024 arasında bir e-posta kampanyasında gördüğünü, bir yıl içinde her gün dünya genelinde binlerce kurumsal ve bireysel cihazı hedefleyen kampanyalara dönüştüğünü yazıyor [6]. MITRE ATT&CK de bu davranışı ayrı bir alt teknik olarak kataloglıyor: T1204.004, "Malicious Copy and Paste" [7].

Tekniği tehlikeli kılan şey, zincirin ortasında insan olması. Komutu kullanıcı çalıştırdığı için klasik ve otomatik güvenlik çözümleri atlanabiliyor [6]. Chrome tarafında da benzer bir kör nokta var: Zararlı indirme tarayıcıda değil terminalde gerçekleştiği için Chrome'un indirme korumaları devreye girmiyordu [2].

## Rakamlarla ClickFix

| Gösterge | Değer | Kaynak |
|---|---|---|
| ESET telemetrisinde artış (2024 2. yarı → 2025 1. yarı) | %517 | [5] |
| Engellenen tüm saldırılar içindeki payı (2025 1. yarı) | Yaklaşık %8; oltalamadan sonra 2. sırada | [5] |
| Huntress yönetilen EDR tespit sinyallerindeki payı (2026) | Yaklaşık %2,2; bunların %99'a yakını yüksek önem dereceli | [4] |
| Microsoft'un gözlemi | Her gün binlerce kurumsal ve bireysel cihazı hedefleyen kampanyalar | [6] |
| Satılık ClickFix kiti aboneliği | Ayda 200–1.500 dolar | [6] |
| En sık görülen son yük | Lumma Stealer (bilgi hırsızı) | [6] |

Alıntılanabilir istatistik: **ClickFix, ESET verisine göre altı ayda %517 artarak oltalamadan sonra en yaygın ikinci saldırı vektörü oldu** [5].

## Yeni vaka: "amazon business" reklamından finger.exe'ye

Huntress araştırmacılarının 21 Ekim 2026'da yayımladığı rapora göre saldırı basit bir aramayla başladı: "amazon business" anahtar kelimesindeki sponsorlu sonuç, sahte bir Amazon giriş sayfasına yönlendiriyordu [3]. Kullanıcı e-posta veya telefon numarasını girdikten sonra sahte bir CAPTCHA açılıyor, "Ben robot değilim" düğmesi panoya bir komut kopyalıyor ve kullanıcıdan bunu Çalıştır penceresine yapıştırması isteniyordu [3].

Komut, 1970'lerden kalma Windows aracı `finger`'ı çağırıyordu [4]. Huntress'e göre komut fazladan boşluk ve tirelerle gizlenmişti; kullanıcı Çalıştır kutusunda yalnızca "Enter tuşuna basın" benzeri bir ifade görüyordu [3]. Zincir sonunda Lumma Stealer'ın bir sürümünü ve uzaktan yönetim aracı NetSupport Client'ın korsan bir kopyasını kuruyordu [3][4]. Google reklamı kaldırdı, ancak araştırmacılara göre saldırgan altyapısı hâlâ çalışıyor [4].

Huntress analisti Sarah Reddish'in özeti şirketler için net: "Hiçbir meşru CAPTCHA sizden Çalıştır, PowerShell veya Komut İstemi'ne komut yapıştırmanızı istemez" [4].

## Google Chrome'un yeni ClickFix koruması ne yapıyor?

Google'ın 20 Ekim tarihli duyurusuna göre Chrome'un Gelişmiş Koruma (Enhanced Protection) modu artık kullanıcının şüpheli bir komutu kopyalamaya yönlendirildiğini fark edebiliyor. Kopyalanan içerik kişisel verilerden arındırılıp Safe Browsing'e analiz için gönderiliyor; sonuç "tehlikeli" çıkarsa Chrome uyarı gösteriyor [1]. Google sistemin geliştiricilerin meşru işini bozmamak için yüksek kesinlikle çalışacak şekilde tasarlandığını belirtiyor [1].

Aynı duyuruda iki yenilik daha var: Düşük güvenli tespitler için yeni "şüpheli site" uyarıları ve sahte antivirüs ile sahte tarayıcı güncellemesi sayfalarını da hedefleyen sunucu tarafı Gemini analizi [1]. Google, Gelişmiş Koruma'yı 2025 itibarıyla 1 milyardan fazla kullanıcının açtığını söylüyor [1].

Önemli not: ClickFix ve Gemini korumaları yalnızca Gelişmiş Koruma açıkken çalışıyor [2]. Yani şirket bilgisayarlarında bu ayar merkezi olarak açılmadıkça yeni koruma devreye girmiyor.

## Gerçek CAPTCHA mı, ClickFix tuzağı mı?

| | Gerçek CAPTCHA | ClickFix tuzağı |
|---|---|---|
| Sizden istediği | Resim seçmek, kutu işaretlemek, bulmaca sürüklemek | Win+R, Ctrl+V, Enter gibi klavye kısayolları [6] |
| Panoya ne olur? | Hiçbir şey kopyalanmaz | Arka planda bir komut kopyalanır [3][6] |
| Hangi pencere açılır? | Hiçbiri, sayfada kalırsınız | Çalıştır, Terminal veya PowerShell [6] |
| Gördüğünüz metin | Doğrulama sorusu | Çoğu zaman gerçek komutu gizleyen kısa bir ifade [3] |
| Sonuç | Siteye erişim | Bilgi hırsızı, uzaktan erişim aracı veya fidye yazılımı [5][6] |

## Şirketler hangi ayarları kapatmalı?

Microsoft ve Huntress'in önerileri birlikte okununca katmanlı bir savunma çıkıyor:

1. **Çalıştır penceresini kısıtlayın.** İşi gerektirmeyen kullanıcılarda Win+R'yi Grup İlkesi ile kapatın [6][4].
2. **Az kullanılan araçları izleyin veya engelleyin.** Huntress, `finger.exe` çalışmasına alarm kurulmasını ve giden TCP/79 trafiğinin izlenmesini ya da engellenmesini öneriyor [4].
3. **PowerShell'i görünür kılın.** Betik bloğu günlüğünü açın, AllSigned veya RemoteSigned gibi yürütme ilkeleri kullanın [6].
4. **Çok satırlı yapıştırmada uyarı verin.** Windows Terminal'de çok satırlı içerik yapıştırılırken uyarı ayarını etkinleştirin [6].
5. **Tarayıcıyı yönetin.** Kurumsal yönetilen tarayıcı kullanın ve Chrome'da Gelişmiş Koruma'yı merkezi olarak açmayı değerlendirin [6][1].
6. **Kullanıcıya tek bir kural öğretin.** Web sayfası komut yapıştırmanızı istiyorsa sayfayı kapatıp BT'ye haber verin [4].

## Türkiye'deki şirketler için KVKK boyutu

ClickFix zincirlerinin en sık son yükü olan bilgi hırsızları tarayıcıda kayıtlı şifreleri, oturum çerezlerini ve e-posta istemcisi verilerini hedefliyor [6]. Kişisel veri sızmışsa iş yalnızca teknik değil: Kişisel Verileri Koruma Kurulu'nun 2019/10 sayılı kararına göre veri sorumlusu ihlali öğrendiği andan itibaren gecikmeksizin ve en geç 72 saat içinde Kurul'a bildirmek zorunda; karar ayrıca bir veri ihlali müdahale planı hazırlanmasını da istiyor [8]. Olay müdahale planınızda "ClickFix komutu çalıştırıldı" senaryosunun, bu bildirim süresini de kapsaması gerekir.

Hesap ve cihaz güvenliğinin temelleri için [telefon ve hesap güvenliği rehberimize](/telefon-ve-hesap-guvenligi/), çalışanların kendi kurduğu araçların yarattığı risk için [gölge yapay zekâ ajanları yazımıza](/calisan-yapay-zeka-ajanlari-guvenlik-riski/), yerel komut çalıştıran yazılımların yalıtımı için de [Microsoft Execution Containers incelememize](/microsoft-execution-containers-ajan-guvenligi/) göz atabilirsiniz. Depo ve saha cihazları tarafındaki benzer "tuş vuruşu" riskini [barkod okuyucu güvenliği yazımızda](/barkod-okuyucu-guvenligi-depo-siber-saldiri/) ele aldık.

## Kontrol listesi: ClickFix saldırısına karşı 10 madde

- [ ] Çalıştır penceresine ihtiyacı olmayan kullanıcı grupları belirlendi ve Win+R kısıtlandı mı?
- [ ] `finger.exe`, `mshta` gibi nadir kullanılan araçlar için alarm veya engel kuralı var mı?
- [ ] Giden TCP/79 trafiği izleniyor veya engelleniyor mu?
- [ ] PowerShell betik bloğu günlüğü açık ve bir SIEM'e akıyor mu?
- [ ] Windows Terminal'de çok satırlı yapıştırma uyarısı açık mı?
- [ ] Şirket tarayıcıları merkezi yönetiliyor, Chrome Gelişmiş Koruma politikası değerlendirildi mi?
- [ ] Onaylanmamış uzaktan yönetim araçları (NetSupport vb.) engelleniyor mu?
- [ ] Çalışan eğitiminde "komut yapıştırtan CAPTCHA" örneği ekran görüntüsüyle gösterildi mi?
- [ ] Komutu çalıştıran çalışan için "bağlantıyı kes, BT'yi ara, şifreleri temiz cihazdan değiştir" akışı yazılı mı?
- [ ] Olay müdahale planı KVKK'nın 72 saatlik bildirim süresini içeriyor mu?

## Sıkça sorulan sorular

### ClickFix saldırısı nedir?

Kullanıcıyı sahte bir hata veya doğrulama ekranıyla kandırıp zararlı bir komutu Çalıştır penceresine, Terminal'e veya PowerShell'e kendi eliyle yapıştırıp çalıştırmaya yönlendiren bir sosyal mühendislik tekniğidir [6].

### Sahte CAPTCHA nasıl anlaşılır?

Gerçek bir CAPTCHA klavye kısayolu, Çalıştır penceresi veya komut yapıştırma istemez. Böyle bir talimat gördüğünüzde sayfa sahtedir [4][6].

### ClickFix saldırıları ne kadar yaygın?

ESET'in 2025 ilk yarı verisine göre ClickFix tespitleri %517 arttı ve engellenen saldırıların yaklaşık %8'ini oluşturarak oltalamadan sonra ikinci sıraya yükseldi [5].

### Chrome ClickFix saldırısını engelliyor mu?

Chrome'un Gelişmiş Koruma modu artık şüpheli komut kopyalamayı analiz edip tehlikeli bulursa uyarı gösteriyor. Bu koruma yalnızca Gelişmiş Koruma açıkken çalışıyor [1][2].

### Komutu çalıştırdıysam ne yapmalıyım?

Cihazın ağ bağlantısını kesin, BT veya güvenlik ekibine hemen haber verin ve şifrelerinizi temiz bir cihazdan değiştirin. Kişisel veri sızmışsa şirketin KVKK'ya 72 saat içinde bildirim yükümlülüğü doğabilir [8].

## Kaynaklar

1. Google, Jasika Bawa, "Our latest defenses against evolving web scams", 20 Ekim 2026. <https://blog.google/security/our-latest-defenses-against-evolving-web-scams/> (Erişim: 22 Ekim 2026)
2. SecurityWeek, Eduard Kovacs, "Google Hardens Chrome Against ClickFix Attacks, Insecure HTTP Connections", 21 Ekim 2026. <https://www.securityweek.com/google-hardens-chrome-against-clickfix-attacks-insecure-http-connections/> (Erişim: 22 Ekim 2026)
3. Huntress, Andrew Brandt ve Sarah Reddish, "Amazon-Themed ClickFix Campaign Serves Up Finger-Licking Malware", 21 Ekim 2026. <https://www.huntress.com/blog/amazon-clickfix-finger> (Erişim: 22 Ekim 2026)
4. Dark Reading, Elizabeth Montalbano, "Decades-Old Windows Utility Powers Modern ClickFix Attack", 21 Ekim 2026. <https://www.darkreading.com/cyberattacks-data-breaches/decades-old-windows-utility-modern-clickfix-attack> (Erişim: 22 Ekim 2026)
5. ESET, "ESET Threat Report: ClickFix fake error surges, spreads ransomware and other malware", 26 Haziran 2025. <https://www.eset.com/us/about/newsroom/research/eset-threat-report-clickfix-fake-error-surges-spreads-ransomware-and-other-malware/> (Erişim: 22 Ekim 2026)
6. Microsoft Threat Intelligence, "Think before you Click(Fix): Analyzing the ClickFix social engineering technique", 21 Ağustos 2025. <https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/> (Erişim: 22 Ekim 2026)
7. MITRE ATT&CK, "User Execution: Malicious Copy and Paste (T1204.004)". <https://attack.mitre.org/techniques/T1204/004/> (Erişim: 22 Ekim 2026)
8. Kişisel Verileri Koruma Kurumu, "Kişisel Veri İhlali Bildirim Usul ve Esaslarına İlişkin Kurulun 24.01.2019 Tarih ve 2019/10 Sayılı Kararına İlişkin Duyuru". <https://www.kvkk.gov.tr/Icerik/5362/Veri-Ihlali-Bildirimi> (Erişim: 22 Ekim 2026)
