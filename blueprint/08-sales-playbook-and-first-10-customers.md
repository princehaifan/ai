# 8. Customer acquisition and sales playbook, and the first 10 customers

> Covers deliverables 12 (Customer acquisition and sales playbook) and 17 (First 10 customer acquisition strategy), plus strategic responsibility 9.
> Supporting templates: `templates/outreach-scripts.md`, `templates/discovery-call-script.md`, `templates/ai-readiness-assessment.md`, `templates/roi-calculator.md`, `templates/proposal-template.md`.

---

## 8.1 Sales philosophy

1. **Diagnose before you prescribe.** Owners buy from people who understand their business. Ask, measure and then propose.
2. **Sell the outcome, demo the product.** Talk about calls, covers and hours. Prove it with a live demo in their context.
3. **Make the cost of inaction visible.** Use the prospect's own numbers in the ROI calculator. No invented industry statistics.
4. **Reduce risk.** Fixed prices, a short minimum term, a pilot option, no lock-in and clear exit terms.
5. **Every deal ends in a monthly plan.** No one-off projects without managed service.

---

## 8.2 Outreach rules (UK law, read before prospecting)

| Channel | Rule | Source |
|---|---|---|
| Email to **limited companies and LLPs** (corporate subscribers) | PECR's consent rule for marketing email does not apply, but you must identify yourself, give a valid contact address and an easy opt-out, and honour opt-outs. UK GDPR still applies to named individuals' data: have a legitimate interests assessment and say where you got their details. | [F, S16] |
| Email or SMS to **sole traders and ordinary partnerships** (individual subscribers) | Treated like consumers: you need **prior consent** (or soft opt-in from an existing relationship). **Don't cold email them.** Visit, call or use LinkedIn instead. | [F, S16] |
| **Live phone calls** | Screen numbers against the **CTPS** (companies) and **TPS** (sole traders and partnerships) before calling. Don't call if registered, unless they've told you they're happy to receive your calls. | [F, S16] |
| **Automated or AI-voice outbound calls** for marketing | Need specific prior consent. **Never use AI voice for cold outreach.** | PECR |
| In-person visits | No PECR restrictions. Be respectful: avoid peak service hours, leave a card and ask for a better time. | — |
| LinkedIn | Platform terms apply; personalised, low-volume, human messages only | — |

**Practical approach:** use **walk-ins, LinkedIn, events, referrals and calls** as the primary channels. Use cold email only to corporate subscribers, at low volume (fewer than 30 a day, personalised), from a separate sending domain, with a clear opt-out. Keep a suppression list in the CRM.

---

## 8.3 The 11-step repeatable sales process

| # | Step | What to do | Tools | Output / exit criterion | Target conversion [A] |
|---|---|---|---|---|---|
| **1** | **Identify potential clients** | Build a list of 200 businesses per launch niche within 30 miles from Google Maps, directories, portals (property) and Companies House. Score each against the ICP (`blueprint/03`). | Google Maps, Apify or manual scraping of *public business listings*, HubSpot | 200 scored prospects per niche in the CRM | — |
| **2** | **Research their business** | 10 minutes per prospect: website, reviews (unanswered? complaints about phones?), booking system used, opening hours, social activity, any public job ads for receptionists | Website, Google reviews, BuiltWith or Wappalyzer | 3 personalised observations noted | — |
| **3** | **Identify operational problems** | Run a quick test where appropriate (call after hours, send a web enquiry, check response time). Form a hypothesis: "likely losing out-of-hours enquiries". | Phone, web forms | Hypothesis plus evidence | — |
| **4** | **Arrange a discovery meeting** | Walk-in, LinkedIn, warm intro, call or email (within PECR rules). Offer the **free AI Opportunity Snapshot**. | Scripts in `templates/outreach-scripts.md`, Cal.com | Meeting booked | 15–20% of contacted |
| **5** | **Conduct an AI readiness assessment** | Free 30-minute snapshot → if qualified, sell the **£495 Readiness Assessment** (or go straight to proposal for simple Starter deals) | `templates/discovery-call-script.md`, `templates/ai-readiness-assessment.md` | BANT-qualified (budget, authority, need, timeline); baseline metrics captured | 50% of snapshots → assessment or proposal |
| **6** | **Demonstrate a relevant solution** | Personalised demo trained on *their* website and FAQs; let them call it; show the monthly report mock-up | Demo stack; Loom for follow-up | Owner says "I want that" | — |
| **7** | **Present a commercial proposal** | Within 48 hours. One-page summary with problem cost (ROI calculator), solution, package, price, timeline, what's not included, next steps. Present it live, not by email only. | `templates/proposal-template.md`, PandaDoc or Qwilr | Proposal presented | — |
| **8** | **Close the deal** | Handle objections (§8.5); offer a pilot or 12-month incentive where appropriate; e-sign; Direct Debit mandate; setup invoice | E-signature, GoCardless, Stripe | Signed agreement plus setup fee paid (50% up front minimum) | 35% of proposals |
| **9** | **Implement the solution** | Onboarding and delivery process (`blueprint/09`) | n8n, voice, chat stack | Live on agreed date | — |
| **10** | **Measure results** | Baseline vs. 30, 60 and 90-day metrics; results review meeting | Reporting dashboard; `templates/monthly-report-template.md` | Documented outcome; testimonial request | — |
| **11** | **Convert to a recurring monthly contract and expand** | Monthly plan starts at go-live (built into every package). At 90 days, propose the next automation or upgrade, and ask for a referral. | CRM expansion pipeline | Monthly plan active; expansion and referral asked | ≥ 25% upgrade within 6 months |

### Pipeline stages in the CRM

`Prospect → Researched → Contacted → Snapshot booked → Snapshot done → Assessment/Proposal → Negotiation → Won → Onboarding → Live → Expansion`
Plus a `Lost` stage (record the reason) and a `Nurture` stage (follow up in 90 days).

---

## 8.4 Sales activity targets (founder, months 2–6)

| Weekly activity | Target |
|---|---|
| New prospects researched | 40 |
| Walk-in visits | 15 (two afternoons a week, outside peak hours) |
| Calls or LinkedIn conversations | 25 |
| Snapshots held | 3 |
| Proposals presented | 1–2 |
| Partner meetings | 1 |
| Events attended | 1 |

**Rule of thumb [A]:** about 30 meaningful conversations → 6 snapshots → 3 proposals → 1 client. Track your actual ratios from week 4 and adjust.

---

## 8.5 Objection handling

| Objection | Response approach |
|---|---|
| **"It's too expensive."** | "Compared with what? Let's use your numbers." Show the ROI calculator: missed enquiries × conversion × value. Compare with the cost of a part-time receptionist. Offer Starter as the entry point. Never discount list price without reducing scope. |
| **"Customers want to speak to a human."** | "Agreed, and they still can. The AI answers instantly when your team can't, and hands over anything complex. Right now, those callers get voicemail." Let them call the demo. |
| **"AI makes things up."** | "That's why we ground answers only in your approved information, test 50 real questions before go-live, and set it to say 'I'll check with the team' when unsure. You see every conversation." |
| **"Is this GDPR compliant?"** | Show the trust pack: data processing agreement, sub-processor list, UK or EU hosting options, retention settings, AI disclosure and DPIA support. |
| **"We tried a chatbot before and it was rubbish."** | "What went wrong?" (Usually: generic, not connected to bookings, nobody maintained it.) "That's exactly why our monthly plan includes reviewing conversations and improving it." |
| **"I need to think about it."** | "Of course. What would you need to see to feel confident?" Agree a specific follow-up date; send a personalised demo recording. |
| **"I'm too busy to set it up."** | "That's the point: we do it. We need about two hours of your time in total, plus your team's FAQs." |
| **"What if it doesn't work?"** | Short minimum term (3 months), pilot pricing for early clients, a clear success plan with agreed KPIs, and an exit pack so you own your data and setup. |
| **"My booking system already has AI."** | "Great, we'll configure it properly and connect it to your phone, WhatsApp and reviews so it all works together." Partner, don't compete. |

---

## 8.6 Sales enablement kit

- [ ] Live demo numbers and chat assistants per niche
- [ ] 10-slide pitch deck (problem → cost → solution → demo → proof → packages → next steps)
- [ ] ROI calculator (sheet and web version)
- [ ] One-page package summary per niche
- [ ] Case study cards (from pilots)
- [ ] Trust pack (security, GDPR, responsible AI)
- [ ] Proposal template, MSA, SOW and DPA
- [ ] Leave-behind card with demo number and QR code to book a snapshot
- [ ] Objection-handling crib sheet (above)

---

## 8.7 First 10 customers: the acquisition strategy

### Goal

**10 paying clients on monthly plans within about 6 months of launch** (5 by day 120). The first three are discounted **pilots** that produce case studies. Clients 4–10 pay list price.

### Why the first 10 are different

You have no proof, so you are selling **trust and willingness to work closely together**. The first 10 come from **warm networks, high-touch local selling and irresistible, low-risk offers**, not marketing funnels.

### The sequence

| Wave | Clients | Source | Offer | Timing |
|---|---|---|---|---|
| **Wave 0: Warm network** | 1–3 (pilots) | Friends, family, former colleagues, your own suppliers (your barber, dentist, local restaurant, accountant), alumni and community groups | **Pilot:** 50% off setup (Starter £475, Growth £1,750), with the normal monthly fee from go-live. In return: case study, testimonial, two referral introductions and permission to use anonymised metrics. | Weeks 5–8 |
| **Wave 1: Proof-led local** | 4–6 | Walk-ins plus "The 7pm Test" campaign in launch niche B; referrals from pilots | List price; assessment credit; first pilot case study as proof | Weeks 9–16 |
| **Wave 2: Partners and events** | 7–10 | First AI breakfast event, two partner agencies, Chamber introductions, LinkedIn | List price; 12-month term incentive | Weeks 12–26 |

### Wave 0 playbook (in detail)

1. **List 50 warm contacts** who own or manage a business, or who can introduce you to one. Use your phone contacts, LinkedIn, WhatsApp groups, family, school-gate networks and religious or community groups.
2. **Personal message** (not a broadcast): *"I've started a business helping local firms use AI to stop missing customers. I'm taking on three pilot clients at half price in exchange for honest feedback and a case study. Do you know any owners who struggle with missed calls or slow replies, or is that you?"*
3. **Ask for introductions, not purchases.** "Who's the busiest business owner you know?"
4. **Run the snapshot**, measure the baseline (missed calls, response times, no-shows) and propose a pilot with a clear success plan.
5. **Over-deliver:** weekly check-ins, fast fixes and a 30-day results review.

### Pilot success plan (agree in writing before you start)

| Element | Example |
|---|---|
| Baseline (measured) | "Over two weeks, 38% of calls went unanswered during service." |
| Success KPIs | Answered-call rate; bookings taken by AI; no-show rate |
| Review dates | Day 14 (check-in), day 30 (results), day 60 (decision on full rollout or upgrade) |
| Client commitments | Provide FAQs and booking access within 5 days; nominate a champion; 30-minute review calls |
| Ostler commitments | Go-live in 10 working days; weekly tuning; transparent report |
| Exit | Cancel after 3 months with 30 days' notice. Data and configuration exported on request. |

### Selection criteria for pilots

Choose pilots that will **produce a strong, quick, visible result**:

- clear measurable pain (high call or enquiry volume)
- a booking or CRM system with integration options
- an owner who is enthusiastic and well-connected (they will refer others)
- in a launch niche, and preferably recognisable locally

**Avoid as pilots:** businesses in crisis, extremely price-sensitive owners, unusual systems with no API, or anything clinical or high-risk.

### First-10 tracker (keep in CRM)

| # | Business | Niche | Source | Package | Setup | MRR | Go-live | Baseline KPI | Day-30 result | Case study? | Referrals given |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | | |
| … | | | | | | | | | | | |

### Measures of success for the first 10

| Metric | Target |
|---|---|
| Pilots signed | 3 by day 60 |
| Pilots converted to ongoing monthly plans | 3 of 3 |
| Case studies published | 2 by day 120 |
| Referral introductions from pilots | ≥ 4 |
| Clients 4–10 at list price | 7 by month 6 |
| Time from first contact to signed (median) | ≤ 21 days |

---

## 8.8 Weekly sales rhythm

| Day | Focus |
|---|---|
| Monday | Pipeline review (30 min), research 40 prospects, LinkedIn posts and outreach |
| Tuesday | Walk-ins (afternoon, outside peak hours), snapshots |
| Wednesday | Delivery and build day |
| Thursday | Walk-ins or calls, proposals, partner meeting |
| Friday | Delivery, client reviews, follow-ups, metrics update |
