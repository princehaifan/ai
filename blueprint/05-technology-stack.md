# 5. Recommended technology stack

> Covers deliverable 8 (Recommended technology stack) and strategic responsibility 8.
> Principle: **buy and configure before you build.** Use proven platforms, keep everything portable, and write custom code only where no platform can do the job.
> Prices are indicative at November 2026 [E, S9–S13]. Check vendor pages before committing; some are in USD or EUR.

---

## 5.1 Architecture at a glance

```
 CUSTOMER CHANNELS                 ORCHESTRATION                     INTELLIGENCE
 ─────────────────                 ─────────────                     ────────────
 Phone ──► Voice AI (Retell/Vapi) ─┐
 Website chat widget ──────────────┤
 WhatsApp (Meta Cloud API/BSP) ────┼──►  n8n (workflows, webhooks,  ──►  LLM router
 Instagram / Messenger ────────────┤     guardrails, logging)            ├─ Claude
 Email (Gmail / M365) ─────────────┘            │                         ├─ OpenAI
                                                │                         └─ Gemini
                                                ▼                        Knowledge base
                                     CLIENT SYSTEMS (via API)            (Postgres + pgvector)
                                     Booking · CRM · POS · PMS ·
                                     Accounting · Calendar
                                                │
                                                ▼
                         OBSERVABILITY & REPORTING: Langfuse (LLM traces) · uptime
                         monitoring · Postgres metrics → monthly client report
```

**Design rules**

1. **One orchestration layer (n8n)** owns business logic, so channels and models can be swapped without rebuilding.
2. **Model-agnostic.** Prompts and tools are defined once and routed to Claude, OpenAI or Gemini according to the task, cost and data-residency needs. No single-vendor dependency.
3. **Separate clients.** Each client gets separate credentials, workflows, knowledge base namespaces and logs. Never mix client data.
4. **Human in the loop by design.** Every assistant has a handover path, plus approval queues for sensitive actions such as refunds, review replies and anything clinical or legal.
5. **Everything is exportable.** Workflows (JSON), prompts and knowledge bases are versioned in Git. Clients can leave with their configuration.

---

## 5.2 Use now (months 0–6)

| Layer | Recommended tool | Why | Indicative cost |
|---|---|---|---|
| **Workflow automation (primary)** | **n8n**: self-hosted Community Edition on a UK or EU VPS, or n8n Cloud Pro | Visual and code-friendly, strong AI and agent nodes, self-hosting keeps data under your control and cost flat per client | Self-host: free software + ~£10–£40/month server. Cloud: Starter ~€20, Pro ~€50/month [S9] |
| Workflow automation (simple clients) | **Make** (or Zapier where the client already uses it) | Quick for simple flows; clients may own the account | Make Core ~$10.59/month for 10k credits [S10] |
| **LLMs** | **Anthropic Claude**, **OpenAI**, **Google Gemini** via API, with a small "router" sub-workflow in n8n | Use small, fast models for FAQs and routing, larger models for reasoning and drafting; diversity reduces outage and pricing risk | Pay per token; most SME assistants cost a few pounds a month [S12] |
| **Voice AI receptionist** | **Retell AI** or **Vapi** (choose one and standardise); UK number via Twilio or the platform's telephony | Mature, low-latency, function calling into n8n, British voices available | ~$0.07–$0.30/min all-in [S11] |
| **WhatsApp** | **Meta WhatsApp Cloud API**, directly or via a Business Solution Provider (e.g. 360dialog, Twilio) | Official API with templates for reminders; per-message pricing since July 2025 [S13] | Meta per-message fees by category + BSP fee (if used) |
| **Web chat widget** | Voiceflow or Botpress (fast builders), or a lightweight custom widget calling n8n | Fast to brand; analytics; human handover | Free to ~$50–$150/month by plan [A: verify] |
| **SMS** | Twilio | Missed-call text-back, reminders | Pay-as-you-go per SMS |
| **Knowledge base / RAG** | **Supabase** (Postgres + pgvector), EU or UK region | One database for knowledge, logs and metrics; row-level security per client | Free tier → ~$25/month Pro [A: verify] |
| **LLM observability** | **Langfuse** (self-hosted or cloud) | Trace every conversation, cost tracking, evaluations, prompt versions | Free self-host / free cloud tier |
| **Uptime and alerting** | Better Stack or UptimeRobot + n8n error workflow → Slack or email | Know about failures before clients do | Free → ~£20/month |
| **Ostler's own CRM** | **HubSpot** (free CRM to start) or Pipedrive | Pipeline, sequences, deal tracking | Free → ~£15–£50/user/month [A] |
| **Proposals and contracts** | PandaDoc, Qwilr, or Google Docs + an e-signature tool | Tracked proposals, e-signature | £0–£40/month |
| **Billing** | **GoCardless** (Direct Debit for monthly fees) + **Stripe** (cards, setup invoices) + **Xero** or FreeAgent | Direct Debit reduces failed payments and churn for UK SMEs | Per-transaction fees; Xero ~£16–£47/month [A] |
| **Scheduling** | Cal.com or Calendly | Discovery call booking | Free → ~£10/month |
| **Workspace** | Google Workspace or Microsoft 365 | Email, documents, shared drives | ~£6–£12/user/month [A] |
| **Knowledge and SOPs** | Notion | Delivery playbooks, client wiki, templates | Free → ~£8/user/month |
| **Security** | 1Password (team vault), enforced MFA everywhere, Cloudflare (DNS, WAF), automated backups | Protects client credentials, which are your biggest risk | ~£4–£8/user/month |
| **Demos** | Demo phone numbers and assistants per niche on the same stack | Live demos close deals | Usage only |

### Why n8n as the core?

- **Data control:** self-hosting in a UK or EU region simplifies UK GDPR conversations, which matters for clinics and law firms.
- **Unit economics:** a flat server cost across many clients, versus per-task pricing that grows with every client.
- **AI-native:** built-in LLM, agent, vector store and tool nodes; easy webhooks for voice platforms.
- **Portability:** workflows export as JSON and can be handed to the client.
- **Trade-off:** you own uptime, patching and backups. Mitigate with managed hosting (Docker on a reputable VPS, automated backups, monitoring), or n8n Cloud until you have 10+ clients. *Check n8n's licence terms (Sustainable Use License) if you ever host n8n as a product for clients to use directly. Running workflows for your clients as a service provider is the common pattern, but confirm your model against the current licence.*

### Model routing guide

| Task | Model class | Notes |
|---|---|---|
| Intent detection, FAQ answers, classification | Small or "mini" models (e.g. Claude Haiku, GPT mini, Gemini Flash) | Cheapest; fast; enough for grounded answers |
| Drafting replies, summarising calls, reviews | Mid-tier models | Better tone and judgement |
| Complex agents, document reasoning, analytics narratives | Frontier models (e.g. Claude Opus or Sonnet, GPT flagship, Gemini Pro) | Use sparingly; cache prompts |
| Voice conversations | The voice platform's recommended low-latency model | Latency matters more than raw capability |

*Ground answers in the client's knowledge base. Instruct the model to say "I'll check with the team" rather than guess. Test against a 30–50 question evaluation set for every client before go-live.*

---

## 5.3 Worked usage-cost example (estimate)

**Growth client: dental practice or restaurant**

| Item | Volume / month | Unit cost (est.) | Monthly |
|---|---|---|---|
| Voice AI minutes | 500 min | ~$0.12/min all-in [S11] | ~$60 ≈ £47 |
| Text conversations (chat + WhatsApp) | 1,500 conversations × ~4k tokens | ~$0.002–$0.005 per conversation on small models [S12] | ~$3–$8 ≈ £2–£6 |
| WhatsApp template messages (reminders) | 600 utility messages | Meta UK utility rate (check rate card) [S13] | ~£5–£15 [A] |
| SMS (missed-call text-back) | 150 | ~£0.04 each [A] | ~£6 |
| Share of n8n server, database, monitoring | — | — | ~£5 |
| **Total usage** | | | **≈ £65–£80** |

At the £495 Growth fee, that leaves headroom for 2.5 hours of support a month at about a 70% gross margin (`blueprint/04` §4.4).

**LLM cost per conversation (method):** cost = (input tokens × input price + output tokens × output price) ÷ 1,000,000. For example, 3,000 input + 500 output tokens on a model priced at $0.75 / $4.50 per million tokens = $0.00225 + $0.00225 = **$0.0045** (under half a penny) [E, S12].

---

## 5.4 Introduce as you grow

| Stage | Trigger | Technology | Why |
|---|---|---|---|
| **Months 6–12** | 10+ clients | Move n8n to queue mode with workers; staging and production environments; Git-based workflow deployment | Reliability and safe changes |
| | Repeated builds | **Template library**: parameterised niche workflows, prompts and eval sets | Cuts setup time, which raises margin |
| | Client reporting load | Automated reporting pipeline (Postgres → Looker Studio or Metabase → PDF and email) | Monthly reports produced without manual effort |
| **Months 12–24** | 30+ clients | **Client portal** (Next.js + Supabase): conversations, approvals, knowledge-base editing, reports | Self-service, stickiness, fewer support tickets |
| | Regulated clients | Formal security programme: Cyber Essentials Plus, ISO 27001 roadmap; UK data residency options | Unlocks healthcare, legal and larger SMEs |
| | Quality at scale | Automated evaluation suites (Langfuse datasets), red-teaming, regression tests on prompt changes | Prevents silent quality decay |
| **Year 2–3** | Proven niche demand | **Proprietary vertical product** (e.g. "Ostler for Restaurants") as a multi-tenant SaaS | Recurring revenue that scales beyond service hours |
| | Data volume | Fine-tuned or distilled small models for high-volume niche tasks; on-premise or private-cloud options | Cost and privacy |

**Avoid early:** building your own voice stack, training models, custom mobile apps, Kubernetes, or any "platform" before 20 clients. All of it is complexity without revenue.

---

## 5.5 Security baseline (non-negotiable from day one)

| Control | Implementation |
|---|---|
| Access | MFA everywhere; 1Password vault; least-privilege API keys scoped per client; no shared logins |
| Data | Encryption in transit (TLS) and at rest; UK or EU regions where available; data minimisation (don't store what you don't need) |
| Retention | Conversation logs kept for 90 days by default (configurable per client); auto-deletion jobs |
| Vendors | Sub-processor register (LLM, voice, messaging, hosting) with DPAs and transfer mechanisms (UK IDTA / UK Addendum / UK–US Data Bridge where applicable) |
| AI safety | Prompt-injection defences (system prompt isolation, tool allow-lists, output validation); no ability for the bot to execute payments or refunds without human approval |
| Monitoring | Error alerts, anomaly alerts (cost spikes, conversation surges), weekly log review |
| Backups | Daily automated backups of n8n and the database, with a monthly restore test |
| Certification | **Cyber Essentials** in the first 90 days [A: fee for micro organisations is a few hundred pounds; check IASME]. Clients and insurers increasingly ask for it. |
| Incident response | One-page incident plan: contain, assess, notify client within 24 hours, notify the ICO within 72 hours if a reportable personal data breach |

---

## 5.6 How success will be measured (technology)

| Metric | Target |
|---|---|
| Assistant uptime | ≥ 99.5% monthly |
| Correct answer rate on client evaluation set before go-live | ≥ 95%; zero critical failures (unsafe, made-up policy, or wrong price) |
| Human-handover success (handover reached a person or a captured message) | 100% |
| Median setup time, Starter | ≤ 10 working days, falling to ≤ 5 by client 10 |
| Usage cost as a share of monthly fee | ≤ 20% |
| Security incidents | Zero reportable breaches; incident drill twice a year |
