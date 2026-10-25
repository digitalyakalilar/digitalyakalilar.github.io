---
title: Windows Server 2016 destek sonu: 12 Ocak 2027'ye kadar geçiş, ESU ve envanter rehberi
date: 2026-10-25
updated: 2026-10-25
description: Windows Server 2016 destek sonu 12 Ocak 2027. Microsoft'un son güncelleme takvimi, Azure Arc ile ESU koşulları, Essentials sürümüne özel riskler, sürüm karşılaştırma tablosu ve BT ekipleri için geçiş kontrol listesi.
cover_title: Windows Server 2016 destek sonu
cover_icon: server
category: dijital-guvenlik
seo_title: Windows Server 2016 destek sonu: geçiş ve ESU rehberi
meta_description: Windows Server 2016 destek sonu 12 Ocak 2027: son güncelleme, Azure Arc ESU koşulları, Essentials riski, sürüm tablosu ve BT için 10 maddelik geçiş listesi.
focus_kw: Windows Server 2016 destek sonu
keywords: Windows Server 2016 destek sonu, Windows Server 2016 desteği ne zaman bitiyor, Windows Server 2016 ESU, Azure Arc ESU, Windows Server 2025 geçiş, sunucu envanteri, yama yönetimi
cover_alt: Windows Server 2016 destek sonu: 12 Ocak 2027 takvimi ve geçiş rehberi kapak görseli
---
Microsoft, Windows Server 2016'nın Ocak 2027 güncellemesinin bu sürüm için yayımlanacak son güvenlik güncellemesi olacağını hatırlattı [1]. **Windows Server 2016 destek sonu** 12 Ocak 2027; bu tarihten sonra Datacenter, Essentials, MultiPoint Premium ve Standard sürümlerinin hiçbiri ücretsiz güvenlik yaması, hata düzeltmesi veya teknik destek almayacak [1][2]. Geriye yaklaşık 11 hafta kaldı. Bu rehberde tarihleri birincil kaynaklardan derledik, ücretli Genişletilmiş Güvenlik Güncellemeleri (ESU) seçeneğinin koşullarını ve bir geçiş kontrol listesini bir araya getirdik.

## Windows Server 2016 desteği ne zaman bitiyor?

Microsoft Learn yaşam döngüsü sayfasına göre Windows Server 2016'nın ana akım desteği 11 Ocak 2022'de bitti; genişletilmiş destek ise 12 Ocak 2027'de (Learn'de UTC olarak 13 Ocak 2027 06:59) sona eriyor [2]. Aynı tarih Hyper-V Server 2016, Windows Server 2016 üzerindeki IIS 10, Windows Storage Server 2016 ve Windows Server 2016 için WSUS gibi bileşenleri de kapsıyor; System Center 2016 ise bir gün önce, 11 Ocak 2027'de destek dışı kalıyor [3].

BleepingComputer'ın aktardığına göre destek bitince sunucular çalışmaya devam edecek ama yeni açıklara karşı korunmayacak; Microsoft müşterilere Windows Server 2025'e geçmeyi öneriyor ve sürümü denemek isteyenler için 180 günlük değerlendirme sürümü sunuyor [1].

### Sürüm karşılaştırma tablosu: Hangi sunucu ne zamana kadar güvende?

| Sürüm | Ana akım destek sonu | Genişletilmiş destek sonu | Durum (25 Ekim 2026) |
|---|---|---|---|
| Windows Server 2016 | 11 Ocak 2022 [2] | 12 Ocak 2027 [2] | Son 11 hafta |
| Windows Server 2019 | 9 Ocak 2024 [4] | 9 Ocak 2029 [4] | Yalnızca güvenlik güncellemesi |
| Windows Server 2022 | 13 Ekim 2026 [5] | 14 Ekim 2031 [5] | Ana akım destek yeni bitti |
| Windows Server 2025 | 13 Kasım 2029 [6] | 14 Kasım 2034 [6] | Ana akım destekte |
| SQL Server 2016 (bağlam) | 13 Temmuz 2021 [7] | 14 Temmuz 2026 [7] | Destek bitti, ESU 1. yıl sürüyor [7] |

Not: Tarihler Microsoft Learn'deki UTC saatlerinin bir gün öncesine denk gelen ABD Pasifik saatine göre yazıldı.

Alıntılanabilir istatistik: **Windows Server 2016'dan 2022'ye geçen bir sunucu, 2031'e kadar; 2025'e geçen bir sunucu ise 2034'e kadar güvenlik güncellemesi alabilir** [5][6]. Kısa vadeli bir "ara durak" seçmek, birkaç yıl sonra aynı projeyi tekrarlamak anlamına gelebilir.

## Windows Server 2016 ESU: Azure Arc ile ücretli uzatma koşulları

Microsoft, Şubat 2026'da Windows Server 2016 için ESU'nun Azure Arc üzerinden sunulacağını duyurdu [8]. Microsoft Learn'deki hazırlık sayfasına göre koşullar şöyle [9]:

| Konu | Windows Server 2016 ESU (Azure Arc) |
|---|---|
| Kapsam | Kritik ve Önemli güvenlik güncellemeleri, en fazla 3 yıl (2030'a kadar) [9] |
| Yapılandırma | 3 Ağustos 2026'dan itibaren [9] |
| Faturalandırma | 13 Ocak 2027'den itibaren [9] |
| Sürümler | Yalnızca Standard ve Datacenter [9] |
| Lisans şartı | Yazılım Güvencesi (Software Assurance) veya SPLA / sunucu aboneliği [9] |
| Ajan | Azure Connected Machine ajanı 1.62 veya üzeri [9] |
| Kapsam dışı | Yeni özellikler ve güvenlik dışı hata düzeltmeleri [9] |

Fiyat konusunda dikkatli olun: Microsoft 1 Nisan 2026'dan itibaren ESU liste fiyatının konumdan ve satış kanalından bağımsız olarak aynı olacağını açıkladı [10]. Güncel çekirdek başı fiyatı Azure fiyat hesaplayıcısından veya lisans iş ortağınızdan teyit edin; üçüncü taraf sitelerdeki fiyatları bütçe kararına esas almayın.

ESU bir çıkış planı değil, zaman kazanma aracıdır. Microsoft da duyurusunda bu dönemi Windows Server 2025'e yükseltmek veya Azure'a taşınmak için bir fırsat olarak tanımlıyor [8]. Microsoft'un ESU sayfasına göre Azure Arc ile alınan ESU kullandıkça öde abonelik modeliyle faturalanıyor; klasik ESU ise Toplu Lisanslama üzerinden yıllık dilimlerle satın alınıyor [11].

## Windows Server 2016 Essentials kullananlar için ayrı uyarı

Küçük ofislerde yaygın olan Essentials sürümü için tablo daha keskin. BleepingComputer, Uzaktan Web Erişimi (Remote Web Access) gibi Essentials özelliklerinin de sona erdiğini aktarıyor [1]. Microsoft destek sayfası, Essentials kullanıcıları için geçiş adımlarını anlatıyor ve remotewebaccess.com hizmetinin de sona ereceğini belirtiyor [12]. Yukarıdaki tabloda gördüğünüz gibi Azure Arc ESU yalnızca Standard ve Datacenter sürümlerini kapsıyor [9]; yani Essentials için "bir yıl daha uzatalım" seçeneği yok.

## Yerinde yükseltme mi, yeni kurulum mu?

Microsoft Learn'e göre Windows Server 2025 ile kümelenmemiş sistemlerde tek seferde dört sürüme kadar yerinde yükseltme yapılabiliyor; Windows Server 2022 ve öncesinde bu sınır iki sürümdü. Küme (cluster) sistemlerinde sıralı yükseltme her seferinde bir sürüm ilerliyor ve her yükseltme için ayrı lisans gerekiyor [13]. Pratikte bu, 2016'dan 2025'e tek adımda geçişin teknik olarak mümkün olduğu, ancak uygulama uyumluluğu ve rol bazında test gerektirdiği anlamına geliyor.

| Senaryo | Önerilen yaklaşım | Neden? |
|---|---|---|
| Tek rol (dosya, yazdırma) | Yeni kurulum + taşıma | Temiz başlangıç, eski ayar kalıntısı yok |
| Kümelenmemiş uygulama sunucusu | Test sonrası yerinde yükseltme | 2025'e tek adım mümkün [13] |
| Hyper-V / dosya kümesi | Sıralı küme yükseltmesi | Her seferinde bir sürüm [13] |
| Essentials | Yeni platforma taşıma | ESU yok [9][12] |
| Üretici desteği belirsiz eski yazılım | Ağ segmentasyonu + ESU + yenileme planı | Zaman kazandırır, riski sıfırlamaz |

## Türkiye'den bakış: Güncel olmayan envanter ulusal risk başlığı

Anadolu Ajansı'nın 22 Ekim tarihli haberine göre Cumhurbaşkanlığı Siber Güvenlik Başkanlığı, PHP'deki kritik açıklar ("PHP2Shell") nedeniyle kamu kurumları başta olmak üzere ülke genelindeki sistemlerde güvenlik taramaları başlattı. Haberde Kamusal Siber Savunma Derneği Başkanı Yakup Özdemir, Türkiye açısından riskin boyutunun kurumların yazılım envanterlerinin güncelliği, açıklara müdahale süreleri ve teknik denetim kapasiteleriyle doğrudan ilişkili olduğunu anlatıyor [14]. Windows Server 2016 sunucuları da aynı soruya tabi: Envanterde nerede çalıştığını bilmediğiniz bir sunucuyu yamalayamazsınız.

Destek dışı bir sunucudan kaynaklanan bir ihlal kişisel veri içeriyorsa KVKK'nın 2019/10 sayılı kararı uyarınca ihlalin öğrenilmesinden itibaren en geç 72 saat içinde Kurul'a bildirim gerekir [15]. Kimlik avı kaynaklı saldırı zincirlerini [ClickFix saldırısı rehberimizde](/clickfix-saldirisi-sahte-captcha-korunma/), KOBİ'ler için dijital olgunluk ölçümünü ise [TÜBİTAK DDX+ rehberimizde](/tubitak-ddx-dijital-olgunluk-kobi-rehberi/) ele almıştık.

## Windows Server 2016 destek sonu için 10 maddelik geçiş kontrol listesi

- [ ] Tüm fiziksel, sanal ve bulut sunucularda işletim sistemi sürümünü listeleyin (Hyper-V Server 2016 ve WSUS dahil) [3]
- [ ] Her sunucunun rolünü, sahibini ve iş kritikliğini yazın
- [ ] Essentials sürümlerini ayrı işaretleyin; ESU kapsamında değiller [9][12]
- [ ] Üzerinde çalışan uygulamaların Windows Server 2022/2025 desteğini üreticiden teyit edin
- [ ] SQL Server 2016 gibi bağımlı ürünlerin kendi destek tarihlerini kontrol edin [7]
- [ ] Yerinde yükseltme mi yeni kurulum mu, rol bazında karar verin [13]
- [ ] ESU gerekiyorsa Software Assurance durumunu ve Azure Arc ajan sürümünü (1.62+) kontrol edin [9]
- [ ] 12 Ocak 2027'ye kadar taşınamayacak sunucuları ağda ayırın ve erişimi daraltın
- [ ] Yedekleme ve geri dönüş planını test edin
- [ ] KVKK ihlal bildirim sürecinin (72 saat) güncel olduğunu doğrulayın [15]

Kişisel cihaz tarafındaki temel önlemler için [telefon ve hesap güvenliği rehberimize](/telefon-ve-hesap-guvenligi/) de göz atabilirsiniz.

## Sıkça sorulan sorular

### Windows Server 2016 desteği ne zaman bitiyor?

12 Ocak 2027'de. Ocak 2027 güncellemesi bu sürüm için son ücretsiz güvenlik güncellemesi olacak [1][2].

### Destek bitince Windows Server 2016 çalışmayı durdurur mu?

Hayır. Sunucular çalışmaya devam eder ama yeni açıklara karşı güvenlik güncellemesi almaz [1].

### Windows Server 2016 için ESU alınabilir mi?

Evet, Standard ve Datacenter sürümleri için Azure Arc üzerinden, en fazla üç yıl. Software Assurance veya SPLA/sunucu aboneliği gerekiyor; faturalandırma 13 Ocak 2027'de başlıyor [9].

### Windows Server 2016 Essentials için ESU var mı?

Microsoft'un ESU koşulları yalnızca Standard ve Datacenter sürümlerini sayıyor; Essentials kullanıcıları için Microsoft geçiş adımlarını öneriyor [9][12].

### 2016'dan doğrudan Windows Server 2025'e yükseltme yapılabilir mi?

Kümelenmemiş sistemlerde evet: Windows Server 2025'e tek seferde dört sürüme kadar yerinde yükseltme destekleniyor. Kümelerde her seferinde bir sürüm ilerlenir [13].

## Kaynaklar

1. BleepingComputer, "Microsoft: Windows Server 2016 reaches end of support in January", 23 Ekim 2026. <https://www.bleepingcomputer.com/news/microsoft/microsoft-windows-server-2016-reaches-end-of-support-in-january/> (Erişim: 25 Ekim 2026)
2. Microsoft Learn, "Windows Server 2016 – Lifecycle". <https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2016> (Erişim: 25 Ekim 2026)
3. Microsoft Learn, "Products and Services Reaching End of Support in 2027". <https://learn.microsoft.com/en-us/lifecycle/end-of-support/end-of-support-2027> (Erişim: 25 Ekim 2026)
4. Microsoft Learn, "Windows Server 2019 – Lifecycle". <https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2019> (Erişim: 25 Ekim 2026)
5. Microsoft Learn, "Windows Server 2022 – Lifecycle". <https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2022> (Erişim: 25 Ekim 2026)
6. Microsoft Learn, "Windows Server 2025 – Lifecycle". <https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2025> (Erişim: 25 Ekim 2026)
7. Microsoft Learn, "SQL Server 2016 – Lifecycle". <https://learn.microsoft.com/en-us/lifecycle/products/sql-server-2016> (Erişim: 25 Ekim 2026)
8. Microsoft Windows Server Blog, "Planning ahead for Windows Server 2016 end of support", 25 Şubat 2026. <https://www.microsoft.com/en-us/windows-server/blog/2026/02/25/planning-ahead-for-windows-server-2016-end-of-support/> (Erişim: 25 Ekim 2026)
9. Microsoft Learn, "Prepare to deliver Extended Security Updates for Windows Server through Azure Arc". <https://learn.microsoft.com/en-us/azure/azure-arc/servers/prepare-extended-security-updates> (Erişim: 25 Ekim 2026)
10. Microsoft Licensing, "Microsoft Services: Pricing Consistency Update", 27 Mart 2026. <https://www.microsoft.com/en-us/licensing/news/services-pricing-consistency-update> (Erişim: 25 Ekim 2026)
11. Microsoft, "Plan your Windows Server and SQL Server end of support" (Extended Security Updates). <https://www.microsoft.com/en/windows-server/extended-security-updates> (Erişim: 25 Ekim 2026)
12. Microsoft Destek, "Windows Server 2016 Essentials end of support", Eylül 2026. <https://support.microsoft.com/en-us/servicing/os/windows/docs/2026/09/windows-server-2016-essentials-end-support> (Erişim: 25 Ekim 2026)
13. Microsoft Learn, "Plan your Windows Server upgrade path". <https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview> (Erişim: 25 Ekim 2026)
14. Anadolu Ajansı, Mert Davut, "Kritik güvenlik açıklarına karşı sistemleri güncelleme uyarısı", 22 Ekim 2026. <https://www.aa.com.tr/tr/bilim-teknoloji/kritik-guvenlik-aciklarina-karsi-sistemleri-guncelleme-uyarisi/4096910> (Erişim: 25 Ekim 2026)
15. KVKK, "Veri İhlali Bildirimi" (2019/10 sayılı Kurul Kararı). <https://www.kvkk.gov.tr/Icerik/5362/Veri-Ihlali-Bildirimi> (Erişim: 25 Ekim 2026)
