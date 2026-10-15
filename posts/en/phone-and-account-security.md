---
title: Phone and account security: An evidence-based guide for professionals
date: 2026-10-15
updated: 2026-10-15
description: From two-factor authentication and passkeys to smishing and a lost-phone plan: a step-by-step guide to protecting your phone and your accounts, backed by NIST, CISA, Google and Apple sources.
cover_title: Phone and account security guide
cover_icon: phone
category: dijital-guvenlik
tr: telefon-ve-hesap-guvenligi
---
Your work email, your company chat app, your banking app and the verification codes for most of your accounts now live on one device: your phone. That makes it both extremely valuable and an attractive target.

Verizon's 2026 Data Breach Investigations Report (DBIR) found that the human element was present in 62% of breaches. The same report notes that in phishing simulations, the median click rate for mobile-centric vectors such as voice calls and text messages is 40% higher than for email [1]. In short, attackers are increasingly going after what's in our pockets.

This guide walks you through practical steps to protect your personal and work accounts, each one tied to the source behind it.

## First, separate two things: device security and account security

Security measures protect two different layers, and mixing them up is a common mistake:

- **Account security** stops other people from getting into your online accounts: email, LinkedIn, WhatsApp, cloud storage. Two-factor authentication (2FA), strong passwords and passkeys live here.
- **Device security** protects what's on your phone if someone gets physical access to it or if it meets malicious software. Screen lock, software updates, app permissions and remote lock/erase live here.

An important point: **two-factor authentication protects your accounts, not your phone.** It makes it much harder for someone to get into an account even if they have your password, but it does nothing for a phone left unlocked on a table. You need to invest in both layers separately.

## For your accounts: multi-factor authentication (2FA/MFA)

The US Cybersecurity and Infrastructure Security Agency (CISA) defines multi-factor authentication (MFA) as requiring a combination of two or more authenticators before a service grants access. The logic is simple: even if an attacker steals your password, they can't pass the second step [2].

The effect has been measured. In a year-long study Google ran with New York University and UC San Diego, an SMS code sent to a recovery phone number helped block 100% of automated bots, 96% of bulk phishing attacks and 76% of targeted attacks. On-device prompts raised those figures to 100%, 99% and 90% respectively [3]. Microsoft likewise says MFA can block over 99.9% of account compromise attacks [4].

### Not every method is equally strong

According to CISA, not all MFA offers the same protection; the standard to aim for is phishing-resistant authentication. The agency points out that the only widely available phishing-resistant method is FIDO/WebAuthn. Still, any MFA is better than no MFA [2].

NIST's digital identity guideline, SP 800-63B, does not consider one-time passcodes (OTP) or out-of-band codes such as SMS to be phishing-resistant. It also classifies authentication over the telephone network (SMS or voice) as a "restricted authenticator" [5].

In practice, from strongest to weakest:

1. **Passkey or hardware security key:** According to the FIDO Alliance, passkeys are phishing-resistant credentials stored on your device and used with the same method you use to unlock it (fingerprint, face, PIN) [6].
2. **App prompt or authenticator app:** Google recommends Google prompts over text codes and notes that prompts also help protect against SIM swap and other phone number-based hacks [7].
3. **SMS code:** In Google's words, any form of 2-Step Verification adds security, but codes sent by text or call can be vulnerable to phone number-based hacks [7].

### Step by step: turn on 2FA for your critical accounts

Start with the accounts that matter most: email (the reset door for everything else), your Apple or Google account, LinkedIn and WhatsApp. Menu names may vary slightly by device language and version.

- **Google account:** Google Account > Security & sign-in > under "How you sign in to Google", turn on 2-Step Verification. In case you lose your phone, print or download the 8-digit backup codes and keep them somewhere safe [7].
- **Apple Account:** Settings > [your name] > Sign-In & Security, then turn on two-factor authentication. Apple says it is now the default security method for most accounts [8].
- **LinkedIn:** Settings & Privacy > Sign in & security > Two-factor authentication. LinkedIn offers an authenticator app or SMS [9].
- **WhatsApp:** Turn it on in the two-step verification section of Settings. WhatsApp says it is upgrading the 6-digit two-step verification PIN to a password; keep your email address up to date there too [10].

> Tip: Never share verification codes. Google states plainly that it will never call you to verify a code [7]. Anyone who calls saying "we're from your bank, can you read me the code you just got?" is almost certainly a scammer.

## Passwords: long, unique and in a password manager

NIST's current guideline overturns a lot of old habits. According to it [5]:

- Passwords used on their own should be **at least 15 characters**; passwords that are only part of MFA can have a minimum of 8.
- Composition rules such as "must include upper case, a number and a symbol" should not be imposed.
- Periodic forced password changes should not be required, but a change should be forced if there is evidence of compromise.
- Password managers and autofill should be allowed; NIST notes that password managers have been shown to increase the likelihood of choosing stronger passwords.

Password reuse is one of the biggest risks. Citing a SANS paper, Microsoft notes that up to 73% of passwords are duplicates [4]. A breach at one site puts every account sharing that password at risk.

**What to do:**

1. Actually use your phone's built-in password manager (iCloud Keychain, Google Password Manager) or another password manager you trust.
2. Start by creating unique, long passwords for critical accounts such as email and banking.
3. Check whether your email address appears in known data breaches with Have I Been Pwned, a free resource built for exactly that purpose [11].
4. Create passkeys wherever they're supported. Google notes that signing in with a passkey bypasses the second step because it verifies that you have your device [7].

## Phishing: watch texts and calls as closely as email

CISA lists the common signs of phishing: urgent or emotionally charged language, requests for personal or financial information, untrusted shortened URLs and lookalike addresses such as "amaz0n.com". CISA also warns that in the age of AI, some phishing emails now have perfect grammar and spelling, so typos are no longer a reliable signal [12].

The 2026 DBIR shows social engineering moving toward voice and mobile channels. Pretexting, where an attacker builds a trusted relationship through an invented scenario, reached 6% of all breaches as an initial access vector, while phishing stayed at 16%, the same as the previous year [1].

**Habits that work:**

- Instead of tapping the link in a message, open the app or website yourself. CISA advises that even if you think a message may be real, you shouldn't call the number in it; use the organization's verified contact details instead [12].
- Pause and check any urgent text like "your parcel is waiting", "your account has been suspended" or "you have a tax refund".
- At work, confirm unexpected requests such as "urgent payment request from the CEO" through a different channel (a call or in person).
- In Türkiye, according to a USOM notice, cyber incident reports and malicious link lists are now handled by the Cyber Security Directorate at siberguvenlik.gov.tr [13].

## For your device: updates, screen lock and permissions

### Don't postpone updates

CISA reminds us that many software updates exist to fix security risks and recommends turning on automatic updates [14]. The 2026 DBIR shows why: exploitation of vulnerabilities has become the most common initial access vector for breaches at 31%, overtaking credential abuse (13%) [1].

**Do:** Turn on automatic updates for the operating system and the app store in Settings. Keep your browser and work apps up to date as well.

### Use a strong screen lock

Alongside two-factor authentication, Apple recommends protecting your device with a passcode and enabling Face ID or Touch ID if supported [8]. On Android, you need to set a PIN, pattern or password for the Find Hub network to help you find a lost device [16]. Avoid easy-to-guess codes such as your birth year or 123456.

### Review app permissions

- **Android:** Go to Settings > Apps > [app] > Permissions to change an app's permissions. Settings > Security & privacy > Privacy > Permission manager shows every app with the same permission (location, camera, microphone, contacts) in one list. There's also a "Pause app activity if unused" option for apps you don't use [15].
- **iPhone:** Review permissions, starting with Location Services, under Settings > Privacy & Security [17].

For location, choose "Allow only while using the app" whenever possible [15].

## If your phone is lost or stolen

Preparation happens before the incident. Check these settings today:

- **Android – Find Hub:** If you've added a Google Account to your device, Find Hub is turned on automatically. You can locate a lost device from another device or a browser, lock it with "Mark as lost", or erase it with a factory reset. You can also find your IMEI number there so your carrier can block the device [16].
- **iPhone – Find My:** Lost Mode locks the device and, on compatible devices, suspends Apple Pay cards. According to Apple, if your Apple Account doesn't have two-factor authentication, you can't erase the device remotely from the Find My app [18]. Here 2FA protects your Apple Account, not the phone itself, which is what makes remote management safe.
- **iPhone – Stolen Device Protection:** Available on iOS 17.3 and later, this feature requires Face ID or Touch ID for actions like using saved passwords when your iPhone is away from familiar locations such as home or work. For critical actions like changing your Apple Account password, it adds a one-hour security delay, so even a thief who knows your passcode can't take over your account right away. It must be turned on before the device is lost: Settings > Face ID & Passcode > Stolen Device Protection [17].

**In the moment, in this order:** mark the device as lost, change your email and banking passwords from another device, call your carrier to block the SIM, and tell your company's IT team about work accounts.

## 15-minute checklist

- [ ] 2FA is on for email, Apple/Google, LinkedIn and WhatsApp; passkeys or app prompts are used where possible.
- [ ] 2FA backup codes are stored somewhere safe.
- [ ] Passwords for critical accounts are unique and stored in a password manager.
- [ ] Your email address has been checked on Have I Been Pwned.
- [ ] Automatic updates are on.
- [ ] A strong screen lock and biometrics are set up.
- [ ] Location, camera, microphone and contacts permissions have been reviewed.
- [ ] Find Hub / Find My is on; Stolen Device Protection is enabled on iPhone.

None of these steps requires technical expertise, but together they close most of the routes attackers use most often.

## References

1. Verizon, "2026 Data Breach Investigations Report – Executive Summary". <https://www.verizon.com/business/resources/executivebriefs/2026-dbir-executive-summary.pdf> (Accessed: October 15, 2026)
2. CISA, "More than a Password". <https://www.cisa.gov/MFA> (Accessed: October 15, 2026)
3. Google Online Security Blog, "New research: How effective is basic account hygiene at preventing hijacking", May 17, 2019. <https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html> (Accessed: October 15, 2026)
4. Microsoft Security Blog, "One simple action you can take to prevent 99.9 percent of attacks on your accounts", August 20, 2019. <https://www.microsoft.com/en-us/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/> (Accessed: October 15, 2026)
5. NIST, "SP 800-63B-4: Digital Identity Guidelines – Authentication and Authenticator Management". <https://pages.nist.gov/800-63-4/sp800-63b.html> (Accessed: October 15, 2026)
6. FIDO Alliance, "Passkeys". <https://fidoalliance.org/passkeys/> (Accessed: October 15, 2026)
7. Google Account Help, "Turn on 2-Step Verification". <https://support.google.com/accounts/answer/185839?hl=en> (Accessed: October 15, 2026)
8. Apple Support, "Two-factor authentication for Apple Account". <https://support.apple.com/en-us/102660> (Accessed: October 15, 2026)
9. LinkedIn Help, "Turn two-factor authentication on and off". <https://www.linkedin.com/help/linkedin/answer/a1381088/turn-two-step-verification-on-and-off> (Accessed: October 15, 2026)
10. WhatsApp Help Center, "How to manage two-step verification settings". <https://faq.whatsapp.com/1920866721452534> (Accessed: October 15, 2026)
11. Have I Been Pwned, "Who, What & Why". <https://haveibeenpwned.com/About> (Accessed: October 15, 2026)
12. CISA, "Recognize and Report Phishing". <https://www.cisa.gov/secure-our-world/recognize-and-report-phishing> (Accessed: October 15, 2026)
13. USOM – National Computer Emergency Response Center of Türkiye, notice (in Turkish). <https://www.usom.gov.tr> (Accessed: October 15, 2026)
14. CISA, "Update Software". <https://www.cisa.gov/secure-our-world/update-software> (Accessed: October 15, 2026)
15. Android Help, "Change app permissions on your Android phone". <https://support.google.com/android/answer/9431959?hl=en> (Accessed: October 15, 2026)
16. Android Help, "Find, secure, or erase a lost Android device". <https://support.google.com/android/answer/6160491?hl=en> (Accessed: October 15, 2026)
17. Apple Support, "About Stolen Device Protection for iPhone". <https://support.apple.com/en-us/120340> (Accessed: October 15, 2026)
18. Apple Support, "Use Find My to locate your lost Apple device or AirTag". <https://support.apple.com/en-us/104978> (Accessed: October 15, 2026)
