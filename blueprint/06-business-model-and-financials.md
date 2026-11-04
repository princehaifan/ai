# 6. Business model, revenue streams and financial projections

> Covers deliverables 9 (Business model and revenue streams) and 14 (Financial projections), plus strategic responsibilities 1, 7 and 14.
> **Everything in this section is a modelled estimate built on assumptions [A].** Nothing here is a forecast or a promise. The live model is `model/financial_model.py`, and the full monthly outputs are in `model/outputs/`. Change the inputs and re-run it whenever real data arrives.

---

## 6.1 Business model on a page

| Element | Ostler's design |
|---|---|
| **Customer** | Owner-led local service businesses (5–100 staff), starting with two niches |
| **Value delivered** | Captured enquiries, fuller diaries, saved admin hours, measured monthly |
| **Offer** | Free snapshot → paid assessment → setup + monthly package → upgrades and training |
| **Revenue engine** | Setup fees fund acquisition and delivery. **Monthly recurring revenue (MRR)** builds long-term value. |
| **Cost structure** | Mostly people (founder, then engineers); low platform costs (~10–15% of revenue) |
| **Moat over time** | Niche templates, case studies, local reputation, partner channels, switching costs from embedded workflows |
| **Key metric** | **Net MRR growth** (new MRR − churned MRR + expansion MRR) |

### Revenue streams

| # | Stream | Type | Price range | Share of revenue (realistic, year 2) [A] | Strategic role |
|---|---|---|---|---|---|
| 1 | AI audits and assessments | One-off | £495–£1,250 | ~2% | Qualifies leads; credited into projects |
| 2 | One-off consultancy (roadmaps, strategy days) | One-off | £650/day; £1,500–£3,500 roadmaps | (in Transformation discovery) | Builds trust with larger SMEs |
| 3 | AI implementation (setup) fees | One-off | £950–£30,000 | ~38% | Funds delivery; front-loads cash |
| 4 | Custom development fees | One-off | From £2,500 | (in Transformation) | High value; use sparingly |
| 5 | **Monthly automation subscriptions** | **Recurring** | £195–£3,000 | **~51%** | **Core value of the company** |
| 6 | Maintenance contracts (standalone managed care) | Recurring | £150–£895 | (in subscriptions) | Low-cost acquisition of clients with existing tools |
| 7 | Staff training | One-off / repeat | £350–£1,350 | ~9% | Door-opener; positions Ostler as the expert |
| 8 | Enterprise consulting | Project | Day rate or SOW | Year 3+ | Expansion route |
| 9 | Usage overage | Recurring, variable | Cost + 20% | Small | Protects margin |
| 10 | Partner referral income (vendor partner programmes) | Recurring | Varies by vendor | Small | Optional; always disclose to clients |

---

## 6.2 Startup costs (one-off, estimates)

| Item | Estimate | Notes |
|---|---:|---|
| Company incorporation (private limited company) | £100 | Check current Companies House fee [A] |
| ICO data protection fee (tier 1) | £52 | [F, S14]; £47 by Direct Debit |
| Solicitor review of contract templates (MSA, SOW, DPA, T&Cs, privacy policy) | £1,200 | Fixed-fee start-up packages are common [A] |
| Brand identity (logo, colours, templates) | £300 | Freelance designer or a design tool [A] |
| Website (self-built on Webflow, Framer or WordPress) + domain | £530 | Building it yourself keeps costs down |
| Laptop and headset (if needed) | £1,200 | Skip if you already own suitable kit |
| Cyber Essentials certification | £400 | [A] check IASME's current micro-organisation fee |
| Demo builds (usage, numbers, tools) for the first 2 months | £300 | Voice minutes, WhatsApp, LLM credits |
| Print (leave-behind cards, one-page leaflets) | £250 | For walk-in visits |
| Networking memberships (Chamber of Commerce, BNI or similar), first instalment | £500 | [A] varies by area |
| UK trade mark (one class) | £170 | [A] check UK IPO fees |
| Contingency | £198 | |
| **Total startup costs** | **£5,200** | |

**Leaner route (~£2,000):** use your existing laptop, a template website, no paid networking in month one, and Cyber Essentials in month three.

---

## 6.3 Monthly operating expenses (estimates)

| Category | Months 1–6 | Months 7–12 (realistic) | Notes |
|---|---:|---:|---|
| Founder draw | £2,000 | £2,000 | Adjust to personal needs. Model scenarios use £1,500 / £2,000 / £2,500. |
| Internal software and tools | £250 | £300 | CRM, workspace, n8n server, monitoring, design, proposals |
| Insurance: professional indemnity (£1m), cyber, public liability | £110 | £110 | Get quotes. PI is essential because clients rely on your advice [A] |
| Accountant and bookkeeping | £120 | £120 | Year-end accounts, corporation tax, VAT later |
| Phone, broadband share, travel | £200 | £250 | Local visits are core to the model |
| Demo and sandbox usage | £80 | £80 | |
| Marketing (events, print, ads, lead data, referral fees) | £600 + £300 per client won | Same formula | See `blueprint/07` |
| Payment processing and banking | ~2% of revenue | ~2% of revenue | GoCardless and Stripe fees |
| **Typical total (before direct client costs)** | **~£3,400–£3,900** | **~£4,000–£4,600** | Staff costs added when hires trigger |

**Hiring triggers in the model (by workload, not by calendar):**

| Hire | Trigger | Fully loaded cost/month [A] |
|---|---|---:|
| Automation engineer / delivery specialist | 18 active clients | £3,600 |
| Client success and sales executive | £12,000 MRR | £3,300 |
| Second automation engineer | 45 active clients | £3,800 |

*Before the first hire, use vetted freelancers paid per project (costed in setup delivery costs) for overflow builds.*

---

## 6.4 Revenue projections: three scenarios

### Scenario assumptions

| Assumption [A] | Conservative | Realistic | Optimistic |
|---|---|---|---|
| New clients in month 1 | 0 | 0 | 0.5 |
| Ramp (extra new clients per month, each month) | +0.12 | +0.25 | +0.35 |
| Ceiling on new clients per month | 2.5 | 4 | 7 |
| Mix: Starter / Growth / Transformation | 70 / 27 / 3% | 60 / 33 / 7% | 50 / 40 / 10% |
| Monthly churn | 5% | 3% | 2.5% |
| Founder draw | £1,500 | £2,000 | £2,500 |
| Training revenue per month | £400 → £900 | £700 → £2,500 | £1,000 → £4,000 |
| Pilot discount | First 3 clients at 50% off setup | Same | Same |

### Results

| Metric | Conservative | **Realistic** | Optimistic |
|---|---:|---:|---:|
| MRR at month 6 | £531 | **£1,389** | £3,518 |
| MRR at month 12 | £2,123 | **£5,763** | £11,814 |
| MRR at month 24 | £7,313 | **£19,019** | £38,304 |
| Active recurring clients, month 12 | 7 | **15** | 27 |
| Active recurring clients, month 24 | 23 | **49** | 86 |
| Year 1 revenue | £27,109 | **£76,229** | £166,709 |
| Year 2 revenue | £119,655 | **£304,978** | £597,685 |
| Year 1 operating profit (after founder draw) | −£18,149 | **£7,215** | £48,960 |
| Year 2 operating profit (after founder draw) | £28,214 | **£88,275** | £231,504 |
| Blended gross margin, year 2 | 73% | **72%** | 71% |
| Sustained monthly break-even | Month 11 | **Month 7** | Month 4 |
| Peak cumulative cash needed | £24,291 | **£18,811** | £12,862 |
| Cash payback including startup costs | Month 22 | **Month 12** | Month 8 |
| Headcount at month 24 (incl. founder) | 2 | **4** | 4 |

*Operating profit is before corporation tax. Client counts are expected values.*

### Realistic case: month by month (selected months)

| Month | New clients | Active clients | MRR | Revenue | Operating profit | Cumulative cash |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.0 | 0.0 | £0 | £0 | −£3,360 | −£8,560 |
| 3 | 0.5 | 0.7 | £286 | £1,687 | −£2,444 | −£14,229 |
| 6 | 1.2 | 3.6 | £1,389 | £4,802 | −£539 | −£18,811 |
| 9 | 2.0 | 8.4 | £3,236 | £10,104 | £3,169 | −£13,155 |
| 12 | 2.8 | 15.0 | £5,763 | £14,644 | £6,050 | £2,015 |
| 18 | 4.0 | 32.5 | £12,529 | £25,765 | £6,528 | £42,792 |
| 24 | 4.0 | 49.4 | £19,019 | £32,254 | £7,167 | £90,291 |

*Profit dips at months 14, 18 and 23 as hires join ahead of the revenue they unlock. That is deliberate capacity investment.*

---

## 6.5 Unit economics

| Metric | Conservative | **Realistic** | Optimistic | Healthy benchmark (rule of thumb) |
|---|---:|---:|---:|---|
| Average monthly fee per client (ARPA) | £315 | **£385** | £446 | — |
| Monthly gross margin per client | £223 | **£271** | £313 | — |
| Recurring gross margin | 71% | **70%** | 70% | ≥ 65% for a tech-enabled service |
| Expected client lifetime (1 ÷ churn) | 20 months | **33 months** | 40 months | — |
| **Customer lifetime value** (gross margin incl. setup) | £5,843 | **£10,815** | £14,620 | — |
| CAC, cash marketing only | £740 | **£532** | £438 | — |
| **CAC, fully loaded** (marketing + half of sales hire + 18 founder hours × £45) | £1,550 | **£1,529** | £1,438 | — |
| **LTV : CAC** | 3.8x | **7.1x** | 10.2x | ≥ 3x |
| CAC payback on monthly margin | 7.0 months | **5.6 months** | 4.6 months | ≤ 12 months |

**Reading this:** even the conservative case clears the common 3:1 LTV:CAC rule of thumb, because the setup fee recovers much of the acquisition cost up front. The weak point is not unit economics but **sales volume in year 1**, which is why the go-to-market plan is so concentrated.

---

## 6.6 Break-even analysis

**Monthly break-even condition (before hires):** fixed costs ≈ £3,400–£3,900 a month, including the founder draw.

- Recurring gross margin alone would need **about 13–14 average clients** (£3,700 ÷ £271).
- In practice, **setup and training margin from 1–2 new clients a month** closes the gap much earlier, which is why the realistic case breaks even in **month 7 with only about 5 active clients**.
- **The safe target is "MRR gross margin covers fixed costs."** In the realistic case that happens at around 14 clients, in about month 12. From then on, a slow sales month doesn't threaten survival.

---

## 6.7 Sensitivity analysis (realistic case)

| Change | MRR month 12 | MRR month 24 | Year 2 revenue | Sustained break-even | Peak cash needed |
|---|---:|---:|---:|---|---:|
| **Base case** | £5,763 | £19,019 | £304,978 | Month 7 | £18,811 |
| Churn 5% a month instead of 3% | £5,409 | £16,515 | £288,765 | Month 7 | £18,855 |
| Sales ramp 40% slower | £3,458 | £12,936 | £209,702 | Month 9 | £22,740 |
| Mix shifts to Starter (80/20/0) | £3,814 | £12,585 | £201,977 | Month 9 | £21,277 |
| All prices 20% lower | £4,611 | £15,215 | £250,463 | Month 8 | £20,874 |
| Direct costs 50% higher | £5,763 | £19,019 | £304,978 | Month 7 | £19,295 |
| Slow ramp **and** 5% churn | £3,245 | £11,375 | £199,840 | Month 9 | £22,832 |

**What this tells you:**

1. **Sales velocity and package mix matter most.** Upselling Starter clients to Growth is worth more than any price change. Design the Starter package as a *stepping stone* (§4.3).
2. **Discounting hurts less than slow selling.** Still, hold list prices and use pilot pricing only for the first three clients per niche.
3. **The business survives the bad combinations.** Even a slow ramp with high churn breaks even by month 9, with £23k peak funding. **Budget £20,000–£25,000 of runway.**

---

## 6.8 Funding options

| Option | Fit | Notes |
|---|---|---|
| Personal savings | ✓✓ | Simplest; keep full ownership |
| Part-time employment or consulting while launching | ✓✓ | Reduces the draw needed; slows the ramp |
| **Start Up Loans** (British Business Bank, government-backed personal loan for business) | ✓ | Fixed interest, includes mentoring. Check current limits and rate on the British Business Bank website [A]. |
| Local growth hub and council grants | ✓ | Vary by area; often small, for digital or skills. Search your local growth hub. |
| Revenue-based or invoice finance | Later | Only once MRR is stable |
| Angel investment | Not recommended now | A services business doesn't need it until a product (Phase 5) exists |

---

## 6.9 Financial KPIs dashboard (track monthly)

| KPI | Formula | Target (realistic) |
|---|---|---|
| MRR | Sum of active monthly fees | £5.8k by month 12 |
| Net new MRR | New + expansion − churned MRR | Positive every month |
| Logo churn | Clients lost ÷ clients at start of month | ≤ 3% |
| Net revenue retention | (Starting MRR + expansion − churn) ÷ starting MRR, annualised | ≥ 100% |
| Gross margin (recurring) | (MRR − direct costs) ÷ MRR | ≥ 65% |
| CAC (fully loaded) | Acquisition cost ÷ new clients | ≤ £1,600 |
| LTV : CAC | | ≥ 3x |
| Cash runway | Cash ÷ monthly net burn | ≥ 3 months at all times |
| Revenue per head | Revenue ÷ headcount | ≥ £75k/year by year 2 |
| Utilisation (delivery staff) | Billable or client hours ÷ available hours | 65–80% |

**Re-run the model:** monthly for the first six months using actual numbers (`python3 model/financial_model.py`), then quarterly.
