---
title: AI agent containment security: What Microsoft Execution Containers (MXC) add
date: 2026-10-16
updated: 2026-10-16
description: Microsoft made Execution Containers generally available to isolate AI agents with file and network policies. What AI agent containment security means against shadow-agent risk at the OS layer.
cover_title: Containing agents at the OS layer
cover_icon: agentshield
category: dijital-guvenlik
tr: microsoft-execution-containers-ajan-guvenligi
seo_title: AI agent containment security: Microsoft MXC
meta_description: AI agent containment security with Microsoft Execution Containers (MXC): process, session, WSL, MicroVM options and a practical IT checklist. Kaynaklı rehber.
focus_kw: AI agent containment security
keywords: AI agent containment security, AI agent sandbox, Microsoft Execution Containers, least-privilege agents, process container, Agent 365
cover_alt: AI agent containment security: Microsoft Execution Containers cover image
---
As agents touch files, networks and apps, productivity rises — and so does the attack surface. According to a Windows Developer Blog post on October 7, 2026, **Microsoft Execution Containers (MXC)** are generally available and provide a policy-driven **containment** layer for agents [1]. This article explains **AI agent containment security** through MXC, links it to the Pluto/OWASP shadow-agent debate, and ends with an IT checklist.

## Three pillars: Containment, identity, manageability

Microsoft's framing has three parts [1]:

1. **Containment** — limit which files and network destinations an agent can use
2. **Identity** — distinguish agent activity from a person (coming with Microsoft Entra / Agent 365)
3. **Manageability** — govern access and monitor agent activity

MXC delivers the first pillar. Developers and IT admins declare allowed resources; MXC enforces the boundary at runtime with the right container [1]. Policy stays outside the agent's control: the agent cannot grant itself more access [1].

## Why a managed boundary matters

Microsoft's example is familiar: a coding agent is asked to update a website. It needs write access to the repo and build tools; it may need to **read** production configuration but must not **change** it. Without a managed boundary, the agent may decide that editing production config is the fastest way to finish [1]. Containment enforces that limit independently of the model.

That lines up with the OWASP "Excessive Agency" warning in our [employee-built agents security piece](/en/employee-built-ai-agents-security-risk/): the root cause is often too much function, permission or autonomy.

## MXC backend spectrum

Microsoft lists isolation levels for different workloads [1]:

| Backend | Availability | Best for |
|---|---|---|
| Process container | Windows 11, macOS, Linux | Lightweight, low-latency work; AppContainer / Seatbelt / Bubblewrap |
| Session container | Windows 11 only | Long-running agents; separate account, desktop, clipboard, input |
| WSL container (WSLc) | Windows 11 only | Linux-first agent toolchains |
| MicroVM | Windows 11 and Linux (experimental) | Higher risk; hardware-backed isolation |

Policy areas include containment type, process launch, filesystem (read/write/deny), network (in/out) and UI access [1].

## Learning modes: Observe, then enforce

On Windows only, process containers can emit an agent activity report. Three modes exist [1]:

| Mode | Ungranted access | Report |
|---|---|---|
| Enforcement | Blocked | No |
| Learning | Blocked + recorded | Yes |
| Permissive | Allowed + recorded | Yes (for policy authoring) |

First policies often block legitimate needs; Learning/Permissive help find the gaps [1].

## Who is using MXC?

The post says GitHub Copilot, OpenClaw, OpenAI Codex, Replit, LM Studio and Unsloth AI already support MXC; Anthropic Claude Code, Box, Perplexity and others are expected to follow. NVIDIA integrated OpenShell with MXC. Windows 365 support for MXC is generally available [1].

For basic account hygiene see [phone and account security](/en/phone-and-account-security/); for HR-connected agents see [AI agents in recruiting](/en/hr-ai-agents-workday-sap-metaview/).


## A practical reading for mixed fleets

MXC is Windows-heavy, with process-container support also on macOS and Linux [1]. Many organizations run mixed fleets: Windows 11 in the office, Macs for developers, Linux on plant terminals. Keeping one policy schema and mapping backends per device matches Microsoft's model [1].

From a privacy angle, if an agent will touch folders or systems with personal data, the isolation boundary is not just a technical preference — it is a data-minimization control. Containment hardens the difference between "give the agent everything and hope" and "give the agent only the task folder" at the OS layer [1].

Cloud-side, general availability of MXC on Windows 365 lets teams run agents on a Cloud PC under central policy instead of on every laptop [1]. That is useful when IT wants to trial agents without widening the local attack surface.

## Checklist: AI agent containment security

- [ ] Is a least-privilege policy (files + network + UI) written per agent?
- [ ] Are production configs / secrets outside the agent's write scope?
- [ ] Do coding agents run inside MXC or an equivalent sandbox?
- [ ] Was Learning mode used to tighten policy from activity reports?
- [ ] Can agent identity be separated from user identity? (Agent 365 roadmap [1])
- [ ] Is an Intune / MDM MXC policy planned?
- [ ] Are employee-built agents in the inventory? ([shadow-agent checklist](/en/employee-built-ai-agents-security-risk/))

## Frequently asked questions

### What is AI agent containment security?

Limiting which files, networks and UI resources an agent (or its generated code) can reach — enforced at the OS/container layer, not by the agent itself. MXC does this with policy-driven containers [1].

### Is MXC an antivirus?

No. It is a containment layer. Identity and manageability are separate pillars [1].

### Why care about session containers?

They separate the agent from the interactive user session — desktop, clipboard and input included [1]. Useful for long-running automation.

### Does it only work on Windows?

Process containers run on Windows, macOS and Linux; session and WSL are Windows 11 only; MicroVM is experimental on Windows 11 and Linux [1].

### Does this replace Pluto-style agent security products?

Complementary. Inventory/behavior tools watch what agents do; MXC constrains what they *can* do at runtime [1]. Defense in depth uses both.

## References

1. Windows Developer Blog, Logan Iyer, "Microsoft Execution Containers: Policy-driven containment for AI agents", October 7, 2026. <https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/> (Accessed: October 16, 2026)
