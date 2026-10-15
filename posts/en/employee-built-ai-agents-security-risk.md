---
title: Are employee-built AI agents the new security gap? What Pluto's funding and OWASP and NIST guidance say
date: 2026-10-15
updated: 2026-10-15
description: Pluto's funding round, reported by Webrazzi, puts a spotlight on the risks of AI agents that employees build themselves. Drawing on OWASP and NIST sources, we map the risks and the concrete steps companies can take.
cover_title: How safe are AI agents built by staff?
cover_icon: agentshield
category: dijital-guvenlik
tr: calisan-yapay-zeka-ajanlari-guvenlik-riski
seo_title: AI agent security risks: A 9-step checklist for companies
meta_description: Employee-built agents and shadow AI widen the attack surface: 9-step checklist on AI agent security risks based on OWASP and NIST guidance and Pluto's funding.
focus_kw: AI agent security risks
keywords: AI agent security risks, shadow AI, excessive agency OWASP LLM06, agent hijacking, MCP security, AI agent security checklist
cover_alt: AI agent security risks and shadow AI, cover image
---
A funding story reported by Turkish tech outlet Webrazzi on October 14 points to a new blind spot for companies. Pluto, a cybersecurity startup founded in 2025, has raised a total of $42.5 million in two stages: an $8.5 million seed round led by TLV Partners, followed by a $34 million Series A led by Jump Capital [1]. In this article we break down AI agent security risks using OWASP, NIST and KVKK sources and offer a 9-step checklist for companies.

What makes the story significant is Pluto's focus. According to Webrazzi, its software monitors the AI tools employees use, as well as plugins, MCP servers and the agents employees create, to detect potential security risks. Pluto focuses in particular on risks from applications built with AI help by employees who are not software developers. When an agent tries to exceed the permissions it was given, the system can stop the action or ask the user for approval [1].

Investor money in a space is not proof on its own, but the signal is clear. The question is no longer just "which AI tools are employees using?" but "what authority are employees handing over to AI?"

## From shadow AI to shadow agents

"Shadow AI" has entered official vocabulary in Türkiye too. The Turkish Personal Data Protection Authority (KVKK) published a document in February 2026 titled "Use of Generative AI Tools in the Workplace", which defines shadow AI as employees using generative AI tools in business processes without the organization's knowledge, approval or control. The Authority notes that for many organizations this is no longer a theoretical risk but something encountered in everyday workflows [3].

The data backs this up. According to Verizon's 2026 Data Breach Investigations Report, 67% of users access AI services from corporate devices using non-corporate accounts. And 45% of employees are now regular AI users on corporate devices, up from 15% the year before. Shadow AI has become the third most common non-malicious insider action in Verizon's data loss prevention (DLP) dataset [2].

Agents add a new layer to this picture. Pasting text into a chatbot carries a data leakage risk. But an agent connected to a mailbox, a file store or a CRM can go beyond reading and take actions such as sending, deleting and changing data.

## AI agent security risks: OWASP's framework

OWASP's generative AI security project defines this risk as Excessive Agency (LLM06:2025). According to OWASP, its root cause is typically one of three things: excessive functionality, excessive permissions or excessive autonomy [4]. Its example is a familiar one: if a plugin set up to summarize emails can also send messages, a maliciously crafted incoming email can trick the agent into forwarding sensitive information to an attacker [4].

In December 2025 OWASP broadened this work with its Top 10 for Agentic Applications. The list includes agent goal hijack (ASI01), misuse of legitimate tools (ASI02), identity and privilege abuse (ASI03) and supply chain vulnerabilities in dynamic ecosystems such as MCP (ASI04) [5]. OWASP sums up its message in one line: once AI began taking actions, the nature of security changed [5].

## NIST: "Agent hijacking" is a measurable risk

The Center for AI Standards and Innovation (CAISI) at the US National Institute of Standards and Technology (NIST) defines agent hijacking as a type of indirect prompt injection. An attacker plants malicious instructions in an email, file or website the agent processes, steering it toward unintended actions [7].

CAISI's experiments show the scale of the risk. Using new attacks developed specifically for the model, the team reported that the attack success rate rose from 11% for the strongest baseline attack to 81%. When each of five injection tasks was attempted 25 times, the average success rate rose from 57% to 80% [7]. The results show that an agent passing a single test does not mean it is safe.

NIST's broader AI Risk Management Framework (AI RMF 1.0) is designed for voluntary use. Its Generative AI Profile (NIST AI 600-1), released in 2024, helps organizations identify risks specific to generative AI [8].

## What it means for companies in Türkiye

For companies in Türkiye, the issue is not only technical but legal. The KVKK document says that banning AI tools outright is unlikely to produce realistic results in practice and may even encourage uncontrolled use. Instead, it recommends approaches based on guidance, balance and awareness [3]. That advice applies to agents as well: rather than suppressing employees' desire to automate their own workflows, companies need to channel it safely.

As no-code agent builders spread, IT and security teams will need to be able to answer: "which agent, acting for whom, connected to which system, with what permissions?" Without that inventory, a mistake by an agent connected to a system holding personal data lands directly on the company as data controller.

For basic account protection, see our [phone and account security guide](/en/phone-and-account-security/); for using AI without leaking company data, see our [guide to free AI tools](/en/free-ai-tools/). And for agents connected to HR systems, read our article on [AI agents in HR](/en/hr-ai-agents-workday-sap-metaview/).

## AI agent security checklist: What should companies do?

Based on OWASP's agent security guidance and Excessive Agency recommendations [4][6] and the KVKK approach [3]:

1. **Build an inventory.** List the AI tools, plugins, MCP servers and employee-built agents in use. Record each one's owner, connected systems and permissions.
2. **Apply least privilege.** Give agents only the tools and permissions their task needs. If read access is enough, don't grant write or delete [4][6].
3. **Run agents in the user's context.** Use the user's own permission scope and limited authorization such as OAuth instead of shared high-privilege accounts [4].
4. **Require human approval for high-impact actions.** Sending email, bulk deletion, payments or permission changes should not run without a person's approval [4][6].
5. **Don't trust external content.** Treat emails, documents and web pages the agent reads as untrusted input. This is the channel agent hijacking uses [6][7].
6. **Log and monitor every action.** Record tool calls, decisions and outcomes, and set alerts for unusual behavior [6].
7. **Vet third-party components.** Assess public skills, plugins and connectors for security before using them. OWASP covers this risk under agentic supply chain vulnerabilities [5]. According to Webrazzi, Pluto's free Plutonium platform is also aimed at analyzing such components [1].
8. **Update policy and training.** Add a dedicated section on agents to your corporate AI policy, and state clearly which data may be processed with agents [3].
9. **Test regularly.** Test agents with prompt injection and privilege escalation scenarios before going live and whenever prompts, tools or models change [6][7].

Employee-built agents are not a trend you can stop with a ban. But they can be made visible, bounded and auditable. Companies that do this today will face fewer "shadow agent" incidents tomorrow.

## Frequently asked questions

### What is shadow AI?

According to Türkiye's data protection authority (KVKK), it is the use of generative AI tools in business processes by employees without the organization's knowledge, approval or control [3].

### What is the "excessive agency" risk in AI agents?

OWASP defines it as LLM06:2025, Excessive Agency. The root cause is usually excessive functionality, excessive permissions or excessive autonomy. If a plugin set up to summarize emails can also send messages, a maliciously crafted incoming email could trick the agent into forwarding sensitive information to an attacker [4].

### What is agent hijacking?

According to CAISI at NIST, it is a form of indirect prompt injection: an attacker plants malicious instructions in an email, file or website the agent processes, steering it into unintended actions [7].

### Is banning employee AI use the answer?

The KVKK document says a complete ban is not realistic in practice and may even encourage uncontrolled use. It recommends approaches based on guidance, balance and awareness instead [3].

## References

1. Webrazzi, Candeğer Muradoğlu, "Siber güvenlik girişimi Pluto, toplamda 42,5 milyon dolar yatırım aldı" (in Turkish), October 14, 2026. <https://webrazzi.com/2026/10/14/siber-guvenlik-girisimi-pluto-toplamda-42-5-milyon-dolar-yatirim-aldi/> (Accessed: October 15, 2026)
2. Verizon, "2026 Data Breach Investigations Report – Executive Summary" (PDF). <https://www.verizon.com/business/resources/executivebriefs/2026-dbir-executive-summary.pdf> (Accessed: October 15, 2026)
3. KVKK, "İş Yerlerinde Üretken Yapay Zekâ Araçlarının Kullanımı" (Use of Generative AI Tools in the Workplace), February 2026 (PDF, in Turkish). <https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/MTY5YTdkNjdjNzJlMjM.pdf> (Accessed: October 15, 2026)
4. OWASP Gen AI Security Project, "LLM06:2025 Excessive Agency". <https://genai.owasp.org/llmrisk/llm062025-excessive-agency/> (Accessed: October 15, 2026)
5. OWASP Gen AI Security Project, "OWASP Top 10 for Agentic Applications – The Benchmark for Agentic Security in the Age of Autonomous AI", December 9, 2025. <https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/> (Accessed: October 15, 2026)
6. OWASP Cheat Sheet Series, "AI Agent Security Cheat Sheet". <https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html> (Accessed: October 15, 2026)
7. NIST, "Technical Blog: Strengthening AI Agent Hijacking Evaluations", January 17, 2025. <https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations> (Accessed: October 15, 2026)
8. NIST, "AI Risk Management Framework". <https://www.nist.gov/itl/ai-risk-management-framework> (Accessed: October 15, 2026)
