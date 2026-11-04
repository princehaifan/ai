"""
12-month financial model for the consultancy (three scenarios).

Every number in this file is an ASSUMPTION or a PROPOSED PRICE, not market data.
Change the inputs and re-run:

    python3 financials/model.py

The output tables are pasted into docs/09-financial-projections.md.

Deliberate simplifications (stated so nobody is misled):
- Revenue is recognised when work is delivered, not when cash arrives.
  Builds/MVPs are split 50% in the month signed and 50% the following month.
- Fixed-price work is assumed to land on budget. Overruns come out of gross margin.
- Hire costs are added to operating costs while project COGS still assume
  contractors. That double-counts some delivery cost, which keeps the model
  on the cautious side.
- No corporation tax, VAT or dividend tax is modelled. All figures GBP ex VAT.
"""

MONTHS = 12

# ---- Proposed average prices (see docs/03-business-model-and-pricing.md) ----
PRICE = {
    "sprint": 5_000,      # AI Opportunity Sprint (blend of £3.5k and £7.5k tiers)
    "build": 18_000,      # Production Pilot / automation build (blend of tiers)
    "mvp": 40_000,        # AI MVP / product build
    "workshop": 3_000,    # half/full-day workshop blend
}
MANAGED_AVG_MRR = 1_800      # blended "Run" managed-service retainer per client per month
FRACTIONAL_MRR = 3_000       # fractional Head of AI retainer per client per month
RETAINER_CHURN = 0.03        # monthly logo churn across retainers

# ---- Direct delivery cost as a share of revenue (contractors, infra, LLM usage) ----
COGS = {
    "sprint": 0.15,       # mostly founder-delivered
    "build": 0.45,        # contractor engineers at ~£450-£650/day
    "mvp": 0.50,
    "workshop": 0.10,
    "managed": 0.30,      # monitoring tooling + contractor support hours
    "fractional": 0.05,
}

# ---- Founder days used per unit (capacity check) ----
FOUNDER_DAYS = {
    "sprint": 5, "build": 8, "mvp": 14, "workshop": 2,
    "managed": 0.75,      # per retainer client per month
    "fractional": 3,      # per fractional client per month
}
FOUNDER_BASELINE_DAYS = 7    # sales, marketing, admin every month
FOUNDER_CAPACITY = 18        # realistic billable+non-billable days in a month

# ---- Fixed operating costs (estimates; replace with real quotes) ----
FIXED_MONTHLY = {
    "software & tools": 450,          # workspace, CRM, outreach data, GitHub, hosting, dev LLM credits
    "insurance (PI + cyber)": 180,
    "accountant & bookkeeping": 150,
    "misc (phone, travel, events)": 250,
}
ONE_OFF = {1: 2_500 + 2_000}          # month 1: legal templates (MSA/SOW/DPA) + brand/website

# ---- Scenarios: deals signed per month (index 0 = month 1) ----
SCENARIOS = {
    "Conservative": {
        "story": "First paid work in month 3, slow referrals, no product builds, no hires.",
        "sprint":     [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
        "build":      [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        "mvp":        [0] * 12,
        "workshop":   [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        "fractional": [0] * 12,                      # new fractional clients signed
        "managed_conversion": 0.6,                   # share of builds/MVPs that take a Run retainer
        "founder_pay": [0, 0, 0, 0, 1_500, 1_500, 1_500, 1_500, 2_000, 2_000, 2_000, 2_000],
        "marketing":  [300] * 12,
        "hire_cost":  [0] * 12,                      # contract/salaried delivery capacity, per month
        "hire_days":  [0] * 12,                      # founder days that capacity absorbs
    },
    "Realistic": {
        "story": "About one sprint a month from month 3, ~45% of sprints become builds, "
                 "two fractional retainers, part-time contract delivery lead from month 7.",
        "sprint":     [0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
        "build":      [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        "mvp":        [0] * 12,
        "workshop":   [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
        "fractional": [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        "managed_conversion": 0.7,
        "founder_pay": [0, 0, 0, 2_500, 2_500, 2_500, 3_000, 3_000, 3_000, 3_500, 3_500, 3_500],
        "marketing":  [400] * 6 + [600] * 6,
        # Contract delivery lead ~2 days/week at ~£550/day
        "hire_cost":  [0] * 6 + [4_800] * 6,
        "hire_days":  [0] * 6 + [8] * 6,
    },
    "Ambitious": {
        "story": "Strong network and a working agency-partner channel by month 4; "
                 "contract delivery lead from month 4, first salaried senior engineer in month 6.",
        "sprint":     [0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3],
        "build":      [0, 0, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2],
        "mvp":        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        "workshop":   [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        "fractional": [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        "managed_conversion": 0.8,
        "founder_pay": [0, 0, 3_000, 3_000, 3_500, 3_500, 4_000, 4_000, 4_500, 4_500, 4_500, 4_500],
        "marketing":  [500] * 4 + [900] * 8,
        # From month 4: contract delivery lead 3 days/wk (~£7.2k). From month 6 add a salaried
        # senior AI engineer at ~£75k + employer NI + pension (~£7.5k/month loaded).
        "hire_cost":  [0] * 3 + [7_200] * 2 + [14_700] * 7,
        "hire_days":  [0] * 3 + [13] * 2 + [30] * 7,
    },
}


def run(s):
    rows = []
    managed_clients = 0.0
    fractional_clients = 0.0
    carry_project = 0.0
    carry_project_cogs = 0.0
    cum = 0.0
    for m in range(MONTHS):
        prev = lambda k: s[k][m - 1] if m else 0

        sprint = s["sprint"][m] * PRICE["sprint"]
        workshop = s["workshop"][m] * PRICE["workshop"]

        build_half = 0.5 * s["build"][m] * PRICE["build"]
        mvp_half = 0.5 * s["mvp"][m] * PRICE["mvp"]
        project_rev = build_half + mvp_half + carry_project
        project_cogs = (build_half * COGS["build"] + mvp_half * COGS["mvp"]) + carry_project_cogs
        carry_project = build_half + mvp_half
        carry_project_cogs = build_half * COGS["build"] + mvp_half * COGS["mvp"]

        # Run retainers start the month after a build/MVP completes (2 months after signing).
        new_managed = (s["build"][m - 2] + s["mvp"][m - 2]) * s["managed_conversion"] if m >= 2 else 0
        managed_clients = managed_clients * (1 - RETAINER_CHURN) + new_managed
        fractional_clients = fractional_clients * (1 - RETAINER_CHURN) + s["fractional"][m]
        managed = managed_clients * MANAGED_AVG_MRR
        fractional = fractional_clients * FRACTIONAL_MRR
        mrr = managed + fractional

        revenue = sprint + workshop + project_rev + mrr
        cogs = (sprint * COGS["sprint"] + workshop * COGS["workshop"] + project_cogs
                + managed * COGS["managed"] + fractional * COGS["fractional"])
        gross = revenue - cogs
        opex = (sum(FIXED_MONTHLY.values()) + s["marketing"][m]
                + ONE_OFF.get(m + 1, 0) + s["hire_cost"][m])
        pre_founder = gross - opex
        profit = pre_founder - s["founder_pay"][m]
        cum += profit

        days = (FOUNDER_BASELINE_DAYS
                + s["sprint"][m] * FOUNDER_DAYS["sprint"]
                + s["workshop"][m] * FOUNDER_DAYS["workshop"]
                + 0.5 * FOUNDER_DAYS["build"] * (s["build"][m] + prev("build"))
                + 0.5 * FOUNDER_DAYS["mvp"] * (s["mvp"][m] + prev("mvp"))
                + managed_clients * FOUNDER_DAYS["managed"]
                + fractional_clients * FOUNDER_DAYS["fractional"]
                - s["hire_days"][m])
        days = max(days, FOUNDER_BASELINE_DAYS)

        rows.append(dict(month=m + 1, revenue=revenue, mrr=mrr, gross=gross, opex=opex,
                         pre=pre_founder, founder=s["founder_pay"][m], profit=profit,
                         cum=cum, retainers=managed_clients + fractional_clients,
                         load=days / FOUNDER_CAPACITY))
    return rows


def fmt(x):
    return f"£{x:,.0f}" if x >= 0 else f"-£{-x:,.0f}"


def main():
    summary = []
    for name, s in SCENARIOS.items():
        rows = run(s)
        print(f"\n### {name} scenario\n")
        print(f"_{s['story']}_\n")
        print("| Month | Revenue | Recurring (MRR) | Gross profit | Operating costs | "
              "Profit before founder pay | Founder pay | Net profit | Cumulative | Founder load |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            print(f"| {r['month']} | {fmt(r['revenue'])} | {fmt(r['mrr'])} | {fmt(r['gross'])} | "
                  f"{fmt(r['opex'])} | {fmt(r['pre'])} | {fmt(r['founder'])} | {fmt(r['profit'])} | "
                  f"{fmt(r['cum'])} | {r['load']:.0%} |")
        rev = sum(r["revenue"] for r in rows)
        gp = sum(r["gross"] for r in rows)
        net = sum(r["profit"] for r in rows)
        low = min(r["cum"] for r in rows)
        first_profit = next((r["month"] for r in rows if r["profit"] > 0), None)
        cum_be = next((r["month"] for r in rows if r["cum"] > 0), None)
        engagements = sum(sum(s[k]) for k in ("sprint", "build", "mvp", "workshop", "fractional"))
        peak = max(r["load"] for r in rows)
        summary.append((name, rev, gp / rev, rows[-1]["mrr"], rows[-1]["retainers"], net,
                        -low if low < 0 else 0, first_profit, cum_be, engagements, peak))

    print("\n### Summary\n")
    print("| Scenario | Year-1 revenue | Gross margin | Month-12 MRR | Retainer clients (m12) | "
          "Year-1 net profit after founder pay | Peak cash needed | First profitable month | "
          "Cumulative break-even month | Paid engagements | Peak founder load |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for (n, rev, gm, mrr, cl, net, cash, fp, be, eng, peak) in summary:
        print(f"| {n} | {fmt(rev)} | {gm:.0%} | {fmt(mrr)} | {cl:.1f} | {fmt(net)} | {fmt(cash)} | "
              f"{fp} | {be} | {eng} | {peak:.0%} |")


if __name__ == "__main__":
    main()
