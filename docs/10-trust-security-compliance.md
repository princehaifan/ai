# 10. Trust, Security and Compliance Framework

> **This is an operating framework, not legal advice.** Laws and guidance here are changing quickly. Several dates below are drawn from secondary commentary and **must be checked against primary sources** (legislation.gov.uk, ico.org.uk, the EU Official Journal) before you rely on them or advise a client. Use a qualified data-protection solicitor for contract templates and for any regulated client.
>
> **Golden rule: never claim a certification, accreditation or compliance status you don't hold and can't evidence.** Say "we follow X principles" or "we're working towards Cyber Essentials", never "we are compliant" without proof.

Labels: **[Verified]** sourced in [sources.md](sources.md) · **[Check]** verify primary source · **[Recommendation]** our choice.

---

## 10.1 The regulatory landscape (as of November 2026)

| Area | What applies | What it means for us and our clients | Label |
|---|---|---|---|
| **UK GDPR + Data Protection Act 2018** | All processing of personal data | Lawful basis, transparency, data minimisation, security, DPIAs for high-risk processing, processor contracts (Art. 28), international transfer safeguards | [Verified] |
| **Data (Use and Access) Act 2025** | Amends UK data protection law, including **automated decision-making (ADM)** rules | Its data-protection provisions were reported as commencing in early 2026. It relaxes some ADM restrictions but keeps safeguards for **significant decisions** (information, human intervention, contesting decisions). The "meaningful human involvement" threshold is now in statute | [Verified via legal commentary; **Check** commencement dates] |
| **ICO guidance** | AI and data protection guidance; ADM guidance (consultation closed May 2026; final guidance expected 2026); a statutory **AI & ADM Code of Practice** to follow (expected 2027) | Track and apply. Use the ICO's AI and data protection risk toolkit in DPIAs | [Verified via commentary; **Check** status] |
| **UK AI regulation** | **No single UK AI Act.** Sector regulators (ICO, CMA, Ofcom, FCA, coordinated through the DRCF) apply existing law using cross-sector AI principles (safety, transparency, fairness, accountability, contestability) | Map each client's sector regulator. Document how each system meets the principles | [Verified] |
| **EU AI Act** | Applies to UK firms placing AI systems on the EU market or whose AI outputs are used in the EU | Prohibited practices and AI-literacy duties already apply. **Transparency duties (Art. 50: telling people they're interacting with AI, labelling AI-generated content)** and high-risk obligations were scheduled for **August 2026**, but the **"Digital Omnibus" amendments may delay or change parts of this**. Check the Official Journal for current dates | [Verified that change is pending; **Check** dates] |
| **PECR** | Our own marketing emails and cookies; clients' AI-driven marketing | See outreach rules in [06-acquisition-and-sales.md §6.6](06-acquisition-and-sales.md) | [Verified principle] |
| **Sector-specific** | FCA (Consumer Duty, SM&CR, operational resilience) for financial services; SRA standards for law firms; ICAEW/ACCA ethics for accountants; NHS DSPT/DTAC and MHRA (software as a medical device) for health; Equality Act 2010 for anything affecting people | We **avoid health, credit and employment-decision systems in year one**. For professional firms, design for client confidentiality and professional-conduct duties | [Recommendation] |

## 10.2 Our risk classification for every engagement

Every opportunity is classified in the Sprint and at proposal stage:

| Tier | Examples | Requirements | Year-1 policy |
|---|---|---|---|
| **Low** | Internal knowledge search over non-sensitive docs, drafting assistance with human send, code assistance | Standard controls | ✅ Accept |
| **Medium** | Customer-facing support agents, document extraction with personal data, CRM enrichment | DPIA input, human-in-the-loop for uncertain outputs, AI disclosure to end users, eval thresholds, logging | ✅ Accept with controls |
| **High** | Decisions with legal or similarly significant effects on individuals (hiring, credit, insurance pricing, benefits, medical triage); EU AI Act high-risk categories; biometric systems | Full DPIA, legal review, meaningful human decision-making, bias testing, regulator engagement | ❌ **Decline in year one** (or advisory-only with the client's legal team) |
| **Prohibited** | Anything in EU AI Act prohibited practices, covert manipulation, social scoring, scraping facial images | n/a | ❌ Never |

## 10.3 Data protection operating model

| Topic | Our standard |
|---|---|
| **Role** | Usually the client is **controller** and we're **processor**. A DPA is signed before we touch personal data |
| **Data minimisation** | Work on samples first; pseudonymise or redact PII before it reaches model providers where feasible; never use production personal data in demos |
| **Where data lives** | In the **client's** environment and accounts by default. We don't keep copies after the project except what the contract requires |
| **AI provider terms** | Use business/API tiers whose terms say customer data isn't used to train models, with zero/limited retention options where available. **Re-check each provider's current terms and data-residency options per engagement** and record them in the sub-processor list |
| **International transfers** | Identify where each provider processes data; use UK adequacy regulations, the UK IDTA/Addendum, or the UK–US data bridge where applicable; prefer UK/EU regions for sensitive work |
| **DPIA** | For medium/high-risk processing we provide a **DPIA input pack** (data flows, risks, mitigations); the client (controller) completes and owns the DPIA |
| **Retention** | Prompt/response logs kept only as long as needed for monitoring and evaluation (default 30–90 days, configurable); eval sets anonymised where possible |
| **Data subject rights** | Systems designed so that personal data in indexes/logs can be found and deleted |
| **Breach response** | Notify client without undue delay (contractually within 24–48 hours) so they can meet the 72-hour ICO deadline; documented incident runbook |
| **ICO registration** | Pay the ICO data protection fee for our own company (micro-organisation tier is currently a small annual fee; **check the current amount**) |

## 10.4 Information security baseline

| Control | Standard from day one |
|---|---|
| Identity | MFA on everything; password manager; SSO where possible; separate admin accounts |
| Devices | Full-disk encryption, auto-updates, screen lock, endpoint protection; no client data on personal devices |
| Access | Least privilege; per-client credentials; access reviewed at project end and revoked within 2 business days |
| Secrets | Cloud secrets manager / vault; never in code, tickets or chat |
| Code | Private repos, branch protection, code review, dependency and secret scanning |
| AI-specific | Prompt-injection testing for agents with tools; tools scoped to minimum permissions; human approval for consequential actions (sending money, emailing customers, deleting data); output filtering; rate limits and spend caps on API keys |
| Logging | Audit logs of agent tool calls and admin actions |
| Vendors | Sub-processor register with security and data terms reviewed |
| Contractors | Same controls, confidentiality and DPA flow-down; client data access only when necessary |

### Certification roadmap (claim only once achieved)

| When | Certification | Why |
|---|---|---|
| By day 90 | **Cyber Essentials** (self-assessed, independently verified) | Low cost, quick, widely recognised in UK B2B. Often a hard requirement for public sector and larger clients |
| Months 6–12 | **Cyber Essentials Plus** (externally tested) | Stronger signal for mid-market clients |
| Year 2 (when enterprise pipeline justifies it) | **ISO/IEC 27001**; consider **ISO/IEC 42001** (AI management system) | Enterprise procurement; differentiator for AI governance |
| Ongoing | A public **Trust page** listing what we actually hold, sub-processors, and our data practices | Shortens security reviews |

## 10.5 Client confidentiality and IP

- Mutual NDA before detailed discovery; confidentiality in the MSA survives termination.
- **No client names, logos or results published without written permission.** Case studies anonymised by default.
- **IP:** client owns bespoke deliverables on full payment; we keep pre-existing IP and the generic Delivery Kit and license it perpetually to the client (see [08-operating-model-and-sops.md §8.4](08-operating-model-and-sops.md)).
- **AI-generated code and content:** disclose that AI tools are used in delivery; all such output is reviewed by a human; contractual warranties cover our deliverables regardless of how they were produced. IP in purely AI-generated output is legally uncertain, so explain this plainly and don't over-promise.
- Open-source licences checked for every dependency (no copyleft surprises in proprietary client code).

## 10.6 AI system risks: our controls

| Risk | Control |
|---|---|
| **Hallucination / inaccuracy** | Retrieval grounding with citations, eval thresholds before go-live, confidence-based routing to human review, scoped use cases |
| **Prompt injection & data exfiltration** | Treat all retrieved/external content as untrusted; isolate tools; least-privilege permissions; injection test suite; no secrets in prompts |
| **Bias & unfair outcomes** | Avoid high-risk decisions in year 1; test outputs across relevant groups where people are affected; human decision-making for anything significant |
| **Model change / deprecation** | Model gateway + regression evals; model changes managed under Run retainers |
| **Cost overruns** | Spend caps, per-task cost tracking, alerts, model tiering and caching |
| **Over-reliance / automation bias** | Clear UI signals, training, sampling audits of approved outputs, a kill switch back to the manual process |
| **Lack of transparency to end users** | Disclose AI interaction (and meet EU AI Act Art. 50 where applicable); label AI-generated content where required |

## 10.7 Human oversight standard

1. Every system has a **named human owner** at the client.
2. **Consequential actions require human approval** until evals and a monitored period justify automation, and even then only for defined low-risk categories.
3. Users can always reach a human (support agents must escalate on request).
4. Decisions with significant effects on individuals are never fully automated by systems we build in year one.
5. Oversight is reviewed in every quarterly Run review.

## 10.8 Third-party AI provider risk

- **Concentration:** design for at least two viable providers per use case (gateway + evals make switching realistic).
- **Terms changes:** review provider terms quarterly; record versions in the sub-processor register.
- **Outages:** fallback model or graceful degradation to human workflow.
- **Pricing changes:** cost monitoring; contractual pass-through of usage costs (clients own accounts).
- **Data location:** document processing regions; use in-region cloud offerings for sensitive clients.
