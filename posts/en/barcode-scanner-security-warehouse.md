---
title: Barcode scanner security: How wireless scanners, handhelds and printers become a way into the warehouse
date: 2026-10-22
updated: 2026-10-22
description: Kaspersky showed that fake keystrokes can be sent to a warehouse computer through a wireless barcode scanner's base station. Why barcode scanner security is the first link in WMS security, and what warehouse managers should check.
cover_title: Barcode scanner security
cover_icon: scanner
category: lojistik-nakliyat
tr: barkod-okuyucu-guvenligi-depo-siber-saldiri
seo_title: Barcode scanner security: Bluetooth risks in the warehouse
meta_description: Barcode scanner security matters: Kaspersky showed a wireless scanner's base station can pass fake keystrokes to a WMS PC. Device table and 10-step checklist.
focus_kw: barcode scanner security
keywords: barcode scanner security, barcode scanner vulnerability, warehouse cybersecurity, Bluetooth keystroke injection, CVE-2026-4272, WMS security, handheld terminal security
cover_alt: Barcode scanner security: wireless scanners, handheld terminals and WMS cyber risk in the warehouse, cover image
---
The handheld scanner that gets triggered thousands of times a day in a warehouse often isn't even in the company's security inventory. Research Kaspersky shared on October 20, 2026 shows the cost of that blind spot: a wireless barcode scanner's base station can let an attacker within Bluetooth range send fake keyboard input to the connected computer [1][3]. This article looks at **barcode scanner security** for warehouse and logistics teams, together with the same research's findings on handheld terminals, thermal printers and the WMS.

## Why barcode scanner security is in the spotlight

During a security audit of a warehouse's digital ecosystem, the Kaspersky Security Services team found a new attack vector in a barcode scanner model from a major manufacturer; the findings were presented at the Security Analyst Summit 2026 in Bali [1]. In a typical setup, handheld scanners talk to a base station, which in turn connects to a workstation or another business system. The main weak point is that there is no authentication between the base station and the scanners [1].

The attack scenario: while an employee works normally with the scanner, an attacker obtains the base station's Bluetooth address, for example by passively eavesdropping on Bluetooth traffic. The attacker then sends the base station a payload that simulates keystrokes; the base station forwards them to the PC, which treats them as legitimate user input [1]. Kaspersky says this can lead to remote code execution without user interaction, and that the same attack pattern was observed across devices from multiple vendors [1].

Kaspersky's technical paper names one example: Honeywell devices affected by CVE-2026-4272 [2]. According to the US National Vulnerability Database (NVD), the flaw was published on April 5, 2026, was scored 8.1 (High) on CVSS 3.1 by Honeywell, and allows an attacker within Bluetooth range of the base station to execute system commands on the connected host without authentication [3]. Honeywell recommends upgrading to the fixed firmware versions [3].

## The scanner is only the door: The real target is the WMS

According to Sergey Sidorov, Head of Industrial Security Services at Kaspersky, every layer of modern logistics, from enterprise platforms to the device in a worker's hand, can become an entry point, and the research shows that can be a single barcode scanner [1][4]. What matters is not the scanner itself but the trusted position of the computer it connects to [1].

The Securelist paper describes the warehouse management system (WMS) as coordinating all eight stages from receiving to shipping, which makes it closer to the "operating system of the entire warehouse" [2]. An attacker who can modify WMS records can alter stock levels, bin locations, picking tasks or shipment information, and a falsified record at receiving is inherited by every later stage [2]. As reminders that cyber incidents do stop warehouse operations, the paper cites an outage affecting warehouse management systems at Morrisons, UNFI's incident that impacted order fulfillment, and reports of an attack that disrupted eight CEVA Logistics warehouses in Europe [2].

## Warehouse devices and attack paths

The table below summarizes the entry points described in Kaspersky's warehouse audit and the related controls:

| Device / area | Attack path described | Key control |
|---|---|---|
| Wireless barcode scanner + base station | Fake keystrokes over Bluetooth; commands on the connected PC [1][2] | Firmware updates; disable unused Bluetooth [1][3] |
| Scanned barcode / QR code | Because the scanner acts as a keyboard, a malicious code can inject keystrokes [2] | Least privilege on the host the scanner is attached to [1] |
| Handheld terminal (Android, kiosk mode) | Kiosk escape exposing the Wi-Fi password or allowing malware installation [2] | Device management and periodic security assessment [2] |
| Mobile thermal printer | In the Securelist example (Zebra ZQ630), a pairing misconfiguration let apps be uploaded over Bluetooth [2] | Harden pairing settings; include printers in endpoint security [2] |
| Network jacks behind racks, cameras | An unplugged camera leaves an active port; unused jacks [2] | Port security; IEEE 802.1X with EAP-TLS device authentication [2] |
| WMS (web-based) | Authorization bypass and web flaws used to alter stock, task and shipment records [2] | Network segmentation, patch management, least privilege [1][2] |

A quotable finding: **according to Kaspersky, there is no authentication between the base station and wireless barcode scanners, so an attacker in range can send keystrokes to the connected PC without user interaction** [1].

## Where does the attacker stand? The parking lot is part of the network

The Securelist paper splits threat actors into external actors with no legitimate relationship to the warehouse and internal actors with legitimate access, such as employees, contractors or temporary staff. One kind of external actor is "proximate": someone in the parking lot, a neighboring unit or a delivery bay who can reach Wi-Fi, Bluetooth and other short-range interfaces without an account or badge [2]. Because radio passes through windows, gates and thin external panels, the paper notes, the network may be reachable from considerably farther away with a directional antenna [2].

The paper also adds an HR note: sorting, packing and courier roles are hired quickly and in volume, so someone can walk in and hold legitimate physical access within days. It recommends a more risk-based hiring approach for roles with access to sensitive areas [2].

## What to do: Kaspersky's recommendations

Kaspersky recommends verifying every new device before it connects to the network, disabling unused Bluetooth interfaces and enforcing strong authentication, segmenting warehouse networks so only essential connections are permitted, promptly patching both devices and the WMS, restricting account permissions to the minimum required, and running regular full-scale attack-path exercises that include insiders with legitimate credentials [1][4]. The technical paper adds radio-frequency surveys and bringing warehouse devices into endpoint security and vulnerability management processes [2].

For a general framework on enterprise Bluetooth use, NIST's Guide to Bluetooth Security (SP 800-121 Rev. 2) covers Bluetooth's security capabilities and recommendations for organizations [5].

We looked at where AI and automation are heading in warehouse operations in our article on [AI agents in the supply chain](/en/supply-chain-ai-agents-warehouse-digital-workers/), and at the software side of freight in [AI freight audit](/en/ai-freight-audit-logistics-ai-operators/). For the layer where IT meets OT in manufacturing, see the [Kardemir Level 3 MES case](/en/kardemir-level-3-mes-isa-95/), and for attacks that trick employees into running commands themselves, our guide on [how to stop ClickFix attacks](/en/how-to-stop-clickfix-attacks/).

## Checklist: Barcode scanner security for the warehouse

- [ ] Does your inventory list the base station model and firmware of every wireless scanner (not just the handheld)?
- [ ] If you use Honeywell base stations, do the versions include the CVE-2026-4272 fix? [3]
- [ ] Is unused Bluetooth turned off on scanners, printers and terminals?
- [ ] Does the computer the scanner is attached to run with standard user rights?
- [ ] Is the warehouse OT network separated from corporate IT and guest Wi-Fi?
- [ ] Do new devices go through an approval step before joining the network?
- [ ] Are unused network jacks and camera ports disabled, and has 802.1X been considered?
- [ ] Are handheld kiosk mode and device management tested regularly?
- [ ] Are the WMS and its integrations on the patch schedule?
- [ ] Do you run an attack-path exercise at least once a year, including a parking-lot scenario?

## Frequently asked questions

### Can a barcode scanner be hacked?

According to Kaspersky's research, some wireless models have no authentication between the base station and the scanner, so an attacker within Bluetooth range can send fake keystrokes to the connected computer [1].

### What is CVE-2026-4272?

A missing authentication for critical function flaw in some Honeywell handheld scanner base stations. Per the NVD, an attacker within Bluetooth range can execute commands on the connected host; Honeywell recommends upgrading to the fixed version [3].

### Does the attacker have to get inside the warehouse?

No. In Kaspersky's threat model, a "proximate" attacker in the parking lot or a delivery bay can reach short-range interfaces such as Bluetooth and Wi-Fi [2].

### What is the most critical system in a warehouse?

According to Kaspersky, the WMS: because it coordinates every stage, compromising it can corrupt stock, task and shipment records and stop the operation [2].

### What should the first step be?

Inventory the model and firmware of every scanner, base station, terminal and printer, then apply updates and switch off unused Bluetooth [1][3].

## References

1. Kaspersky, "Your order is delayed: Kaspersky identifies vulnerabilities in barcode scanners, posing potential threat for the warehouse industry", October 20, 2026. <https://www.kaspersky.com/about/press-releases/your-order-is-delayed-kaspersky-identifies-vulnerabilities-in-barcode-scanners-posing-potential-threat-for-the-warehouse-industry> (Accessed: October 22, 2026)
2. Securelist (Kaspersky), Sergey Sidorov, Haidar Kabibo and Victor Zvarykin, "The journey of a paper unicorn: adventures inside a modern warehouse", October 20, 2026. <https://securelist.com/paper-unicorn-warehouse-security/121537/> (Accessed: October 22, 2026)
3. NIST National Vulnerability Database, "CVE-2026-4272". <https://nvd.nist.gov/vuln/detail/CVE-2026-4272> (Accessed: October 22, 2026)
4. DC Velocity, "Kaspersky: Hackers could access warehouse software through wireless barcode scanners", October 20, 2026. <https://www.dcvelocity.com/technology/warehouse-it/kaspersky-hackers-could-access-warehouse-software-through-wireless-barcode-scanners> (Accessed: October 22, 2026)
5. NIST, John Padgette et al., "SP 800-121 Rev. 2, Guide to Bluetooth Security" (includes updates as of January 2022). <https://csrc.nist.gov/pubs/sp/800/121/r2/upd1/final> (Accessed: October 22, 2026)
