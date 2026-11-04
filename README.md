# Ostler: AI consultancy startup blueprint for UK local businesses

A complete, execution-ready blueprint for launching a profitable AI consultancy that helps local businesses use AI to capture more customers, reduce admin and grow, delivered as a managed monthly service with measured results.

*"Ostler" is a working name. Check availability before you use it (`blueprint/01` §1.4).*

---

## The idea in 60 seconds

- **Who:** owner-led UK local businesses with 5–100 staff whose revenue depends on calls, bookings and enquiries. Start with two niches in one area.
- **Problem:** most firms have heard of AI but haven't put it into their operations. The barriers they report are "we don't see the need" and "we lack the skills" ([DSIT 2026](https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research)).
- **Offer:** AI receptionists, WhatsApp and web booking assistants, reminder and no-show flows, review and lead automation, document workflows and staff training, built on proven platforms and connected to the client's existing systems.
- **Model:** free snapshot → £495 assessment → **setup fee + monthly managed plan** (£195 / £495 / £1,500+) → upgrades and training.
- **Numbers (realistic scenario, modelled):** 15 clients and £5.8k MRR at month 12; 49 clients and £19k MRR at month 24; break-even in month 7; about £19k peak funding need; LTV:CAC of about 7x. Details in `blueprint/06`.
- **Edge:** niche playbooks, local presence, measured outcomes, compliance by default, transparent pricing. **We sell outcomes, not chatbots.**

---

## Where to find each required deliverable

| # | Deliverable | File |
|---|---|---|
| 1 | Executive summary | [`blueprint/01-executive-summary-and-positioning.md`](blueprint/01-executive-summary-and-positioning.md) §1.1 |
| 2 | Business concept and value proposition | [`blueprint/01`](blueprint/01-executive-summary-and-positioning.md) §1.2 |
| 3 | Recommended company positioning | [`blueprint/01`](blueprint/01-executive-summary-and-positioning.md) §1.3 |
| 4 | Target market and customer personas | [`blueprint/03-customers-personas-and-industry-playbooks.md`](blueprint/03-customers-personas-and-industry-playbooks.md) §3.1–3.2 |
| 5 | Industry-by-industry problems and AI solutions | [`blueprint/03`](blueprint/03-customers-personas-and-industry-playbooks.md) §3.3–3.4 |
| 6 | Complete service catalogue | [`blueprint/04-service-catalogue-and-packages.md`](blueprint/04-service-catalogue-and-packages.md) §4.2 |
| 7 | Productised packages and pricing | [`blueprint/04`](blueprint/04-service-catalogue-and-packages.md) §4.1, §4.3–4.4 |
| 8 | Recommended technology stack | [`blueprint/05-technology-stack.md`](blueprint/05-technology-stack.md) |
| 9 | Business model and revenue streams | [`blueprint/06-business-model-and-financials.md`](blueprint/06-business-model-and-financials.md) §6.1 |
| 10 | Competitor and market analysis | [`blueprint/02-market-and-competitor-analysis.md`](blueprint/02-market-and-competitor-analysis.md) |
| 11 | Branding and marketing strategy | [`blueprint/07-brand-and-marketing.md`](blueprint/07-brand-and-marketing.md) |
| 12 | Customer acquisition and sales playbook | [`blueprint/08-sales-playbook-and-first-10-customers.md`](blueprint/08-sales-playbook-and-first-10-customers.md) §8.1–8.6 |
| 13 | Client onboarding and delivery process | [`blueprint/09-onboarding-delivery-and-operations.md`](blueprint/09-onboarding-delivery-and-operations.md) |
| 14 | Financial projections | [`blueprint/06`](blueprint/06-business-model-and-financials.md) §6.2–6.9 and [`model/`](model/) |
| 15 | Legal and compliance considerations | [`blueprint/10-legal-and-compliance.md`](blueprint/10-legal-and-compliance.md) |
| 16 | 90-day launch plan | [`blueprint/11-90-day-launch-plan.md`](blueprint/11-90-day-launch-plan.md) |
| 17 | First 10 customer acquisition strategy | [`blueprint/08`](blueprint/08-sales-playbook-and-first-10-customers.md) §8.7 |
| 18 | Long-term growth and scalability strategy | [`blueprint/12-growth-and-scale.md`](blueprint/12-growth-and-scale.md) |
| — | Operations and team structure | [`blueprint/09`](blueprint/09-onboarding-delivery-and-operations.md) §9.7–9.8 |
| — | Execution roadmap, phases 1–5 | Phases 1–3: [`blueprint/11`](blueprint/11-90-day-launch-plan.md) · Phases 4–5: [`blueprint/12`](blueprint/12-growth-and-scale.md) |
| — | Sources and evidence register | [`SOURCES.md`](SOURCES.md) |

## Ready-to-use templates

| Template | Use it for |
|---|---|
| [`templates/outreach-scripts.md`](templates/outreach-scripts.md) | Walk-ins, LinkedIn, PECR-compliant email, calls, partners, referrals, events |
| [`templates/discovery-call-script.md`](templates/discovery-call-script.md) | The free 30-minute AI Opportunity Snapshot |
| [`templates/ai-readiness-assessment.md`](templates/ai-readiness-assessment.md) | The paid £495 assessment: questionnaire, scoring and report outline |
| [`templates/roi-calculator.md`](templates/roi-calculator.md) | Quantifying the cost of missed calls, no-shows and admin from the prospect's own numbers |
| [`templates/proposal-template.md`](templates/proposal-template.md) | Commercial proposals |
| [`templates/client-onboarding-checklist.md`](templates/client-onboarding-checklist.md) | Contract → baseline → access → compliance → build → test → launch → day 30 |
| [`templates/dpia-and-ai-risk-checklist.md`](templates/dpia-and-ai-risk-checklist.md) | DPIA screening and AI risk controls for every deployment |
| [`templates/monthly-report-template.md`](templates/monthly-report-template.md) | The monthly results report that justifies the retainer |
| [`templates/ai-acceptable-use-policy.md`](templates/ai-acceptable-use-policy.md) | A staff AI policy handed to clients and training attendees |

## Financial model

```bash
python3 model/financial_model.py
```

- Inputs (prices, costs, ramp, churn, hiring triggers) are at the top of [`model/financial_model.py`](model/financial_model.py). Every input is labelled as an assumption.
- Outputs regenerate in [`model/outputs/`](model/outputs/): a Markdown summary plus month-by-month CSVs for each scenario, which open in Excel or Google Sheets.
- **Replace the assumptions with your real numbers** after your first 20 sales conversations and first 3 clients, then re-run.

## How the evidence is labelled

- **[F] Fact:** verified against an official or primary source.
- **[E] Estimate:** based on published benchmarks or vendor pages.
- **[A] Assumption:** our working figure, to be validated.

Every source is listed with links in [`SOURCES.md`](SOURCES.md), with research dated November 2026. Prices, vendor terms and regulations change. **Re-check before relying on any figure commercially.** Nothing here is legal, tax or financial advice, and no revenue or savings are guaranteed.

## Suggested reading order

1. `blueprint/01` (the strategy on two pages)
2. `blueprint/11` (what to do on Monday)
3. `blueprint/08` (how to win the first 10 clients)
4. `blueprint/04` (what you're selling and for how much)
5. Everything else as you need it
