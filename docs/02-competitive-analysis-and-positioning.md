# 2. Competitive Analysis and Positioning

Labels: **[Verified]** sourced in [sources.md](sources.md) · **[Estimate]** our judgement · **[Recommendation]** our choice.

> **Limit of this analysis:** public pricing for consultancies is rare. Where pricing is shown it comes from benchmarks, not the firm's own rate card. Before launch, spend one afternoon checking the websites, Clutch profiles and LinkedIn headcounts of the 10–15 nearest competitors in your city and niche. Replace the archetypes below with named firms.

---

## 2.1 Competitor map (archetypes with UK examples)

| Archetype | Examples | Who they serve | Positioning | Pricing (public or benchmark) | Strengths | Weaknesses we exploit |
|---|---|---|---|---|---|---|
| **Global consultancies & integrators** | Accenture (now owns Faculty [Verified]), Deloitte, Capgemini, Kainos | FTSE/enterprise, public sector | Large-scale transformation | Project minimums often £100k+ [Estimate] | Brand, scale, procurement access | Too expensive and slow for 20–500-staff firms. Juniors do the work. |
| **Model-vendor deployment arms** | OpenAI (acquiring Tomoro [Verified]); vendor partner programmes | Enterprise | "Get value from our models" | Not public | Model access, prestige | Tied to one vendor. Enterprise focus. Clients worry about lock-in. |
| **Specialist UK AI/data consultancies** | Mind Foundry, Cambridge Consultants, Oakland, ICS.AI, Peak [Verified that they exist/are listed] | Enterprise, government, defence, specific sectors | Deep data science, decision intelligence, sector platforms | Not public; enterprise-level [Estimate] | Credibility, depth | Not focused on fast LLM/agent implementation for growth companies. |
| **"AI automation agencies"** | Hundreds of small no-code shops (often US-style) | Small businesses, coaches, e-commerce | "Automate your business with AI" | $2k–$15k setup + $500–$1.5k/month [Verified as vendor-blog benchmarks] | Cheap, fast, good marketing | Brittle Zapier/Make chains. No evaluation, security or engineering depth. Overpromise. High churn. |
| **Software dev agencies adding "AI"** | Most UK digital agencies | Existing app clients | "We also do AI" | Day rates ~£500–£900 [Estimate] | Existing relationships, full-stack teams | AI is a sideline. Little eval/RAG/agent depth. **These are our partners, not just competitors.** |
| **Freelancers & fractional AI leads** | Upwork, LinkedIn, Toptal | Startups | Individual expertise | ~£500–£1,000+/day [Verified ranges, weak sources] | Cheap, flexible | Single point of failure. No support or run capability. Can't scale. |
| **Off-the-shelf AI SaaS** | Intercom Fin, Zendesk AI, Glean, Microsoft Copilot | Everyone | "Buy, don't build" | Per seat / per resolution | Fast, cheap to start | Generic. Doesn't fit unusual workflows or proprietary data. **We should recommend these when they fit.** That honesty is part of the brand. |

## 2.2 Where the gap is

Plotting **delivery depth** (prototype → production-grade, measured, maintained) against **accessible price and speed for 20–500-staff companies**:

```
                    Production-grade, measured, maintained
                                   ▲
          Global consultancies     │      ★ OUR POSITION
          Specialist AI firms      │      Senior, vendor-neutral, fixed-price,
          Vendor deployment arms   │      6-week pilots with agreed metrics
                                   │      and a team that runs it afterwards
   Expensive / slow ◄──────────────┼──────────────► Accessible / fast
                                   │
                                   │      AI automation agencies
                                   │      Freelancers
                                   │      Dev agencies "adding AI"
                                   ▼
                       Prototype / demo / brittle
```

**The underserved segment:** growth-stage tech companies and professional firms that need production-grade AI (evaluated, secure, maintained), can't buy Accenture, and have been burned by demos that never shipped. [Estimate, consistent with DSIT skills barrier and MIT integration findings]

## 2.3 Unique Value Proposition

The brief's draft promise:

> "We help technology founders and businesses turn AI opportunities into working products, intelligent systems and measurable business results."

It's directionally right but generic: any competitor could say it. The refined version adds **who**, **how fast**, **what proof** and **what happens after**. [Recommendation]

### Refined UVP

> **We turn one expensive, repetitive workflow into a working AI system in six weeks, with the success metric agreed before we start, an evaluation suite that proves it, and a team that keeps it running afterwards.**

### Short form (website hero)

> **AI that ships. Results you can measure.**

### The five differentiators (each must be provable, not claimed)

| # | Differentiator | How we prove it | Why competitors don't do it |
|---|---|---|---|
| 1 | **Metric-first.** Every engagement starts with a baseline and an agreed acceptance metric | The metric is written into the SOW | Agencies sell features. Big firms sell programmes. |
| 2 | **Evaluation-backed.** We build a test set with the client and report accuracy, failure modes and cost per task before go-live | Client gets the eval report and the harness | Requires engineering discipline most shops lack |
| 3 | **Production, not prototype.** Pilots run on real data, in the client's environment, with monitoring, guardrails and human review | Live system at week 6 | No-code agencies stop at demos |
| 4 | **Vendor-neutral.** We pick models and tools on cost, security and fit, and we recommend off-the-shelf SaaS when it beats a custom build | Written build-vs-buy recommendation in every Sprint | Vendor arms and partner-incentivised firms can't be neutral |
| 5 | **We stay.** Every build comes with a "Run" plan (monitoring, evals, prompt and model updates, cost optimisation) | Retainer SLA | Freelancers and project shops leave after handover |

### Risk reversal: the "Acceptance Guarantee" [Recommendation]

For Production Pilots: *"If the system doesn't meet the acceptance metric we agreed on the evaluation set we built together, we keep working at no extra charge for up to two more weeks. If it still doesn't, you don't pay the final milestone."*

- It's credible because the metric is measured on a **co-created test set**, not open-ended business outcomes we don't control.
- It's affordable because the Sprint de-risks feasibility first. We only offer it on scoped Pilots after a Sprint or equivalent discovery.
- Exposure is capped at roughly 2 weeks' delivery cost plus the final milestone (typically 30–40% of the fee).

### Positioning statement (internal)

> For **UK technology companies and growing professional firms** that have experimented with AI but haven't got it into production, **[Company]** is the **implementation-focused AI consultancy** that delivers **working, measured AI systems in weeks**. Unlike **large consultancies**, we're senior, fast and affordable. Unlike **automation agencies and freelancers**, we build production-grade systems with evaluation, security and ongoing support.

## 2.4 What we will NOT compete on

- **Lowest price.** We'll lose to no-code agencies and offshore shops, and that's fine.
- **Enterprise-scale transformation programmes** in year one.
- **Frontier research or training foundation models.**
- **Hype.** No "10x your business with AI agents" claims. The brand's credibility is the asset.
