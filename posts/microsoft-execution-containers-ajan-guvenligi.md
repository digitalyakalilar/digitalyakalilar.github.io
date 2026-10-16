---
title: Yapay zekâ ajanı güvenlik izolasyonu: Microsoft Execution Containers (MXC) ne getiriyor?
date: 2026-10-16
updated: 2026-10-16
description: Microsoft, yapay zekâ ajanlarını dosya ve ağ sınırlarıyla izole eden Execution Containers'ı genel kullanıma açtı. Yapay zekâ ajanı güvenlik izolasyonu, gölge ajan riskine karşı OS düzeyinde ne vaat ediyor?
cover_title: Ajanları OS düzeyinde izole etmek
cover_icon: agentshield
category: dijital-guvenlik
seo_title: Yapay zekâ ajanı güvenlik izolasyonu: Microsoft MXC
meta_description: Yapay zekâ ajanı güvenlik izolasyonu: Microsoft Execution Containers (MXC) process, session ve MicroVM ile ajanları nasıl sınırlıyor? Kontrol listesi.
focus_kw: yapay zekâ ajanı güvenlik izolasyonu
keywords: yapay zekâ ajanı güvenlik izolasyonu, AI agent sandbox, Microsoft Execution Containers, ajan yetki sınırı, process container, Agent 365
cover_alt: Yapay zekâ ajanı güvenlik izolasyonu: Microsoft Execution Containers kapak görseli
---
Ajanlar dosyalara, ağa ve uygulamalara dokundukça verim artıyor; aynı anda yeni bir güvenlik yüzeyi açılıyor. Microsoft Windows Developer Blog'unda 7 Ekim 2026'da yayımlanan yazıya göre **Microsoft Execution Containers (MXC)** artık genel kullanıma açık ve ajanlar için politika güdümlü bir **containment** (izolasyon) katmanı sunuyor [1]. Bu yazıda **yapay zekâ ajanı güvenlik izolasyonu** konusunu MXC üzerinden inceliyor, Pluto / OWASP tartışmasıyla bağlıyor ve BT ekipleri için bir kontrol listesi veriyoruz.

## Üç sütun: Containment, identity, manageability

Microsoft'un çerçevesi üç başlıkta toplanıyor [1]:

1. **Containment** — ajanın erişebileceği dosya ve ağ hedeflerini sınırlamak
2. **Identity** — ajan etkinliğini kişiden ayırmak (Microsoft Entra / Agent 365 ile yakında)
3. **Manageability** — erişimi yönetmek ve ajan etkinliğini izlemek

MXC birinci sütunu sağlıyor. Geliştiriciler ve BT yöneticileri ajanın kullanabileceği kaynakları tanımlıyor; MXC uygun konteyner ile bu politikayı çalışma anında zorunlu kılıyor [1]. Politika ajanın kontrolü dışında kalıyor: Ajan kendine ek yetki veremiyor [1].

## Neden yönetilen bir sınır şart?

Microsoft'un örneği tanıdık: Bir kod ajanından web sitesini güncellemesi isteniyor. Depoya yazma ve derleme araçlarına ihtiyaç var; üretim sunucu yapılandırmasını **okuması** gerekebilir ama **değiştirmemesi** gerekir. Yönetilen sınır yoksa ajan, görevi bitirmenin en hızlı yolu diye üretim yapılandırmasını değiştirmeyi "mantıklı" bulabilir [1]. Containment bu sınırı modelden bağımsız uygular.

Bu, [gölge ajan yazımızda](/calisan-yapay-zeka-ajanlari-guvenlik-riski/) OWASP'ın "aşırı yetki" (Excessive Agency) uyarısıyla aynı çizgide: Sorun çoğu zaman aşırı işlev, aşırı izin veya aşırı özerklik.

## MXC backend spektrumu

Microsoft farklı iş yükleri için farklı izolasyon seviyeleri listeliyor [1]:

| Backend | Kullanılabilirlik | Ne için |
|---|---|---|
| Process container | Windows 11, macOS, Linux | Hafif, düşük gecikmeli işler; AppContainer / Seatbelt / Bubblewrap |
| Session container | Yalnızca Windows 11 | Uzun süren ajanlar; ayrı hesap, masaüstü, pano, girdi sınırı |
| WSL container (WSLc) | Yalnızca Windows 11 | Linux-öncelikli ajan araç zincirleri |
| MicroVM | Windows 11 ve Linux (deneysel) | Daha yüksek risk; donanım destekli izolasyon |

Politika alanları: containment tipi, süreç başlatma, dosya sistemi (okuma/yazma/yasak), ağ (giriş/çıkış), kullanıcı arayüzü erişimi [1].

## Öğrenme modları: Önce gözlemle, sonra kilitle

Yalnızca Windows'ta process container'lar ajan etkinlik raporu üretebiliyor. Üç mod var [1]:

| Mod | İzinsiz erişim | Rapor |
|---|---|---|
| Enforcement | Engellenir | Yok |
| Learning | Engellenir + kayda alınır | Var |
| Permissive | İzin verilir + kayda alınır | Var (politika yazımı için) |

İlk kurulumda politika meşru ihtiyaçları da kesebilir; Learning/Permissive bu boşlukları görmeye yarıyor [1].

## Kimler MXC kullanıyor?

Yazıya göre GitHub Copilot, OpenClaw, OpenAI Codex, Replit, LM Studio ve Unsloth AI hâlihazırda MXC destekliyor; Anthropic Claude Code, Box, Perplexity ve diğerleri destek açıklayacak. NVIDIA OpenShell'i MXC ile entegre etti. Windows 365 üzerinde MXC desteği genel kullanıma açıldı [1].

Temel hesap güvenliği için [telefon ve hesap güvenliği rehberimize](/telefon-ve-hesap-guvenligi/); İK sistemlerine bağlanan ajanlar için [işe alım ajanları yazımıza](/ik-yapay-zeka-ajanlari-workday-sap-metaview/) bakın.


## Türkiye'deki şirketler için pratik okuma

MXC Windows ağırlıklı bir platform özelliği; macOS/Linux process container desteği de var [1]. Türkiye'de karma cihaz filoları yaygındır: Ofis Windows 11, geliştirici Mac, fabrika terminali Linux. Bu durumda politika şemasını ortak tutup backend'i cihaza göre seçmek Microsoft'un önerdiği modele uyuyor [1].

KVKK açısından kritik nokta şu: Ajan kişisel veri içeren klasörlere veya müşteri sistemlerine bağlanacaksa, izolasyon sınırı teknik bir tercih değil, veri minimizasyonu aracıdır. Containment "ajana her şeyi verip ummak" ile "ajana yalnızca görev dosyasını vermek" arasındaki farkı işletim sistemi düzeyinde sabitler [1].

Bulut tarafında Windows 365 MXC desteğinin genel kullanıma açılması, ajanı yerel cihazda değil Cloud PC üzerinde izole çalıştırmayı da mümkün kılıyor [1]. Bu, saha laptop'larında ajan denemelerini merkezî politikalaya almak isteyen BT ekipleri için ek bir seçenek.

## Kontrol listesi: Yapay zekâ ajanı güvenlik izolasyonu

- [ ] Her ajan için en az yetki politikası (dosya + ağ + UI) yazılı mı?
- [ ] Üretim yapılandırması / sırlar ajanın yazma kapsamı dışında mı?
- [ ] Kod ajanları MXC veya eşdeğer sandbox içinde mi çalışıyor?
- [ ] Learning modunda aktivite raporu toplanıp politika sıkılaştırıldı mı?
- [ ] Ajan kimliği kullanıcı kimliğinden ayrılabiliyor mu? (Agent 365 yol haritası [1])
- [ ] Intune / MDM ile kurumsal MXC politikası planlandı mı?
- [ ] Çalışanların kurduğu ajanlar envanterde mi? ([gölge ajan kontrol listesi](/calisan-yapay-zeka-ajanlari-guvenlik-riski/))

## Sıkça sorulan sorular

### Yapay zekâ ajanı güvenlik izolasyonu nedir?

Ajanın (veya ürettiği kodun) erişebileceği dosya, ağ ve arayüz kaynaklarını, ajanın kendi kararından bağımsız olarak işletim sistemi / konteyner katmanında sınırlamak. MXC bunu politika güdümlü konteynerlerle yapıyor [1].

### MXC bir antivirüs mü?

Hayır. Containment katmanı: Ne yapılabileceğini sınırlar. Kimlik ve yönetilebilirlik ayrı sütunlar [1].

### Session container neden önemli?

Ajanı kullanıcının etkileşimli oturumundan ayırır; masaüstü, pano ve girdi sınırları ayrıdır [1]. Uzun süren otomasyonlar için uygun.

### Yalnızca Windows'ta mı çalışır?

Process container Windows, macOS ve Linux'ta; session ve WSL yalnızca Windows 11'de; MicroVM Windows 11 ve Linux'ta deneysel [1].

### Bu, Pluto gibi ajan güvenlik ürünlerinin yerini alır mı?

Tamamlayıcı. Pluto tipi ürünler ajan envanteri ve davranış izlemeye odaklanır; MXC çalışma anı izolasyonu sağlar [1]. İkisi birlikte savunma derinliği oluşturur.

## Kaynaklar

1. Windows Developer Blog, Logan Iyer, "Microsoft Execution Containers: Policy-driven containment for AI agents", 7 Ekim 2026. <https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/> (Erişim: 16 Ekim 2026)
