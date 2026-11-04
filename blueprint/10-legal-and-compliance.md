# 10. Legal, compliance and data protection

> Covers deliverable 15 (Legal and compliance considerations) and strategic responsibility 13.
> **This is not legal advice.** It is an informed checklist to discuss with a UK solicitor, ideally one with technology and data protection experience, before you sign your first client. Budget about £1,200 for template review (`blueprint/06`).
> Supporting template: `templates/dpia-and-ai-risk-checklist.md`.

---

## 10.1 Company set-up

| Item | Action | Notes |
|---|---|---|
| Legal structure | **Private limited company** | Limits personal liability, looks credible to clients, tax-efficient once profitable |
| Registration | Companies House incorporation; register for Corporation Tax with HMRC within 3 months of starting to trade | |
| VAT | Register when taxable turnover exceeds **£90,000** in a rolling 12 months (or voluntarily earlier) [F, S20] | Most SME clients reclaim VAT, so voluntary early registration can be fine. Discuss with your accountant. |
| Business bank account | Separate from personal finances from day one | |
| ICO data protection fee | Pay **£52** (tier 1) before processing personal data [F, S14] | Renew annually |
| Insurance | **Professional indemnity** (at least £1m; clients may ask for £2m+); **cyber liability**; **public liability** (on-site visits); **employers' liability** (legally required once you employ staff) | Disclose AI services accurately to insurers. Some policies exclude AI errors unless declared. |
| Trade mark | UK IPO filing for your brand (classes 35, 41, 42) | Optional, but protects the brand you're building |

---

## 10.2 Client contracts

Use a **Master Services Agreement (MSA)** plus a **Statement of Work (SOW)** or order form for each package, plus a **Data Processing Agreement (DPA)**.

| Clause | What it should say |
|---|---|
| **Scope** | Precise deliverables, limitations and assumptions (copy from the package definitions in `blueprint/04`) |
| **No guarantees** | Ostler commits to delivering services with reasonable skill and care. **No guarantee of revenue, savings or specific outcomes.** KPIs are measured and reported, not guaranteed. |
| **Client responsibilities** | Accurate content (prices, allergens, policies), timely approvals, lawful basis for their customers' data, their own regulatory obligations |
| **AI limitations** | AI outputs can be wrong. The client approves content and configurations. Human oversight is required for decisions with legal or similarly significant effects. |
| **Fees and payment** | Setup fee (50% on signing, 50% at go-live); monthly fee by Direct Debit in advance; usage overage at cost + 20%; late payment terms; right to suspend for non-payment |
| **Term and termination** | 3-month minimum then rolling monthly with 30 days' notice (or a 12-month term at a discount); termination for breach |
| **Intellectual property** | Client owns its data and content. Ostler owns its templates, know-how and reusable components and grants the client a licence to use the deliverables while subscribed (and specified items after exit). |
| **Third-party platforms** | Services depend on third-party providers (LLM, voice, messaging, hosting). Their outages, price changes or policy changes are outside Ostler's control. Ostler may pass through material price changes with notice. |
| **Limitation of liability** | Cap total liability (commonly 12 months' fees, or the fees paid under the SOW), excluding liability that can't be limited by law; exclude indirect and consequential loss. **Have a solicitor set the cap**, and check it is reasonable under UCTA. |
| **Data protection** | Reference the DPA; Ostler acts as **processor** for client customer data |
| **Confidentiality** | Mutual |
| **Acceptable use** | Client won't use the systems for unlawful marketing, deception, discrimination or prohibited content |
| **Exit** | Data export and deletion process; reasonable transition assistance (chargeable) |
| **Subcontracting** | Ostler may use vetted subcontractors and sub-processors, listed in the DPA |
| **Governing law** | England and Wales (or Scotland or Northern Ireland as appropriate) |

---

## 10.3 Data protection (UK GDPR, Data Protection Act 2018, Data (Use and Access) Act 2025)

### Roles

| Data | Ostler's role | Implication |
|---|---|---|
| Client's customers' data processed by assistants and workflows | **Processor** (the client is controller) | Article 28 DPA required; act only on documented instructions; sub-processor approval; assist with rights requests and DPIAs; breach notification to client without undue delay |
| Ostler's own prospects, clients' staff contacts, website visitors | **Controller** | Privacy notice, lawful basis (legitimate interests for B2B, with an LIA), PECR compliance, retention |
| AI vendors (LLM, voice, messaging, hosting) | **Sub-processors** of Ostler | DPAs with each; international transfer mechanisms; maintain a public sub-processor list |

### Compliance checklist

- [ ] **ICO fee** paid [S14]
- [ ] **Record of processing activities (ROPA)** for Ostler, plus a processing record per client
- [ ] **Privacy notice** for Ostler's website, plus **template privacy wording** for each client's website, covering AI assistants, call recording and transcription, retention and sub-processors
- [ ] **DPA template** (Article 28 compliant) and a **sub-processor register**
- [ ] **DPIA screening for every client.** A full DPIA is required where processing is likely to be high risk, e.g. **health data** (clinics, gyms collecting injuries), large-scale monitoring, innovative technology that significantly affects people, or children's data. *Helping the client complete it is part of the Growth and Transformation packages.*
- [ ] **International transfers:** where vendors process data outside the UK, rely on UK adequacy regulations (e.g. the EEA), the **UK–US Data Bridge** (for certified US organisations), or the **IDTA / UK Addendum** with a transfer risk assessment. Prefer **UK or EU hosting** options where available.
- [ ] **Vendor training settings:** confirm in each provider's commercial terms that API data is not used for model training. Enable zero or limited data retention where offered and needed (especially for health data).
- [ ] **Data minimisation:** assistants collect only what is needed (e.g. name, phone, booking time). No dates of birth, medical details or payment card numbers in chat.
- [ ] **Retention:** default 90-day conversation log retention, configurable; automated deletion
- [ ] **Data subject rights:** process to find, export and delete a person's data across systems within one month
- [ ] **Breach response:** notify the client without undue delay. The controller must report notifiable breaches to the ICO **within 72 hours**.
- [ ] **Complaints:** the Data (Use and Access) Act 2025 introduced a requirement for controllers to have a data protection complaints process (reported in force from June 2026) [S15]. Have one for Ostler and include it in client templates.
- [ ] **Call recording and transcription:** callers must be told at the start ("This call is answered by an AI assistant and may be recorded and transcribed to help us serve you").

### Automated decision-making (ADM)

The Data (Use and Access) Act 2025 replaced UK GDPR Article 22 with a new regime (Articles 22A–22D). Solely automated decisions with legal or similarly significant effects are more widely permitted, **subject to safeguards** (information, the right to contest, and human intervention). Stricter limits remain where **special category data** is involved [F, S15].

**Ostler's policy, stricter than the legal minimum:** assistants and models may **recommend, triage and draft**, but **a human makes** any decision with significant effects on a person. Examples: refusing a tenancy application, cancelling a membership, prioritising patients, credit or finance decisions, hiring. Document this in every SOW.

---

## 10.4 Marketing law (for Ostler and for clients' campaigns)

| Rule | Application |
|---|---|
| **PECR: email and SMS marketing** | Clients' campaigns to consumers need consent or the soft opt-in (existing customer, similar products, opt-out offered at collection and in every message). Build consent capture and unsubscribe handling into every campaign workflow. Ostler's own B2B outreach must follow the corporate/individual subscriber rules [S16] (see `blueprint/08` §8.2). |
| **PECR: calls** | Screen against TPS and CTPS. **No automated (AI-voice) marketing calls without specific consent.** |
| **WhatsApp Business Platform policies** | Opt-in required before business-initiated messages; approved templates only; respect blocks and opt-outs; quality ratings affect sending limits [S13] |
| **Fake reviews: DMCC Act 2024** | Writing, commissioning or publishing fake reviews, or concealing incentivised reviews, is a banned practice [F, S19]. **Ostler's review service only asks genuine customers for reviews and drafts *responses* for approval.** It never generates reviews, and never "review-gates" by asking only happy customers in a misleading way (also against Google's policies). |
| **Consumer protection** | Assistants must not make misleading statements about prices, availability or terms. Ground every answer in approved content. |

---

## 10.5 AI-specific obligations and good practice

| Area | Requirement / best practice |
|---|---|
| **UK regulatory approach** | The UK has no single AI Act. Existing regulators (ICO, CMA, FCA, MHRA, CQC, Ofcom, EHRC) apply their rules to AI, guided by government principles: safety, transparency, fairness, accountability, contestability. Follow the **ICO's guidance on AI and data protection**. |
| **Transparency** | Always disclose that customers are talking to an AI assistant, at the start of calls and in chat widgets. Offer a route to a human. |
| **EU AI Act** | Clients serving people in the EU (hotels with EU guests, e-commerce) should meet **Article 50 transparency duties** (applying from 2 August 2026): disclose AI interaction, and label synthetic content where relevant [S17]. Ostler's standard disclosure covers the chatbot duty. Take EU legal advice for EU-established clients. |
| **Equality Act 2010** | AI must not discriminate on protected characteristics (e.g. lead scoring, tenant screening, hiring). Test for bias; keep humans in the loop. |
| **Accuracy and safety** | Ground answers in client data; refuse rather than guess; red-flag escalation; evaluation before go-live and after changes |
| **Accessibility** | Always offer an alternative channel (human call-back or email); widgets that meet accessibility standards |
| **Security** | Protect against prompt injection and data exfiltration; least-privilege tools; no unattended payments, refunds or deletions |
| **Records** | Keep design decisions, test results and change logs for each client. They are evidence of due diligence if something goes wrong. |

**Publish an "Ostler Responsible AI Commitment"** on the website. In plain English: we disclose AI, keep humans in charge of important decisions, protect data, test before launch, and fix problems fast.

---

## 10.6 Sector-specific regulation

| Sector | Key considerations | Ostler's stance |
|---|---|---|
| **Healthcare** (clinics, dentists, physios, pharmacies, GP practices) | Health data is special category data (DPIA required); CQC registration duties stay with the provider; professional regulators (GDC, GMC, GPhC, HCPC); **MHRA**: software with a medical purpose may be a medical device; **NHS**: DSPT, DTAC, clinical safety standards **DCB0129** (manufacturer) and **DCB0160** (deploying organisation) [S18]; Caldicott principles; confidentiality | **Admin only**: booking, FAQs, reminders, forms, document routing. **No clinical advice, diagnosis or triage decisions.** Scripted red-flag escalation to 999, 111 or staff. NHS work only through an assured partner. Compliance pack add-on. |
| **Legal services** | SRA Standards: firms stay responsible for client service, confidentiality and privilege, supervision; no unauthorised reserved legal activities by AI | Intake, scheduling, internal knowledge search, document drafting **for lawyer review**. Never client-facing legal advice. |
| **Accountancy** | Money Laundering Regulations (customer due diligence), professional body codes (ICAEW, ACCA), confidentiality | Automate document collection and reminders. **Humans make AML decisions.** |
| **Financial services** (car dealer finance, insurance, mortgages via estate agents) | FCA regulation: financial promotions, Consumer Duty, no unauthorised regulated advice | Assistants give factual information and route to authorised staff. No product recommendations. |
| **Estate and letting agents** | Consumer protection (material information in listings), Property Ombudsman or Property Redress Scheme codes, AML, Renters' Rights changes, anti-discrimination in lettings | AI-drafted descriptions checked by humans; no automated tenant rejection; fair, consistent enquiry handling |
| **Hospitality and food** | Allergen information law (Food Information Regulations; PPDS labelling); licensing; consumer law on deposits and cancellations | Allergen answers only from the verified allergen matrix, with a "please confirm with staff" step; deposit terms quoted verbatim |
| **Education and children** | Safeguarding (KCSIE for schools), the ICO **Age Appropriate Design Code** for services likely to be used by children, parental consent | Assistants aimed at parents, not children; strict data minimisation; DPIA |
| **Gyms and fitness** | Health questionnaires (special category data); consumer contracts and cancellation rights | Don't collect health data in chat; keep cancellations human-handled or a transparent self-service flow |

---

## 10.7 Compliance calendar

| When | Task |
|---|---|
| Before first client | Company, bank, ICO fee, insurance, solicitor-reviewed MSA/SOW/DPA/T&Cs, privacy notice, sub-processor register, DPIA template, incident plan |
| First 90 days | Cyber Essentials; responsible AI page; complaints procedure; SOPs for rights requests and breaches |
| Every client | DPIA screening; DPA signed; disclosure and privacy wording live; evaluation and test record; access logged |
| Monthly | Review vendor changes (models, terms, pricing); sub-processor register updates |
| Quarterly | Access review; conversation audit sample for bias and accuracy; regulatory update check (ICO, DSIT, sector regulators, EU AI Act) |
| Annually | ICO fee renewal; insurance review; Cyber Essentials renewal; contract template review; staff data protection training |

---

## 10.8 How compliance success will be measured

| Metric | Target |
|---|---|
| Clients with signed DPA before processing | 100% |
| Clients with DPIA screening documented | 100% |
| Reportable data breaches | 0 |
| Data subject requests completed within one month | 100% |
| Assistants with AI disclosure and human route | 100% |
| Cyber Essentials | Certified by day 90; renewed annually |
| Regulatory review completed | Every quarter |
