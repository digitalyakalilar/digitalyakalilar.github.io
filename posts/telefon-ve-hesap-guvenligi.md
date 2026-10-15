---
title: Telefon ve hesap güvenliği: Beyaz yakalılar için kanıta dayalı rehber
date: 2026-10-15
updated: 2026-10-15
meta_description: İki adımlı doğrulama, passkey, oltalama SMS'leri ve kayıp telefon planı: NIST, CISA, Google ve Apple kaynaklarıyla telefon ve hesap güvenliği rehberi.
description: İki adımlı doğrulamadan passkey'lere, oltalama SMS'lerinden kayıp telefon senaryosuna; NIST, CISA, Google ve Apple kaynaklarıyla telefonunu ve hesaplarını korumanın adım adım yolu.
cover_title: Telefon ve hesap güvenliği rehberi
cover_icon: phone
category: dijital-guvenlik
---
İş e-postan, şirket içi mesajlaşma uygulaman, banka uygulaman ve çoğu hesabının doğrulama kodları artık aynı cihazda: telefonunda. Bu da telefonu hem çok değerli hem de saldırganlar için cazip bir hedef hâline getiriyor.

Verizon'un 2026 Veri İhlali Araştırmaları Raporu (DBIR), incelenen ihlallerin %62'sinde insan unsurunun rol oynadığını ortaya koyuyor. Aynı rapora göre oltalama simülasyonlarında sesli arama ve SMS gibi mobil odaklı kanallarda tıklama oranının medyanı, e-postaya göre %40 daha yüksek [1]. Kısacası saldırganlar artık cebimize daha çok yöneliyor.

Bu rehberde, kişisel ve iş hesaplarını korumak için uygulayabileceğin adımları, her birinin dayandığı kaynakla birlikte bulacaksın.

## Önce ayrımı netleştir: cihaz güvenliği ve hesap güvenliği

Güvenlik önlemleri iki farklı katmanı korur ve bu ikisini karıştırmak yaygın bir hatadır:

- **Hesap güvenliği:** E-posta, LinkedIn, WhatsApp, bulut depolama gibi çevrim içi hesaplarına başkasının girmesini engeller. İki adımlı doğrulama (2FA), güçlü şifreler ve passkey'ler bu katmandadır.
- **Cihaz güvenliği:** Telefonun fiziksel olarak birinin eline geçtiğinde ya da zararlı bir yazılımla karşılaştığında içindekileri korur. Ekran kilidi, yazılım güncellemeleri, uygulama izinleri ve uzaktan kilitleme/silme bu katmandadır.

Önemli bir not: **İki adımlı doğrulama telefonunu değil, hesaplarını korur.** Şifren çalınsa bile hesabına girilmesini zorlaştırır; ama kilidi açık bırakılmış bir telefonu korumaz. Bu yüzden iki katmana da ayrı ayrı yatırım yapman gerekir.

## Hesapların için: çok faktörlü doğrulama (2FA/MFA)

ABD Siber Güvenlik ve Altyapı Güvenliği Ajansı (CISA), çok faktörlü doğrulamayı (MFA) bir hizmete erişim verilmeden önce iki veya daha fazla doğrulayıcının birlikte istenmesi olarak tanımlar. Mantık basit: saldırgan şifreni ele geçirse bile ikinci adımı geçemez [2].

Etkisi araştırmalarla da ölçülmüş durumda. Google'ın New York Üniversitesi ve UC San Diego ile yürüttüğü bir yıllık çalışmada, kurtarma telefonuna gönderilen SMS kodu otomatik botların %100'ünü, toplu oltalama saldırılarının %96'sını ve hedefli saldırıların %76'sını engelledi. Cihaz üzerindeki onay bildirimleri (prompt) ise bu oranları sırasıyla %100, %99 ve %90'a çıkardı [3]. Microsoft da MFA'nın hesap ele geçirme saldırılarının %99,9'undan fazlasını engelleyebildiğini belirtiyor [4].

### Her yöntem aynı derecede güçlü değil

CISA'ya göre her MFA türü aynı korumayı sağlamaz; hedeflenmesi gereken standart oltalamaya dayanıklı (phishing-resistant) doğrulamadır. Ajans, yaygın olarak erişilebilen oltalamaya dayanıklı yöntemin FIDO/WebAuthn olduğunu vurguluyor. Yine de hiç MFA olmamasındansa herhangi bir MFA'nın olması daha iyidir [2].

ABD Ulusal Standartlar ve Teknoloji Enstitüsü'nün (NIST) dijital kimlik kılavuzu SP 800-63B, tek seferlik kodları (OTP) ve SMS gibi ayrı kanaldan gelen kodları oltalamaya dayanıklı saymaz. Kılavuz, telefon şebekesi üzerinden (SMS veya sesli arama) doğrulamayı ayrıca "kısıtlı doğrulayıcı" olarak sınıflandırır [5].

Pratikte güçlüden zayıfa doğru sıralama şöyle özetlenebilir:

1. **Passkey veya donanım güvenlik anahtarı:** FIDO Alliance'a göre passkey'ler cihazında saklanan, ekran kilidini açtığın yöntemle (parmak izi, yüz, PIN) kullanılan ve oltalamaya dayanıklı kimlik bilgileridir [6].
2. **Uygulama bildirimi veya doğrulama uygulaması:** Google, SMS yerine Google bildirimlerini öneriyor ve bunların SIM kart değiştirme (SIM swap) gibi telefon numarasına dayalı saldırılara karşı da yardımcı olduğunu belirtiyor [7].
3. **SMS kodu:** Google'ın ifadesiyle her 2FA biçimi güvenlik katar, ancak SMS veya aramayla gelen kodlar telefon numarasına dayalı saldırılara açık olabilir [7].

### Adım adım: kritik hesaplarında 2FA'yı aç

Önceliği en kritik hesaplarına ver: e-posta (diğer tüm hesapların şifre sıfırlama kapısıdır), Apple veya Google hesabın, LinkedIn ve WhatsApp. Menü adları cihazının diline ve sürümüne göre küçük farklılıklar gösterebilir.

- **Google hesabı:** Google Hesabı > Güvenlik ve oturum açma > "Google'da nasıl oturum açtığınız" altında 2 Adımlı Doğrulama'yı aç. Telefonunu kaybetme ihtimaline karşı 8 haneli yedek kodları yazdırıp güvenli bir yerde sakla [7].
- **Apple hesabı:** Ayarlar > [adın] > Giriş ve Güvenlik (Sign-In & Security) yolunu izleyerek iki faktörlü doğrulamayı aç. Apple'a göre bu yöntem, artık çoğu hesap için varsayılan güvenlik yöntemi [8].
- **LinkedIn:** Ayarlar ve Gizlilik > Oturum açma ve güvenlik > İki faktörlü kimlik doğrulama. LinkedIn, doğrulama uygulaması veya SMS seçeneği sunuyor [9].
- **WhatsApp:** Ayarlardaki iki adımlı doğrulama bölümünden özelliği aç. WhatsApp, iki adımlı doğrulamada kullanılan 6 haneli PIN'i şifreye dönüştürdüğünü duyurdu; ayarlarda e-posta adresini de güncel tut [10].

> İpucu: Doğrulama kodlarını kimseyle paylaşma. Google, kodu doğrulamak için seni asla aramayacağını açıkça belirtiyor [7]. "Bankadan arıyoruz, gelen kodu okur musunuz?" diyen biri büyük olasılıkla dolandırıcıdır.

## Şifreler: uzun, benzersiz ve bir şifre yöneticisinde

NIST'in güncel kılavuzu, şifre konusundaki pek çok eski alışkanlığı değiştirdi. Kılavuza göre [5]:

- Tek başına kullanılan şifreler **en az 15 karakter** olmalı; MFA'nın parçası olan şifreler için alt sınır 8 karakter.
- "Büyük harf, rakam, özel karakter zorunlu" gibi kompozisyon kuralları dayatılmamalı.
- Şifreler periyodik olarak zorla değiştirtilmemeli; ancak ele geçirildiğine dair bir kanıt varsa değiştirilmeli.
- Şifre yöneticileri ve otomatik doldurma desteklenmeli; NIST, şifre yöneticilerinin daha güçlü şifre seçimini artırdığını belirtiyor.

Şifre tekrarı en büyük risklerden biri. Microsoft'un aktardığı bir SANS çalışmasına göre şifrelerin %73'üne kadarı kopya, yani başka bir yerde de kullanılan şifreler [4]. Bir sitedeki sızıntı, aynı şifreyi kullandığın tüm hesapları riske atar.

**Ne yapmalı?**

1. Telefonundaki yerleşik şifre yöneticisini (iCloud Anahtar Zinciri, Google Şifre Yöneticisi) ya da güvendiğin bir şifre yöneticisini aktif kullan.
2. Önce e-posta ve banka gibi kritik hesaplar için benzersiz, uzun şifreler oluştur.
3. E-posta adresinin bilinen veri ihlallerinde yer alıp almadığını Have I Been Pwned üzerinden kontrol et. Site, veri ihlallerinde ifşa olmuş hesapları sorgulamak için ücretsiz bir kaynak olarak kurulmuştur [11].
4. Destekleyen hizmetlerde passkey oluştur. Google'a göre passkey ile oturum açtığında, cihazın elinde olduğunu doğruladığı için ikinci adım ayrıca istenmez [7].

## Oltalama: e-posta kadar SMS ve aramalara da dikkat

CISA'ya göre oltalama mesajlarının ortak işaretleri şunlardır: acele ettiren veya duygusal baskı kuran dil, kişisel ya da finansal bilgi talebi, güvenilmeyen kısaltılmış bağlantılar ve "amaz0n.com" gibi hatalı adresler. CISA, yapay zekâ çağında bazı oltalama e-postalarının artık kusursuz dil bilgisiyle yazıldığını, bu nedenle yazım hatalarına güvenmemek gerektiğini de vurguluyor [12].

DBIR 2026, sosyal mühendisliğin giderek daha çok sesli arama ve mobil kanallara kaydığını gösteriyor. Raporda, güvenilir bir ilişki kurgulanarak kullanıcının kandırıldığı "pretexting" yöntemi, ilk erişim yöntemi olarak tüm ihlallerin %6'sına ulaştı; oltalama ise bir önceki yıldaki gibi %16'da kaldı [1].

**Uygulanabilir alışkanlıklar:**

- Mesajdaki bağlantıya tıklamak yerine uygulamayı ya da siteyi kendin aç. CISA, gerçek olabileceğini düşündüğün bir mesajda bile mesajdaki numarayı aramamayı, kurumun doğrulanmış iletişim bilgilerini kullanmayı öneriyor [12].
- "Kargonuz bekliyor", "hesabınız askıya alındı", "vergi iadeniz var" gibi aciliyet vurgulu SMS'lerde dur ve kontrol et.
- İş yerinde "CEO'dan acil ödeme talebi" gibi beklenmedik isteklerde, talebi farklı bir kanaldan (telefon, yüz yüze) teyit et.
- Türkiye'de siber olay bildirimleri ve zararlı bağlantı listeleri, USOM'un duyurusuna göre artık Siber Güvenlik Başkanlığı'nın siberguvenlik.gov.tr adresi üzerinden yürütülüyor [13].

## Cihazın için: güncellemeler, ekran kilidi ve izinler

### Güncellemeleri erteleme

CISA, yazılım güncellemelerinin birçoğunun güvenlik açıklarını kapatmak için yayımlandığını hatırlatıyor ve otomatik güncellemeleri açmayı öneriyor [14]. Bunun neden önemli olduğunu DBIR 2026 da gösteriyor: güvenlik açıklarının istismar edilmesi, %31 ile ihlallerde en yaygın ilk erişim yöntemi hâline geldi ve çalınmış kimlik bilgilerinin kötüye kullanımını (%13) geride bıraktı [1].

**Yap:** Ayarlar'dan işletim sistemi ve uygulama mağazası için otomatik güncellemeyi aç. Tarayıcını ve iş uygulamalarını da güncel tut.

### Güçlü bir ekran kilidi kullan

Apple, iki faktörlü doğrulamaya ek olarak cihazın bir parola ile korunmasını ve destekleniyorsa Face ID veya Touch ID kullanılmasını öneriyor [8]. Android'de de Bul (Find Hub) ağının kayıp cihazı bulmana yardım edebilmesi için PIN, desen veya şifre ayarlanmış olması gerekiyor [16]. Tahmini kolay kodlardan (doğum yılı, 123456 gibi) kaçın.

### Uygulama izinlerini gözden geçir

- **Android:** Ayarlar > Uygulamalar > [uygulama] > İzinler yolundan her uygulamanın izinlerini değiştirebilirsin. Ayarlar > Güvenlik ve gizlilik > Gizlilik > İzin yöneticisi ekranında ise aynı izne (konum, kamera, mikrofon, rehber) sahip tüm uygulamaları tek listede görürsün. Kullanılmayan uygulamalar için "kullanılmıyorsa uygulama etkinliğini duraklat" seçeneği de mevcut [15].
- **iPhone:** Ayarlar > Gizlilik ve Güvenlik bölümünden konum servisleri başta olmak üzere izinleri gözden geçirebilirsin [17].

Konum izni için mümkün olduğunda "yalnızca uygulamayı kullanırken" seçeneğini tercih et [15].

## Telefon kaybolur veya çalınırsa

Hazırlık, olay anından önce yapılır. Şu ayarları bugün kontrol et:

- **Android – Find Hub:** Cihaza bir Google hesabı eklediysen Find Hub otomatik olarak açılır. Kaybolan cihazı başka bir cihazdan veya tarayıcıdan bulabilir, "kayıp olarak işaretle" ile kilitleyebilir ya da fabrika ayarlarına sıfırlayarak silebilirsin. Operatörünün cihazı engelleyebilmesi için IMEI numaranı da buradan bulabilirsin [16].
- **iPhone – Bul (Find My):** Kayıp Modu cihazı kilitler ve uyumlu cihazlarda Apple Pay kartlarını askıya alır. Apple'a göre hesabında iki faktörlü doğrulama yoksa cihazı Bul uygulamasından uzaktan silemezsin [18]. Buradaki 2FA, cihazı değil Apple hesabını koruyarak uzaktan yönetimi güvenli kılıyor.
- **iPhone – Çalınan Cihaz Koruması:** iOS 17.3 ve sonrasında sunulan bu özellik, iPhone tanıdık konumların (ev, iş) dışındayken kayıtlı şifrelere erişim gibi işlemler için Face ID veya Touch ID ister. Apple hesabı şifresini değiştirmek gibi kritik işlemlerde ise bir saatlik güvenlik gecikmesi uygular. Böylece parolanı öğrenen bir hırsız bile hesabını hemen ele geçiremez. Özelliğin cihaz kaybolmadan önce açılmış olması gerekir: Ayarlar > Face ID ve Parola > Çalınan Cihaz Koruması [17].

**Olay anında sıra:** Cihazı kayıp olarak işaretle, başka bir cihazdan e-posta ve banka şifrelerini değiştir, operatörünü arayarak SIM kartını kapattır, iş hesapların için şirketinin BT ekibine haber ver.

## 15 dakikalık kontrol listesi

- [ ] E-posta, Apple/Google, LinkedIn ve WhatsApp'ta 2FA açık; mümkünse passkey veya uygulama bildirimi kullanılıyor.
- [ ] 2FA yedek kodları güvenli bir yerde saklı.
- [ ] Kritik hesapların şifreleri benzersiz ve bir şifre yöneticisinde.
- [ ] E-posta adresin Have I Been Pwned'de kontrol edildi.
- [ ] Otomatik güncellemeler açık.
- [ ] Güçlü bir ekran kilidi ve biyometri ayarlı.
- [ ] Konum, kamera, mikrofon ve rehber izinleri gözden geçirildi.
- [ ] Find Hub / Bul açık; iPhone'da Çalınan Cihaz Koruması etkin.

Bu adımların hiçbiri teknik uzmanlık gerektirmiyor; ama birlikte uygulandığında, saldırganların en sık kullandığı yolların çoğunu kapatıyor.

## Kaynaklar

1. Verizon, "2026 Data Breach Investigations Report – Executive Summary". <https://www.verizon.com/business/resources/executivebriefs/2026-dbir-executive-summary.pdf> (Erişim: 15 Ekim 2026)
2. CISA, "More than a Password". <https://www.cisa.gov/MFA> (Erişim: 15 Ekim 2026)
3. Google Online Security Blog, "New research: How effective is basic account hygiene at preventing hijacking", 17 Mayıs 2019. <https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html> (Erişim: 15 Ekim 2026)
4. Microsoft Security Blog, "One simple action you can take to prevent 99.9 percent of attacks on your accounts", 20 Ağustos 2019. <https://www.microsoft.com/en-us/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/> (Erişim: 15 Ekim 2026)
5. NIST, "SP 800-63B-4: Digital Identity Guidelines – Authentication and Authenticator Management". <https://pages.nist.gov/800-63-4/sp800-63b.html> (Erişim: 15 Ekim 2026)
6. FIDO Alliance, "Passkeys". <https://fidoalliance.org/passkeys/> (Erişim: 15 Ekim 2026)
7. Google Hesabı Yardım, "Turn on 2-Step Verification". <https://support.google.com/accounts/answer/185839?hl=en> (Erişim: 15 Ekim 2026)
8. Apple Destek, "Two-factor authentication for Apple Account". <https://support.apple.com/en-us/102660> (Erişim: 15 Ekim 2026)
9. LinkedIn Yardım, "Turn two-factor authentication on and off". <https://www.linkedin.com/help/linkedin/answer/a1381088/turn-two-step-verification-on-and-off> (Erişim: 15 Ekim 2026)
10. WhatsApp Yardım Merkezi, "How to manage two-step verification settings". <https://faq.whatsapp.com/1920866721452534> (Erişim: 15 Ekim 2026)
11. Have I Been Pwned, "Who, What & Why". <https://haveibeenpwned.com/About> (Erişim: 15 Ekim 2026)
12. CISA, "Recognize and Report Phishing". <https://www.cisa.gov/secure-our-world/recognize-and-report-phishing> (Erişim: 15 Ekim 2026)
13. USOM – Ulusal Siber Olaylara Müdahale Merkezi, duyuru. <https://www.usom.gov.tr> (Erişim: 15 Ekim 2026)
14. CISA, "Update Software". <https://www.cisa.gov/secure-our-world/update-software> (Erişim: 15 Ekim 2026)
15. Android Yardım, "Change app permissions on your Android phone". <https://support.google.com/android/answer/9431959?hl=en> (Erişim: 15 Ekim 2026)
16. Android Yardım, "Find, secure, or erase a lost Android device". <https://support.google.com/android/answer/6160491?hl=en> (Erişim: 15 Ekim 2026)
17. Apple Destek, "About Stolen Device Protection for iPhone". <https://support.apple.com/en-us/120340> (Erişim: 15 Ekim 2026)
18. Apple Destek, "Use Find My to locate your lost Apple device or AirTag". <https://support.apple.com/en-us/104978> (Erişim: 15 Ekim 2026)
