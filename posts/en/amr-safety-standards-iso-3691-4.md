---
title: AMR safety standards: ISO 3691-4, the new EU Machinery Regulation and simulation-based certification
date: 2026-10-22
updated: 2026-10-22
description: TÜV SÜD and Accenture presented a concept that uses digital twins and simulation to speed up safety certification of autonomous mobile robots. Here is how AMR safety standards, ISO 3691-4 and the Machinery Regulation fit together.
cover_title: AMR safety standards
cover_icon: amr
category: endustri-4-0
tr: otonom-mobil-robot-amr-guvenlik-sertifikasyonu
seo_title: AMR safety standards: ISO 3691-4 and Machinery Regulation
meta_description: AMR safety standards explained: what ISO 3691-4 covers, how the EU Machinery Regulation 2023/1230 changes things in 2027, and TÜV SÜD's simulation-based model.
focus_kw: AMR safety standards
keywords: AMR safety standards, ISO 3691-4, AGV vs AMR, autonomous mobile robot safety, physical AI certification, Machinery Regulation 2023/1230, Turkey industrial robots
cover_alt: AMR safety standards: ISO 3691-4 and simulation-based certification for autonomous mobile robots, cover image
---
Deploying an autonomous mobile robot (AMR) that shares aisles with people can take far longer than buying the robot; much of the time goes into getting the safety concept accepted. On October 21, 2026, TÜV SÜD and Accenture presented the concept of a "Physical AI Safety Suite" that aims to shorten this process with digital twins and simulation [1]. In the same week, Turkey published a new Machinery Safety Regulation aligned with EU Regulation 2023/1230 [6]. This guide brings together the standards, regulation and practice behind **AMR safety standards**.

## AGV vs AMR: Why the definition matters for AMR safety standards

Under the International Federation of Robotics' definitions, based on ISO 8373, an automated guided vehicle (AGV) is a mobile platform "following a predetermined path indicated by markers or external guidance commands"; because it lacks the autonomy to determine its own path, IFR counts it as a robotic device rather than a robot [4]. AMRs are often used in industrial environments, but IFR classifies them as professional service robots; if an AMR carries a robot arm, the arm is counted separately as an industrial robot [4].

| | AGV | Autonomous mobile robot (AMR) |
|---|---|---|
| Path | Predetermined path, markers or external commands [4] | A mobile robot travelling under its own control [4] |
| IFR classification | Robotic device, not a robot [4] | Professional service robot [4] |
| Safety standard | Covered by ISO 3691-4 [3] | Covered by ISO 3691-4 [3] |
| Shows up in industrial robot statistics? | No [4] | No; counted as a service robot [4] |
| Typical hazard | Obstacles and collisions on a fixed route | Meeting people on changing routes; workers getting trapped [1] |

That distinction matters when you read the robot statistics below: IFR's industrial robot figures do not include AMRs.

## What ISO 3691-4 covers

ISO 3691-4:2023 specifies safety requirements and the means of verifying them for driverless industrial trucks and their systems. Its examples include "automated guided vehicle", "autonomous mobile robot", "bots", "automated guided cart", "tunnel tugger" and "under cart" [3]. Trucks guided solely by mechanical means such as rails, and remotely controlled trucks, are out of scope [3].

The standard makes one point that every project team should remember: the condition of the operating zone has a significant effect on safe operation, and preparing the operating zone is specified in a separate annex (Annex A) [3]. Safety is not just a property of the robot; floors, aisle widths, mixed-use areas and markings are part of it. According to ISO, the 2023 edition is expected to be replaced by ISO/DIS 3691-4 within the coming months [3].

## The TÜV SÜD and Accenture model: Test before the robot arrives

Accenture's announcement notes that at a medium-sized production plant, iterative coordination, validation and acceptance of safety concepts can take several weeks [1]. The Physical AI Safety Suite partially digitizes the manual assessment of facilities and equipment and the preparation of certification packages, using digital twins and AI-powered simulations. TÜV SÜD estimates the digital process could bring production online up to 30% sooner [1][2].

The concept checks automation on three connected layers, with TÜV SÜD providing independent assessment and retaining responsibility for certification [1]:

| Layer | Question | What happens |
|---|---|---|
| 1. Industrial layouts | Where can physical AI be deployed safely? | Routes, clearances, mixed-use zones and collaboration areas are assessed virtually before robots arrive; a structured evidence package is generated for TÜV SÜD review [1] |
| 2. Robot fleets | How does physical AI operate safely? | Fleet behavior is simulated to find hazards such as workers becoming trapped by AMRs; during operation, facility-mounted cameras extend perception beyond a single robot's view [1] |
| 3. Individual robots | What is physical AI allowed to do? | Site-specific conditions such as load, speed, floor and lighting are tested in simulation, including scenarios hard to cover in physical tests [1] |

Sarat Maitin of Accenture describes a familiar problem: "Too often, companies test automation concepts against industry standards after the equipment, layouts and workflows have already been established" [1]. That usually means expensive rework.

Note: the suite was presented as a concept at NVIDIA GTC Berlin 2026, and the 30% figure is TÜV SÜD's estimate [1].

## Regulation: EU 2023/1230 and Turkey's new rules

According to EU-OSHA, the new Machinery Regulation 2023/1230 replaces the Machinery Directive 2006/42/EC and aims to better cover new technologies such as autonomous mobile machinery (robots), connected equipment and AI modules using learning techniques that ensure safety functions [5]. It applies from January 20, 2027 [5].

Turkey moved in parallel: the Ministry of Industry and Technology published the Machinery Safety Regulation (2023/1230/EU) in the Official Gazette of October 16, 2026 (issue 33402). It repeals the previous regulation based on 2006/42/EC, most provisions take effect on January 20, 2027, and it references high-risk AI systems and cybersecurity certification [6].

IFR figures reported by Anadolu Agency show where Turkish manufacturing stands [7]:

| Indicator (2025) | Turkey |
|---|---|
| New industrial robot installations | 3,194 (down 9%) |
| Operational stock | 30,990 (all-time high, 15th worldwide) |
| Robot density (manufacturing, per 10,000 employees) | 52 (374 in automotive) |
| Applications of new robots | 59% handling, 16% welding |
| Largest customer industry | Metal (31% share, 990 units) |

Quotable stat: **59% of new industrial robots installed in Turkey in 2025 went into handling, while manufacturing has just 52 robots per 10,000 employees** [7]. As material-flow automation grows, safety approval for the AMRs that move loads between robot cells will come up more often.

## Safety is not only physical

Kaspersky's warehouse security paper points out that AGVs and AMRs can themselves be targeted, for example by affecting their navigation or preventing them from reaching their destination. If an AGV loses its control channel, the safe reaction may be to halt in place, and a stopped machine can block an entire route [8]. Safety engineers and security teams belong at the same table in any AMR project.

We covered simulation and digital twins in [Unilever's digital twin rollout](/en/digital-twin-manufacturing-examples-unilever/), plant data and AI in [Ford Otosan's APEM case](/en/ford-otosan-mega-ai-apem-factory-energy/), and robots working with software in the warehouse in [supply chain AI agents](/en/supply-chain-ai-agents-warehouse-digital-workers/). For warehouse device cyber risk, see [barcode scanner security](/en/barcode-scanner-security-warehouse/).

## Checklist: Before you start an AMR project

- [ ] Is the vehicle type clear: fixed-route AGV or self-navigating AMR?
- [ ] Can the supplier show ISO 3691-4 conformity and verification records?
- [ ] Has the operating zone (floors, aisle widths, mixed-use and pedestrian areas) been assessed before delivery?
- [ ] Have the layout and fleet behavior been tested in simulation or a digital twin?
- [ ] Does the risk assessment include workers getting trapped between AMRs?
- [ ] Are site-specific conditions (load, speed, floor, lighting) written into acceptance tests?
- [ ] Is there a plan for machines placed on the market after January 20, 2027?
- [ ] Is the fleet's network in OT security scope, and is behavior on loss of the control channel defined?
- [ ] Are safety, maintenance and IT security on the project team?

## Frequently asked questions

### Which safety standard applies to AMRs?

ISO 3691-4:2023, which specifies safety requirements and verification for driverless industrial trucks and their systems, explicitly including autonomous mobile robots [3].

### What is the difference between an AGV and an AMR?

An AGV follows a predetermined path set by markers or external commands and is a robotic device under IFR definitions; an AMR travels under its own control and is classified as a professional service robot [4].

### When does the EU Machinery Regulation 2023/1230 apply?

From January 20, 2027, replacing Directive 2006/42/EC [5]. Turkey's aligned regulation also takes effect largely on that date [6].

### Can simulation replace physical safety testing?

Not entirely. In the TÜV SÜD and Accenture concept, simulation generates evidence earlier, while TÜV SÜD keeps responsibility for independent assessment and certification [1].

### How much faster can certification be?

TÜV SÜD estimates that the digital process could bring production online up to 30% sooner [1].

## References

1. Accenture Newsroom, "TÜV SÜD and Accenture Accelerate Certification of Physical AI in Automated Factories and Warehouses with NVIDIA Technologies to Drive Manufacturing Productivity", October 21, 2026. <https://newsroom.accenture.com/news/2026/tuv-sud-and-accenture-accelerate-certification-of-physical-ai-in-automated-factories-and-warehouses-with-nvidia-technologies-to-drive-manufacturing-productivity> (Accessed: October 22, 2026)
2. DC Velocity, "Accenture collaboration will speed up rollout of AMRs in factories and warehouses", October 21, 2026. <https://www.dcvelocity.com/material-handling/robotics/accenture-collaboration-will-speed-up-rollout-of-amrs-in-factories-and-warehouses> (Accessed: October 22, 2026)
3. ISO, "ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems". <https://www.iso.org/standard/83545.html> (Accessed: October 22, 2026)
4. International Federation of Robotics, "Introduction into service robotics: Definitions" (World Robotics Service Robots 2021). <https://ifr.org/img/worldrobotics/Definitions_WR_Service_Robots_2021.pdf> (Accessed: October 22, 2026)
5. EU-OSHA, "Regulation 2023/1230/EU - machinery". <https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery> (Accessed: October 22, 2026)
6. Official Gazette of Türkiye (Resmî Gazete), Ministry of Industry and Technology, "Makine Emniyeti Yönetmeliği (2023/1230/AB)", October 16, 2026, issue 33402 (in Turkish). <https://www.resmigazete.gov.tr/eskiler/2026/10/20261016-12.htm> (Accessed: October 22, 2026)
7. Dünya (source: Anadolu Agency), "Türkiye'nin fabrikalarında tarihi rekor: Sayıları 30 bini aştı" (IFR World Robotics data, in Turkish), October 2, 2026. <https://www.dunya.com/sektorler/bilim-ve-teknoloji/turkiyenin-fabrikalarinda-tarihi-rekor-sayilari-30-bini-asti-haberi-842311> (Accessed: October 22, 2026)
8. Securelist (Kaspersky), Sergey Sidorov, Haidar Kabibo and Victor Zvarykin, "The journey of a paper unicorn: adventures inside a modern warehouse", October 20, 2026. <https://securelist.com/paper-unicorn-warehouse-security/121537/> (Accessed: October 22, 2026)
