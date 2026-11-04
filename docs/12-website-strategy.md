# 12. Website and Digital Presence Strategy

**Goal of the website:** turn a visitor who already half-trusts us (from LinkedIn, a referral or an outreach email) into a **booked consultation**. In year one, almost nobody will find us through search, so the site is a **credibility and conversion tool**, not a traffic engine. [Recommendation]

**Principles**
- Lead with **business outcomes and proof**, not technologies.
- Every page has **one primary call to action**: *Book a 30-minute consultation*. The secondary CTA is a lead magnet.
- Say "we" honestly. Don't fake a large team. Show the founder.
- No invented logos, metrics or testimonials. Until case studies exist, use **demo projects** with real eval results, clearly labelled as demos.
- Fast, accessible (WCAG 2.2 AA), mobile-first, UK English.
- **Build:** Next.js on Vercel or a polished site builder (Framer/Webflow). Ship v1 in **≤ 10 working days**. Polish later.

## Sitemap

```
Home
├── Services
│   ├── AI Strategy & Opportunity Sprint
│   ├── AI Automation
│   ├── AI Agents
│   ├── AI Product Development
│   └── Managed AI (Run)
├── How we work (Sprint → Pilot → Run, + Acceptance Guarantee)
├── Industries
│   ├── SaaS & technology companies
│   └── Professional services firms
├── Work (case studies + demo projects)
├── Insights (articles, teardowns, templates)
├── About
├── Trust & security
├── Contact
└── Book a consultation
```

## Page-by-page plan

### Home
| | |
|---|---|
| **Purpose** | Make the promise clear in 5 seconds, prove credibility in 30, convert in 90 |
| **Structure** | 1) **Hero:** "AI that ships. Results you can measure." Sub-line: "We turn one expensive, repetitive workflow into a working AI system in six weeks, with the success metric agreed before we start." CTA: *Book a consultation*. 2) **Problem strip:** "Most AI pilots never reach production" (cite MIT carefully, with a link). 3) **Three-step model:** Sprint → Pilot → Run, with prices "from £3,500". 4) **What we build:** 4 outcome cards (support, documents, knowledge, AI features). 5) **Proof:** case study or demo with a real metric chart. 6) **Why us:** the 5 differentiators. 7) **Founder note** with photo. 8) **FAQ** (security, cost, timelines, "can't we just use ChatGPT?"). 9) Final CTA |
| **Messaging** | Outcome-first, calm, specific |
| **Conversion objective** | Consultation bookings; secondary: Opportunity Scorecard downloads |
| **CTAs** | Book a consultation · Take the AI Opportunity Scorecard |

### AI Strategy & Opportunity Sprint
| | |
|---|---|
| **Purpose** | Sell the entry product |
| **Structure** | Who it's for → what you get (deliverables list + sample anonymised output) → timeline (day by day) → price (£3,500 / £7,500, credited against a Build) → what happens next → FAQ |
| **Conversion objective** | Sprint enquiries |
| **CTA** | Book a Sprint scoping call |

### AI Automation
| | |
|---|---|
| **Purpose** | Capture ops leaders with repetitive-work pain |
| **Structure** | Pain ("your team spends X hours on Y") → workflows we automate (support, documents, CRM, internal ops) → how we measure (baseline vs after) → example workflow diagram → pricing ranges → proof → CTA |
| **Messaging** | "Take the most repetitive workflow off your team's plate in six weeks" |
| **CTA** | Book a consultation · Download the Production AI Checklist |

### AI Agent Development
| | |
|---|---|
| **Purpose** | Credibility with technical buyers (CTOs) |
| **Structure** | What agents are good (and bad) at → our approach (simplest architecture, scoped tools, human approvals, evals) → agent types (support, sales research, operations, knowledge) → safety & oversight → technical depth section (architecture diagram, eval example) → CTA |
| **Messaging** | Candid, no hype: "Agents that do real work, with guardrails you can audit" |
| **CTA** | Talk to an engineer |

### AI Product Development
| | |
|---|---|
| **Purpose** | Win funded startups needing AI features/MVPs |
| **Structure** | For founders & CTOs → MVP Blueprint (£6k) and MVP Build (£25k–£60k) → what "production-ready" includes (evals, analytics, cost per user) → you own the code → timeline → CTA |
| **CTA** | Book an MVP scoping call |

### Managed AI (Run)
| | |
|---|---|
| **Purpose** | Explain why AI needs ongoing care; sell retainers, including to companies whose AI was built by others |
| **Structure** | "AI systems degrade quietly" → what Run includes (tiers table) → monthly value report example → "Inherited an AI system? We'll audit it." → CTA |
| **CTA** | Book a free 30-minute AI system health check *(the check is free; any audit beyond it is paid)* |

### How we work
Sprint → Pilot → Run in detail, the weekly demo rhythm, the **Acceptance Guarantee** (precise wording, with conditions), the security approach. CTA: Book a consultation.

### Industries (SaaS & tech; Professional services)
| | |
|---|---|
| **Purpose** | Make each ICP feel "this is for us" |
| **Structure** | Industry-specific pains → 3–4 use cases with typical metrics → compliance notes (e.g. confidentiality for law/accountancy) → relevant proof → industry lead magnet → CTA |
| **SEO** | Target problem-specific long-tail terms (e.g. "AI document automation for accountancy firms UK") |

### Work (Case studies)
| | |
|---|---|
| **Purpose** | Proof, the biggest conversion driver |
| **Structure per case study** | Client context (anonymised if needed) → problem + **baseline** → what we built (architecture diagram) → **how we measured** → results with numbers → what didn't work → client quote (**with written permission only**) → CTA |
| **Before real case studies exist** | Publish 2–3 **demo projects**, clearly labelled "Demo built on public data", with real eval results and code walkthrough videos |

### Insights
Articles, teardowns, templates. Each piece ends with a relevant lead magnet or CTA. Newsletter sign-up (monthly). Publishing cadence matches the content plan in [06-acquisition-and-sales.md](06-acquisition-and-sales.md).

### About
Founder story (why implementation, why measurement), values, how we work with contractors/partners (honestly), photo. CTA: Book a consultation.

### Trust & security
What we actually hold (e.g. Cyber Essentials **once achieved**), data-handling principles, client-owned environments, AI provider sub-processors, human oversight standard, contact for security questionnaires. **No claims without evidence.**

### Contact & Book a consultation
| | |
|---|---|
| **Purpose** | Remove friction |
| **Structure** | Embedded calendar (30-minute slots), short form (name, company, role, "what would you like AI to fix?", company size), what to expect on the call, response-time promise (1 business day) |
| **Qualification** | Company-size field routes very small enquiries to the Scorecard / Starter offers automatically |
| **Conversion objective** | Booked call with a pre-qualified prospect |

## Technical & tracking checklist

- [ ] Privacy-friendly analytics (cookie banner if using non-essential cookies; PECR)
- [ ] Conversion events: booking completed, lead magnet downloaded, newsletter sign-up
- [ ] UTM conventions for LinkedIn, outreach and partner links
- [ ] Schema markup (Organization, Service, FAQ, Article)
- [ ] Privacy notice and cookie policy; company number and registered office in the footer (required for UK Ltd websites)
- [ ] Page speed > 90 on mobile; accessible colour contrast and alt text
- [ ] A dedicated outreach domain separate from the main site domain for email deliverability

## Other digital presence

| Asset | Purpose |
|---|---|
| **Founder LinkedIn** (primary channel) | Optimised headline: "I help tech companies get AI into production, measurably" + featured section with demo projects and Scorecard |
| Company LinkedIn page | Credibility; repost founder content |
| GitHub organisation | Public demo repos (eval harness examples, RAG starter lite) to show engineering quality |
| YouTube / Loom | 3–5 minute demo walkthroughs embedded on the site |
| Clutch / partner directories | Listings once there are reviews (with client permission) |
| Newsletter | Monthly: one insight, one teardown, one template |
