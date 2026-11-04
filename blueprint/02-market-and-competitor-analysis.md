# 2. Market research and competitor analysis

> Covers deliverable 10 (Competitor and market analysis) and strategic responsibility 3 (Market research).
> Evidence labels: **[F]** fact · **[E]** estimate · **[A]** assumption. Source codes refer to `SOURCES.md`.

---

## 2.1 Market facts (verified)

| Fact | Figure | Source |
|---|---|---|
| UK private sector businesses, start of 2025 | ~5.7 million (up 3.5% year on year) | [F, S1] |
| SMEs as share of businesses | 99.85% (5,681,930) | [F, S1] |
| Businesses with no employees beyond the owner | ~4.27 million | [F, S1] |
| **Implied employing businesses** | **~1.4 million** | Derived from S1 |
| SME share of private sector jobs / turnover | ~60% / ~51% (£2.8trn) | [F, S1] |
| Businesses using at least one AI technology | ~32% in 2026 (DSIT survey); ~35% of firms with 10+ staff by mid-2026 (ONS) | [F, S2, S4] |
| Adoption pattern | Widening, not deepening: mostly ad-hoc staff use of chatbots | [F, S2] |
| Top barriers to adoption | No perceived need (71%), lack of skills (60%), then ethics, cost and unclear regulation | [F, S3] |
| Small-firm skills gap | 46% of small firms say they lack the skills or knowledge to use AI well (FSB, via secondary source) | [E, S5] |
| Results among adopters | Most report productivity gains; most have **not yet** seen revenue change | [F, S3] |

### What the facts mean for Ostler

1. **The demand is latent, not active.** "No perceived need" is the top barrier, so cold "do you want AI?" pitches will fail. Lead with a **specific, costed problem**, such as missed calls, no-shows or slow lead response, and present AI as the fix.
2. **The skills gap is the product.** Owners know AI matters but can't implement it. Done-for-you implementation with training is exactly what is missing.
3. **Revenue proof is scarce.** Most adopters haven't seen revenue impact [S3]. A consultancy that **measures and reports** outcomes stands apart immediately.
4. **Shallow adoption creates upgrade demand.** Businesses already paying for ChatGPT seats are warm prospects for proper workflow automation.

---

## 2.2 Market sizing (bottom-up, local)

Top-down "AI market is worth £X billion" figures don't help a local consultancy. What matters is **how many reachable, qualified businesses are within driving distance**, and what share you need.

### Method: pull real numbers for your area in 30 minutes

1. Go to **Nomis → UK Business Counts – enterprises / local units** (ONS, free).
2. Select your local authority areas, for example a city and its neighbouring districts.
3. Filter by **employment size band** (exclude 0–4 employees for the core pool; keep 5–249).
4. Filter by **SIC code** for your target niches:

| Niche | SIC 2007 codes |
|---|---|
| Restaurants, cafés | 56101, 56102, 56103 |
| Hotels and accommodation | 55100, 55201, 55202, 55209 |
| Fitness facilities | 93130 |
| Hairdressing and beauty | 96020 |
| Dental practices | 86230 |
| Other human health (private clinics, physio) | 86900, 86220 |
| Real estate agencies | 68310 |
| Accounting, bookkeeping | 69201, 69202, 69203 |
| Legal activities | 69101, 69102, 69109 |
| Retail (non-specialised and specialised) | 47110, 47190, 477xx |
| Cleaning | 81210, 81221, 81229 |
| Construction (specialised trades) | 43xxx |

5. Record the counts in a sheet. That is your **serviceable available market (SAM)**.

### Illustrative example (assumptions, to be replaced with your Nomis data)

| Step | Figure | Basis |
|---|---|---|
| Employing local units in target niches within a ~30-mile radius of a mid-sized UK city | 4,000 | [A] illustrative |
| Share that are "good fit" (owner-led, 5–100 staff, booking- or enquiry-heavy, some digital tools) | 40% → 1,600 | [A] |
| Share reachable in 24 months (visited, called, emailed or met at events) | 60% → 960 | [A] |
| Win rate across the full funnel | 5% → **~48 clients** | [A] |

The realistic financial scenario needs **about 49 active clients by month 24** (`model/outputs`). That is **about 3% of good-fit businesses** in a single city region. **The plan does not depend on winning a large market share. It depends on focus and execution in one area.**

### Revenue pool (estimate)

If 1,600 good-fit businesses each spent an average of £385 a month (the realistic-case blended fee), the local serviceable revenue pool would be **about £7.4 million a year** [E: 1,600 × £385 × 12]. Ostler's 24-month realistic target is about 3% of that.

---

## 2.3 Competitive landscape

### Competitor categories

| # | Category | Typical offer and price | Strengths | Weaknesses | How Ostler wins |
|---|---|---|---|---|---|
| 1 | **DIY AI receptionists and chatbots** (e.g. Fasthosts AI Receptionist) | £39–£99/month, self-set-up, no contract [E, S7] | Very cheap, instant, credible brands | Owner must configure it; generic; little integration; no one measures results | Sell **outcomes and integration**. Offer to configure or manage these tools when that is the best fit for the client. |
| 2 | **Freelance and small "AI automation agencies"** | £200–£500 setup, £100–£300/month for chat; £3k–£10k bespoke [E, S6] | Cheap, fast, often technically strong | Often generalist, remote, short-lived; weak on compliance, training and support | Local presence, niche playbooks, compliance pack, training and a monthly ROI report |
| 3 | **Vertical software vendors** (booking, POS, PMS and practice systems adding AI features) | Bundled into existing subscriptions | Already installed; data is native | Single-system, not cross-channel; generic; no implementation help | **Partner, don't fight.** Configure their AI features as part of the package and connect them to other channels. |
| 4 | **Web design and digital marketing agencies** adding chatbots | Bundled with websites and SEO | Existing client relationships | AI is a side-line; limited depth in operations automation | Become their **white-label AI delivery partner** (see the partnerships section in `blueprint/07`) |
| 5 | **Managed IT providers (MSPs)** adding Copilot and AI | Per-seat IT support plus Microsoft 365 Copilot projects | Trusted, on-site, security-strong | Focus on IT infrastructure, not front-of-house revenue workflows | Partner and referral relationship: they handle IT, Ostler handles revenue workflows |
| 6 | **Human answering services and virtual receptionists** | Per-call or monthly bundles (verify locally; not verified here) | Human warmth, established | Expensive at volume; limited hours or after-hours premiums | AI first line with human escalation, at much lower cost per call. Position as "AI plus your team". |
| 7 | **Large consultancies and systems integrators** | £600+/day consultants [F, S8]; enterprise programmes | Brand, depth | Don't serve micro or small firms economically | Not a direct competitor. Possible future subcontracting route. |
| 8 | **Doing nothing / the owner's nephew** | Free | No cost, no risk | Missed revenue continues; fragile set-ups | Make the cost of inaction visible with the ROI calculator |

### Pricing benchmark map

| Offer | Market low | Market mid | Market high | Ostler price | Rationale |
|---|---|---|---|---|---|
| Website or WhatsApp chat assistant, managed | £49/month + £199 setup [S6] | £200–£400/month + £300–£500 setup [S6] | £500–£1,500/month + £3k–£10k setup [S6] | **£195/month + £950 setup** (Starter, includes one workflow and reporting) | Above DIY, at the lower end of managed, because the offer is narrow and templated |
| AI voice receptionist | £39–£99/month DIY [S7] | £147–£299/month managed [S7] | £497–£1,497/month + setup [S7] | **In Growth: £495/month + £3,500 setup** (voice + chat + integrations + campaigns) | Bundled, multi-channel, measured. Cheaper than bespoke, richer than single-channel. |
| Consultancy day rate | — | £588/day UK median [F, S8] | £662/day London median [F, S8] | **£650/day; £495 fixed-price assessment** | Market median; fixed prices preferred for SMEs |

**Positioning conclusion:** Ostler should **not compete on price** with DIY tools. It should compete on **outcomes, integration, accountability and trust**, priced in the managed mid-market band, with a low-risk entry product (Starter) and a clear upgrade path.

---

## 2.4 Local competitor research method (repeat each quarter)

1. **Google search** "AI receptionist [town]", "AI chatbot [town]", "AI automation agency [county]" and "AI consultant [city]". List the first 20 results.
2. **LinkedIn search** for people titled "AI automation" or "AI consultant" within 25 miles.
3. **Ask prospects** in every discovery call: "Has anyone else pitched you AI tools? What did they offer?" Log the answers in the CRM.
4. **Check the vertical software used by your niche.** Look at each booking or POS vendor's AI features page and changelog.
5. **Mystery-shop two competitors** a year: request a quote and record price, scope, contract terms and quality.
6. Record findings in a sheet with: name, offer, price, contract, niche, strengths, weaknesses, reviews and last checked date.

**Tools:** Google, LinkedIn (free or Sales Navigator ~£80/month [A]), Google Sheets. **Cost:** 3–4 hours a quarter.
**Success measure:** you can answer "why you rather than X?" for every competitor a prospect names, and win-loss notes show price is the reason for fewer than 20% of losses.

---

## 2.5 SWOT

| Strengths | Weaknesses |
|---|---|
| Low startup cost; high gross margin (~70% modelled on subscriptions) | No brand, case studies or track record yet |
| Fast to deliver with existing platforms | Founder-dependent delivery and sales |
| Local, niche, outcome-led positioning | Reliance on third-party AI and platform vendors |
| Recurring revenue model | Limited capital |

| Opportunities | Threats |
|---|---|
| Latent demand and a 60% skills gap [S3] | Price compression from DIY tools [S7] |
| Free government AI training raising awareness [S5] | Vertical software vendors bundling AI for free |
| Partner channels (web agencies, MSPs, accountants) | AI errors damaging client reputations (needs guardrails) |
| Regulated sectors need compliant implementers | Regulatory change (DUAA 2025, EU AI Act for EU-facing clients) [S15, S17] |
| Productising niche playbooks into SaaS later | Vendor price rises or API changes |

**Mitigations for the main threats:** keep integrations portable (n8n workflows and prompts held as versioned exports); build on two or more LLM providers; include usage pass-through clauses in contracts; guardrails, testing and human handover on every assistant; quarterly regulatory review.
