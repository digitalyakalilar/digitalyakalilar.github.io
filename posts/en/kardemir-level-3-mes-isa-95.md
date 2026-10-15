---
title: KARDEMİR moves 27 plants to Level 3: Why ISA-95 and MES matter for factories
date: 2026-10-15
updated: 2026-10-15
description: Turkish steelmaker Karabük Demir Çelik is building an ISA-95-based production management layer between ERP and shop-floor automation, and tracking ladles and torpedo cars with image processing. We look at the project, the ISA-95 levels and the lessons for manufacturers in Türkiye.
cover_title: KARDEMİR goes Level 3 with MES
cover_icon: mes
category: endustri-4-0
tr: kardemir-seviye-3-mes-isa-95
seo_title: ISA-95 levels and MES: KARDEMİR's Level 3 rollout
meta_description: What are the ISA-95 levels and where does MES fit? KARDEMİR's Level 3 production management rollout across 27 plants and the lessons for manufacturers.
focus_kw: ISA-95 levels
keywords: ISA-95 levels, ISA-95, MES vs ERP, ISA-95 Level 3, manufacturing execution system, IEC 62264, KARDEMİR
cover_alt: ISA-95 levels and MES: KARDEMİR's Level 3 production management rollout, cover image
---
Karabük Demir ve Çelik Fabrikaları (KARDEMİR), a company with a significant place in Türkiye's industrial history, has gone public with a wide-ranging project to move its production onto a data-driven footing. According to a company statement carried by İhlas News Agency (İHA) on October 9, KARDEMİR plans to roll out a Level 3 Production Management System, developed on the international ISA-95 approach, across 27 plants by mid-2027 [1]. The project also includes image processing and AI applications. Below, we use KARDEMİR's project to explain the ISA-95 levels and where MES fits.

The story offers a concrete example of how digital transformation should be approached in heavy industry. Let's look at the project first, then at the ISA-95 logic behind it.

## What does the project involve?

According to the statement, the Level 3 Production Management System creates a central production management layer between enterprise planning systems and the Level 2 expert automation and process control systems on the shop floor [1]. The company sums up what the system does: production orders, quality and inventory data, material movements and traceability data are managed on a shared structure, strengthening data integrity along the production chain [1].

In the first phase, the Steel Production and Continuous Casting processes are being brought into active use. KARDEMİR says this improves the traceability of production movements and data standardization, while reducing the need for manual data collection and consolidation [1].

Perhaps the most instructive part of the statement is its insistence that this is "not just a software or automation project". According to the company, production methods, data entry points, production flows between plants and existing business processes are being examined in detail, with processes redesigned where needed. The aim is to build accumulated field knowledge, from workers and foremen to engineers and managers, into the system design [1].

## Image processing: A new data source

The second pillar of the project is generating new data from the floor. KARDEMİR combines data from Level 2 systems with information from image processing and feeds it into Level 3. As part of this, it is working on automatically recognizing critical carriers such as ladles and torpedo cars with image processing and tracking their movements [1].

The goals fall under three headings: monitoring carrier movements inside the plant in real time, reducing manual data entry and automatically linking movement data to production processes. The overall aim is greater end-to-end production traceability [1].

Knowing in what order, when and where ladles and torpedo cars carrying molten metal move is critical for both efficiency and quality traceability. Having that information come automatically from cameras rather than from records keyed in by operators directly affects the quality of the data feeding the Level 3 layer.

## ISA-95 levels explained: What does "Level 3" mean?

ISA-95, the reference KARDEMİR uses, is an international series of standards developed by the International Society of Automation (ISA) and also known as IEC 62264. According to ISA, its purpose is to define the exchange of information between an enterprise's business systems and its manufacturing control systems [2]. The model has five levels [2]:

| Level | Scope | Typical systems |
|---|---|---|
| 0 | Physical production process | Machinery, field assets |
| 1 | Sensing and manipulating the process | Sensors, valves, smart devices |
| 2 | Monitoring and supervisory control | PLC, DCS |
| 3 | Manufacturing operations management | MES, SCADA |
| 4 | Business planning and logistics | ERP |

ISA notes that the standard primarily deals with the interface between Levels 3 and 4 [2]. In other words, it defines how an ERP decision such as "make this much of this product" reaches the floor, and how what actually happened on the floor flows back to the ERP. The layer KARDEMİR is building fills exactly that gap.

According to ISA, the standard is technology-agnostic: it defines activities, not products. That is why it remains widely used as a reference architecture for describing boundaries between systems in the era of Industry 4.0 and the Internet of Things [2]. It also helps IT and manufacturing teams agree on common terms in integration projects, and aims to reduce the risk, cost and errors of implementing them [2].

## Analysis: The real investment is in data discipline

Three lessons stand out from the KARDEMİR example.

**First, sequencing.** The company positions AI alongside Level 3, not instead of it. Even image-processing output is not sent to a standalone dashboard but into the shared structure where production orders and traceability records live [1]. Given how often AI projects stall on "where is the data, who owns it and how reliable is it?", this sequencing looks like a deliberate choice.

**Second, process design.** The space the statement gives to redesigning processes and capturing field knowledge [1] is a reminder that MES projects are as much organizational as technical.

**Third, staged rollout.** The first phase starts with steel production and continuous casting, with expansion to 27 plants planned by mid-2027 [1]. This reduces the risk of spreading across the whole site before value has been proven in a critical process.

## What it means for companies in Türkiye

KARDEMİR's project also lines up with the public agenda for the digital transformation of Turkish industry. Speaking at the IPA II Closing Conference on October 14, Ahmet Halit Hatip, Director General for EU and Foreign Relations at the Ministry of Industry and Technology, said they were accelerating the digital transformation of manufacturing under IPA III and bringing 300 businesses into digital transformation [3].

Not every manufacturer operates at KARDEMİR's scale. But the ISA-95 levels offer a checklist that works at any size: is there a layer between your ERP (Level 4) and your machines (Levels 0–2) that manages production orders, quality and traceability, or does that work still run on spreadsheets and manually entered records?

For SMEs that have not yet measured their digital maturity, TÜBİTAK TÜSSİDE's DDX+ model offers an official starting point that assesses processes and data management [4]. See our [DDX+ guide](/en/tubitak-ddx-digital-maturity-sme-guide/) for details.

Related reading: in our article on [AI agents in the supply chain](/en/supply-chain-ai-agents-warehouse-digital-workers/) we cover SAP's Manufacturing Assistant for the shop floor, and our [AI agent security checklist](/en/employee-built-ai-agents-security-risk/) looks at the permission risks of AI tools connected to production systems.

## Practical takeaways

1. **Map your levels.** List your plant's systems against ISA-95's five levels and identify which data is carried by hand between Levels 3 and 4 [2].
2. **Define data first, then buy software.** Agree common definitions for production orders, batches, quality results and stock movements. Without a shared data structure, neither MES nor AI will deliver the expected value [1][2].
3. **Choose the pilot area wisely.** As KARDEMİR did [1], start with a critical process where traceability problems are most expensive.
4. **Treat manual data entry as a target metric.** The number of manually keyed records and the time spent on consolidation can be concrete measures of the project's success.
5. **Bring the floor into the design.** Capturing operator and foreman knowledge in the system design prevents screens that nobody uses [1].
6. **Plan cybersecurity from day one.** As connections between Level 2 and Levels 3/4 grow, operational technology (OT) security matters more. The ISA/IEC 62443 series provides the core standards framework for securing industrial automation and control systems [5].

KARDEMİR's project shows that digital transformation in heavy industry starts not with flashy AI demos but with a solid production management layer. Whether it hits its mid-2027 target will be a benchmark worth watching for the sector.

## Frequently asked questions

### What is ISA-95?

An international series of standards developed by the International Society of Automation (ISA), also known as IEC 62264. Its purpose is to define the exchange of information between an enterprise's business systems and its manufacturing control systems [2].

### What are the ISA-95 levels?

The model has five levels: Level 0 is the physical production process, Level 1 sensing and manipulating the process, Level 2 monitoring and supervisory control (PLC, DCS), Level 3 manufacturing operations management (MES, SCADA) and Level 4 business planning and logistics (ERP) [2].

### What is the difference between MES and ERP?

In the ISA-95 model, ERP sits at Level 4 and handles business planning and logistics, while MES sits at Level 3 and manages manufacturing operations. The standard deals primarily with the interface between these two levels [2].

### When will KARDEMİR's Level 3 project be complete?

According to the company, the system will be rolled out across 27 plants by mid-2027. The first phase brings the Steel Production and Continuous Casting processes into active use [1].

## References

1. İhlas Haber Ajansı (İHA), "KARDEMİR'de dijital üretim dönemi: 27 tesiste devreye alınacak" (in Turkish), October 9, 2026. <https://www.iha.com.tr/karabuk-haberleri/kardemirde-dijital-uretim-donemi-27-tesiste-devreye-alinacak-497803969> (Accessed: October 15, 2026)
2. International Society of Automation (ISA), "ISA-95 Standard: Enterprise-Control System Integration". <https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard> (Accessed: October 15, 2026)
3. Haberler.com / Anadolu Agency, "Ankara'da IPA II kapanış konferansında 300 işletme dijital dönüşümle buluşturuluyor" (in Turkish), October 14, 2026. <https://www.haberler.com/guncel/ankara-da-ipa-ii-kapanis-konferansinda-300-isletme-20328194-haberi/> (Accessed: October 15, 2026)
4. TÜBİTAK TÜSSİDE, "DDX+ Digital Transformation Model" (in Turkish). <https://ddx.tubitak.gov.tr/> (Accessed: October 15, 2026)
5. International Society of Automation (ISA), "ISA/IEC 62443 Series of Standards". <https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards> (Accessed: October 15, 2026)
