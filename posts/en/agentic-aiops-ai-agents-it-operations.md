---
title: Agentic AIOps: how AI agents are changing IT operations (2026 guide)
date: 2026-10-31
updated: 2026-10-31
description: What agentic AIOps is and how AI agents run IT operations. Gartner's 2027 predictions, Google SRE's autonomy levels table, guardrails, token cost control and a starter checklist.
cover_title: Agentic AIOps
cover_icon: aiops
category: yapay-zeka-verimlilik
tr: aiops-nedir-yapay-zeka-ajanlari-bt-operasyonlari
seo_title: Agentic AIOps: AI agents in IT operations (2026 guide)
meta_description: Agentic AIOps: Gartner expects 50% of organizations to use AI agents with minimal human involvement in IT ops by 2030. Autonomy levels table and checklist.
focus_kw: agentic AIOps
keywords: agentic AIOps, AIOps, AI agents IT operations, AIOps use cases, AIOps tools, human-on-the-loop, SRE autonomy levels, incident management, ITSM, Gartner I&O trends 2027
cover_alt: Agentic AIOps: cover graphic of AI agents monitoring servers and an incident dashboard in IT operations
---
When your checkout page goes down, the first person everyone calls is usually the senior engineer who knows the system best. In a guest post published on Webrazzi on October 28, Berkay Özuygur, co-founder and CEO of Parny, warns about the risk of that knowledge living in a few people's heads and compares AIOps to a "senior architect with 20 years at the company" who carries that memory into the system [1]. So what is **agentic AIOps**, how are AI agents changing it, and where should organizations start? Gartner's 2027 predictions, published on October 26, 2026 [2], and the autonomy levels published by Google's SRE team [4] give a concrete framework.

## What is AIOps? A short definition

AIOps means AI-assisted IT operations. According to the Webrazzi post, AIOps learns the relationships between applications, services and infrastructure from the live system data and recorded operational knowledge it can access, and looks at the system as a whole rather than at a single error [1]. Classic monitoring says "something is broken". AIOps tries to answer "why is it broken, and what should we do?"

The post walks through a hypothetical case. Payments start failing after a new software release. AIOps examines error logs, service response times, database connection load and recent changes together. If the evidence points to the new release and rolling back is safe, it performs the rollback within the policies and permissions you set. Where approval is required, it proposes the action with its reasoning and applies it once approved [1]. The author runs an AIOps company and the piece is a guest post, so below we back it up with independent data.

## From human-in-the-loop to human-on-the-loop

Gartner's top AI trends in infrastructure and operations (I&O), published on October 26, 2026, say AI agents are driving a shift from reactive, human-in-the-loop operations to proactive, human-on-the-loop operations [2]. In short:

- **Human-in-the-loop:** the system proposes a fix, a person approves it, then it is applied [1].
- **Human-on-the-loop:** the system applies the fix itself within agreed policies and permissions, while the team watches and steps in when needed [1].

Key Gartner figures for 2027 [2]:

| Gartner prediction or finding (October 26, 2026) | Value |
|---|---|
| Heads of I&O who see scaling AI proofs of concept to I&O adoption as a priority for the next 12 months | 58% (survey of 272, April–May 2026) |
| Organizations using AI agents with minimal human involvement in IT operations by 2030 | 50% (nearly 0% in 2026) |
| How far enterprises using AI agents in IT ops on uncapped, token-based pricing will exceed initial cost expectations (through 2027, compared with subscription models) | More than 50% |
| Large enterprises running production AI workloads across at least three environments by 2029 | 80% |
| Enterprises merging their NOC and SOC by 2030 | 25% (5% in 2026), with over 25% lower tooling and staff spend |

Source: Gartner press release [2]. ITPro's coverage reports the same findings [3].

Quotable stat: **Gartner predicts that by 2030, 50% of organizations will use AI agents with minimal human involvement in IT operations, up from nearly 0% in 2026** [2].

## Reality check: most AIOps projects are not yet paying back

In April 2026, Gartner painted a more cautious picture. In a survey of 782 I&O leaders in November and December 2025, only 28% of AI use cases in I&O fully succeeded and met ROI expectations, and 20% failed outright [5]. 57% of leaders reported at least one failure [5].

Failures were most common in exactly the areas AIOps promises: auto-remediation, self-healing infrastructure and agent-led management of workflows across systems [5]. 53% of AI wins came from IT service management (ITSM) [5]. The lesson is to start with small, mature and measurable use cases.

## Google SRE autonomy levels: how much should an agent be allowed to do?

Google SRE's "AI in SRE" paper defines five levels of agent autonomy [4]. Use the table as a reference when you evaluate AIOps tools: which level does this product actually operate at?

| Level | Monitor | Investigate | Mitigate (approve) | Actuate | Self-direct |
|---|---|---|---|---|---|
| L0 – Manual | Automation | Human | Human | Human | Human |
| L1 – Assisted | Automation | Automation | Human | Human | Human |
| L2 – Partial (human approval) | Automation | Automation | Human | Automation | Human |
| L3 – High | Automation | Automation | Automation | Automation | Human |
| L4 – Full | Automation | Automation | Automation | Automation | Automation |

Source: Google SRE, "AI in SRE: How Google is Engineering the Future of Reliable Operations", Table 1 [4].

Google's own measurements show that even the lower levels deliver value. The purely informational "Incident Hypothesis" feature (L1) cut mean time to mitigate (MTTM) by 10%. Investigation Dashboards cut MTTM by roughly 44% for supported incidents, and the ML-based anomaly detection behind them increased findings by 195% [4]. These results come from Google's own environment, so don't expect the same numbers everywhere.

## Guardrails for agentic AIOps

Google SRE sets out four architectural guardrails for any AI agent that touches production [4]:

| Guardrail [4] | What it means |
|---|---|
| No ambient access and least privilege | Agents never run on their developers' standing credentials; they have distinct identities and get permissions on demand |
| Agentic circuit breakers | Agent-specific rate limits and automatic breakers stop runaway loops; every action must be interruptible |
| Mandatory dry run | Every API an agent uses must support a dry_run mode that shows the outcome and blast radius in advance |
| Zero-trust, safe-by-default actuation | Infrastructure tools must be unable to take down production on their own, whoever calls them |

These principles map closely to the agent security issues in our posts on [Microsoft execution containers](/en/microsoft-execution-containers-ai-agent-security/) and [employee-built AI agents](/en/employee-built-ai-agents-security-risk/).

## Token costs: "no telemetry, no deployment"

One Gartner prediction is about budget. Through 2027, enterprises that run AI agents in IT operations on uncapped, token-based pricing will exceed their initial cost expectations by more than 50%, compared with those on subscription models. Gartner recommends a strict "no telemetry, no deployment" policy [2]. In other words, no agent should go live if its usage and cost can't be measured. We cover this in detail in our [guide to managing AI token costs](/en/manage-ai-token-costs-finops/).

## Market signal: money is flowing to IT operations agents

Webrazzi reported on October 30, 2026 that Serval, a US company focused on IT operations, raised a $150 million Series C led by Sequoia at a $3 billion valuation [6]. Its AI agents manage employee access permissions, resolve technical issues and track software and hardware assets. IT and security teams decide what the agents can access, and sensitive actions can require human approval [6]. That corresponds to L2 in the table above.

Some Türkiye context: according to TÜİK's AI Statistics 2026 bulletin, the share of enterprises using AI rose from 7.5% to 14%. In telecommunications, programming and IT it reached 63.7% [7]. IT teams are the heaviest AI users, so AIOps decisions are likely to be made there first.

## Checklist for getting started with AIOps

- [ ] Start where success is best proven: IT service management and incident investigation [5]
- [ ] For each use case, write down the target level from Google's L0–L4 table and cap it at L1–L2 at first [4]
- [ ] Give agents their own identities; never let them use human credentials [4]
- [ ] Define written policies and permission limits for actions like rollbacks, and list the cases that need approval [1]
- [ ] Make sure every API the agent uses supports dry run and has a circuit breaker [4]
- [ ] "No telemetry, no deployment": don't go live until token usage and cost are measured [2]
- [ ] Measure today's MTTM as a baseline, or you won't be able to prove any improvement [4]
- [ ] Record post-incident learnings so the knowledge doesn't stay with a few people [1]
- [ ] Keep expectations low for auto-remediation and self-healing infrastructure, where failure is most common [5]
- [ ] Validate vendor claims with a pilot in your own environment

## Frequently asked questions

### What is agentic AIOps?

It is AI-assisted IT operations in which goal-driven software agents carry out IT workflows such as incident triage, change validation and remediation with minimal human intervention [2].

### What does human-on-the-loop mean?

The AI system applies a fix itself within agreed policies and permissions, while the team monitors and steps in when needed. In human-in-the-loop, a person must approve before anything is applied [1][2].

### Do AIOps projects succeed?

In a Gartner survey of 782 I&O leaders, only 28% of AI use cases in I&O fully succeeded and met ROI expectations, and 20% failed outright [5].

### How much autonomy should AI agents get in IT operations?

Google SRE defines five autonomy levels, L0 to L4, and releases agents at lower, human-approved levels before scaling them up [4].

### How do you control AIOps costs?

Gartner predicts that enterprises running AI agents in IT ops on uncapped, token-based pricing will exceed initial cost expectations by more than 50% through 2027. It recommends a "no telemetry, no deployment" policy [2].

## References

1. Webrazzi, Berkay Özuygur (guest author, co-founder and CEO of Parny), "AIOps: Tech ekibinin 20 yıllık kıdemli mimarı" (in Turkish), October 28, 2026. <https://webrazzi.com/2026/10/28/aiops-tech-ekibinin-20-yillik-kidemli-mimari/> (Accessed: October 31, 2026)
2. Gartner, "Gartner Identifies the Top AI Trends in Infrastructure and IT Operations for 2027", October 26, 2026. <https://www.gartner.com/en/newsroom/press-releases/2026-10-26-gartner-identifies-the-top-ai-trends-in-infrastructure-and-it-operations-for-2027> (Accessed: October 31, 2026)
3. ITPro, Emma Woollacott, "AI is crucial to infrastructure and IT operations but only if it's done right, Gartner report says", October 26, 2026. <https://www.itpro.com/infrastructure/ai-is-crucial-to-infrastructure-and-it-operations-but-only-if-its-done-right-gartner-report-says> (Accessed: October 31, 2026)
4. Google SRE, Ioannis Papapanagiotou, Stevan Malesevic, Chris Heiser and Ruslan Meshenberg, "AI in SRE: How Google is Engineering the Future of Reliable Operations". <https://sre.google/resources/practices-and-processes/ai-engineering-reliable-operations/> (Accessed: October 31, 2026)
5. Gartner, "Gartner Says AI Projects in I&O Stall Ahead of Meaningful ROI Returns", April 7, 2026. <https://www.gartner.com/en/newsroom/press-releases/2026-04-07-gartner-says-artificial-intelligence-projects-in-infrastructure-and-operations-stall-ahead-of-meaningful-roi-returns> (Accessed: October 31, 2026)
6. Webrazzi, Candeğer Muradoğlu, "Serval, 3 milyar değerleme üzerinden 150 milyon dolar yatırım aldı" (in Turkish), October 30, 2026. <https://webrazzi.com/2026/10/30/serval-3-milyar-degerleme-uzerinden-150-milyon-dolar-yatirim-aldi/> (Accessed: October 31, 2026)
7. Anadolu Agency, Mertkan Oruç, "Türkiye yapay zekayı en çok bilişimde, en az inşaatta kullanıyor" (TÜİK AI Statistics 2026, in Turkish), October 3, 2026. <https://www.aa.com.tr/tr/bilim-teknoloji/turkiye-yapay-zekayi-en-cok-bilisimde-en-az-insaatta-kullaniyor/4076782> (Accessed: October 31, 2026)
