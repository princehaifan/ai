# 9. Client onboarding, delivery, operations and team structure

> Covers deliverable 13 (Client onboarding and delivery process) and strategic responsibilities 11 (Client onboarding and delivery) and 12 (Operations and team structure).
> Supporting templates: `templates/client-onboarding-checklist.md`, `templates/dpia-and-ai-risk-checklist.md`, `templates/monthly-report-template.md`.

---

## 9.1 Delivery principles

1. **Standardise first, customise second.** Every build starts from a niche template.
2. **Baseline before build.** If you didn't measure it before, you can't prove it after.
3. **Ship in slices.** Get something live in week one or two (e.g. missed-call text-back), then layer up.
4. **Test like it's your reputation**, because it's the client's reputation.
5. **Handover is a beginning.** Monthly optimisation is part of the product.

---

## 9.2 The delivery lifecycle (Growth package example, 6 weeks)

| Phase | Timing | Activities | Client involvement | Exit criteria |
|---|---|---|---|---|
| **0. Contract and kick-off** | Day 0–2 | Signed MSA, SOW and DPA; setup invoice paid (50% minimum); Direct Debit mandate; welcome email with onboarding form; kick-off call booked | 60-minute kick-off | Access requests sent; champion named |
| **1. Discover and baseline** | Week 1 | Process mapping; capture baseline metrics (call logs, response times, no-shows, booking volumes); collect FAQs, policies, prices, tone of voice; systems access (least-privilege); DPIA screening | Champion: 2–3 hours | Baseline recorded; content pack ≥ 80% complete; DPIA decision made |
| **2. Design** | Week 1–2 | Conversation flows; handover rules; red-flag scripts; integration design; sign-off of scripts and the "never say" list | 45-minute design sign-off | Signed flow design |
| **3. Build** | Week 2–4 | Configure from template: knowledge base, assistants, voice agent, integrations, workflows, reporting, logging | Minimal | All components in staging |
| **4. Test** | Week 3–5 | Evaluation set of 30–50 real questions; edge cases (angry caller, wrong language, prompt injection, medical or legal red flags); integration tests (bookings land correctly); load test; **client user-acceptance testing (UAT)** | Champion and owner: 1 hour UAT | ≥ 95% correct, zero critical failures, UAT sign-off |
| **5. Launch** | Week 2 (chat), 4 (voice), 6 (campaigns) | Staged go-live; call forwarding rules (e.g. AI answers after 3 rings or out of hours first); staff training session; AI disclosure live; monitoring alerts on | Half-day staff training | Live; first-week hypercare plan active |
| **6. Hypercare** | 2 weeks after each go-live | Daily conversation review; rapid fixes; check-in at day 3 and day 10 | 15-minute check-ins | Error rate stable; client confident |
| **7. Optimise and report** | Monthly, ongoing | Conversation review, prompt tuning, KB updates, monthly report, quarterly strategy review, expansion ideas | 30-minute monthly or quarterly review | KPI trend vs. baseline; renewal and expansion |

**Starter package:** the same phases compressed into **10 working days** (discover and design on days 1–2, build on days 3–6, test on days 7–8, launch on days 9–10).
**Transformation:** paid discovery, then fortnightly sprints, each with its own design → build → test → release cycle and a sprint review.

---

## 9.3 Onboarding essentials

**Welcome pack (sent within 24 hours of signing):**

- welcome letter with named contacts and support hours
- the timeline with dates
- onboarding form (business details, opening hours, services and prices, FAQs, tone, escalation contacts, systems used)
- access request list (booking system, website, phone provider, Google Business Profile, Meta Business Manager), with *instructions to invite us as a user, never to share passwords*
- data processing agreement and privacy notice wording for their website
- "How AI will work in your business" one-pager to share with staff

**Kick-off agenda (60 minutes):**

1. Goals and success KPIs (confirm the success plan)
2. Walk through a customer's journey today
3. Agree escalation rules: who gets what, when, and how
4. Agree the "never say or do" list (e.g. no prices for X, no medical advice, no promises on availability)
5. Content collection plan and deadlines
6. Dates for UAT, training and go-live

---

## 9.4 Quality assurance standard

| Test | Standard |
|---|---|
| Knowledge accuracy | ≥ 95% correct on an evaluation set built from real customer questions |
| Critical failures | Zero: invented prices or policies, unsafe advice, failure to escalate a red flag, abusive or off-brand language |
| Handover | 100% of handover requests reach a person or create a message with full context |
| Integrations | 20 test bookings created, amended and cancelled correctly |
| Prompt injection | Assistant refuses to reveal system instructions, ignores "ignore previous instructions", and cannot be talked into unapproved actions |
| Disclosure | Assistant states it is an AI assistant at the start of voice calls and in the chat widget |
| Accessibility | Chat widget keyboard-navigable; voice agent speaks clearly at a moderate pace; offers a human option |
| Data | No unnecessary personal data collected; retention settings applied; logs pseudonymised where possible |

Record every test run in the client's delivery record, and re-run the evaluation set after every significant prompt or model change.

---

## 9.5 Ongoing service management

| Activity | Frequency | Owner |
|---|---|---|
| Automated health checks and alerts | Continuous | Monitoring |
| Conversation sampling and review (20 per client or all flagged ones) | Weekly or monthly by plan | Delivery engineer |
| Knowledge-base and content updates | Per plan allowance | Delivery engineer |
| Model and platform updates; re-run of evaluation set | When vendors change models; monthly check | Delivery lead |
| Monthly performance report | Monthly (first working week) | Automated, with commentary from the account owner |
| Quarterly business review | Quarterly (Growth+) | Founder or account manager |
| Usage and margin check | Monthly | Founder |
| Renewal and expansion conversation | Month 3, then every 6 months | Founder or account manager |

**Support SLAs:** see the package table in `blueprint/04` §4.2F. Priority 1 incidents (assistant down, wrong bookings, data issue) get a response within 2 business hours for every plan, with a workaround (e.g. revert call forwarding) within 4 hours.

---

## 9.6 Client health score (churn prevention)

| Signal | Green | Amber | Red |
|---|---|---|---|
| KPI trend vs. baseline | Improving | Flat | Worse |
| Engagement (attends reviews, responds) | Yes | Slow | Ghosting |
| Support tickets | Few, minor | Repeated issues | Escalations or complaints |
| Usage | Within plan | Very low (not using it) | Over allowance with no upgrade |
| Payment | On time | One failure | Repeated failures |

Review health monthly. **Any red flag triggers a founder call within 5 working days.** Amber triggers an extra optimisation session.

---

## 9.7 Operations

### Core operating systems

| Area | System |
|---|---|
| Sales pipeline | HubSpot (or Pipedrive) |
| Delivery tracking | Notion board per client: phases, tasks, decisions, access log |
| Knowledge and SOPs | Notion wiki: playbooks, templates, checklists, prompts library |
| Code and configuration | Git repository: n8n workflow exports, prompts, eval sets per client, all versioned |
| Credentials | 1Password vaults per client; access reviewed quarterly |
| Finance | Xero + GoCardless + Stripe; monthly management accounts |
| Support | Shared inbox (help@) + ticket labels; later a help-desk tool |
| Reporting | Database → dashboard → monthly PDF and email |

### Standard operating procedures to write in the first 90 days

1. Prospect research and qualification
2. Snapshot and assessment delivery
3. Proposal and contract
4. Client onboarding (access, content, DPIA)
5. Niche template deployment (one per launch niche)
6. Testing and go-live checklist
7. Incident response
8. Monthly reporting
9. Offboarding and data export or deletion
10. New team member onboarding (security first)

### Founder's time allocation (months 1–6)

| Activity | Share |
|---|---|
| Selling (prospecting, meetings, proposals) | 40% |
| Delivery (building, testing, support) | 40% |
| Marketing content and partnerships | 10% |
| Admin, finance, learning | 10% |

---

## 9.8 Team structure and hiring roadmap

| Stage | Team | Trigger (from model) | Notes |
|---|---|---|---|
| **Months 0–~12** | Founder + freelancers (overflow build, design, bookkeeping) | — | Keep fixed costs low; build SOPs and templates |
| **Hire 1** | **Automation engineer / delivery specialist** (n8n, APIs, LLM prompting, testing) | ~18 active clients (month 14 realistic) | Frees the founder to sell; salary assumption ~£30–£38k [A]. Consider an apprentice or graduate with strong mentoring. |
| **Hire 2** | **Client success and sales executive** (account management, renewals, upsells, snapshots) | ~£12k MRR (month 18 realistic) | Owns retention and expansion; part-commission |
| **Hire 3** | **Second automation engineer** | ~45 active clients (month 23 realistic) | Specialise by niche or by voice or chat |
| **Year 2–3** | Head of delivery; niche specialists (hospitality, property, healthcare compliance); part-time DPO-style privacy adviser; marketing executive | Revenue ≥ £400k and multiple niches | Introduce delivery pods (1 lead + 2 engineers per ~60 clients) |

**Contractor vs. employee:** check IR35 and employment status rules when using freelancers regularly.
**Culture and values:** honesty about what AI can and can't do; client outcomes first; document everything; security by default.

---

## 9.9 Offboarding (build trust by making leaving easy)

1. Written notice per contract (30 days after the minimum term).
2. Export pack: conversation logs (if requested and lawful), knowledge base content, workflow descriptions, and configuration where the client owns the accounts.
3. Disable integrations, revoke all access, rotate any shared keys.
4. Delete or return client personal data per the DPA. Confirm deletion in writing.
5. Exit interview: reason for leaving, logged in the CRM. Feed it into product improvements.

---

## 9.10 How delivery success will be measured

| Metric | Target |
|---|---|
| On-time go-live (vs. date agreed at kick-off) | ≥ 90% |
| Client effort to onboard (owner hours) | ≤ 3 hours, Starter; ≤ 6 hours, Growth |
| First-month critical incidents | 0 |
| Client satisfaction at day 30 (1–10) | ≥ 9 |
| Clients with documented KPI improvement at day 90 | ≥ 80% |
| Template reuse (share of build from templates) | ≥ 70% by client 10 |
| Gross margin per client | ≥ 65% |
| Monthly logo churn | ≤ 3% |
