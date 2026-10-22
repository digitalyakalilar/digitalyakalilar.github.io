---
title: How to stop ClickFix attacks: A company guide to fake CAPTCHA lures
date: 2026-10-22
updated: 2026-10-22
description: A fake "I'm not a robot" box gets an employee to run the attacker's command by hand. Google just added ClickFix protection to Chrome and Huntress documented a new campaign. How ClickFix works and what companies should lock down.
cover_title: How to stop ClickFix attacks
cover_icon: captcha
category: dijital-guvenlik
tr: clickfix-saldirisi-sahte-captcha-korunma
seo_title: How to stop ClickFix attacks: Fake CAPTCHA defense guide
meta_description: How to stop ClickFix attacks: ESET saw a 517% surge in fake CAPTCHA lures. Chrome's new protection, a new Huntress case and a 10-point checklist for companies.
focus_kw: how to stop ClickFix attacks
keywords: how to stop ClickFix attacks, ClickFix attack detection, fake CAPTCHA scam, block Run dialog, finger.exe ClickFix, Chrome ClickFix protection, Lumma Stealer
cover_alt: How to stop ClickFix attacks: company defenses against fake CAPTCHA commands, cover image
---
You tick an "I'm not a robot" box on a website, and a short instruction appears: press the Windows key and R, paste with Ctrl+V, hit Enter. That is a ClickFix attack, and the person who downloads the malware is the employee, not the attacker [6]. Google added protection against ClickFix commands to Chrome on October 20, 2026 [1], and a day later security firm Huntress documented a new campaign that started with a sponsored Google ad [3][4]. This guide covers **how to stop ClickFix attacks**: how the technique works, the numbers behind it and which settings companies should lock down, with sources.

## What is a ClickFix attack?

Microsoft describes ClickFix as a social engineering technique that exploits people's tendency to fix minor technical issues themselves and harmless-looking steps like CAPTCHA checks. Users are told to paste and run a command in the Windows Run dialog, Windows Terminal or PowerShell [6]. Microsoft first observed it in an email campaign between March and June 2024, and within a year it was seeing campaigns targeting thousands of enterprise and end-user devices globally every day [6]. MITRE ATT&CK catalogs the behavior as its own sub-technique: T1204.004, "Malicious Copy and Paste" [7].

What makes it dangerous is the human in the middle of the chain. Because the user launches the command, it can get past conventional and automated security solutions [6]. Chrome had a similar blind spot: the malicious download happens in the terminal rather than the browser, so Chrome's download protections never came into play [2].

## ClickFix by the numbers

| Indicator | Value | Source |
|---|---|---|
| Growth in ESET telemetry (H2 2024 → H1 2025) | 517% | [5] |
| Share of all blocked attacks (H1 2025) | Nearly 8%; second only to phishing | [5] |
| Share of Huntress managed EDR detection signals (2026) | Roughly 2.2%; nearly 99% of them high severity | [4] |
| Microsoft's observation | Campaigns targeting thousands of enterprise and end-user devices daily | [6] |
| Price of a ClickFix kit subscription | $200 to $1,500 per month | [6] |
| Most prolific final payload | Lumma Stealer (infostealer) | [6] |

A quotable statistic: **in ESET's data, ClickFix grew 517% in six months to become the second most common attack vector after phishing** [5].

## The new case: From an "amazon business" ad to finger.exe

According to the Huntress report published on October 21, 2026, the attack began with a simple search: the sponsored result for "amazon business" led to a fake Amazon login page [3]. After the user entered an email or phone number, a fake CAPTCHA appeared, the "I'm not a robot" button copied a command to the clipboard, and the user was told to paste it into the Run dialog [3].

The command called `finger`, a Windows utility dating back to the early internet [4]. Huntress says the command was padded with extra spaces and hyphens, so the Run box appeared to say little more than "Push the Enter key" [3]. The chain ended by installing a version of Lumma Stealer and a pirated copy of the NetSupport Client remote management tool [3][4]. Google removed the ad, but the researchers say the attacker infrastructure remains online [4].

Huntress analyst Sarah Reddish sums it up for companies: no legitimate CAPTCHA asks users to paste a command into Run, PowerShell or Command Prompt [4].

## What Chrome's new ClickFix protection does

According to Google's October 20 announcement, Chrome's Enhanced Protection mode can now spot when a user is being manipulated into copying a suspicious command. The clipboard payload is scrubbed of personal information and sent to Safe Browsing for analysis, and if the verdict is dangerous, Chrome shows a warning [1]. Google says the system is designed for high precision to avoid disrupting legitimate developer activity [1].

The same announcement adds new "suspicious site" warnings for lower-confidence verdicts and server-side Gemini analysis that also targets fake antivirus and fake browser update pages [1]. Google says more than 1 billion users had turned on Enhanced Protection as of 2025 [1].

One important caveat: the ClickFix and Gemini protections only work when Enhanced Protection is on [2]. Unless that setting is enabled centrally on company machines, the new protection does not apply.

## Real CAPTCHA or ClickFix lure?

| | Real CAPTCHA | ClickFix lure |
|---|---|---|
| What it asks | Pick images, tick a box, drag a puzzle piece | Keyboard shortcuts like Win+R, Ctrl+V, Enter [6] |
| What happens to your clipboard | Nothing is copied | A command is copied in the background [3][6] |
| Which window opens | None; you stay on the page | Run, Terminal or PowerShell [6] |
| The text you see | A verification question | Often a short phrase that hides the real command [3] |
| Outcome | Access to the site | Infostealer, remote access tool or ransomware [5][6] |

## How to stop ClickFix attacks: What to lock down

Read together, Microsoft's and Huntress's recommendations add up to layered defense:

1. **Restrict the Run dialog.** Disable Win+R via Group Policy for users who don't need it [6][4].
2. **Watch or block rarely used utilities.** Huntress recommends alerting on unexpected `finger.exe` activity and monitoring or blocking outbound TCP/79 [4].
3. **Make PowerShell visible.** Turn on script block logging and use execution policies such as AllSigned or RemoteSigned [6].
4. **Warn on multi-line paste.** Enable the Windows Terminal setting that warns when pasted text contains multiple lines [6].
5. **Manage the browser.** Use enterprise-managed browsers and consider enabling Chrome Enhanced Protection centrally [6][1].
6. **Teach one rule.** If a web page asks you to paste a command, close it and call IT [4].

## The KVKK angle for companies in Türkiye

Infostealers, the most common ClickFix payload, target saved browser passwords, cookies and email client data [6]. If personal data leaks, the problem is not only technical: under Turkish data protection board decision 2019/10, a data controller must notify the board without delay and within 72 hours at the latest after learning of a breach, and must prepare a data breach response plan [8]. A "ClickFix command was run" scenario in your incident response plan should cover that clock as well.

For account and device basics, see our [phone and account security guide](/en/phone-and-account-security/). For the risk of tools employees set up themselves, read our piece on [employee-built AI agents](/en/employee-built-ai-agents-security-risk/), and for isolating software that runs local commands, our [Microsoft Execution Containers review](/en/microsoft-execution-containers-ai-agent-security/). We cover a similar "keystroke injection" risk on the warehouse floor in our article on [barcode scanner security](/en/barcode-scanner-security-warehouse/).

## Checklist: 10 steps against ClickFix

- [ ] Have you identified user groups that don't need the Run dialog and restricted Win+R?
- [ ] Are there alert or block rules for rarely used tools such as `finger.exe` and `mshta`?
- [ ] Is outbound TCP/79 monitored or blocked?
- [ ] Is PowerShell script block logging on and feeding a SIEM?
- [ ] Is the multi-line paste warning enabled in Windows Terminal?
- [ ] Are company browsers centrally managed, and has a Chrome Enhanced Protection policy been considered?
- [ ] Are unapproved remote management tools (NetSupport, etc.) blocked?
- [ ] Does employee training show a screenshot of a "CAPTCHA that asks you to paste a command"?
- [ ] Is there a written flow for an employee who ran the command: disconnect, call IT, change passwords from a clean device?
- [ ] Does your incident response plan include KVKK's 72-hour notification window?

## Frequently asked questions

### What is a ClickFix attack?

A social engineering technique that uses a fake error or verification screen to trick users into pasting and running a malicious command themselves in the Run dialog, Terminal or PowerShell [6].

### How can you tell a fake CAPTCHA?

A real CAPTCHA never asks for keyboard shortcuts, the Run dialog or pasting a command. If you see such an instruction, the page is fake [4][6].

### How common are ClickFix attacks?

ESET's H1 2025 data showed ClickFix detections up 517%, accounting for nearly 8% of blocked attacks and ranking second after phishing [5].

### Does Chrome block ClickFix attacks?

Chrome's Enhanced Protection mode now analyzes suspicious command copying and shows a warning if it is judged dangerous. It only works when Enhanced Protection is on [1][2].

### What should I do if I ran the command?

Disconnect the device from the network, tell IT or security right away and change your passwords from a clean device. If personal data leaked, a company in Türkiye may have to notify the KVKK board within 72 hours [8].

## References

1. Google, Jasika Bawa, "Our latest defenses against evolving web scams", October 20, 2026. <https://blog.google/security/our-latest-defenses-against-evolving-web-scams/> (Accessed: October 22, 2026)
2. SecurityWeek, Eduard Kovacs, "Google Hardens Chrome Against ClickFix Attacks, Insecure HTTP Connections", October 21, 2026. <https://www.securityweek.com/google-hardens-chrome-against-clickfix-attacks-insecure-http-connections/> (Accessed: October 22, 2026)
3. Huntress, Andrew Brandt and Sarah Reddish, "Amazon-Themed ClickFix Campaign Serves Up Finger-Licking Malware", October 21, 2026. <https://www.huntress.com/blog/amazon-clickfix-finger> (Accessed: October 22, 2026)
4. Dark Reading, Elizabeth Montalbano, "Decades-Old Windows Utility Powers Modern ClickFix Attack", October 21, 2026. <https://www.darkreading.com/cyberattacks-data-breaches/decades-old-windows-utility-modern-clickfix-attack> (Accessed: October 22, 2026)
5. ESET, "ESET Threat Report: ClickFix fake error surges, spreads ransomware and other malware", June 26, 2025. <https://www.eset.com/us/about/newsroom/research/eset-threat-report-clickfix-fake-error-surges-spreads-ransomware-and-other-malware/> (Accessed: October 22, 2026)
6. Microsoft Threat Intelligence, "Think before you Click(Fix): Analyzing the ClickFix social engineering technique", August 21, 2025. <https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/> (Accessed: October 22, 2026)
7. MITRE ATT&CK, "User Execution: Malicious Copy and Paste (T1204.004)". <https://attack.mitre.org/techniques/T1204/004/> (Accessed: October 22, 2026)
8. Personal Data Protection Authority (KVKK), "The Board Decision No. 2019/10 of 24.01.2019 about Procedures and Principles of Personal Data Breach Notification". <https://www.kvkk.gov.tr/Icerik/6647/The-Board-Decision-No-2019-10-of-24-01-2019-about-Procedures-and-Principles-of-Personal-Data-Breach-Notification-> (Accessed: October 22, 2026)
