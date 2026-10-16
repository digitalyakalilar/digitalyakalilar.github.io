---
title: Sistemleri değiştirmeden işe alım yapay zekâsı: Providence ve IBM'in RITA ajanı ne öğretiyor?
date: 2026-10-16
updated: 2026-10-16
description: Providence, Oracle HCM'ini sökmeden IBM watsonx Orchestrate üzerinde RITA ajanını kurdu. İdari yükün yüzde 90 azaldığı iddia ediliyor. Sistem değiştirmeden işe alım yapay zekâsı Türkiye'deki İK ekipleri için ne anlama geliyor?
cover_title: Sistemleri sökmeden işe alım ajanı
cover_icon: hragents
category: ik-teknolojileri
seo_title: Sistem değiştirmeden işe alım yapay zekâsı: Providence RITA
meta_description: Sistem değiştirmeden işe alım yapay zekâsı mümkün mü? Providence ve IBM'in RITA ajanı Oracle HCM üstünde yüzde 90 idari yük azalması iddiasıyla ne öğretiyor?
focus_kw: sistem değiştirmeden işe alım yapay zekâ
keywords: sistem değiştirmeden işe alım yapay zekâ, İK yapay zekâ ajanı, Oracle HCM ajan, iç transfer otomasyonu, watsonx Orchestrate, işe alım idari yükü
cover_alt: Sistem değiştirmeden işe alım yapay zekâsı: Providence ve IBM RITA ajanı kapak görseli
---
Büyük İK yazılımlarını yenilemek pahalı, riskli ve uzun sürer. Ekim 2026'da Providence Health ile IBM'in paylaştığı örnek, başka bir yolu gösteriyor: Mevcut Oracle Fusion Cloud HCM ve Recruiting ortamını yerinde bırakıp üstüne bir yapay zekâ ajanı orkestre etmek. RITA (Requisition and Internal Transfer Agent), IBM watsonx Orchestrate üzerinde çalışan bir "dijital işçi" olarak tanıtılıyor [1]. Bu yazıda **sistem değiştirmeden işe alım yapay zekâsı** yaklaşımını kaynaklarıyla inceliyor, Workday ve SAP'nin ajan duyurularıyla karşılaştırıyor ve Türkiye'deki İK ekipleri için pratik bir kontrol listesi çıkarıyoruz.

## Providence neden ajan kurdu?

Providence, ABD'de yaklaşık 119 bin bakıcıya (caregiver) sahip büyük bir sağlık sistemi [1]. IBM'e göre işe alım çok parçalı hâle gelmişti: Yöneticiler birden fazla sistem arasında geziyor, onaylar manuel ilerliyor, iç hareketlilik yavaşlıyordu. Kritik ayrıntı şu: Yıllık işe alım faaliyetinin neredeyse yarısı iç transferlerden geliyordu; süreç o kadar ağırdı ki bazı çalışanlar kurum içinde geçiş yapmak yerine ayrılıp dış aday olarak yeniden başvurmayı tercih ediyordu [1].

Şirket, çekirdek İK sistemlerini değiştirmek yerine iş akışını yeniden tasarlamayı seçti. IBM Consulting; Oracle uzmanlığı, yapay zekâ mühendisliği ve deneyim tasarımını bir araya getirerek tıkanan noktaları tespit etti ve RITA'yı mevcut Oracle Fusion Cloud HCM ile Oracle Fusion Cloud Recruiting üzerinde orkestre etti [1][2].

## RITA ne yapıyor?

IBM'in açıklamasına göre RITA şu adımları sadeleştiriyor [1]:

- Pozisyon talebi (requisition) oluşturma
- Onay yönlendirme
- İç transferler
- İlan / iş pazarlama içeriği
- İşe alım durumu güncellemeleri

Ajan, Oracle ortamının dışındaki diğer sistem ve veri kaynaklarına da bağlanabiliyor; IBM bu kaynakları tek tek adlandırmadı [1]. Önemli olan mimari seçim: Yeni bir İK platformu değil, watsonx Orchestrate'in "ajanik kontrol düzlemi" üzerinden mevcut sistemlerin orkestrasyonu [1].

IBM case study'sine göre RITA, Providence'ın yedi eyaletlik sisteminde tüm pozisyon talebi oluşturma ve tüm "basit" iç transferleri üstlenecek şekilde kurum genelinde kullanılıyor [2].

## Paylaşılan sonuçlar (şirket iddiası)

| Metrik | IBM / Providence iddiası |
|---|---|
| İşe alım yöneticisinin idari eforu | %90 azalma [1] |
| İç transferle yeni role başlama | Ortalama 12 gün daha erken [1] |
| Transfer maliyeti | %60 düşüş [1] |
| Süreç doğruluğu | %70'e varan iyileşme [1] |

Bu rakamlar basın bülteni ve vaka çalışmasından geliyor; bağımsız denetim, örneklem büyüklüğü veya baz çizgi tanımları kamuoyuna ayrıntılı açılmadı. Üçüncü taraf özetlerde aynı rakamların daha erken tarihlerde de anıldığına dikkat çekiliyor [3]. Yazıda bunları "kanıtlanmış evrensel sonuç" değil, **ölçülebilir hedef koyulmuş bir proje örneği** olarak okuyoruz.

## Karşılaştırma: RITA vs Workday / SAP ajanları

Aynı haftalarda Workday "otopilot" ajanlarını [4], SAP ise SuccessFactors 2H 2026 ile "Otonom İK" vizyonunu duyurdu. RITA'nın farkı ürün kataloğu değil, **entegrasyon stratejisi**:

| | Providence + IBM RITA | Workday Autopilot | SAP SuccessFactors |
|---|---|---|---|
| Temel yaklaşım | Mevcut Oracle HCM üstüne orkestrasyon [1] | Platforma gömülü otopilot ajanlar [4] | HCM sürümüne gömülü ajanlar |
| Tipik kullanıcı | Zaten Oracle kullanan büyük kurum | Workday müşterisi | SAP SuccessFactors müşterisi |
| Öne çıkan vaat | İdari süre ve iç hareketlilik [1] | Aday bulma + onaylı iletişim [4] | Eleme, eşleştirme, mülakat ajanları |
| Sistem değiştirme | Hayır [1] | Hayır (kendi platformunda) | Hayır (kendi platformunda) |

Türkiye'de Workday veya SAP kullanan ekipler için [işe alımda yapay zekâ ajanları karşılaştırma yazımız](/ik-yapay-zeka-ajanlari-workday-sap-metaview/) doğrudan ilgili. RITA örneği ise özellikle **Oracle (veya benzeri) HCM'i olan, platform değiştirmeye hazır olmayan** kurumlara ders veriyor.

## Türkiye'deki İK ekipleri için ne anlama geliyor?

1. **Önce süreç, sonra ajan.** Providence tarafında Carol McDaniel ve Greg Till'in vurgusu, teknolojiden önce bakıcıların kariyer hareketini kolaylaştırmak [1]. Kötü bir onay zincirini otomatikleştirmek, kötü süreci hızlandırır.
2. **KVKK'daki otomatik karar hakkı duruyor.** 6698 sayılı Kanun'un 11. maddesi, münhasıran otomatik sistemlerle aleyhe sonuç doğuran analizlere itiraz hakkını tanıyor. İç transfer veya eleme kararında nihai insan onayı hâlâ kritik — bu noktayı [Workday/SAP yazımızda](/ik-yapay-zeka-ajanlari-workday-sap-metaview/) da işlemiştik.
3. **Güvenlik envanteri şart.** Ajanın hangi sisteme, hangi yetkiyle bağlandığı kayıt altına alınmalı. Çalışanların kendi kurduğu ajan riskleri için [gölge ajan güvenliği yazımıza](/calisan-yapay-zeka-ajanlari-guvenlik-riski/) bakın.
4. **Ölçüm tanımını satın.** "%90 azalma" gibi iddiaları kopyalamadan önce kendi baz çizginizi (talep başına dakika, transfer süresi, hata oranı) yazın.

## Kontrol listesi: Sistem değiştirmeden işe alım yapay zekâsı

- [ ] Hangi adımlar ajan orkestre edecek, hangisi yalnızca insan? (talep, onay, ilan, transfer, ret)
- [ ] Mevcut HCM/ATS API ve onay motoru ajanla uyumlu mu?
- [ ] Her ajan eylemi kimlik, zaman damgası ve gerekçeyle loglanıyor mu?
- [ ] Adaya veya çalışana giden mesaj insan onayından geçiyor mu?
- [ ] İç transfer ile dış işe alım için ayrı özerklik seviyeleri tanımlandı mı?
- [ ] KVKK aydınlatma ve itiraz süreçleri ajan senaryosuna güncellendi mi?
- [ ] Başarı metrikleri (süre, maliyet, doğruluk, çalışan deneyimi) proje öncesi ölçüldü mü?

Aday tarafı için [LinkedIn profil ipuçları rehberimize](/linkedin-profil-ipuclari/) de göz atabilirsiniz.

## Sıkça sorulan sorular

### Sistem değiştirmeden işe alım yapay zekâsı mümkün mü?

Providence örneğinde Oracle Fusion Cloud HCM ve Recruiting yerinde bırakıldı; RITA watsonx Orchestrate üzerinden bu sistemleri orkestre etti [1]. Yani ajan, çekirdek İK platformunun yerine değil üstüne kuruldu.

### RITA neyin kısaltması?

Requisition and Internal Transfer Agent — pozisyon talebi ve iç transfer ajanı [1].

### Paylaşılan yüzde 90 ve 12 gün rakamları bağımsız doğrulandı mı?

Hayır. Rakamlar IBM basın bülteni ve vaka çalışmasından geliyor [1][2]; bağımsız denetim ayrıntısı kamuoyuna açılmadı.

### Bu yaklaşım KOBİ'ler için de geçerli mi?

Mimari ders (önce süreç, sonra orkestrasyon) ölçekten bağımsız. Ancak watsonx Orchestrate + Oracle Fusion tipi bir kurulum büyük kurum profiline daha yakın; KOBİ'ler aynı prensibi kendi ATS/İK araçlarının API'leri üzerinden daha hafif ajanlarla deneyebilir.

### Workday veya SAP kullanan şirket RITA'ya bakmalı mı?

Doğrudan değil. Kendi platformunun ajan özelliklerini (Workday Autopilot, SuccessFactors ajanları) değerlendirmeli [4]. RITA, özellikle mevcut Oracle yığınını korumak isteyenler için örnek.

## Kaynaklar

1. IBM Newsroom, Jennifer Edeline, "Providence Health Collaborates with IBM Using AI to Reduce Hiring Admin Time Without Replacing a Single System", 7 Ekim 2026. <https://newsroom.ibm.com/2026-10-07-providence-health-collaborates-with-ibm-using-ai-to-reduce-hiring-admin-time-without-replacing-a-single-system> (Erişim: 16 Ekim 2026)
2. IBM, "Orchestrating a better way to hire and grow talent" (Providence Health case study). <https://www.ibm.com/case-studies/providence-health> (Erişim: 16 Ekim 2026)
3. Data Phoenix, "Providence deploys IBM AI agent across existing HR systems", 7 Ekim 2026. <https://dataphoenix.info/news/providence-ibm-rita-hiring-ai-agent> (Erişim: 16 Ekim 2026)
4. Workday Newsroom, "Workday Launches Autopilot Agents That Get Real Work Done Across HR, Finance, and IT", 13 Ekim 2026. <https://newsroom.workday.com/2026-10-13-Workday-Launches-Autopilot-Agents-That-Get-Real-Work-Done-Across-HR,-Finance,-and-IT> (Erişim: 16 Ekim 2026)
