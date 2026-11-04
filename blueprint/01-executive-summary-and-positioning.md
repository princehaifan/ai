# 1. Executive summary, business concept and positioning

> Covers deliverables 1 (Executive summary), 2 (Business concept and value proposition) and 3 (Recommended company positioning).
> Evidence labels: **[F]** fact · **[E]** estimate · **[A]** assumption. Source codes such as [S1] refer to `SOURCES.md`.

---

## 1.1 Executive summary

### The opportunity

- The UK had about **5.7 million private sector businesses** at the start of 2025, and **99.85% were SMEs** [F, S1]. About 1.4 million of them employ staff. That is the realistic pool for paid AI services, because non-employers rarely have the volume of calls, bookings or admin that automation pays back on.
- AI adoption is **widening but shallow**. Government surveys put business use of at least one AI tool at roughly a third in 2026 [F, S2, S4]. Most of that is staff using chatbots informally, not automated processes [F, S2].
- The two biggest barriers that firms report are **"we don't see the need" (71%)** and **"we lack the skills" (60%)** [F, S3]. A consultancy that turns AI into a specific, measured business outcome removes both barriers. That is the business.
- The market is crowded at the cheap end. Self-serve AI receptionists cost **£39–£99 a month** [E, S7], and freelance chatbot builders charge **£200–£500 setup plus £100–£300 a month** [E, S6]. The gap is a **trusted local partner** who diagnoses the problem, integrates AI with the tools the business already uses, measures the result and keeps improving it.

### The business

**Working name: Ostler** *(an ostler looked after travellers' horses at a coaching inn: the dependable local hand who kept business moving. Check availability before you commit; see §1.4.)*

Ostler is a **managed AI operations partner for local service businesses**. It finds where a business is losing money or time, such as missed calls, no-shows, slow replies, manual admin or unanswered reviews. It then fixes those problems with proven AI and automation tools and runs them as a monthly managed service with a monthly results report.

### How it makes money

| Revenue stream | Price point (ex VAT) | Role |
|---|---|---|
| AI Opportunity Snapshot | Free (30 minutes) | Lead generation |
| AI Readiness Assessment | £495 (credited against a project) | Paid qualification |
| AI Starter | £950 setup + £195/month | Entry product: one channel and one workflow |
| AI Growth | £3,500 setup + £495/month | Core product: multi-channel, integrated |
| AI Transformation | From £12,000 setup + £1,500/month | Custom builds after a paid discovery |
| AI Managed Care (standalone) | £150–£895/month | Looking after systems others built |
| Training | £350–£1,350 per session | Trust-builder and upsell route |

These prices sit inside the published UK market ranges: above the DIY tools, in line with managed providers and below bespoke agencies [E, S6, S7]. See `blueprint/04` for the full catalogue.

### The numbers (modelled, not promised)

From `model/financial_model.py`. All of it rests on assumptions you must validate.

| | Conservative | **Realistic** | Optimistic |
|---|---:|---:|---:|
| Active clients, month 12 | 7 | **15** | 27 |
| MRR, month 12 | £2.1k | **£5.8k** | £11.8k |
| MRR, month 24 | £7.3k | **£19.0k** | £38.3k |
| Year 2 revenue | £120k | **£305k** | £598k |
| Sustained break-even (after founder draw) | Month 11 | **Month 7** | Month 4 |
| Peak cash needed (incl. £5.2k startup) | £24k | **£19k** | £13k |
| Lifetime value : fully loaded CAC | 3.8x | **7.1x** | 10.2x |

**Plan to fund roughly £20,000–£25,000** (savings, a Start Up Loan or part-time income) to cover setup costs and a modest founder draw until break-even.

### The plan in one line

**Weeks 1–4:** pick two niches, build three demos and validate pricing in 20 conversations. **Weeks 5–8:** sign three discounted pilots. **Weeks 9–13:** deliver them, measure them and turn them into case studies and monthly contracts. Then repeat the playbook niche by niche.

### What will decide success

1. **Niche focus.** Be known for something specific, such as "the people who stop dental practices missing new-patient calls", not "AI for everyone".
2. **Measured outcomes.** A baseline before go-live and a monthly report after it. This is what justifies the monthly fee and lowers churn.
3. **Recurring revenue discipline.** Every project ends in a managed-service contract. MRR, not setup fees, makes the company valuable.
4. **Platform, not custom code.** Reuse templates across clients so margins rise as you grow.
5. **Trust and compliance.** UK GDPR, transparency and human oversight are selling points, especially in healthcare and professional services.

---

## 1.2 Business concept and value proposition

### The core insight

Local businesses do not want "AI". They want:

- fewer missed calls and enquiries
- fewer no-shows and empty slots
- faster replies, at any hour
- less admin for owners and staff
- more reviews, repeat visits and referrals
- someone local they trust to set it up and fix it when it breaks

AI is now cheap and capable enough to deliver these results. However, most owners lack the time, skills and confidence to pick, connect and maintain the tools [F, S3]. **Ostler sells the outcome and owns the complexity.**

### Value proposition (customer-facing)

> **"We find where your business is losing customers and hours, then put AI to work fixing it. We set it up around the tools you already use, train your team, and send you a report every month showing what it's done. No jargon, no lock-in, no in-house tech team needed."**

### Value proposition canvas

| Customer jobs | Pains | Gains they want |
|---|---|---|
| Answer calls and messages | Missing calls while busy with customers | Every enquiry captured, 24/7 |
| Fill the diary or tables | No-shows, last-minute gaps | Fuller diary, deposits, automatic waitlists |
| Win new customers | Slow replies lose leads to competitors | Reply in seconds, not hours |
| Keep customers coming back | No time for follow-ups | Automatic reminders, rebooking and win-backs |
| Manage reputation | Reviews go unanswered | More reviews and a consistent, timely response |
| Run the back office | Re-typing data, chasing paperwork | Admin hours given back |
| Make decisions | Gut feel and spreadsheets | Simple dashboards and forecasts |

| Ostler's pain relievers | Ostler's gain creators |
|---|---|
| AI receptionist (voice), WhatsApp and web assistants, linked to the booking system | Monthly ROI report that shows the results |
| Automated reminders, deposits, waitlists and confirmations | Reactivation and review campaigns |
| Lead capture, qualification and instant follow-up | Staff trained to use AI safely every day |
| Document and email triage automation | Continuous optimisation, with each month better than the last |
| Local, named support contact and UK GDPR-ready set-up | Roadmap from quick wins to deeper transformation |

### Why now

- **Capability and cost:** voice AI now runs at about **$0.07–$0.30 a minute all-in** [E, S11], and a typical text conversation on a small LLM costs a fraction of a penny, roughly £1–£4 per thousand conversations at autumn-2026 list prices [E, S12; worked example in `blueprint/05`]. Running an AI receptionist now costs a fraction of a part-time salary.
- **Awareness without capability:** adoption has tripled since 2023, but mostly as shallow use [F, S2]. Businesses have heard of AI but haven't put it into their operations.
- **Government push:** free national AI skills training targets SME staff [F, S5]. That builds awareness, which Ostler can turn into implementation.
- **Regulatory clarity:** the Data (Use and Access) Act 2025 reforms UK GDPR, including automated decision-making [F, S15]. Businesses need someone to get this right for them.

---

## 1.3 Recommended company positioning

### Positioning statement

> **For** owner-led local businesses with 3–100 staff that lose time and revenue to calls, bookings and admin,
> **Ostler is** a managed AI operations partner
> **that** finds the highest-value problems, fixes them with proven AI tools connected to your existing systems, and reports measurable results every month.
> **Unlike** DIY AI tools that leave you to set them up alone, freelancers who build a chatbot and disappear, or big consultancies built for corporates,
> **Ostler** stays accountable for the outcome: local, plain-English, transparent pricing, and no lock-in.

### Where Ostler sits in the market

```
                     HIGH TOUCH / ACCOUNTABLE FOR OUTCOMES
                                     │
     Big consultancies               │        ► OSTLER ◄
     (£££, corporate focus)          │        Managed AI operations partner
                                     │        Outcome-priced, local, niche playbooks
   ──────────────────────────────────┼───────────────────────────────────────
     CUSTOM / EXPENSIVE              │                 PACKAGED / AFFORDABLE
                                     │
     Bespoke dev agencies            │        DIY AI receptionists & chatbot
     (£8k–£60k builds)               │        SaaS (£39–£99/month) [S7]
                                     │        Freelance chatbot builders [S6]
                                     │
                     LOW TOUCH / CUSTOMER DOES THE WORK
```

### The five positioning pillars

| Pillar | What it means in practice | Proof point to build |
|---|---|---|
| **1. Outcomes, not tech** | Proposals priced against a measured problem, e.g. "about 40 missed calls a week" | Baseline and monthly ROI report for every client |
| **2. Industry playbooks** | Pre-built flows for each niche: the booking systems, FAQs and compliance rules that apply | Niche landing pages and demo assistants |
| **3. Local and human** | Named account manager, in-person visits, training on site | Google reviews from local clients |
| **4. Safe and compliant by default** | DPIA template, AI disclosure, human handover, UK and EU data hosting options | Trust page, Cyber Essentials certification, data processing agreement on request |
| **5. Transparent, no lock-in** | Fixed prices published on the website; client owns their data and configurations | Exit clause and export pack in every contract |

### Brand promise and tone

- **Promise:** *"Practical AI that pays its way."*
- **Tone:** plain English, warm, confident and specific. Avoid hype words such as "revolutionary", "game-changing" and "10x". Talk about calls, covers, bookings and hours, not models and tokens.
- **Taglines to test:**
  - "Never miss another customer."
  - "Practical AI for local business."
  - "Your business, answered."

---

## 1.4 Naming and identity checklist

Before you commit to "Ostler" or any other name:

| Check | Where | Cost |
|---|---|---|
| Company name available | Companies House name search (free) | Free |
| Trade mark conflicts in class 35 (business consultancy), 42 (software/IT) and 41 (training) | UK IPO search; consider filing yourself | ~£170 for one class online, +£50 for each extra class [A: check current IPO fees] |
| .co.uk and .com domains, plus social handles | Any registrar; Namecheckr | £10–£30/year |
| Not confusingly similar to a local competitor | Google Maps search in your target area | Free |

Alternative names to test with five target customers: *Kindred AI, Fettle, Wayside AI, Bellwether Ops, Hearth AI.* Choose the name customers remember and can spell after hearing it once.

---

## How success will be measured (whole business)

| Metric | 90-day target | 12-month target (realistic case) |
|---|---|---|
| Discovery conversations held | 40 | 200+ |
| Paying clients (recurring) | 3 pilots | 15 |
| Monthly recurring revenue | £600+ | £5,800 |
| Client-reported outcome improvement vs. baseline | Measured for 100% of clients | Measured for 100% of clients |
| Monthly logo churn | n/a | ≤ 3% |
| Net Promoter Score | First 3 testimonials | NPS ≥ 50, 10 case studies |
