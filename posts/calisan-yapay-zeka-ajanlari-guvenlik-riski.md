---
title: Çalışanların kurduğu yapay zekâ ajanları yeni güvenlik açığı mı? Pluto yatırımı ve OWASP, NIST rehberleri ne söylüyor?
date: 2026-10-15
updated: 2026-10-15
description: Webrazzi'nin aktardığı Pluto yatırımı, çalışanların kendi kurduğu yapay zekâ ajanlarından doğan riskleri gündeme taşıdı. OWASP ve NIST kaynaklarına dayanarak riskleri ve şirketlerin atabileceği somut adımları derledik.
cover_title: Çalışanların kurduğu ajanlar ne kadar güvenli?
cover_icon: agentshield
category: dijital-guvenlik
seo_title: Yapay zekâ ajanı güvenliği: 9 maddelik kontrol listesi
meta_description: Çalışanların kurduğu ajanlar ve gölge yapay zekâ yeni bir risk alanı. OWASP ve NIST'e dayanan yapay zekâ ajanı güvenliği kontrol listesi ve KVKK notları.
focus_kw: yapay zekâ ajanı güvenliği
keywords: yapay zekâ ajanı güvenliği, gölge yapay zekâ, gölge yapay zekâ nedir, aşırı yetki OWASP LLM06, ajan ele geçirme, MCP güvenliği
cover_alt: Yapay zekâ ajanı güvenliği ve gölge yapay zekâ riski kapak görseli
---
Webrazzi'nin 14 Ekim'de aktardığı bir yatırım haberi, şirketlerin yeni bir kör noktasına dikkat çekiyor. 2025'te kurulan siber güvenlik girişimi Pluto, iki aşamada toplam 42,5 milyon dolar yatırım aldı. TLV Partners liderliğindeki 8,5 milyon dolarlık tohum turunu Jump Capital liderliğinde 34 milyon dolarlık A serisi izledi [1]. Bu yazıda yapay zekâ ajanı güvenliğini OWASP, NIST ve KVKK kaynaklarıyla ele alıyor, şirketler için 9 maddelik bir kontrol listesi sunuyoruz.

Haberi önemli kılan, Pluto'nun odaklandığı alan. Webrazzi'ye göre şirketin yazılımı, çalışanların kullandığı yapay zekâ araçlarını, eklentileri, MCP sunucularını ve çalışanların oluşturduğu ajanları izleyerek olası güvenlik risklerini tespit ediyor. Pluto özellikle yazılım geliştirici olmayan çalışanların yapay zekâ yardımıyla oluşturduğu uygulamalardan kaynaklanan risklere odaklanıyor. Bir ajan kendisine verilen yetkileri aşmaya çalıştığında sistem işlemi durdurabiliyor ya da kullanıcıdan onay isteyebiliyor [1].

Yatırımcıların bu alana para koyması tek başına bir kanıt değil, ama sinyal net. Soru artık yalnızca "çalışanlar hangi yapay zekâ aracını kullanıyor?" değil, "çalışanlar yapay zekâya hangi yetkileri devrediyor?"

## Gölge yapay zekâdan gölge ajana

"Gölge yapay zekâ" kavramı Türkiye'de de resmî literatüre girdi. KVKK'nın Şubat 2026'da yayımladığı "İş Yerlerinde Üretken Yapay Zekâ Araçlarının Kullanımı" dokümanı Gölge YZ'yi, üretken yapay zekâ araçlarının kurumun bilgisi, onayı veya kurumsal kontrolü dışında çalışanlar tarafından iş süreçlerinde kullanılması olarak tanımlıyor. Kurum, bu olgunun pek çok kuruluş için teorik bir risk olmaktan çıkıp günlük iş akışlarında karşılaşılan bir duruma dönüştüğünü belirtiyor [3].

Veriler de bunu destekliyor. Verizon'un 2026 Veri İhlali Araştırmaları Raporu'na göre kullanıcıların %67'si kurumsal cihazlarından yapay zekâ hizmetlerine kurumsal olmayan hesaplarla erişiyor. Çalışanların %45'i ise artık kurumsal cihazlarında düzenli yapay zekâ kullanıcısı sayılıyor, bir önceki yıl bu oran %15'ti. Gölge yapay zekâ, Verizon'un veri kaybı önleme (DLP) verilerinde kötü niyet içermeyen içeriden kaynaklı eylemler arasında üçüncü sıraya yükseldi [2].

Ajanlar bu tabloya yeni bir katman ekliyor. Bir sohbet aracına metin yapıştırmak veri sızıntısı riski taşır. Ancak e-posta kutusuna, dosya deposuna ya da CRM'e bağlanan bir ajan, okumanın ötesinde gönderme, silme ve değiştirme gibi eylemler de yapabilir.

## Yapay zekâ ajanı güvenliğinde risk nerede? OWASP'ın çerçevesi

OWASP'ın üretken yapay zekâ güvenlik projesi, bu riski "aşırı yetki" (Excessive Agency, LLM06:2025) başlığıyla tanımlıyor. OWASP'a göre sorunun kök nedeni genellikle üç şeyden biri: aşırı işlevsellik, aşırı izin ve aşırı özerklik [4]. Verilen örnek tanıdık: E-postaları özetlemek için kurulan bir eklenti mesaj gönderme yetkisine de sahipse, kötü amaçla hazırlanmış bir gelen e-posta ajanı kandırarak hassas bilgileri saldırgana ilettirebilir [4].

OWASP Aralık 2025'te bu alanı genişleterek "Ajan Uygulamaları için İlk 10" listesini yayımladı. Listede ajanın hedefinin ele geçirilmesi (ASI01), meşru araçların kötüye kullanımı (ASI02), kimlik ve yetki istismarı (ASI03) ile MCP gibi dinamik ekosistemlerdeki tedarik zinciri açıkları (ASI04) gibi başlıklar yer alıyor [5]. OWASP'ın vurgusu şu cümlede özetleniyor: Yapay zekâ eylemde bulunmaya başladığı anda güvenliğin doğası değişti [5].

## NIST: "Ajan ele geçirme" ölçülebilir bir risk

ABD Ulusal Standartlar ve Teknoloji Enstitüsü (NIST) bünyesindeki Center for AI Standards and Innovation (CAISI), ajan ele geçirmeyi (agent hijacking) bir tür dolaylı istem enjeksiyonu olarak tanımlıyor. Saldırgan, ajanın işlediği bir e-postaya, dosyaya ya da web sitesine kötü amaçlı talimatlar yerleştiriyor ve ajanı istenmeyen eylemlere yönlendiriyor [7].

CAISI'nin deneyleri riskin boyutunu da gösteriyor. Ekip, model için özel geliştirilen yeni saldırılarla saldırı başarı oranının en güçlü temel saldırıdaki %11'den %81'e çıktığını raporladı. Beş farklı enjeksiyon görevinde her saldırı 25 kez denendiğinde ortalama başarı oranı %57'den %80'e yükseldi [7]. Bu sonuçlar, bir ajanın tek bir testi geçmesinin güvenli olduğu anlamına gelmediğini gösteriyor.

NIST'in daha geniş çerçevesi olan Yapay Zekâ Risk Yönetimi Çerçevesi (AI RMF 1.0) gönüllü kullanım için tasarlandı. 2024'te yayımlanan Üretken Yapay Zekâ Profili (NIST AI 600-1) ise kurumların üretken yapay zekâya özgü riskleri belirlemesine yardımcı oluyor [8].

## Bu ne anlama geliyor? Türkiye'deki şirketler için

Türkiye'deki şirketler için mesele yalnızca teknik değil, hukuki de. KVKK dokümanı, yapay zekâ araçlarını tamamen yasaklamanın uygulamada gerçekçi sonuçlar doğurmayacağını, hatta kontrol dışı kullanımı teşvik edebileceğini belirtiyor. Kurum bunun yerine yönlendirme, denge ve farkındalık temelli yaklaşımlar öneriyor [3]. Bu öneri ajanlar için de geçerli: Çalışanların kendi iş akışlarını otomatikleştirme isteğini bastırmak yerine bu isteği güvenli bir kanala yönlendirmek gerekiyor.

Özellikle kod yazmadan ajan kurmayı sağlayan araçlar yaygınlaştıkça, BT ve bilgi güvenliği ekiplerinin "hangi ajan, kimin adına, hangi sisteme, hangi yetkiyle bağlı?" sorusuna cevap verebilmesi gerekecek. Bu envanter yoksa kişisel veri içeren bir sisteme bağlanan ajanın yaptığı bir hata, veri sorumlusu olarak doğrudan şirketin sorumluluğuna girer.

Temel hesap güvenliği adımları için [telefon ve hesap güvenliği rehberimize](/telefon-ve-hesap-guvenligi/), şirket verisini sızdırmadan yapay zekâ kullanmak için [ücretsiz yapay zekâ araçları rehberimize](/ucretsiz-yapay-zeka-araclari/) göz atabilirsiniz. İK sistemlerine bağlanan ajanlar için de [işe alımda yapay zekâ ajanları yazımız](/ik-yapay-zeka-ajanlari-workday-sap-metaview/) yol gösterici olabilir.

## Yapay zekâ ajanı güvenliği kontrol listesi: Şirketler ne yapmalı?

OWASP'ın ajan güvenliği rehberi ve aşırı yetki önerileri [4][6] ile KVKK yaklaşımı [3] temel alınarak:

1. **Envanter çıkarın.** Kullanılan yapay zekâ araçlarını, eklentileri, MCP sunucularını ve çalışanların kurduğu ajanları listeleyin. Her biri için sahibini, bağlı olduğu sistemleri ve yetkilerini kaydedin.
2. **En az yetki ilkesini uygulayın.** Ajana yalnızca görevi için gereken araçları ve izinleri verin. Okuma yeterliyse yazma ve silme yetkisi tanımlamayın [4][6].
3. **Ajanı kullanıcının kimliğiyle çalıştırın.** Paylaşılan yüksek yetkili hesaplar yerine kullanıcının kendi yetki kapsamı ve OAuth gibi sınırlı yetkilendirme kullanılsın [4].
4. **Yüksek etkili eylemlerde insan onayı şartı koyun.** E-posta gönderimi, toplu silme, ödeme ya da yetki değişikliği gibi eylemler insan onayı olmadan çalışmasın [4][6].
5. **Dış içeriğe güvenmeyin.** Ajanın okuduğu e-posta, belge ve web sayfalarını güvenilmeyen girdi olarak ele alın. Ajan ele geçirme bu kanaldan geliyor [6][7].
6. **Her eylemi kaydedin ve izleyin.** Araç çağrılarını, kararları ve sonuçlarını kayıt altına alın, olağandışı davranışlar için uyarı kurun [6].
7. **Üçüncü taraf bileşenleri inceleyin.** Herkese açık beceri, eklenti ve bağlantıları kullanmadan önce güvenlik açısından değerlendirin. OWASP bu riski ajan tedarik zinciri başlığında ele alıyor [5]. Webrazzi'nin aktardığına göre Pluto'nun ücretsiz Plutonium platformu da bu tür bileşenleri analiz etmeye yönelik [1].
8. **Politika ve eğitimi güncelleyin.** Kurumsal yapay zekâ politikasına ajanlar için ayrı bir bölüm ekleyin. Hangi verilerin ajanlarla işlenebileceğini açıkça yazın [3].
9. **Düzenli test edin.** Ajanı yayına almadan önce ve istem, araç ya da model değiştiğinde istem enjeksiyonu ve yetki aşımı senaryolarıyla test edin [6][7].

Çalışanların kurduğu ajanlar yasaklanarak durdurulabilecek bir eğilim değil. Ancak görünür, sınırlandırılmış ve denetlenebilir hâle getirilebilir. Bunu bugün yapan şirketler, yarının "gölge ajan" olaylarıyla daha az karşılaşacak.

## Sıkça sorulan sorular

### Gölge yapay zekâ nedir?

KVKK'nın tanımına göre üretken yapay zekâ araçlarının kurumun bilgisi, onayı veya kurumsal kontrolü dışında çalışanlar tarafından iş süreçlerinde kullanılması [3].

### Yapay zekâ ajanlarında "aşırı yetki" riski nedir?

OWASP bu riski LLM06:2025 "Excessive Agency" başlığıyla tanımlıyor. Kök neden genellikle aşırı işlevsellik, aşırı izin ya da aşırı özerklik. Örneğin e-posta özetlemek için kurulan bir eklenti mesaj gönderme yetkisine de sahipse, kötü amaçlı bir e-posta ajanı kandırıp hassas bilgileri saldırgana ilettirebilir [4].

### Ajan ele geçirme (agent hijacking) nedir?

NIST bünyesindeki CAISI'ye göre bir tür dolaylı istem enjeksiyonu. Saldırgan, ajanın işlediği bir e-postaya, dosyaya ya da web sitesine kötü amaçlı talimatlar yerleştirerek ajanı istenmeyen eylemlere yönlendiriyor [7].

### Çalışanların yapay zekâ kullanımını yasaklamak çözüm mü?

KVKK dokümanına göre tamamen yasaklamak uygulamada gerçekçi sonuçlar doğurmuyor, hatta kontrol dışı kullanımı teşvik edebiliyor. Kurum yönlendirme, denge ve farkındalık temelli yaklaşımlar öneriyor [3].

## Kaynaklar

1. Webrazzi, Candeğer Muradoğlu, "Siber güvenlik girişimi Pluto, toplamda 42,5 milyon dolar yatırım aldı", 14 Ekim 2026. <https://webrazzi.com/2026/10/14/siber-guvenlik-girisimi-pluto-toplamda-42-5-milyon-dolar-yatirim-aldi/> (Erişim: 15 Ekim 2026)
2. Verizon, "2026 Data Breach Investigations Report – Executive Summary" (PDF). <https://www.verizon.com/business/resources/executivebriefs/2026-dbir-executive-summary.pdf> (Erişim: 15 Ekim 2026)
3. KVKK, "İş Yerlerinde Üretken Yapay Zekâ Araçlarının Kullanımı", Şubat 2026 (PDF). <https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/MTY5YTdkNjdjNzJlMjM.pdf> (Erişim: 15 Ekim 2026)
4. OWASP Gen AI Security Project, "LLM06:2025 Excessive Agency". <https://genai.owasp.org/llmrisk/llm062025-excessive-agency/> (Erişim: 15 Ekim 2026)
5. OWASP Gen AI Security Project, "OWASP Top 10 for Agentic Applications – The Benchmark for Agentic Security in the Age of Autonomous AI", 9 Aralık 2025. <https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/> (Erişim: 15 Ekim 2026)
6. OWASP Cheat Sheet Series, "AI Agent Security Cheat Sheet". <https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html> (Erişim: 15 Ekim 2026)
7. NIST, "Technical Blog: Strengthening AI Agent Hijacking Evaluations", 17 Ocak 2025. <https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations> (Erişim: 15 Ekim 2026)
8. NIST, "AI Risk Management Framework". <https://www.nist.gov/itl/ai-risk-management-framework> (Erişim: 15 Ekim 2026)
