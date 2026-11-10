---
title: Deepfake CEO fraud: inside the $129M case and a payment verification checklist for finance teams
date: 2026-11-10
updated: 2026-11-10
description: Three people are charged in the US with using AI to clone the voices and faces of CEOs and lawyers and steal more than $129 million from companies. The case step by step, Gartner data, cases from Türkiye and a payment approval checklist.
cover_title: Deepfake CEO fraud
cover_icon: deepfake
category: dijital-guvenlik
tr: ceo-dolandiriciligi-deepfake-ses-klonlama-onlemleri
seo_title: Deepfake CEO fraud: the $129M case and a checklist
meta_description: Deepfake CEO fraud now uses cloned voices and video calls. The $129M US case step by step, Gartner data, cases from Türkiye and a payment verification list.
focus_kw: deepfake CEO fraud
keywords: deepfake CEO fraud, deepfake CEO fraud case, CEO fraud prevention, how to prevent deepfake scams, voice cloning fraud, business email compromise, payment verification, social engineering
cover_alt: Deepfake CEO fraud: cover graphic of an impersonated executive video call and a verification check
---
The phone rings. It is the CEO. The voice is familiar, and there may even be video. He says he is working on a confidential financial transaction, needs your help, and puts you in touch with a lawyer at a large law firm who is handling the deal. The lawyer is polite and sounds competent. Eventually he asks you to wire money to a bank account. According to the US Justice Department, this is exactly how a **deepfake CEO fraud** scheme worked between 2024 and 2026, taking more than $129 million from companies [1]. In this post we walk through the case, look at Gartner's numbers and build a verification checklist finance teams can actually use.

## What is deepfake CEO fraud?

CEO fraud is when an attacker impersonates a senior executive to push an employee into a payment or a sensitive action. For years the main tool was a spoofed email. Now attackers add AI-generated voice and video.

Gartner's Craig Porter puts it plainly: attackers can combine phishing, business email compromise (BEC), synthetic media and aggregated personal context across multiple channels [3]. So the risk is not one fake email. Email, phone, video calls and chat apps can all be pieces of the same script.

## The $129 million deepfake CEO fraud case, step by step

On November 5, 2026, the US Attorney's Office for the Southern District of New York unsealed an indictment against three people [1]. According to the indictment, the defendants:

1. Called employees at target companies while posing as those companies' CEOs.
2. Asked for help with a confidential financial transaction, using AI to mimic the CEO's voice and/or image.
3. Directed the employee to "lawyers" at major international law firms supposedly working on the deal.
4. Impersonated those lawyers as well, to make the transaction look real.
5. Had the "lawyer" instruct the employee to wire a large sum to an account the conspirators controlled [1].

The money went to accounts in the US, Spain, Portugal, Greece, the UAE, Singapore, Austria, Slovakia and China, and was then converted into cryptocurrency [1]. One defendant allegedly kept a handwritten script titled "Lawyer Call," including language designed to convince victims not to discuss their communications with colleagues [1].

Some of the victims listed in the indictment:

| Victim (as described in the indictment) | Loss |
|---|---|
| Financial technology company headquartered in the UK | $11,578,474 |
| Pet food company headquartered in Florida | $5,242,747 |
| Hospital system headquartered in Missouri | $4,829,580 |
| Mutual fund company headquartered in Massachusetts | $4,639,918 |
| Hospital system headquartered in California | $2,968,497 |
| Bank headquartered in Rhode Island | $2,684,580 |

Source: US Department of Justice, SDNY [1]. These are allegations in an indictment; the defendants are presumed innocent unless proven guilty [1].

What struck us: a bank and a fintech are on the list. So "our finance team would never fall for this" is not much of a defense. ITPro reports that the scheme usually targeted accounts department staff [2].

## Deepfake and social engineering by the numbers

Gartner surveyed 297 senior cybersecurity leaders between March and May 2026 [3]. The results show this case is not an outlier:

| Share of CISOs reporting at least one incident in the past 12 months | Value |
|---|---|
| Email phishing, spear-phishing or business email compromise | 79% |
| Vishing or smishing | 58% |
| Deepfake during an employee **audio** call | 41% |
| Deepfake during an employee **video** call | 36% |

Source: Gartner, September 22, 2026 [3].

Quotable stat: **According to Gartner, 4 in 10 CISOs reported at least one deepfake social engineering incident during an employee audio call in the past 12 months** [3].

Gartner's key point is that AI increases the volume, personalization and credibility of social engineering while reducing the reliability of familiar detection cues [3]. In other words, "the voice sounded a bit robotic" is becoming a weak signal.

## What it looks like in Türkiye

We could not find national statistics on deepfake CEO fraud against companies in Türkiye. The reported cases mostly target individuals:

- In February 2026, an operation centered in Osmaniye found that suspects had used AI to imitate the faces and voices of senior state officials in fake investment ads on social media; their accounts showed 410 million Turkish lira in transaction volume, and 5 of 8 suspects were jailed pending trial [4].
- In October 2026, Murat Çiftçi, CEO of the insurance broker IBS, warned companies about fake payment instructions delivered in a cloned executive voice. He noted that such losses can occur without any unauthorized access to company systems, and that money sent by a deceived employee may not be covered by every cyber policy [5].

The $129 million case was also widely covered in the Turkish business press [6]. It is a good moment to put the topic on the board's agenda.

## Why it works: three levers

Reading the indictment, we saw the script lean on three things:

- **Authority:** The request comes from the CEO. Where hierarchy is strong, saying "no" is hard.
- **Secrecy:** The deal is "confidential." The script specifically discourages the employee from talking to colleagues [1].
- **Apparent confirmation:** A second "expert" (the lawyer) joins. The employee feels they are trusting two people, not one [1].

The antidote to all three is the same: a predefined verification step that does not depend on the channel the request arrived on.

## Attack steps and the controls that stop them

| Attack step | Red flag | Preventive control |
|---|---|---|
| Call or message in an executive's name [1] | Unusual channel, emphasis on a "confidential deal" | Call back on the number you already have on file [5] |
| Hand-off to a third party (lawyer, adviser) [1] | An outside expert you have never dealt with | Verify the third party's contact details from your own records |
| "Don't tell anyone" instruction [1] | Pressure to keep it secret | Require a second approver for every high-value transfer [5] |
| Wire to a new or foreign account [1] | First-time payee | Holding period and dual approval for new payees |
| Account recovery or password reset | New device or privilege change the same day | Correlate identity events with payment events [3] |

Table compiled by us from the methods and recommendations in the cited sources.

## CEO fraud prevention checklist for finance teams

Built on Gartner's three recommended actions [3] and the operational advice from IBS [5]:

- [ ] Do not treat voice or video alone as proof of identity [5]
- [ ] Confirm wire transfers, bank detail changes and unusual payment requests through a different channel [5]
- [ ] Set dual approval and transaction limits for high-value payments [5]
- [ ] Verify supplier bank detail changes only through registered contact channels [5]
- [ ] Protect high-value workflows such as account recovery, privileged access and payment authorization with phishing-resistant authentication [3]
- [ ] Teach "pause, verify, report" rather than "spot the fake," and apply it to every channel [3]
- [ ] Test verification and reporting behavior with simulations [3]
- [ ] Correlate impersonation reports with new devices, privilege changes and financial transactions [3]
- [ ] Add multi-channel impersonation to your incident response playbooks [3]
- [ ] Check whether your cyber and crime policies cover social engineering losses [5]

There is an HR side to this list too. Employees will only question a "confidential" request if they are sure they won't be punished for it. To check whether training actually changes behavior, see our guide on [how to measure training effectiveness](/en/how-to-measure-training-effectiveness-habit-hugging/). For personal account hygiene, read our [phone and account security guide](/en/phone-and-account-security/), and for the fake-carrier version of the same trick in logistics, our post on [fictitious pickup cargo theft](/en/fictitious-pickup-cargo-theft-freight-fraud-prevention/).

## Frequently asked questions

### What is deepfake CEO fraud?

It is when an attacker impersonates a senior executive, using AI-generated voice or video, to get an employee to make a payment or take a sensitive action. In the $129 million US case, the defendants allegedly used AI to mimic CEOs' voices and images [1].

### How can you spot a deepfake call?

Gartner says AI is reducing the reliability of familiar detection cues [3]. Rather than trying to hear the fake, it is more reliable to verify critical requests through an independent channel.

### Has voice cloning fraud happened in Türkiye?

We found no national statistics for attacks on companies. There are cases targeting individuals: in February 2026, an Osmaniye-based network that used AI-imitated voices and faces in fake investment ads was broken up, with 410 million lira in transaction volume identified [4].

### Does cyber insurance cover deepfake fraud?

Not always. According to IBS CEO Murat Çiftçi, a loss caused by a deceived employee sending money may not be covered by every cyber policy; crime insurance, fraud cover and the cyber policy should be reviewed together [5].

### How common are deepfake calls?

In Gartner's survey of 297 CISOs, 41% reported at least one deepfake social engineering incident on an audio call and 36% on a video call in the past 12 months [3].

## References

1. US Department of Justice, US Attorney's Office SDNY, "Three Foreign Nationals Arrested And Charged With Scheme To Use Super Intelligence To Defraud Companies Of $129 Million", November 5, 2026 (updated November 6, 2026). <https://www.justice.gov/usao-sdny/pr/three-foreign-nationals-arrested-and-charged-scheme-use-super-intelligence-defraud> (Accessed: November 10, 2026)
2. ITPro, Emma Woollacott, "Three charged after impersonating CEOs and attorneys in $129 million deepfake fraud scheme", November 6, 2026. <https://www.itpro.com/security/cyber-crime/three-charged-after-impersonating-ceos-and-attorneys-in-usd129-million-deepfake-fraud-scheme> (Accessed: November 10, 2026)
3. Gartner, "Gartner Survey Finds 41% of CISOs Reported At Least One Social Engineering Incident Involving a Deepfake in the Past 12 Months", September 22, 2026. <https://www.gartner.com/en/newsroom/press-releases/2026-09-22-gartner-survey-finds-41-percent-of-cisos-reported-at-least-one-social-engineering-incident-involving-a-deepfake-in-the-past-12-months> (Accessed: November 10, 2026)
4. Güneş (İHA), "Yapay zekalı vurgun: 410 milyon TL'lik dolandırıcılık! Görüntü ve sesleri taklit ettiler" (in Turkish), February 11, 2026. <https://www.gunes.com/yasam/yapay-zekali-vurgun-410-milyon-tllik-dolandiricilik-goruntu-ve-sesleri-taklit-ettiler-1225034> (Accessed: November 10, 2026)
5. n24, Abdulsena Yurtseven, "IBS CEO'su Murat Çiftçi'den şirketlere ses klonlama uyarısı" (in Turkish), October 20, 2026. <https://n24.com.tr/sirket/ibs-ceosu-murat-ciftciden-sirketlere-ses-klonlama-uyarisi> (Accessed: November 10, 2026)
6. Ekonomim, "Yapay zekayla CEO'ları taklit ettiler, 129 milyon dolar çaldılar" (in Turkish), November 7, 2026. <https://www.ekonomim.com/dunya/yapay-zekayla-ceolari-taklit-ettiler-129-milyon-dolar-caldilar-haberi-929779> (Accessed: November 10, 2026)
