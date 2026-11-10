---
title: Soğuk zincir siber güvenliği: 700 marketin soğutucusu nasıl ele geçirildi, Türkiye'de 136 açık kayıt ve kontrol listesi
date: 2026-11-10
updated: 2026-11-10
description: Fransa'da 700 market sitesinin soğutma kontrol cihazları bir gecede uzaktan ele geçirildi; Fransa 9 Kasım'da saldırıyı İran Devrim Muhafızları'na bağlı bir birime atfetti. Zaman çizelgesi, açık cihaz sayıları, Türkiye verisi ve soğuk zincir için kontrol listesi.
cover_title: Soğuk zincir siber güvenliği
cover_icon: coldchain
category: lojistik-nakliyat
seo_title: Soğuk zincir siber güvenliği: soğutma kontrol cihazları
meta_description: Soğuk zincir siber güvenliği artık gıda güvenliği demek. Fransa'da 700 marketi vuran saldırı, Türkiye'de 136 açık kayıt ve soğutma kontrol cihazı listesi.
focus_kw: soğuk zincir siber güvenliği
keywords: soğuk zincir siber güvenliği, soğutma kontrol cihazları, endüstriyel soğutma sistemleri, soğuk zincir yönetimi, soğuk hava deposu, Danfoss, xweb, OT güvenliği, CISA, CERT-FR
cover_alt: Soğuk zincir siber güvenliği: ele geçirilen soğutma kontrol cihazı ve yükselen sıcaklık kapak görseli
---
Pazar gecesini pazartesiye bağlayan saatlerde, Fransa'daki yüzlerce marketin dondurucuları sessizce buz çözme moduna geçti. Sabah gelen çalışanlar, CNN'in aktardığına göre dolapların altında su birikintileri ve bozulmuş ürünlerle karşılaştı [10]. Kimse kapıyı kırmamıştı; saldırganlar internete açık soğutma kontrol panellerine uzaktan bağlanmıştı. Bu olay, **soğuk zincir siber güvenliği** konusunu bir anda BT ekiplerinin değil, gıda, ilaç ve lojistik işletmelerinin gündemine taşıdı. 9 Kasım 2026'da Fransa, saldırıyı İran Devrim Muhafızları'na bağlı bir birime atfetti [1][2]. Bu yazıda ne olduğunu, ne kadar cihazın açıkta olduğunu, Türkiye'deki verileri ve uygulanabilir bir kontrol listesini bir araya getirdik.

## Ne oldu? Soğutma saldırılarının zaman çizelgesi

| Tarih | Gelişme | Kaynak |
|---|---|---|
| 9 Ağustos 2026 | Claroty Team82, Danfoss AK-SM 800A yönetim arayüzünde kimlik doğrulama atlatma ("günün kodu") dahil açıkları yayımladı; Danfoss R4.3.1 sürümüyle düzeltti | [6] |
| 11-12 Ekim 2026 | Fransa'da yaklaşık 700 perakende sitesinde soğutma kontrol cihazlarının buz çözme ayarları yüksek sıcaklığa çekildi; büyük ürün kaybı ve en az 15 yangın başlangıcı | [1] |
| 12 Ekim 2026 | CERT-FR, Danfoss AK-SM/AK-SC ile Copeland ve Dixell xweb sistemleri için uyarı yayımladı (16 Ekim'de güncellendi) | [3] |
| 19 Ekim 2026 | ESET Türkiye, Türkiye'de uzaktan soğutma kontrolüyle ilişkili olabilecek 136 internet erişimli kayıt bildirdi | [8] |
| 1-2 Kasım 2026 | İkinci dalga: Yaklaşık on iki Avrupa ülkesinde soğutma sistemleri etkilendi; Fransız kan kurumu EFS'nin üç sitesinde soğuk odalar 110 °C'ye programlandı, personel müdahale etti | [5] |
| 5 Kasım 2026 | CISA, FBI, HHS, USDA ve ABD Ulaştırma Bakanlığı soğutma ve soğuk zincir izleme sistemleri için ortak uyarı yayımladı | [4] |
| 9 Kasım 2026 | Fransa ilk dalgayı İran Devrim Muhafızları'na bağlı Shahid Kaveh birimine atfetti; Paris Savcılığı adli soruşturma açtı | [1][2][9] |

Önemli bir not: Fransız makamlarının atfı Ekim'deki ilk dalgayla ilgili. ANSSI Genel Müdürü Vincent Strubel, EFS saldırısı için "yöntem benzer olsa da aynı saldırgan olduğunu söylemeye izin veren bir şey yok" dedi; diğer Avrupa ülkelerindeki saldırılar henüz atfedilmedi [7].

## Saldırı nasıl çalıştı?

Paris Savcılığı'na göre saldırganlar, web arayüzleri üzerinden ekipmanların kontrolünü uzaktan ele geçirdi, süresiz ve anormal buz çözme döngüleri başlattı ve belirli bir sıcaklığın üzerinde devreye girmesi gereken sensör alarmlarını devre dışı bıraktı [7]. Önce Danfoss, ardından Dixell ve Copeland sistemlerine ulaşıldı [7].

Siber güvenlik şirketi Sekoia'nın değerlendirmesi çarpıcı: Saldırılar sofistike değildi [5]. Asıl sorun, güncellenmemiş Danfoss kontrol cihazlarının doğrudan internete açık olmasıydı [5]. Sekoia'nın kurduğu tuzak sistemlerde (honeypot), saldırganların "Supervisor" ve "admin" hesaplarına "12345" parolasıyla parola püskürtme denemeleri yaptığı görüldü [5].

Sekoia ayrıca yapay zekâ ile ilgili bir uyarı yapıyor: Halka açık ürün yazılımı ve internete açık cihazlar bir araya geldiğinde, büyük dil modelleri küçük ölçekli endüstriyel kontrol ve bina otomasyon sistemlerine saldırının giriş eşiğini düşürebiliyor [5].

## Rakamlarla internete açık soğutma kontrol cihazları

| Ölçüm | Değer | Kaynak |
|---|---|---|
| Censys'te görünen Danfoss AK-SM 800A cihazı (Ağustos 2026) | 2.765 | [6] |
| İnternete açık Danfoss sistemi, 11 Ekim 2026 | 2.700'den fazla (yaklaşık 1.700'ü Fransa'da) | [5] |
| 12 Ekim 16.00 itibarıyla Fransa'da erişilemez hâle gelenler | Daha önce açık olanların yaklaşık yarısı | [5] |
| Danfoss ve xweb aileleri, dünya geneli (Censys) | 9 Ekim: 6.695 → 5 Kasım: 3.124 (%53 düşüş) | [11] |
| Türkiye, 14 Ekim 2026 (ESET Türkiye) | 136 kayıt: 10'u Danfoss, 126'sı xweb panelleriyle ilişkili | [8] |

Tablo, belirtilen kaynaklardaki verilerden tarafımızca derlenmiştir. Kayıt sayısı fiziksel cihaz sayısı değildir; internete açık olmak her cihazın açık barındırdığı anlamına gelmez [8][11].

Alıntılanabilir istatistik: **ESET Türkiye, 14 Ekim 2026'da Türkiye'de uzaktan soğutma kontrolüyle ilişkili olabilecek 136 internet erişimli kayıt tespit etti; bu, 136 işletmenin saldırıya açık olduğu anlamına gelmiyor** [8].

## Türkiye için ne anlama geliyor?

Türkiye'de bu saldırılardan etkilenen bir işletmeye dair bilgi bulamadık. Ama iki sinyal var:

- DW Türkçe'ye konuşan Prof. Dr. Tuna Tuğcu, saldırılarla gündeme gelen Danfoss AK-SM 820A, 850A ve 880A modellerinin şirketin Türkiye sayfasında da pazarlandığını, hangi işletmelerde kullanıldıklarının ve güncelleme durumlarının ise bilinmediğini belirtiyor [11].
- ESET'in tespit ettiği kayıtlar yalnızca marketleri kapsamıyor; soğuk hava depoları, eczaneler ve üretim tesisleri de benzer kontrol sistemlerini kullanabiliyor [8].

Haber Anadolu Ajansı'nda da yer aldı; Fransa Dışişleri Bakanı Barrot saldırıyı Fransa topraklarında yapılan ilk geniş çaplı sabotaj amaçlı siber saldırı olarak niteledi [9]. Kısacası konu "Fransa'nın sorunu" değil. Soğutma panelinizi internetten kimin, nasıl yönettiğini bilmiyorsanız, ilk soru o.

## Sorumluluk kimde?

Sekoia'nın önemli bir tespiti var: Bu önlemlerin sorumluluğu çoğu zaman tesis sahibi, entegratör, bakım firması ve üretici arasında dağılmış durumda; ama bu dağınıklık kalıcı bir açığa dönüşmemeli [5].

| Rol | Ne yapmalı? |
|---|---|
| Tesis sahibi (market, depo, eczane, fabrika) | Envanter çıkarmak; hangi panelin internete açık olduğunu bakım firmasına yazılı sordurmak [4][8] |
| Bakım / soğutma servis firması | Uzaktan erişimi VPN veya korumalı ağa taşımak; IP filtrelemeyi yalnızca geçici çözüm saymak [3] |
| Entegratör | OT cihazlarını ayrı bir VLAN'da, iş ağından ayrı kurmak [4] |
| Üretici | Ürün yazılımı güncellemelerini yayımlamak; destek dışı cihazlar için değişim yolu sunmak [3][6] |
| Sigorta / hukuk | Servis firmasına veri akışını kesmeden önce sözleşme koşullarını kontrol etmek [3] |

Tablo, belirtilen kaynaklardaki öneriler esas alınarak tarafımızca hazırlanmıştır.

## Soğutma kontrol cihazları için soğuk zincir siber güvenliği kontrol listesi

CISA ve ortaklarının 5 Kasım uyarısı [4], CERT-FR'nin önerileri [3] ve ESET Türkiye'nin değerlendirmesi [8] üzerine kurulu bir liste:

- [ ] Kontrol panellerini doğrudan internete açmayın; uzaktan erişim gerekiyorsa güncel bir güvenlik duvarı veya uç cihaz arkasına alın [4]
- [ ] Uzaktan bakımı yalnızca güvenli VPN veya korumalı ağ üzerinden yapın [3]
- [ ] OT cihazlarını iş ağından ayrı, özel bir VLAN'a taşıyın [4]
- [ ] Varsayılan parolaları değiştirin; mümkün olan yerde oltalamaya dayanıklı çok faktörlü doğrulama kullanın [4]
- [ ] Ürün yazılımını güncelleyin; Danfoss AK-SM 800A için R4.3.1 veya sonrası [6]. Danfoss cihazlarında güvenlik seviyesini "Strict" moda alın [3]
- [ ] Desteği bitmiş cihazları tespit edip değiştirin; bu cihazlarda yalnızca fabrika ayarlarına dönmek yeterli değil [3][4]
- [ ] Değişiklik yapabilecek cihaz ve IP adreslerini izin listesine alın [4]
- [ ] Buz çözme aralıkları dahil tüm konfigürasyonu kontrol edin [3]
- [ ] Ayar noktaları için makul sınırlar tanımlayın ve sapmalar için alarm kurun [4]
- [ ] Kontrol panelinden bağımsız bir sıcaklık sensörü ve alarm mekanizması kullanın [8]
- [ ] Yedekleri çevrim dışı ve tesis dışında tutun, düzenli test edin [4]
- [ ] Günlük kaydını açın, beklenmeyen kimlik doğrulama ve yapılandırma değişikliklerini izleyin [4][5]

OT tarafında genel bir çerçeve için [endüstriyel kontrol sistemleri güvenliği yazımıza](/endustriyel-kontrol-sistemleri-siber-guvenligi-yz-ajani/), depo cihazlarının benzer riskleri için [barkod okuyucu güvenliği yazımıza](/barkod-okuyucu-guvenligi-depo-siber-saldiri/), destek süresi biten sistemler için de [Windows Server 2016 destek sonu rehberimize](/windows-server-2016-destek-sonu-gecis-rehberi/) göz atabilirsiniz.

## Sıkça sorulan sorular

### Soğuk zincir siber güvenliği neden önemli?

Soğutma kontrol cihazları ele geçirildiğinde sıcaklık değiştirilebiliyor, ürünler bozulabiliyor ve yangın riski oluşabiliyor. CISA'ya göre bu, güvensiz saklanan ürünlerin tüketilmesi hâlinde tüketicilere dolaylı zarar da verebilir [4].

### Fransa'daki market saldırısını kim yaptı?

Fransız makamları 9 Kasım 2026'da Ekim'deki saldırıyı İran Devrim Muhafızları'na bağlı Shahid Kaveh birimine atfetti [1][2]. Kasım başındaki ikinci dalga ise henüz atfedilmedi [7].

### Türkiye'de internete açık soğutma paneli var mı?

ESET Türkiye, 14 Ekim 2026'da 136 internet erişimli kayıt tespit etti (10'u Danfoss, 126'sı xweb panelleriyle ilişkili). Şirket, bunun 136 işletmenin saldırıya açık ya da ele geçirilmiş olduğu anlamına gelmediğini vurguluyor [8].

### Soğutma kontrol cihazımın güvenli olduğunu nasıl anlarım?

İlk adım, panelin internetten doğrudan erişilebilir olup olmadığını ve bakım firmasının nasıl bağlandığını öğrenmek. CERT-FR, doğrudan internet erişiminin kaldırılmasını ve erişimin yalnızca güvenli VPN veya korumalı ağ üzerinden sağlanmasını öneriyor [3].

### Saldırıda hangi cihazlar hedef alındı?

CERT-FR uyarısında Danfoss AK-SM ve AK-SC serileri ile Copeland xweb ve Dixell xweb sistemleri sayılıyor [3].

## Kaynaklar

1. CERT-FR / Centre de Coordination des Crises Cyber (C4), "Activités cyber offensives ciblant la France menées par des acteurs iraniens liés au CGRI" (CERTFR-2026-CTI-009), 9 Kasım 2026. <https://www.cert.cyber.gouv.fr/cti/CERTFR-2026-CTI-009/> (Erişim: 10 Kasım 2026)
2. Fransa Dışişleri Bakanlığı, "Déclaration d'attribution à l'Iran de cyberattaques visant la France", 9 Kasım 2026. <https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/declaration-d-attribution-a-l-iran-de-cyberattaques-visant-la-france> (Erişim: 10 Kasım 2026)
3. CERT-FR, "Incident de sécurité ciblant les contrôleurs à distance des installations de réfrigération" (CERTFR-2026-ALE-012), 12 Ekim 2026 (16 Ekim 2026'da güncellendi). <https://www.cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/> (Erişim: 10 Kasım 2026)
4. CISA, FBI, HHS, USDA ve DoT, "US Government Partners Urge Hardening Industrial Refrigeration and Cold Chain Monitoring Systems", 5 Kasım 2026. <https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems> (Erişim: 10 Kasım 2026)
5. Sekoia, "The Cold Chain on Fire: Unpatched Danfoss controllers exploited", 10 Kasım 2026. <https://www.sekoia.com/fr/blog/the-cold-chain-on-fire-unpatched-danfoss-controllers-exploited> (Erişim: 10 Kasım 2026)
6. Claroty Team82, Amir Zaltzman, "Freeze the Controller, Defrost the Food: Uncovering Vulnerabilities in Danfoss Refrigeration Controllers", 9 Ağustos 2026. <https://www.claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers> (Erişim: 10 Kasım 2026)
7. franceinfo, Luc Chagnon, "La France accuse l'Iran de la cyberattaque contre des frigos de supermarchés…", 9 Kasım 2026. <https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/cyberattaque-contre-des-frigos-de-supermarches-le-parquet-de-paris-ouvre-une-enquete-visant-une-unite-des-gardiens-de-la-revolution-iraniens_8274806.html> (Erişim: 10 Kasım 2026)
8. Teknoblog, Sabri Küstür, "ESET, Türkiye'de soğutma kontrolüyle ilişkili 136 kayıt bildirdi", 19 Ekim 2026. <https://www.teknoblog.com/eset-sogutma-panelleri-icin-turkiye-yi-uyardi/> (Erişim: 10 Kasım 2026)
9. Anadolu Ajansı, Şeyma Yiğit, "Fransa Dışişleri Bakanı Barrot: (Marketlere) siber saldırının sorumluluğu İran Devrim Muhafızları'na ait", 9 Kasım 2026. <https://www.aa.com.tr/tr/dunya/fransa-disisleri-bakani-barrot-marketlere-siber-saldirinin-sorumlulugu-iran-devrim-muhafizlarina-ait/4117829> (Erişim: 10 Kasım 2026)
10. CNN, "What to know about the cyberattack that targeted supermarket refrigeration systems in France", 14 Ekim 2026. <https://www.cnn.com/2026/10/14/europe/france-cyberattack-supermarket-fridges-intl> (Erişim: 10 Kasım 2026)
11. DW Türkçe, Pelin Ünker, "Avrupa'da hacklenen soğutma sistemleri Türkiye'de de satılıyor", 9 Kasım 2026. <https://www.dw.com/tr/avrupada-marketler-hacklendi-t%C3%BCrkiyede-risk-ne/a-79900913> (Erişim: 10 Kasım 2026)
