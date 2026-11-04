# 1. Market Opportunity and Ideal Customer Profiles

> **Key to labels used in every document**
> - **[Verified]**: from a named source, listed in [sources.md](sources.md). Check the original before quoting it publicly.
> - **[Estimate]**: our reasoned estimate. Not market data.
> - **[Recommendation]**: a strategic choice we are making, with reasons.

---

## 1.1 What the market tells us

### Adoption is rising fast, but depth is shallow

| Signal | Figure | Label |
|---|---|---|
| UK businesses using at least one AI technology (DSIT AI Adoption Survey 2026, 3,503 interviews, fieldwork Jan–Apr 2026) | **32%** in 2026, up from **16%** in 2025 | [Verified] |
| Uptake among larger firms in the same survey | **52%** | [Verified] |
| Biggest barriers reported by DSIT 2026 | Capability-related, led by **limited skills** | [Verified] |
| BCC survey (mostly SMEs) reporting active AI use | 54% in March 2026, up from 35% in 2025 | [Verified, but different definition from DSIT] |
| Enterprise GenAI pilots that produce measurable P&L impact (MIT NANDA, *The GenAI Divide*, 2025) | About **5%**. About 95% show no measurable return | [Verified, widely reported; read the method before quoting] |
| MIT's explanation for failure | Poor integration into workflows and a "learning gap". **Not** model quality | [Verified] |
| Where MIT found the best ROI | **Back-office automation**, even though most budgets go to sales and marketing tools | [Verified] |

**What this means:** the UK market has moved from "should we use AI?" to "we tried AI and it didn't stick". Companies don't lack access to models. They lack the skills to put AI into real workflows, measure it, and keep it running. A consultancy that sells **integration, measurement and operation**, rather than strategy decks or chatbot demos, is pointing at the actual gap. [Recommendation]

### The competitive landscape is consolidating upward

- **Faculty** (one of the UK's best-known applied-AI firms) was reported acquired by **Accenture** in January 2026. [Verified]
- **Tomoro** (London applied-AI consultancy, founded 2023, ~120 staff, OpenAI alliance partner) was reported in May 2026 to be acquired by **OpenAI** for its deployment business. [Verified]

**What this means:** the best independent UK AI implementers are being absorbed into global consultancies and model vendors. Those buyers will point the talent at **large enterprises**. That leaves a widening gap for **vendor-neutral, senior, implementation-focused** help for companies with 20–500 staff, which can't afford Accenture and don't want to be locked to one model provider. [Estimate + Recommendation]

### Price benchmarks (market rates, not our prices)

| Benchmark | Figure | Label |
|---|---|---|
| Median UK contract rate, Agentic AI Engineer (ITJobsWatch, 6 months to Feb 2026) | **£638/day** | [Verified, advertised median] |
| Median contract rate, AI Consultant, City of London (ITJobsWatch, 6 months to Feb 2026) | **£662/day** | [Verified, advertised median] |
| Recruiter placement data, mid-to-principal AI Engineers (La Fosse, H2 2026) | **~£800–£900/day** | [Verified, region labels unclear] |
| Senior independent AI consultants (practitioner guides) | £800–£1,500+/day | [Weak: vendor/marketing pages] |
| AI automation agency packages (mostly US guides) | Setup $2k–$50k + retainer $500–$8k/month | [Weak: vendor blogs, ±10x spread] |

Our proposed prices are in [03-business-model-and-pricing.md](03-business-model-and-pricing.md). They are set against these benchmarks and against the value of the problem solved, not against cost.

---

## 1.2 Challenging the brief's customer list

The brief lists ten segments. Chasing all ten in year one would be a mistake. A new consultancy wins by being **the obvious choice for one buyer with one expensive problem**. Each segment is scored below. [Recommendation]

| Segment | Pain intensity | Budget | Speed to buy | Reachability | AI-readiness | Verdict |
|---|---|---|---|---|---|---|
| **B2B SaaS / tech companies, 20–200 staff (Seed–Series B)** | High (board pressure to ship AI features; support/sales costs) | £15k–£100k/project | Fast (founder/CTO decides) | High (LinkedIn, VCs, communities) | High (APIs, data, engineers) | **PRIMARY BEACHHEAD** |
| **Professional services firms, 20–250 staff** (accountancy, legal, recruitment, insurance brokers, consultancies) | Very high (document-heavy, billable-hour leakage) | £10k–£60k | Medium (partner sign-off) | Medium (associations, LinkedIn) | Low–medium (messy data, Microsoft 365) | **SECONDARY (from month 3)** |
| **Software development agencies** | High (clients ask for AI; they lack depth) | Rev share / white-label | Fast | High | High | **CHANNEL PARTNER, not end customer** |
| **VCs and accelerators** | Medium (portfolio value-add) | Low direct | Medium | Medium | n/a | **CHANNEL PARTNER** |
| Venture-backed companies (general) | High | High | Fast | High | Varies | Folded into primary |
| SMEs (general, non-tech) | Medium | £3k–£15k | Slow | Low | Low | Only via productised Starter offers |
| E-commerce businesses | Medium (support volume, catalogue ops) | £5k–£25k | Fast | Medium | Medium | Opportunistic (£2m+ revenue brands only) |
| Early-stage / pre-seed founders | High | **Low** | Fast | High | High | Productised MVP Blueprint only. Don't do open-ended builds for equity |
| Digital transformation companies | Medium | Medium | Slow | Medium | Medium | Treat as partners (like agencies) |
| Enterprise technology departments | High | Very high | **Very slow** (procurement, ISO 27001, security questionnaires) | Low | Medium | **Year 2**, after case studies and certifications |

**Why B2B SaaS is the beachhead:** buyers are technical enough to value engineering quality, they already have APIs and data, the founder or CTO can sign £20k without a procurement process, and every one of them is being asked by investors and customers "what's your AI story?". They also talk to each other, so one good case study travels through investor and founder networks.

---

## 1.3 Ideal Customer Profiles

### ICP 1 (Primary): "The Scaling SaaS Company"

| Attribute | Detail |
|---|---|
| Profile | UK B2B SaaS or tech-enabled company, 20–200 staff, £2m–£30m ARR, Seed to Series B |
| Buyer | CTO / VP Engineering (product AI), COO / Head of Customer Success (internal automation), CEO-founder (strategy) |
| Biggest operational problems | (1) Support ticket volume growing faster than headcount; (2) customers and investors asking for AI features the team can't ship well; (3) sales/CS teams buried in manual research, CRM hygiene and onboarding; (4) internal knowledge scattered across Notion, Confluence, Slack and Drive |
| AI adoption challenges | Engineers can call an API but lack production experience with retrieval, evaluation, agent reliability, cost control and guardrails. Roadmap is full. Previous "AI hackathon" prototypes never shipped |
| Willingness to pay | **High** for things tied to revenue or headcount: £15k–£60k per project, £1.5k–£5k/month to run it [Estimate] |
| How they buy | CTO or founder decides within 2–6 weeks. Wants a fixed price, a clear scope, and proof the team can ship. Needs a security answer (DPA, data flows) but rarely full procurement |
| Most likely purchases | AI Opportunity Sprint → Production Pilot (support agent, in-product copilot/RAG feature, sales research agent) → Run retainer. Fractional Head of AI for companies without AI leadership |
| How to reach them | Founder-led LinkedIn content, targeted cold email to CTOs/COOs after funding announcements or AI job ads, VC portfolio partnerships, agency partners, SaaS communities and events (SaaStock, London tech meetups) |
| Trigger events | Funding round, new AI job posting they can't fill, a competitor launching AI features, support backlog, board asking for an AI plan |

### ICP 2 (Secondary): "The Document-Heavy Professional Firm"

| Attribute | Detail |
|---|---|
| Profile | UK accountancy, law, recruitment, insurance broking, property or consulting firm, 20–250 staff |
| Buyer | Managing Partner / COO / Head of Operations. IT manager or MSP is an influencer (often a blocker) |
| Biggest operational problems | Hours lost to reading, extracting, summarising and drafting from documents. Onboarding and KYC paperwork. Proposal and report writing. Knowledge locked in senior people's heads |
| AI adoption challenges | Confidentiality and professional-conduct worries, Microsoft 365 data sprawl, staff using unapproved ChatGPT accounts, no in-house engineers |
| Willingness to pay | Medium–high when framed in recovered billable hours: £8k–£40k projects, £750–£3k/month [Estimate] |
| How they buy | Partner consensus, 1–3 months, risk-averse. References and a credible data-protection story matter more than technical depth |
| Most likely purchases | AI Readiness & Governance Sprint (incl. acceptable-use policy), document processing automation, internal knowledge assistant over their own files, workshops for staff |
| How to reach them | Professional bodies and regional associations, accountants' and lawyers' tech events, MSP partnerships, LinkedIn content on "AI for [profession]" with worked examples |
| Trigger events | Staff caught using public AI tools with client data, competitor firm announcing AI, recruitment difficulties, PI insurer or regulator questions |

### Channel Partner Profile: "The Software Agency without AI depth"

- UK/EU software development agencies (10–100 staff) whose clients now ask for AI features.
- They resell or white-label our AI delivery (we build the AI layer, they own the client and the rest of the app).
- Commercials: 15–20% referral fee for introductions, or wholesale day rate for white-label delivery. [Recommendation]
- Why they buy: protect their client relationships without hiring scarce AI engineers.

---

## 1.4 The problems we will build the business on

We prioritise problems that are **expensive, recurring and measurable**: the brief's own test. [Recommendation]

| Problem | Typical metric we move | Why it is a good first problem |
|---|---|---|
| Tier-1 customer support volume | % tickets resolved or drafted by AI, cost per ticket, first-response time | Clear baseline in Zendesk/Intercom; high volume; strong ROI story |
| Document intake & extraction (invoices, contracts, KYC, CVs, claims) | Minutes per document, error rate, throughput | Back-office ROI (consistent with MIT finding); measurable with a labelled test set |
| Internal knowledge search & drafting | Time-to-answer, deflected internal questions, adoption | Universal, low regulatory risk, fast to pilot |
| Sales & account research, CRM hygiene | Hours saved per rep, meetings booked, CRM completeness | Revenue-linked; founders care |
| AI features inside a SaaS product | Feature shipped, activation/usage, retention, AI cost per user | Directly tied to investor story and revenue |

Problems we avoid in year one: autonomous decisions with legal effect on individuals (credit, hiring decisions, medical), high-risk categories under the EU AI Act, and anything where we can't build a test set. See [10-trust-security-compliance.md](10-trust-security-compliance.md).
