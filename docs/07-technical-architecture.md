# 7. Delivery and Technical Architecture

Labels: **[Recommendation]** throughout unless stated. Tool capabilities and regional availability change often, so **re-check provider docs at the start of each engagement**.

---

## 7.1 Principles for choosing technology

1. **Simplest thing that meets the acceptance metric.** A well-prompted single model call beats an agent. A single agent with good tools beats a multi-agent system. Add complexity only when evals prove it's needed.
2. **The client owns it.** Code in the client's repository, infrastructure in the client's cloud and API accounts where possible. No black boxes, no lock-in.
3. **Model-agnostic by design.** A thin internal interface over model providers, so we can switch models on cost, quality or data-residency grounds without rewriting the app.
4. **Evaluation is part of the product.** Every system ships with a test set, an eval harness and tracing.
5. **Boring infrastructure.** PostgreSQL, Docker, managed cloud services. Innovation goes into the AI layer, not the plumbing.
6. **Standard stack, few exceptions.** Fewer tools means faster delivery, easier maintenance under Run retainers and easier hiring.

## 7.2 The default stack and when to deviate

| Layer | Default choice | Use when | Avoid / alternative when |
|---|---|---|---|
| **LLM providers** | **Anthropic Claude API** and **OpenAI API** as primary options, chosen per use case on eval results | Most text, reasoning, extraction, coding and agent workloads | Strict data residency or enterprise cloud commitments → the same model families through **AWS Bedrock, Azure OpenAI or Google Vertex AI** in the client's cloud and region (check regional model availability). Very high volume or simple tasks → smaller/cheaper model tiers or open-weight models |
| **Backend / AI services** | **Python** (FastAPI) | AI pipelines, retrieval, agents, evals, data work: the strongest AI ecosystem | Client is a TypeScript-only shop and the AI layer is thin → TypeScript (Node) with provider SDKs |
| **Frontend / apps** | **TypeScript + React / Next.js** | Admin UIs, review queues, copilots, MVPs | Client has an existing frontend → integrate via API instead |
| **Agent orchestration** | **Provider SDKs with plain code first** (tool-use loop, structured outputs) | Most agents: easier to debug, fewer dependencies | **LangGraph** when you need durable, stateful, multi-step workflows with branching, retries and human-in-the-loop checkpoints |
| **Retrieval / ingestion** | Own pipeline on PostgreSQL + **pgvector**, hybrid search (vector + full-text), a reranker | Most RAG systems up to millions of chunks | **LlamaIndex** for complex, varied document ingestion and parsing (many file types, connectors) where it saves real time. A dedicated vector DB only at large scale or with specific latency needs |
| **Database** | **PostgreSQL** | Everything: app data, vectors, logs, eval results | n/a |
| **Managed Postgres / backend-as-a-service** | **Supabase** for Starter/MVP clients (auth, storage, Postgres, pgvector out of the box) | Speed for startups and MVPs | Enterprise/regulated → managed Postgres in the client's cloud (AWS RDS / Azure / GCP Cloud SQL) |
| **Workflow automation** | **n8n** (self-hostable) | Business-system glue: CRMs, email, spreadsheets, webhooks. Self-hosting keeps data in the client's environment | **Zapier** only if the client already runs on it and volumes are low. **Make** for clients already using it. Neither for complex, high-volume or sensitive flows → write code |
| **Containers & deploy** | **Docker**, deployed to the client's cloud (AWS/Azure/GCP) or a simple PaaS for startups (e.g. Render, Fly.io, Vercel for frontends) | All services | n/a |
| **Infrastructure as code** | **Terraform** (or the cloud's native tool if the client standardises on it) | Growth/Enterprise deployments | Starter builds on PaaS can skip it |
| **Observability & tracing** | **Langfuse** (self-hostable, open source) for LLM traces, cost and eval scores. Cloud-native logging for infra | Every production system | Client already uses Datadog etc. → integrate with it |
| **Evaluation** | Our eval harness (pytest-style) + **promptfoo** or Langfuse evals; LLM-as-judge **calibrated against human labels** | Every system | n/a |
| **Secrets & auth** | Cloud secrets manager; SSO (OIDC/SAML) for enterprise | Always | Never secrets in code or n8n plain fields |
| **CI/CD** | GitHub Actions (or the client's CI): tests + eval regression suite on every change | Always | n/a |

### What we deliberately don't do by default
- Fine-tuning models: only when evals show prompting + retrieval can't reach the target, and there's enough quality data.
- Training custom ML models: only for clear tabular/forecasting problems, via specialist contractors.
- Multi-agent frameworks for problems a single agent can solve.
- Building on no-code tools for anything business-critical or sensitive.

## 7.3 Reference architecture (Production Pilot)

```
 ┌─────────────── Client environment (their cloud / their API accounts) ────────────────┐
 │                                                                                        │
 │  Sources                Ingestion              Knowledge            AI Service         │
 │  ─────────             ─────────              ─────────            ──────────          │
 │  Help desk  ─┐        ┌──────────┐          ┌──────────────┐     ┌─────────────────┐   │
 │  Docs/Drive ─┼──────► │ Parse,   │ ───────► │ PostgreSQL   │ ◄── │ Retrieval       │   │
 │  CRM / DB   ─┤        │ clean,   │          │ + pgvector   │     │ + rerank        │   │
 │  Email      ─┘        │ PII scrub│          │ + full-text  │     ├─────────────────┤   │
 │                       └──────────┘          └──────────────┘     │ Agent / LLM     │   │
 │                                                                  │ orchestration   │──►│── Model provider API
 │  Users / systems                                                 │ (tools, guards) │   │   (Claude / OpenAI /
 │  ──────────────                                                  ├─────────────────┤   │    Bedrock / Azure)
 │  Web app / Slack / ───► API gateway (auth, rate limits) ───────► │ Guardrails:     │   │
 │  Help desk / CRM                                                 │ input/output    │   │
 │        ▲                                                         │ checks, PII,    │   │
 │        │            ┌──────────────────────┐                     │ policy rules    │   │
 │        └────────────│ Human review queue   │ ◄── low confidence ─┴─────────────────┘   │
 │                     │ (approve/edit/reject)│                              │            │
 │                     └──────────────────────┘                              ▼            │
 │                                                       Tracing, cost, eval scores       │
 │                                                       (Langfuse) → dashboards, alerts  │
 └────────────────────────────────────────────────────────────────────────────────────────┘
```

## 7.4 The reusable Delivery Kit (our compounding advantage)

Build these during the first 60 days (the demo projects double as the first version) and improve them on every engagement. They're **our pre-existing IP**: clients get a perpetual licence to use them inside their delivered system (see contracts in [10-trust-security-compliance.md](10-trust-security-compliance.md)).

| Component | What it does | Saves |
|---|---|---|
| **Project template repo** | FastAPI + Next.js skeleton, Docker, CI, linting, config, secrets handling | 2–3 days per project |
| **Model gateway** | Provider-agnostic interface, retries, fallbacks, cost logging, model routing | 1–2 days; makes model migrations cheap (good for Run margins) |
| **RAG starter** | Ingestion, chunking, hybrid search, reranking, citations | 3–5 days |
| **Agent starter** | Tool-use loop, permission model, human-approval step, tracing | 3–5 days |
| **Eval harness** | Test-set format, metrics (accuracy, faithfulness, task success, cost, latency), LLM-judge calibration, HTML report | 2–4 days; core of the Acceptance Guarantee |
| **Guardrails pack** | PII detection/redaction, prompt-injection checks for tool-using agents, output validation | 1–2 days; reduces risk |
| **Review-queue UI** | Approve/edit/reject interface feeding back into eval sets | 2–3 days |
| **Value dashboard** | Baseline vs current metrics, cost per task: the screen we show in Run reviews | 1–2 days; sells renewals |
| **Documentation templates** | Architecture doc, runbook, data-flow diagram, model card, DPIA input | 1–2 days |
| **n8n node library** | Tested nodes for common CRMs, help desks, email | Variable |

**Target:** by month 6, a Growth Production Pilot needs ~30–40% fewer engineering days than the first one did. Because pricing is fixed, that efficiency becomes margin. [Estimate]

## 7.5 Development process

| Week | Pilot phase | Key outputs |
|---|---|---|
| 0 | **Mobilise** | Access granted, data-processing terms signed, baseline metrics captured, test set started with client SMEs |
| 1 | **Spike** | End-to-end thin slice on real data; first eval run; risks surfaced early |
| 2–3 | **Build** | Integrations, retrieval/agent logic, guardrails, review queue; eval scores tracked per iteration |
| 4 | **Harden** | Security review, load/cost testing, failure handling, monitoring, runbook |
| 5 | **Shadow / draft mode** | Runs on live traffic with humans approving every output; compare against baseline |
| 6 | **Go-live & acceptance** | Acceptance metric measured on agreed eval set; go/no-go; handover; Run starts |

**Weekly rhythm:** Monday plan · Thursday client demo (always show working software + current eval score) · Friday written status (progress, eval trend, risks, decisions needed).

## 7.6 Testing and quality procedures

| Test type | Standard |
|---|---|
| Unit & integration tests | Required for all non-trivial code; run in CI |
| **Eval suite** | Minimum 50–200 labelled cases per use case (more for high-stakes), covering typical, edge and adversarial inputs; built with client SMEs |
| Regression evals | Run on every prompt, model or retrieval change; merge blocked on regression beyond agreed tolerance |
| LLM-as-judge | Allowed only after agreement with human labels is checked on a sample |
| Security tests | Prompt-injection and data-exfiltration tests for any agent with tools; least-privilege API keys; dependency scanning |
| Cost & latency tests | Projected monthly cost at expected volume, signed off by client before go-live |
| User acceptance | Client SMEs review a sample of outputs in shadow mode |

## 7.7 Documentation standards (every delivery)

1. **README**: what it does, how to run it, how to deploy.
2. **Architecture document** with data-flow diagram (which data goes to which provider, where it's stored, retention).
3. **Runbook**: monitoring, common failures, escalation, how to roll back a prompt or model.
4. **Model & prompt register**: versions, purpose, eval scores, change history.
5. **Eval report** at acceptance (scores, known failure modes, limitations).
6. **Handover recording** (30–60 minutes walkthrough).
7. **DPIA input pack** for the client's data-protection lead.

## 7.8 Our own internal stack (lean)

| Need | Tool type |
|---|---|
| Email, docs, calendar | Google Workspace or Microsoft 365 |
| CRM & sequences | HubSpot (free/starter) or Attio / Pipedrive |
| Prospect data | Sales Navigator + one data tool (e.g. Apollo) |
| Proposals & e-signature | Template docs + e-signature tool |
| Projects | Linear or Notion |
| Finance | Xero or FreeAgent + an accountant |
| Code | GitHub (organisation per client, or client's own) |
| Password manager | 1Password or Bitwarden (business), with MFA everywhere |
| Internal AI | Our own research agent, proposal-drafting assistant and meeting summariser: built on our stack and used as demos |
