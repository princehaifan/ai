# 8. Operating Model and Standard Operating Procedures

Labels: **[Recommendation]** throughout. Salary and day-rate figures are **[Estimate]** unless they cite [sources.md](sources.md).

---

## 8.1 Who does what: founder, AI, outsourced

| Function | Months 1–6 | Months 7–12 | Year 2 |
|---|---|---|---|
| **Strategy, sales, client relationships** | Founder | Founder | Founder + Head of Delivery shares accounts |
| **Discovery & Sprints** | Founder | Founder + delivery lead | Delivery lead / senior consultants |
| **AI engineering** | Founder (architecture, critical code) + 1–2 vetted contractors | Contract delivery lead + contractors; first salaried senior engineer (ambitious case) | Core team of 3–5 engineers + contractor bench |
| **Project management** | Founder, using the templates below | Delivery lead | Delivery/PM lead |
| **Quality assurance** | Peer review between founder and contractor; eval gates | Delivery lead owns QA checklist | QA built into team process |
| **Marketing content** | Founder writes; AI-assisted drafting; freelance editor/designer as needed | Freelance content producer (~4 hrs/week) | Marketing generalist |
| **Lead research & list building** | AI research agent + founder | Part-time virtual assistant (VA) + agent | SDR/BD hire when MRR > £30k |
| **Admin, scheduling, invoicing** | AI tools + VA (~5 hrs/week) | VA | Operations coordinator |
| **Bookkeeping, payroll, tax** | **Outsourced** accountant | Outsourced | Outsourced |
| **Legal (contracts, IP, DPAs)** | **Outsourced**: one-off template pack from a tech solicitor | Outsourced as needed | Outsourced |
| **Data protection advice (regulated clients)** | Outsourced partner (DPO-as-a-service) | Outsourced | Outsourced |

### Where AI runs the business internally
- Prospect research and account briefs (our own agent, used as a live demo).
- First drafts of proposals, SOWs and status reports from call transcripts.
- Meeting notes, action items and CRM updates.
- Content repurposing (long-form → posts → newsletter).
- Code assistance and test generation in delivery (always reviewed by a human).

**Rule:** AI drafts, humans decide. Nothing client-facing goes out without founder or delivery-lead review.

## 8.2 Building the contractor bench (weeks 1–6)

- **Target:** 3 vetted contractors: (1) a senior Python/AI engineer (RAG, agents), (2) a full-stack TypeScript engineer, (3) an automation/integration specialist (n8n, CRMs).
- **Where to find them:** your own network, ex-colleagues, local AI meetups, open-source contributors, selective freelance platforms.
- **Vetting:** a paid 1-day test task (build a small RAG + eval on a public dataset), reference check, security-hygiene check (MFA, device encryption).
- **Commercials:** day rates of roughly **£450–£650/day** for strong mid-senior contractors outside IR35 [Estimate; UK medians for AI engineer contracts are ~£640/day advertised, see sources]. Agree rates for 6 months.
- **Contracts:** subcontractor agreement with IP assignment to us (so we can assign to clients), confidentiality, data-protection terms, right to substitute, and an IR35 status determination where it applies.
- **Non-solicit** of clients and of each other.

## 8.3 Hiring triggers (don't hire on hope)

| Hire | Trigger (all must be true) | Indicative cost |
|---|---|---|
| **Contract delivery lead** (2–3 days/week) | Founder load > 100% for 4+ weeks (see model) **and** ≥ 2 concurrent Builds | ~£550–£650/day [Estimate] |
| **First salaried senior AI engineer** | Contractor spend > £8k/month for 3 months **and** MRR ≥ £8k **and** 3 months' salary in reserve | ~£70k–£95k salary (London) + NI + pension [Estimate] |
| **Head of Delivery** | 4+ concurrent clients **and** founder spending > 50% of time on delivery | ~£90k–£120k [Estimate] |
| **BD / sales hire** | MRR ≥ £30k **and** a documented sales playbook with proven conversion rates | Base + commission |

## 8.4 Standard Operating Procedures

### SOP-1: Client onboarding (within 5 business days of signature)

| # | Step | Owner | Done when |
|---|---|---|---|
| 1 | Countersigned MSA + SOW + DPA filed; deposit invoice paid | Founder | Payment received |
| 2 | Welcome email: team, schedule, what we need, kickoff date | Founder/VA | Sent |
| 3 | Client-side contacts named: sponsor, day-to-day owner, SMEs, IT/security | Client | Named in project doc |
| 4 | Access requests: systems, data samples, API accounts in **client's name** | Delivery | Access confirmed, least privilege |
| 5 | Data inventory: what personal/sensitive data is involved, lawful basis, location | Delivery + client DPO | Recorded in project risk log |
| 6 | Kickoff meeting: goals, **baseline metric capture**, acceptance metric confirmed, weekly demo slot booked | Founder | Minutes shared |
| 7 | Project workspace created (repo, tracker, shared channel) | Delivery | Live |
| 8 | Risk log and RAID started | Delivery | Created |

### SOP-2: Project delivery

1. Work in weekly cycles (see [07-technical-architecture.md §7.5](07-technical-architecture.md)).
2. **Weekly demo** of working software and the current eval score, every week, without exception.
3. **Friday status report** (template): progress, eval trend, budget burn (days used vs planned), risks, decisions needed.
4. **Change control:** any new requirement → written change request with impact on scope, time and price → client approval before work starts. Small changes (< 0.5 day) may be absorbed at the lead's discretion and logged.
5. **Phase gates:** spike review (end of week 1: go / adjust / stop), shadow-mode review (week 5), acceptance (week 6).
6. **Early-warning rule:** if budget burn exceeds progress by > 15%, the founder is told the same day and the client within the week, with options.

### SOP-3: Quality control: the go-live checklist

- [ ] Acceptance metric met on the agreed eval set; eval report produced
- [ ] Regression eval suite in CI
- [ ] Code reviewed by a second engineer; tests passing
- [ ] Security: least-privilege keys, secrets in a vault, prompt-injection tests passed (for tools/agents), dependency scan clean
- [ ] Data flows documented; retention settings configured; DPIA input pack delivered
- [ ] Human-review path working for low-confidence outputs
- [ ] Monitoring, alerting and cost tracking live
- [ ] Projected monthly running cost signed off by client
- [ ] Runbook, architecture doc and handover recording delivered
- [ ] Client sign-off recorded

### SOP-4: Support (Run retainers)

| Severity | Definition | Response (Growth) | Response (Enterprise) |
|---|---|---|---|
| P1 | System down or producing harmful/incorrect output at scale | Same business day | Agreed SLA (e.g. 2 business hours) |
| P2 | Degraded quality or a feature broken | Next business day | 1 business day |
| P3 | Minor issue / improvement request | Scheduled into monthly improvement hours | Scheduled |

- **Monthly value report** to every Run client: usage, eval scores, incidents, cost trend, value delivered vs baseline, recommended next improvements.
- **Quarterly review** with the sponsor: renewal health and next opportunities.
- Kill-switch documented for every system: how to revert to the manual process instantly.

### SOP-5: Contract management

| Document | Purpose | Key clauses |
|---|---|---|
| **Master Services Agreement (MSA)** | Signed once per client | Liability cap (typically fees paid in the previous 12 months), IP, confidentiality, warranties (no warranty of specific AI outputs beyond agreed acceptance tests), termination, governing law (England & Wales) |
| **Statement of Work (SOW)** | One per engagement | Scope, deliverables, exclusions, **acceptance metric and method**, timeline, price, payment milestones, client dependencies |
| **Data Processing Agreement (DPA)** | Where we process personal data | UK GDPR Art. 28 terms, sub-processor list (including AI providers), security measures, international transfer mechanisms, breach notification |
| **Run Schedule** | Managed services | Service levels, included hours, exclusions, 3-month minimum then monthly rolling, 30-day notice |
| **Mutual NDA** | Pre-sale | Standard |
| **Subcontractor Agreement** | Contractors | IP assignment, confidentiality, DPA flow-down, non-solicit |

**IP position (recommended):** the client owns bespoke deliverables (code written for them, their data, prompts specific to their business) **on full payment**. We keep our pre-existing IP and generic Delivery Kit components, and grant the client a perpetual, royalty-free licence to use them within the delivered system. This lets us reuse our accelerators while giving clients what they need. Have a tech solicitor draft the template pack. Budget ~£1,500–£3,500 [Estimate].

**Contract hygiene:** CRM records renewal dates; 60-day renewal reminders; signed documents stored in one place; every change request in writing.

## 8.5 Founder operating rhythm

| Cadence | Activity |
|---|---|
| Daily | 2 hours pipeline (outreach, follow-ups, content) before delivery work |
| Weekly | Monday: pipeline review + delivery planning. Friday: metrics review (dashboard below) + client status reports |
| Monthly | Finance review (cash, invoices, margin by project), content plan, partner check-ins |
| Quarterly | Strategy review against decision gates; price review; offer refinement |

### Weekly business dashboard (one page)

New outreach · replies · discovery calls · proposals sent/value · wins/value · pipeline value (weighted) · active projects and burn · MRR · founder load % · cash in bank · overdue invoices.
