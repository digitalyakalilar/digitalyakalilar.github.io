---
title: Refrigeration cyber attack in France: what 700 hit supermarkets teach cold chain operators, plus a controller checklist
date: 2026-11-10
updated: 2026-11-10
description: Refrigeration controllers at about 700 retail sites in France were taken over remotely in a single night; on November 9 France attributed the attack to a unit tied to Iran's Revolutionary Guard. Timeline, exposure numbers, data from Türkiye and a cold chain checklist.
cover_title: Refrigeration cyber attack
cover_icon: coldchain
category: lojistik-nakliyat
tr: soguk-zincir-siber-guvenligi-sogutma-kontrol-cihazlari
seo_title: Refrigeration cyber attack: cold chain security checklist
meta_description: A refrigeration cyber attack hit about 700 French retail sites. Timeline, exposed controller counts, 136 records in Türkiye and a cold chain security checklist.
focus_kw: refrigeration cyber attack
keywords: refrigeration cyber attack, fridge cyber attack France, cold chain cybersecurity, Danfoss refrigeration controller, industrial refrigeration systems, xweb, OT security, CISA, CERT-FR
cover_alt: Refrigeration cyber attack: cover graphic of a compromised refrigeration controller with a rising temperature gauge
---
Overnight from Sunday to Monday, freezers in hundreds of French supermarkets quietly switched into defrost mode. Staff arriving in the morning found pools of water under the cases and spoiled products, CNN reported [10]. Nobody had broken a door. The attackers had connected remotely to refrigeration control panels that were reachable from the internet. This **refrigeration cyber attack** turned cold chain security from an IT topic into a problem for food, pharma and logistics operators overnight. On November 9, 2026, France attributed the attack to a unit linked to Iran's Islamic Revolutionary Guard Corps [1][2]. Here is what happened, how many devices were exposed, what the data says about Türkiye, and a checklist you can use.

## What happened: a timeline of the refrigeration attacks

| Date | Development | Source |
|---|---|---|
| August 9, 2026 | Claroty Team82 published flaws in the Danfoss AK-SM 800A web interface, including a "code-of-the-day" authentication bypass; Danfoss fixed them in firmware R4.3.1 | [6] |
| October 11-12, 2026 | Defrost settings on refrigeration controllers at about 700 retail sites in France were set to high temperatures; major stock losses and at least 15 fire outbreaks | [1] |
| October 12, 2026 | CERT-FR issued an alert for Danfoss AK-SM/AK-SC and Copeland and Dixell xweb systems (updated October 16) | [3] |
| October 19, 2026 | ESET Türkiye reported 136 internet-reachable records in Türkiye possibly linked to remote refrigeration control | [8] |
| November 1-2, 2026 | Second wave: refrigeration systems hit in around a dozen European countries; cold rooms at three sites of the French blood service EFS were reprogrammed to 110 °C before staff intervened | [5] |
| November 5, 2026 | CISA, FBI, HHS, USDA and the US Department of Transportation issued a joint fact sheet on industrial refrigeration and cold chain monitoring systems | [4] |
| November 9, 2026 | France attributed the first wave to the IRGC-linked Shahid Kaveh unit; the Paris prosecutor opened a judicial investigation | [1][2][9] |

One important caveat: the French attribution covers the October wave. ANSSI director general Vincent Strubel said that although the modus operandi of the EFS attack is similar, nothing so far allows them to say it was the same attacker; attacks in other European countries have not been attributed yet [7].

## How the refrigeration cyber attack worked

According to the Paris prosecutor, the attackers took remote control of the equipment through web interfaces, launched abnormal defrost cycles of unlimited duration, and disabled the probe alarms that should trigger above a certain temperature [7]. They reached Danfoss systems first, then Dixell and Copeland [7].

Sekoia's assessment is blunt: the campaigns were not sophisticated [5]. The main issue was unpatched Danfoss controllers exposed directly to the internet [5]. In Sekoia's honeypots, attackers ran password-spraying attempts against the "Supervisor" and "admin" accounts with the password "12345" [5].

Sekoia also flags an AI angle: combining publicly available firmware with exposed devices, large language models can lower the barrier to attacking small industrial control and building automation systems [5].

## Exposed refrigeration controllers by the numbers

| Measure | Value | Source |
|---|---|---|
| Danfoss AK-SM 800A devices visible in Censys (August 2026) | 2,765 | [6] |
| Internet-exposed Danfoss systems, October 11, 2026 | More than 2,700 (about 1,700 in France) | [5] |
| French systems no longer reachable by 4 p.m. on October 12 | Roughly half of those previously exposed | [5] |
| Danfoss and xweb families worldwide (Censys) | October 9: 6,695 → November 5: 3,124 (−53%) | [11] |
| Türkiye, October 14, 2026 (ESET Türkiye) | 136 records: 10 linked to Danfoss panels, 126 to xweb panels | [8] |

Table compiled by us from the cited sources. A record is not the same as a physical device, and being reachable does not mean every device is vulnerable [8][11].

Quotable stat: **ESET Türkiye found 136 internet-reachable records in Türkiye possibly linked to remote refrigeration control on October 14, 2026, while stressing this does not mean 136 businesses are vulnerable** [8].

## What it means for Türkiye

We found no reports of businesses in Türkiye hit by these attacks. But there are two signals:

- Speaking to DW Turkish, Prof. Tuna Tuğcu noted that the Danfoss AK-SM 820A, 850A and 880A models at the center of the attacks are marketed on the company's Türkiye page, while it is unknown where they are installed and whether they are updated [11].
- The records ESET found are not limited to supermarkets; cold storage facilities, pharmacies and production sites can use similar control systems [8].

Anadolu Agency also covered the attribution; French Foreign Minister Barrot described it as the first large-scale sabotage cyberattack carried out on French soil [9]. So this is not just "France's problem." If you don't know who manages your refrigeration panel over the internet, and how, that is the first question to ask.

## Who is responsible?

Sekoia makes an important point: responsibility for these measures is often split between asset owners, integrators, maintenance providers and equipment vendors, but that split should not result in persistent exposure [5].

| Role | What to do |
|---|---|
| Asset owner (store, warehouse, pharmacy, plant) | Build an inventory; ask the maintenance provider in writing which panels are internet-facing [4][8] |
| Refrigeration service provider | Move remote access to a VPN or protected network; treat IP filtering only as a stopgap [3] |
| Integrator | Put OT devices on a dedicated VLAN, separate from business networks [4] |
| Vendor | Ship firmware updates; offer a replacement path for end-of-life devices [3][6] |
| Insurance / legal | Check contract terms before cutting the data feed to the service provider [3] |

Table prepared by us based on the recommendations in the cited sources.

## Cold chain security checklist for refrigeration controllers

Built on the November 5 CISA-led fact sheet [4], CERT-FR's recommendations [3] and ESET Türkiye's assessment [8]:

- [ ] Do not expose control panels directly to the internet; if remote access is needed, put it behind an up-to-date firewall or edge device [4]
- [ ] Allow remote maintenance only via a secure VPN or protected network [3]
- [ ] Move OT devices to a dedicated VLAN separate from business networks [4]
- [ ] Change default passwords and use phishing-resistant MFA wherever feasible [4]
- [ ] Update firmware; for Danfoss AK-SM 800A that means R4.3.1 or later [6]. Set Danfoss devices to the "Strict" security level [3]
- [ ] Identify and replace end-of-life devices; a factory reset alone is not enough on unpatched devices [3][4]
- [ ] Allowlist the devices and IP addresses authorized to make changes [4]
- [ ] Review the full configuration, including defrost ranges [3]
- [ ] Define safe setpoint limits and alert on deviations [4]
- [ ] Use an independent temperature sensor and alarm that does not depend on the control panel [8]
- [ ] Keep offline, offsite backups and test them [4]
- [ ] Enable logging and watch for unexpected authentication and configuration changes [4][5]

For a broader OT framework, see our post on [OT vulnerability management best practices](/en/ot-vulnerability-management-best-practices/); for similar risks in warehouse devices, our piece on [barcode scanner security](/en/barcode-scanner-security-warehouse/); and for systems running out of support, our [Windows Server 2016 end of support guide](/en/windows-server-2016-end-of-support-migration/).

## Frequently asked questions

### Why does cold chain cybersecurity matter?

When refrigeration controllers are compromised, temperatures can be changed, stock can spoil and fire hazards can arise. CISA notes this can also indirectly harm consumers if products are consumed after unsafe storage [4].

### Who was behind the refrigeration cyber attack in France?

On November 9, 2026, French authorities attributed the October attack to the Shahid Kaveh unit linked to Iran's Revolutionary Guard [1][2]. The early-November second wave has not been attributed yet [7].

### Are there internet-exposed refrigeration panels in Türkiye?

ESET Türkiye found 136 internet-reachable records on October 14, 2026 (10 linked to Danfoss, 126 to xweb panels). The company stresses this does not mean 136 businesses are vulnerable or compromised [8].

### How do I know if my refrigeration controller is safe?

Start by finding out whether the panel is directly reachable from the internet and how your maintenance provider connects. CERT-FR recommends removing direct internet exposure and allowing access only through a secure VPN or protected network [3].

### Which devices were targeted?

The CERT-FR alert lists the Danfoss AK-SM and AK-SC series and the Copeland xweb and Dixell xweb systems [3].

## References

1. CERT-FR / Cyber Crisis Coordination Centre (C4), "Activités cyber offensives ciblant la France menées par des acteurs iraniens liés au CGRI" (CERTFR-2026-CTI-009, in French), November 9, 2026. <https://www.cert.cyber.gouv.fr/cti/CERTFR-2026-CTI-009/> (Accessed: November 10, 2026)
2. French Ministry for Europe and Foreign Affairs, "Déclaration d'attribution à l'Iran de cyberattaques visant la France" (in French), November 9, 2026. <https://www.diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/declaration-d-attribution-a-l-iran-de-cyberattaques-visant-la-france> (Accessed: November 10, 2026)
3. CERT-FR, "Incident de sécurité ciblant les contrôleurs à distance des installations de réfrigération" (CERTFR-2026-ALE-012, in French), October 12, 2026 (updated October 16, 2026). <https://www.cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/> (Accessed: November 10, 2026)
4. CISA, FBI, HHS, USDA and DoT, "US Government Partners Urge Hardening Industrial Refrigeration and Cold Chain Monitoring Systems", November 5, 2026. <https://www.cisa.gov/resources-tools/resources/us-government-partners-urge-hardening-industrial-refrigeration-and-cold-chain-monitoring-systems> (Accessed: November 10, 2026)
5. Sekoia, "The Cold Chain on Fire: Unpatched Danfoss controllers exploited", November 10, 2026. <https://www.sekoia.com/fr/blog/the-cold-chain-on-fire-unpatched-danfoss-controllers-exploited> (Accessed: November 10, 2026)
6. Claroty Team82, Amir Zaltzman, "Freeze the Controller, Defrost the Food: Uncovering Vulnerabilities in Danfoss Refrigeration Controllers", August 9, 2026. <https://www.claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers> (Accessed: November 10, 2026)
7. franceinfo, Luc Chagnon, "La France accuse l'Iran de la cyberattaque contre des frigos de supermarchés…" (in French), November 9, 2026. <https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/cyberattaque-contre-des-frigos-de-supermarches-le-parquet-de-paris-ouvre-une-enquete-visant-une-unite-des-gardiens-de-la-revolution-iraniens_8274806.html> (Accessed: November 10, 2026)
8. Teknoblog, Sabri Küstür, "ESET, Türkiye'de soğutma kontrolüyle ilişkili 136 kayıt bildirdi" (in Turkish), October 19, 2026. <https://www.teknoblog.com/eset-sogutma-panelleri-icin-turkiye-yi-uyardi/> (Accessed: November 10, 2026)
9. Anadolu Agency, Şeyma Yiğit, "Fransa Dışişleri Bakanı Barrot: (Marketlere) siber saldırının sorumluluğu İran Devrim Muhafızları'na ait" (in Turkish), November 9, 2026. <https://www.aa.com.tr/tr/dunya/fransa-disisleri-bakani-barrot-marketlere-siber-saldirinin-sorumlulugu-iran-devrim-muhafizlarina-ait/4117829> (Accessed: November 10, 2026)
10. CNN, "What to know about the cyberattack that targeted supermarket refrigeration systems in France", October 14, 2026. <https://www.cnn.com/2026/10/14/europe/france-cyberattack-supermarket-fridges-intl> (Accessed: November 10, 2026)
11. DW Turkish, Pelin Ünker, "Avrupa'da hacklenen soğutma sistemleri Türkiye'de de satılıyor" (in Turkish), November 9, 2026. <https://www.dw.com/tr/avrupada-marketler-hacklendi-t%C3%BCrkiyede-risk-ne/a-79900913> (Accessed: November 10, 2026)
