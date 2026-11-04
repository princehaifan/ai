# Northwright: AI Consultancy Startup Blueprint

*Working name. See [brand identity](docs/05-brand-identity.md) for name options and the checks to run before committing.*

An execution-ready blueprint for an **implementation-focused AI consultancy** serving UK technology companies and growing businesses, with a path to international expansion.

> **How to read this blueprint.** Every claim is labelled **[Verified]** (sourced in [docs/sources.md](docs/sources.md)), **[Estimate]** (our reasoned judgement) or **[Recommendation]** (a strategic choice). No customer demand, testimonials or revenue have been assumed as fact. The financial projections come from a transparent model ([`financials/model.py`](financials/model.py)) that you can edit and re-run.

---

## Executive Summary

### The opportunity
UK AI adoption doubled in a year: **32% of businesses used AI in 2026, up from 16% in 2025** (DSIT) [Verified]. But adoption is shallow. DSIT finds **skills** to be the main barrier, and MIT's 2025 *GenAI Divide* study reported that **~95% of enterprise GenAI pilots produce no measurable P&L impact**, mainly because of poor integration into workflows rather than model quality [Verified]. Meanwhile the best independent UK AI implementers are being bought by giants (**Faculty by Accenture; Tomoro by OpenAI**, both reported in 2026) [Verified], which pulls their focus towards large enterprises. **The gap:** senior, vendor-neutral, production-grade AI implementation for companies with 20–500 staff.

### What we sell
Four launch products in a **Land → Build → Run → Expand** model ([pricing](docs/03-business-model-and-pricing.md), [catalogue](docs/04-service-catalogue.md)):

| Product | Price (proposed, ex VAT) | Role |
|---|---|---|
| **AI Opportunity Sprint** (1–2 weeks) | £3,500 / £7,500, credited against a Build | Paid entry point; ranked, costed roadmap |
| **Production Pilot** (6 weeks) | £8k–£15k Starter · £20k–£45k Growth · £60k+ Enterprise | One workflow into production, with an agreed acceptance metric and an **Acceptance Guarantee** |
| **Run** (managed AI) | £750 · £2,000–£3,500 · £6,000–£12,000 per month | Monitoring, evals, model/prompt updates, cost optimisation: the recurring engine |
| **Fractional Head of AI** | £3,000–£6,000 per month | Senior AI leadership for scale-ups (capped at 3 clients) |

### Who buys it
- **Primary beachhead:** UK B2B SaaS / tech companies, 20–200 staff, Seed–Series B. CTO, COO or founder buyers who need AI features shipped and support/ops costs contained.
- **Secondary (from month 3):** document-heavy professional firms (accountancy, legal, recruitment, insurance broking).
- **Channels:** software agencies (white-label/referral) and VCs/accelerators (portfolio access).
- Explicitly **deprioritised in year 1:** enterprise (slow procurement), pre-seed founders (low budgets), general SMEs. See [market & ICPs](docs/01-market-and-customers.md).

### Why they choose us
> **"We turn one expensive, repetitive workflow into a working AI system in six weeks, with the success metric agreed before we start, an evaluation suite that proves it, and a team that keeps it running afterwards."**

Metric-first · evaluation-backed · production not prototype · vendor-neutral (we recommend off-the-shelf tools when they win) · we stay to run it. See [competitive analysis](docs/02-competitive-analysis-and-positioning.md).

### How we win customers
Warm network in **week 3**, signal-based outbound (50 personalised contacts/week), agency and VC partnerships, proof-led founder content on LinkedIn, workshops, and case studies. A 10-step sales process with qualification scoring, templates and weekly targets. See [acquisition & sales](docs/06-acquisition-and-sales.md).

### How we deliver
A deliberately small default stack: **Claude / OpenAI APIs** (or the same models through Bedrock/Azure/Vertex for data residency), **Python + FastAPI**, **TypeScript + Next.js**, **PostgreSQL + pgvector** (Supabase for startups), **n8n** for business-system glue, **LangGraph only when stateful orchestration is needed**, Docker, Langfuse and an eval harness on every project. A reusable **Delivery Kit** turns each project into future margin. See [technical architecture](docs/07-technical-architecture.md).

### The numbers (12 months, from the model)

| Scenario | Year-1 revenue | Month-12 MRR | Net profit after founder pay | Peak cash needed |
|---|---|---|---|---|
| Conservative | ~£83k | ~£2k | ~£25k | ~£7k |
| **Realistic** | **~£195k** | **~£10k** | **~£63k** | **~£7k** |
| Ambitious | ~£567k | ~£24k | ~£198k | ~£6k |

**The key finding:** cash and demand aren't the binding constraint. **Founder time is.** Founder load exceeds 100% by months 4–6 in the Realistic case, so the contractor bench, Delivery Kit and hiring triggers matter more than any marketing tactic. If you have a thin network or no consulting sales experience, **treat Conservative as your realistic plan.** See [financial projections](docs/09-financial-projections.md).

### The first 90 days
Foundation (validate with 8–10 interviews, launch website and demo projects, warm outreach by week 3) → Market entry (outbound, partners, **first paid Sprint by week 7**) → Growth (first Pilot delivered, Run retainer, first case study). Decision gates at days 30, 60 and 90. See the [90-day roadmap](docs/13-90-day-roadmap.md).

---

## Blueprint contents

| # | Deliverable (from the brief) | Document |
|---|---|---|
| 1 | Executive summary | This page |
| 2 | Market opportunity analysis | [01-market-and-customers.md](docs/01-market-and-customers.md) |
| 3 | Ideal customer profiles | [01-market-and-customers.md §1.3](docs/01-market-and-customers.md) |
| 4 | Competitive analysis | [02-competitive-analysis-and-positioning.md](docs/02-competitive-analysis-and-positioning.md) |
| 5 | Business model | [03-business-model-and-pricing.md](docs/03-business-model-and-pricing.md) |
| 6 | Service catalogue | [04-service-catalogue.md](docs/04-service-catalogue.md) |
| 7 | Pricing strategy | [03-business-model-and-pricing.md §3.3–3.5](docs/03-business-model-and-pricing.md) |
| 8 | Brand positioning | [05-brand-identity.md](docs/05-brand-identity.md) |
| 9 | Customer acquisition strategy | [06-acquisition-and-sales.md](docs/06-acquisition-and-sales.md) |
| 10 | Sales and conversion framework | [06-acquisition-and-sales.md §6.2–6.5](docs/06-acquisition-and-sales.md) |
| 11 | Technical architecture | [07-technical-architecture.md](docs/07-technical-architecture.md) |
| 12 | Operational structure & SOPs | [08-operating-model-and-sops.md](docs/08-operating-model-and-sops.md) |
| 13 | Financial projections | [09-financial-projections.md](docs/09-financial-projections.md) · [model](financials/model.py) |
| 14 | Risk assessment | [11-risk-assessment.md](docs/11-risk-assessment.md) |
| 15 | Website strategy | [12-website-strategy.md](docs/12-website-strategy.md) |
| 16 | 90-day execution roadmap | [13-90-day-roadmap.md](docs/13-90-day-roadmap.md) |
| 17 | First-year growth strategy | [14-growth-and-scalability.md §14.1](docs/14-growth-and-scalability.md) |
| 18 | Long-term scalability strategy | [14-growth-and-scalability.md §14.2–14.5](docs/14-growth-and-scalability.md) |
| + | Trust, security & compliance | [10-trust-security-compliance.md](docs/10-trust-security-compliance.md) |
| + | Sources & evidence register | [sources.md](docs/sources.md) |

## Assumptions in the brief that this blueprint challenges

1. **Ten customer segments → one beachhead plus one secondary.** Focus wins the first customers.
2. **A full service menu from day one → four launch products.** Everything else is capability, sold on request.
3. **"Think like McKinsey/Accenture" → think like a senior, productised boutique.** Leverage pyramids and long programmes don't suit a startup.
4. **Build AI products/SaaS → only after the same solution has sold 3+ times.**
5. **Enterprise customers → year 2**, after case studies and security certifications.

## Your first five actions this week

1. Run the name checks and pick a name ([§5.1](docs/05-brand-identity.md)).
2. Book **10 validation interviews** with CTOs/COOs at UK SaaS companies.
3. Write down **50 people** in your network for the week-3 founding-client message ([template](docs/06-acquisition-and-sales.md)).
4. Get quotes for PI + cyber insurance and a tech-solicitor contract template pack.
5. Start **Demo Project 1** (AI support agent with an eval report on public data).

## Updating the financial model

```bash
python3 financials/model.py          # prints all scenario tables
```

Edit prices, deal counts, conversion rates, costs or hires at the top of `financials/model.py`, then paste the output into `docs/09-financial-projections.md`.
