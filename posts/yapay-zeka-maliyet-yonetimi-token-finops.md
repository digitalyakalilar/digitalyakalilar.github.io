---
title: Yapay zekâ maliyet yönetimi: Token faturası büyümeden FinOps ile kontrol
date: 2026-10-19
updated: 2026-10-19
description: Bulut ve yapay zekâ harcamalarını tek yerde yöneten North 60 milyon dolar yatırım aldı; FinOps uygulayıcılarının %98'i artık YZ harcamasını yönetiyor. Yapay zekâ maliyet yönetimi için token fiyatlamasının gizli kalemleri ve kontrol listesi.
cover_title: Token faturası büyümeden kontrol
cover_icon: costs
category: yapay-zeka-verimlilik
seo_title: Yapay zekâ maliyet yönetimi: Token ve FinOps rehberi
meta_description: Yapay zekâ maliyet yönetimi neden şart? FinOps ekiplerinin %98'i YZ harcaması yönetiyor, North 60 milyon dolar aldı. Token fiyatlamasının gizli kalemleri.
focus_kw: yapay zekâ maliyet yönetimi
keywords: yapay zekâ maliyet yönetimi, token maliyeti nedir, FinOps nedir, yapay zekâ maliyeti, bulut maliyet optimizasyonu, North TokenFlow, FinOps for AI
cover_alt: Yapay zekâ maliyet yönetimi: Token ve FinOps rehberi kapak görseli
---
Şirketlerde yapay zekâ kullanımı arttıkça yeni bir fatura kalemi büyüyor: model başına, kullanıcı başına ve en çok da **token** başına ödenen ücretler. Webrazzi'nin 16 Ekim 2026'da aktardığına göre bulut ve yapay zekâ harcamalarını tek platformda toplayan ABD merkezli North, 60 milyon dolarlık B serisi yatırım aldı [1]. Bu haber, **yapay zekâ maliyet yönetimi** konusunun artık mühendislik ekibinin yan işi değil, finans ve operasyonun ortak gündemi olduğunu gösteriyor. Bu yazıda FinOps verileri, token fiyatlamasının gizli kalemleri ve Türkiye'deki şirketler için bir kontrol listesiyle konuyu ele alıyoruz.

## Haber: North 60 milyon dolar yatırım aldı

Webrazzi'nin haberine göre North'un B serisi turuna PeakSpan Capital liderlik etti; şirket 2023'te Matt Biringer ve Yassine Açoine tarafından kuruldu [1]. Platform AWS, Microsoft Azure ve Google Cloud harcamalarını tek yerde topluyor, gereksiz harcama alanlarını tespit ediyor ve yeni bir özellik devreye alındığında ortaya çıkabilecek ek maliyeti hesaplamaya çalışıyor [1].

Şirketin kendi açıklamasına göre North, yaklaşık 2 milyar dolarlık yönetilen bulut harcaması üzerinden müşterilerine 400 milyon dolardan fazla tasarruf sağladı; son sürüm North v3 ile Azure desteği eklendi, OpenAI, Anthropic ve Snowflake ile yerel entegrasyonlar geldi [2]. Bu rakamlar şirket beyanı; bağımsız doğrulaması yok.

Yapay zekâ tarafındaki ürün TokenFlow: model kullanımını, maliyet atamasını, bütçeleri ve finansal kontrolleri bulut altyapısıyla aynı sistemde topluyor [2]. Ürün sayfasında TokenFlow'un token harcamasını modellere, sağlayıcılara ve ekiplere göre izleyip sınır (cap) koyabildiği ve şu an seçili kullanıcılarla beta aşamasında olduğu belirtiliyor [3].

North CEO'su Biringer'in SiliconANGLE'a söylediği cümle konunun özünü veriyor: Piyasanın geri kalanı optimizasyonu bir mühendislik sorunu olarak görüyor; ona göre bu bir iş sorunu [4].

## Yapay zekâ maliyet yönetimi neden ayrı bir disiplin oldu?

FinOps Foundation'ın Şubat 2026'da yayımladığı altıncı State of FinOps anketi, toplam yıllık bulut harcaması 83 milyar doları aşan şirketleri temsil eden 1.192 katılımcıya dayanıyor [5]. Bulgular:

| Gösterge | 2024 | 2025 | 2026 |
|---|---|---|---|
| YZ harcamasını yöneten FinOps ekibi | %31 | %63 | **%98** [5][6] |
| SaaS harcamasını yöneten (veya planlayan) | — | %65 | %90 [5] |
| Lisans maliyetini yöneten | — | %49 | %64 [6] |
| Veri merkezi maliyetini yöneten | — | %36 | %48 [5] |

Alıntılanabilir istatistik: **FinOps ekiplerinin %98'i artık yapay zekâ harcamasını yönetiyor; iki yıl önce bu oran %31'di** [5]. Rapora göre "FinOps for AI" ileriye dönük bir numaralı öncelik, yapay zekâ maliyet yönetimi de ekiplerin edinmek istediği bir numaralı beceri [5]. Birçok kuruma YZ yatırımlarını optimizasyon tasarruflarıyla kendi kendine finanse etmesi söyleniyor [5].

## Token maliyeti nedir? Faturayı büyüten 4 gizli kalem

FinOps Foundation'ın token fiyatlaması üzerine çalışma grubu makalesi, ilan edilen "token başına fiyatın" yanıltıcı olabileceğini anlatıyor [7]:

| Kalem | Ne oluyor? | Pratik etkisi |
|---|---|---|
| Girdi–çıktı farkı | Çıktı tokenları genellikle girdi tokenlarından 3-5 kat pahalı [7] | Uzun özet ve metin üreten senaryolar daha pahalı |
| Modalite primi | Görsel yorumlamak eşdeğer metnin kabaca iki katı; bazı amiral modellerde ses girdisi metnin 8 katından fazla [7] | Görsel/ses içeren iş akışları ayrı bütçelenmeli |
| Model katmanı | En gelişmiş model en yüksek token fiyatına sahip [7] | Her iş için en pahalı model gerekmeyebilir |
| Bağlam penceresi şişmesi | API'ler çoğunlukla durumsuz; çok turlu sohbette geçmiş her istekte yeniden gönderiliyor [7] | Uzun sohbetlerde maliyet hızla katlanır |

Makale, maliyeti düşürmek için istem önbelleğe alma (prompt caching) ve toplu işleme (batch) gibi tekniklerin yanı sıra en ucuz modeli seçmek yerine "kullanım senaryosu başına birim maliyet" yaklaşımını öneriyor [7].

## Türkiye'de durum: YZ kullanan şirket oranı ikiye katlandı

TÜİK'in Ekim 2026'da yayımladığı verilere göre yapay zekâ kullanan girişimlerin oranı %7,5'ten %14'e çıktı [8]. Hürriyet Daily News'ün aktardığı aynı bültene göre YZ kullanmayan şirketler en çok iç uzmanlık eksikliğini (%72,3), sorumluluk belirsizliğini (%66,4) ve gizlilik risklerini (%65,4) gerekçe gösteriyor [9].

Yani Türkiye'de yapay zekâ maliyet yönetimi henüz çoğu şirket için erken bir konu; ama kullanım ikiye katlanırken maliyet disiplinini baştan kurmak, sonradan "fatura şoku" yaşamaktan daha kolay.

## Hangi yaklaşım kime uygun?

| Yaklaşım | Uygun olduğu durum | Sınırı |
|---|---|---|
| Sağlayıcı konsolu ve tablo | Tek model sağlayıcısı, birkaç ekip | Ekip bazında atama ve tahmin zor |
| İç FinOps süreci (etiketleme, bütçe, uyarı) | Bulut FinOps pratiği olan şirket | YZ token verisini ayrıca bağlamak gerekir |
| Birleşik platform (North gibi) | Çok bulut + çok model sağlayıcısı | Platform maliyeti ve veri erişimi değerlendirilmeli; tasarruf rakamları satıcı beyanı [2] |

Hangi yolu seçerseniz seçin, yapay zekâ ajanlarının nereye bağlandığını bilmek maliyet kadar güvenlik için de önemli. Bu konuda [çalışanların kurduğu yapay zekâ ajanları yazımıza](/calisan-yapay-zeka-ajanlari-guvenlik-riski/) ve [Microsoft Execution Containers incelememize](/microsoft-execution-containers-ajan-guvenligi/) bakabilirsiniz. Küçük ekipler için başlangıç noktası olarak [ücretsiz yapay zekâ araçları rehberimiz](/ucretsiz-yapay-zeka-araclari/) de faydalı.

## Kontrol listesi: Yapay zekâ maliyet yönetimi

- [ ] Hangi ekip hangi model/sağlayıcıyı kullanıyor; envanter çıkarıldı mı?
- [ ] Her API anahtarı bir ekibe ve kullanım senaryosuna etiketlendi mi?
- [ ] Ekip ve senaryo bazında aylık bütçe ve uyarı eşikleri tanımlandı mı?
- [ ] Girdi ve çıktı tokenları ayrı raporlanıyor mu?
- [ ] Uzun sohbetlerde bağlam özetleme veya önbellekleme uygulanıyor mu?
- [ ] Basit işler için daha küçük model seçeneği test edildi mi?
- [ ] "Senaryo başına maliyet" (ör. özet başına, bilet başına) KPI'ı ölçülüyor mu?
- [ ] YZ faturası finans ekibinin aylık bulut raporuna dahil mi?

## Sıkça sorulan sorular

### Yapay zekâ maliyet yönetimi nedir?

Yapay zekâ modellerine, API'lere ve altyapıya yapılan harcamayı görünür kılmak, ekiplere atamak, bütçelemek ve optimize etmek. State of FinOps 2026'ya göre FinOps ekiplerinin %98'i artık YZ harcamasını yönetiyor [5].

### Token maliyeti nedir?

Dil modellerinin işlediği metin parçaları (token) için ödenen ücret. FinOps Foundation'a göre çıktı tokenları genellikle girdi tokenlarından 3-5 kat pahalı; görsel ve ses gibi modaliteler daha da pahalı olabiliyor [7].

### FinOps nedir?

FinOps Foundation'ın tanımıyla teknolojinin iş değerini en üst düzeye çıkaran, zamanında veriye dayalı karar almayı sağlayan ve mühendislik, finans ve iş ekipleri arasındaki iş birliğiyle finansal sorumluluk yaratan bir operasyonel çerçeve ve kültürel pratik [10]. Vakıf misyonunu 2026'da "bulutun değeri"nden "teknolojinin değeri"ne genişletti [5].

### North nedir, ne yapıyor?

ABD merkezli bir bulut ve yapay zekâ maliyet yönetimi platformu. Webrazzi'ye göre AWS, Azure ve Google Cloud harcamalarını tek yerde topluyor; TokenFlow çözümüyle YZ model kullanımı ve maliyetini izliyor [1].

### Yapay zekâ faturası en çok nerede şişer?

FinOps Foundation'a göre en büyük gizli maliyet, çok turlu sohbetlerde geçmişin her istekle yeniden gönderilmesinden kaynaklanan bağlam penceresi şişmesi [7].

## Kaynaklar

1. Webrazzi, "Bulut ve yapay zeka maliyet yönetimi girişimi North, 60 milyon dolar yatırım aldı", 16 Ekim 2026. <https://webrazzi.com/2026/10/16/bulut-ve-yapay-zeka-maliyet-yonetimi-girisimi-north-60-milyon-dolar-yatirim-aldi/> (Erişim: 19 Ekim 2026)
2. North.cloud Newsroom, "North.cloud Raises $60M Series B to Unify Spend Intelligence and Enable Full Automation Across Cloud, AI, and Data", 15 Ekim 2026. <https://north.cloud/newsroom/north-series-b-release> (Erişim: 19 Ekim 2026)
3. North.cloud, "TokenFlow" ürün sayfası. <https://north.cloud/features/tokenflow> (Erişim: 19 Ekim 2026)
4. SiliconANGLE, Mike Wheatley, "North.cloud bags $60M in funding to help businesses keep runaway cloud costs in check", 15 Ekim 2026. <https://siliconangle.com/2026/10/15/north-cloud-bags-60m-in-funding-to-help-businesses-keep-runaway-cloud-costs-in-check/> (Erişim: 19 Ekim 2026)
5. FinOps Foundation, "State of FinOps 2026 Report". <https://data.finops.org/> (Erişim: 19 Ekim 2026)
6. The Linux Foundation, "State of FinOps Survey: AI Value and Skills Top Priorities as FinOps Matures Across Technology Value", 19 Şubat 2026. <https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1> (Erişim: 19 Ekim 2026)
7. FinOps Foundation, "GenAI FinOps: How Token Pricing Really Works". <https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/> (Erişim: 19 Ekim 2026)
8. Anadolu Ajansı, Mertkan Oruç, "Türkiye yapay zekayı en çok bilişimde, en az inşaatta kullanıyor" (TÜİK Yapay Zekâ İstatistikleri 2026), 3 Ekim 2026. <https://www.aa.com.tr/tr/bilim-teknoloji/turkiye-yapay-zekayi-en-cok-bilisimde-en-az-insaatta-kullaniyor/4076782> (Erişim: 19 Ekim 2026)
9. Hürriyet Daily News, "AI usage among individuals, businesses in Türkiye doubles", 2 Ekim 2026. <https://www.hurriyetdailynews.com/ai-usage-among-individuals-businesses-in-turkiye-doubles-227631> (Erişim: 19 Ekim 2026)
10. FinOps Foundation, "What is FinOps?" (güncelleme: Mart 2026). <https://www.finops.org/introduction/what-is-finops/> (Erişim: 19 Ekim 2026)
