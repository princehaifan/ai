# DPIA screening and AI risk checklist (per client deployment)

> The **client is the controller** and owns the DPIA. Ostler, as processor, helps them complete it. Use the ICO's DPIA template for full assessments. This checklist is the screening step plus AI-specific controls. Not legal advice.

---

## Part A: DPIA screening (is a full DPIA needed?)

Answer yes or no. **Any "yes" means a full DPIA is likely needed**, so complete one before go-live.

| # | Question | Y/N |
|---|---|---|
| 1 | Will the system process **special category data** (health, ethnicity, religion, sexual orientation, biometric, etc.) or **criminal offence data**? | |
| 2 | Will it process data about **children** or other vulnerable people? | |
| 3 | Will it make or support decisions with **legal or similarly significant effects** on people (e.g. access to services, tenancy, membership cancellation, credit)? | |
| 4 | Does it involve **large-scale** processing or **systematic monitoring** (e.g. call recording and transcription of all calls at volume)? | |
| 5 | Does it use **innovative technology** (e.g. AI voice agents, LLMs) in a way people might not expect? | |
| 6 | Does it **combine datasets** from different sources (e.g. booking history + marketing + reviews) for profiling? | |
| 7 | Will data be **transferred outside the UK** (e.g. to US-based AI vendors)? | |
| 8 | Could a data breach cause **significant harm** (financial, reputational, distress)? | |

*Many AI receptionist and assistant deployments will trigger Q5 and Q7, so treat a short DPIA as standard practice for Growth and Transformation clients.*

---

## Part B: Data flow summary

| Item | Detail |
|---|---|
| Data subjects | e.g. callers, website visitors, customers, staff |
| Personal data collected | e.g. name, phone number, email, booking details, call audio and transcript |
| Special category data | None intended. Controls in place to avoid collection (see Part C). |
| Purpose | e.g. answering enquiries, managing bookings, sending reminders |
| Lawful basis (controller) | e.g. contract (bookings), legitimate interests (answering enquiries), consent (marketing) |
| Systems and sub-processors | e.g. voice platform, LLM provider, messaging provider, hosting, booking system |
| Hosting regions and transfer mechanisms | e.g. EU region; UK–US Data Bridge / IDTA for US vendor |
| Retention | e.g. transcripts 90 days; booking data per the client's policy |
| Access | Named Ostler engineers (MFA); client staff via portal |

---

## Part C: AI-specific risk controls

| Risk | Control | In place? |
|---|---|---|
| **Inaccurate or made-up answers** (prices, policies, allergens) | Retrieval from approved content only; "I'll check with the team" fallback; evaluation set ≥ 95%; monthly sampling | |
| **Unsafe advice** (medical, legal, financial) | Topic guardrails; scripted red-flag escalation (999/111/staff); no advice in regulated areas | |
| **Lack of transparency** | AI disclosure at the start of calls and in chat; privacy notice updated; EU AI Act Art. 50 where EU users | |
| **No route to a human** | Handover on request and on low confidence; out-of-hours message capture with callback | |
| **Collection of unnecessary sensitive data** | Prompts instruct the assistant not to request health or financial details; redaction of card numbers; data minimisation | |
| **Automated significant decisions** | Assistant may recommend or triage only; humans decide (DUAA 2025 safeguards; Ostler policy) | |
| **Bias or discrimination** | No protected-characteristic inputs; review outcomes by segment where relevant; Equality Act check | |
| **Prompt injection or misuse** | Isolated system prompts; tool allow-lists; no payments, refunds or deletions without human approval; rate limiting | |
| **Data breach** | MFA; least-privilege keys; encryption; per-client separation; backups; incident plan (client notified without undue delay; ICO within 72 hours by controller if notifiable) | |
| **Vendor use of data** | API terms confirm no training on customer data; zero or limited retention enabled where needed | |
| **Over-reliance or deskilling of staff** | Staff training; human review of drafted replies; clear ownership | |
| **Marketing without consent** | Consent checks in campaign workflows; unsubscribe handling; PECR rules applied | |
| **Accessibility** | Alternative channels; clear speech; accessible widget | |

---

## Part D: Sign-off

| Role | Name | Date | Decision |
|---|---|---|---|
| Client (controller) | | | Approve / approve with conditions / reject |
| Ostler delivery lead | | | |
| Review date (12 months, or on material change) | | | |
