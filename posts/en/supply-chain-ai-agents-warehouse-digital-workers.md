---
title: AI agents in the supply chain and "digital workers" in the warehouse: What SAP, Descartes, IFS Softeon and CEVA are doing
date: 2026-10-15
updated: 2026-10-15
description: In the first two weeks of October, SAP, Descartes, IFS Softeon and CEVA Logistics announced AI agents and robotics for supply chain and warehouse operations. The common theme: autonomy that runs within human approvals and defined permissions.
cover_title: The era of the warehouse digital worker
cover_icon: warehouse
category: lojistik-nakliyat
tr: tedarik-zinciri-yapay-zeka-ajanlari-depo-dijital-isci
seo_title: AI agents in the supply chain: SAP, Descartes, IFS, CEVA
meta_description: How AI agents in the supply chain change warehouses: SAP Joule agents, the Descartes Agent Control Plane, IFS Softeon digital workers and CEVA's RaaS robots.
focus_kw: AI agents in supply chain
keywords: AI agents in supply chain, AI in warehouse management, AI agents in logistics, digital workers, robotics as a service, WMS
cover_alt: AI agents in the supply chain and digital workers in the warehouse, cover image
---
The first two weeks of October 2026 belonged to AI agents in supply chain software. On October 6, Descartes introduced a "control plane" that keeps agents within approvals and permissions [2]. On October 8, SAP announced new Joule agents for the supply chain [1]. On October 13, IFS Softeon unveiled "digital workers" embedded in its warehouse management system [3]. And on October 14 came news that CEVA Logistics had started using AI-driven robots as a service at two European warehouses [4]. Here we compare what AI agents in the supply chain mean for warehouse and logistics teams.

These announcements give different answers to the same question: how much of planning, warehousing and shipping can we hand over to AI, and where does the human stay in the loop?

## At a glance: Four announcements

| Company | What was announced | Date | Who stays in control |
|---|---|---|---|
| SAP | New Joule assistants and agents for the supply chain | October 8 [1] | Agents initiate coordinated action when authorized [1] |
| Descartes | Agent Control Plane on the GLN | October 6 [2] | Customer-defined permissions and approval points [2] |
| IFS Softeon | Fulfillment Flow with area-based digital workers | October 13 [3] | The warehouse manager makes the final call [3] |
| CEVA and Sereact | Returns sorting via robotics as a service (RaaS) | Reported October 14 [4] | Teams focus on supervision, exceptions and quality control [4] |

## SAP: Joule agents from planning to dispatch

At SAP Connect, SAP said it was expanding the capabilities of six Joule Assistants introduced earlier at SAP Sapphire and adding specialized Joule Agents for critical supply chain tasks [1]. The highlights [1]:

- **Supply Chain Planning Assistant:** Helps planners sense, simulate and resolve exceptions in a single workspace.
- **Manufacturing Assistant:** Aims to help teams respond to plant-floor disruptions as they happen.
- **Logistics Assistant:** New capabilities span warehousing, outbound optimization, fulfillment and transportation dispatching.
- **Asset Operations Assistant:** Turns equipment and maintenance signals into action by supporting the initiation, screening and simulation of maintenance requests.
- **Business Network Assistant:** Improves collaboration with suppliers and logistics partners on sourcing, contracting and exception handling.

SAP plans general availability for these new capabilities in Q4 2026 [1]. One customer example it shared speaks directly to logistics teams. Stephan Schissler, CIO of Doehler, which makes natural ingredients for the food, beverage and nutrition industries, says the Logistics Issue Resolution Agent detects the root cause and recommends a resolution, and that his logistics team has recovered roughly a third of the time once lost to troubleshooting [1].

The concept SAP keeps coming back to is "decision velocity". The company argues that supply chain decisions are interconnected and that isolated intelligence only creates isolated value. Agents need to understand how a decision in one domain affects the next [1].

## Descartes: A "control plane" for agents

Descartes is targeting a different problem: coordination across companies and trading partners. The Agent Control Plane, introduced at the company's Innovation Forum in Chicago, is built on the Descartes Global Logistics Network (GLN). Its aim is to coordinate AI agents across applications and trading partners so they can execute multi-step workflows within defined guardrails, policies and human oversight [2].

Ken Wood, Executive Vice President of Product Management at Descartes, notes that even with connected systems, supply chain teams spend significant time interpreting updates from emails, messages and portals, rekeying information and coordinating next steps [2]. The control plane applies customer-defined permissions and approval points and keeps a traceable record of agent actions [2].

## IFS Softeon: Area-based "digital workers" in the warehouse

The most concrete warehouse announcement came from IFS Softeon. At the heart of its Fulfillment Flow are "digital workers", AI agents that each focus on one area of the operation: inbound, wave management, labor, automation, slotting and replenishment, and outbound [3].

Each digital worker is built on the same six intelligence pillars: the facility itself, live operations, adjacencies between areas, site goals such as cutoffs and service levels, available associates and automation. IFS Softeon says traditional warehouse AI tends to optimize one area at the expense of another. In Fulfillment Flow, digital workers share what they see with a central operational agent responsible for flow across the whole facility, so the effect of each decision on adjacent areas such as receiving yards or manufacturing line feeds is taken into account [3].

The decision structure is clearly defined. Digital workers act like experienced area supervisors, escalating observations and ideas to the central agent. The central agent suggests to the warehouse manager how the operation should respond. The manager sets priorities and makes the final call [3]. As IFS Softeon CTO Mark Fralick puts it: "The warehouse manager stays in control" [3].

## CEVA and Sereact: Renting the robot instead of buying it

On the physical side, CEVA Logistics has deployed dual-arm robots from German robotics company Sereact at its warehouses in Greven, Germany and Świebodzin, Poland. The robots identify, grasp and sort returned items for fashion retailer Zalando. According to Supply Chain Digital, they do this without article-specific training or predetermined SKU profiles [4].

Two details matter from a warehouse operations perspective. The first is the commercial model: the deployment is delivered as Robotics-as-a-Service (RaaS) [4]. The second is the new human role: warehouse teams are expected to focus on station supervision, exception management and quality control [4]. Chris Walton, SVP Contract Logistics at CEVA, describes returns handling as one of the toughest operations because of unpredictable volumes, manual quality checks and seasonality [4].

## AI agents in the supply chain: The common thread is "bounded autonomy"

What ties the four announcements together is that none of them promises a "fully autonomous warehouse". SAP stresses that agents can trigger coordinated action "when authorized" [1], Descartes highlights customer-defined permissions and approval points [2], and IFS Softeon says the final decision stays with the warehouse manager [3]. Even in the CEVA case, a human team handles exceptions next to the robot [4].

The second common point is architecture. AI sits not on a separate screen but inside the system where the work gets done: the ERP, the WMS, the logistics network. That means an agent is only as good as the operational data it runs on.

## What it means for companies in Türkiye

For manufacturers and logistics providers in Türkiye running SAP or similar enterprise systems, these agents will come up as part of existing licenses and release cycles. For 3PL firms in contract logistics, CEVA's RaaS model is a notable example. Paying per use instead of making a large capital investment can make it easier to trial automation, especially in seasonal operations with unpredictable volumes.

At the same time, the benefits these systems promise depend heavily on clean, up-to-date operational data. In a facility with a weak location structure, poor inventory accuracy and loose work-order discipline, an agent will simply reproduce the existing chaos faster.

For the data layer these agents depend on, see [KARDEMİR's ISA-95-based Level 3 project](/en/kardemir-level-3-mes-isa-95/). For the HR agents SAP announced in the same period, read our article on [AI agents in HR](/en/hr-ai-agents-workday-sap-metaview/), and before granting agents permissions, check our [AI agent security checklist](/en/employee-built-ai-agents-security-risk/).

## Practical takeaways

1. **Start with exceptions.** As in the Doehler example [1], choosing recurring logistics issues and exception handling as the first use case gives you a measurable starting point.
2. **Write an authority matrix.** Define in advance which decisions stay with the agent and which stay with the shift supervisor or warehouse manager. Vendor approval points [2][3] should be configured to match it.
3. **Make agent logs mandatory.** A traceable record of what information the agent used and what action it took [2] will be needed for both incident analysis and customer audits.
4. **Measure cross-area impact.** To avoid improving one area while breaking another, track KPIs at the level of facility flow, not one area at a time [3].
5. **Consider RaaS for automation.** For processes with variable volumes, taking robots as a service rather than buying them [4] can reduce risk and upfront investment.
6. **Redefine the team's role.** Prepare a training plan for supervision, exception management and quality control [4] at the same time as the automation project.

The era of the warehouse "digital worker" is beginning. In this first wave, what will matter most is not how smart the agent is, but how well it divides the work with the people on the floor.

## Frequently asked questions

### What is a "digital worker" in the warehouse?

As IFS Softeon defines it, an AI agent focused on a single area of the warehouse (receiving, wave management, labor, automation, slotting and replenishment, or shipping). Digital workers share what they see with a central operations agent that orchestrates flow across the site, and the warehouse manager makes the final decision [3].

### When will SAP's new supply chain agents be available?

SAP plans to make the new capabilities generally available in the fourth quarter of 2026 [1].

### What is robotics as a service (RaaS)?

A commercial model in which robots are used as a service rather than bought outright. CEVA Logistics deployed Sereact's robots at its Greven and Świebodzin warehouses under this model [4].

### Will AI agents in the supply chain replace people?

None of these four announcements promises a fully autonomous warehouse. Approval points and final decisions stay with people, and in CEVA's case warehouse teams are expected to focus on station supervision, exception handling and quality control [1][2][3][4].

## References

1. SAP News Center, Devesh Mishra, "SAP Expands Joule Assistants and Agents to Advance Autonomous Supply Chain Management", October 8, 2026. <https://news.sap.com/2026/10/joule-assistants-agents-advance-autonomous-scm/> (Accessed: October 15, 2026)
2. Descartes Systems Group, "Descartes Unveils Next Step in Supply Chain AI with Agent Control Plane", October 6, 2026. <https://www.descartes.com/resources/news/descartes-unveils-next-step-supply-chain-ai-agent-control-plane> (Accessed: October 15, 2026)
3. IFS, "IFS Softeon launches Fulfillment Flow to bring context-aware AI to warehouse operations", October 13, 2026. <https://www.ifs.com/en/insights/news/ifs-softeon-launches-fulfillment-flow-to-bring-context-aware-ai-to-warehouse-operations> (Accessed: October 15, 2026)
4. Supply Chain Digital, Nick Edstrom, "CEVA and Zalando Use AI Robots for Fashion Returns", October 14, 2026. <https://supplychaindigital.com/operations/ceva-and-zalando-use-ai-robots-for-fashion-returns> (Accessed: October 15, 2026)
