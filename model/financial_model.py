"""
24-month financial model for a lean UK AI consultancy serving local businesses.

Every input below is an ASSUMPTION unless its comment says otherwise. Change the
inputs, re-run, and the outputs (Markdown + CSV) regenerate:

    python3 model/financial_model.py

Outputs:
    model/outputs/financial_model_outputs.md
    model/outputs/<scenario>_monthly.csv

Client counts are expected values (fractions allowed) so the curves stay smooth;
read "7.4 active clients" as "about 7".
"""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass, field

MONTHS = 24
OUT_DIR = os.path.join(os.path.dirname(__file__), "outputs")

# --------------------------------------------------------------------------
# Package economics (per client).  Prices sit inside the UK market ranges
# cited in blueprint/02 and blueprint/04; they are our proposed list prices.
# --------------------------------------------------------------------------
PACKAGES = {
    #              setup fee  monthly fee  monthly direct cost  setup delivery cost
    "Starter":        dict(setup=950,   mrr=195,  cogs=55,  setup_cost=250),
    "Growth":         dict(setup=3500,  mrr=495,  cogs=150, setup_cost=1000),
    "Transformation": dict(setup=12000, mrr=1500, cogs=450, setup_cost=4500),
}
# cogs = platform/LLM/telephony/messaging usage + support & monitoring time
# setup_cost = contractor time, tools and usage during the build (founder time excluded
#              until delivery staff are hired; their salary then sits in fixed costs)


@dataclass
class Scenario:
    name: str
    first_month_clients: float      # new clients won in month 1 (expected value)
    monthly_ramp: float             # extra new clients per month, each month
    max_new_per_month: float        # sales-capacity ceiling before extra hires
    mix: dict                       # share of new clients by package
    monthly_churn: float            # share of active recurring clients lost per month
    paid_assessments_per_client: float  # paid assessments sold per new client won
    training_rev_per_month: list = field(default_factory=list)  # (from_month, £/month)
    founder_draw: float = 2000      # monthly founder salary/drawings
    marketing_base: float = 600     # monthly paid marketing, events, print, lead data, demo usage
    marketing_per_new_client: float = 300  # incremental acquisition spend per client won (ads, travel, referral fees)


SCENARIOS = [
    Scenario(
        name="Conservative",
        first_month_clients=0.0,
        monthly_ramp=0.12,
        max_new_per_month=2.5,
        mix={"Starter": 0.70, "Growth": 0.27, "Transformation": 0.03},
        monthly_churn=0.05,
        paid_assessments_per_client=0.5,
        training_rev_per_month=[(4, 400), (12, 900)],
        founder_draw=1500,
    ),
    Scenario(
        name="Realistic",
        first_month_clients=0.0,
        monthly_ramp=0.25,
        max_new_per_month=4.0,
        mix={"Starter": 0.60, "Growth": 0.33, "Transformation": 0.07},
        monthly_churn=0.03,
        paid_assessments_per_client=0.6,
        training_rev_per_month=[(3, 700), (9, 1500), (16, 2500)],
        founder_draw=2000,
    ),
    Scenario(
        name="Optimistic",
        first_month_clients=0.5,
        monthly_ramp=0.35,
        max_new_per_month=7.0,
        mix={"Starter": 0.50, "Growth": 0.40, "Transformation": 0.10},
        monthly_churn=0.025,
        paid_assessments_per_client=0.7,
        training_rev_per_month=[(2, 1000), (7, 2500), (13, 4000)],
        founder_draw=2500,
    ),
]

# Pilot pricing: the first clients get 50% off setup in exchange for a case study and testimonial
PILOT_CLIENTS = 3
PILOT_SETUP_DISCOUNT = 0.5

# Founder selling time per client won (prospecting, visits, demo, proposal), valued at an
# opportunity cost.  Used only for the "fully loaded" CAC line, not for cash flow.
FOUNDER_SALES_HOURS_PER_WIN = 18
FOUNDER_HOURLY_VALUE = 45

ASSESSMENT_PRICE = 495          # paid AI Readiness Assessment (credited if they buy)
ASSESSMENT_CREDIT_RATE = 0.6    # share of paid assessments that convert and are credited
TRAINING_COGS = 0.15            # materials, venue, travel as share of training revenue

# One-off startup costs (estimates; see blueprint/06 for the line items)
STARTUP_COSTS = 5200

# Fixed monthly overheads that exist from month 1 (estimates)
BASE_OVERHEADS = {
    "Software & tools (internal)": 250,
    "Insurance (PI, cyber, PL) monthly equivalent": 110,
    "Accountant & bookkeeping": 120,
    "Phone, broadband share, travel": 200,
    "Demo environments & sandbox usage": 80,
}

# Hires: triggered by load, not by calendar.  Monthly cost includes employer
# NI, pension and equipment, rounded up.  Salaries are assumptions to validate
# against local job adverts.
HIRES = [
    # (role, trigger type, threshold, monthly fully loaded cost)
    ("Automation engineer / delivery specialist", "active_clients", 18, 3600),
    ("Client success & sales executive",            "mrr",           12000, 3300),
    ("Second automation engineer",                  "active_clients", 45, 3800),
]


def training_for(s: Scenario, month: int) -> float:
    rev = 0.0
    for start, amount in s.training_rev_per_month:
        if month >= start:
            rev = amount
    return rev


def run(s: Scenario) -> list[dict]:
    active = {k: 0.0 for k in PACKAGES}
    hired: dict[str, int] = {}
    rows = []
    cumulative_cash = -STARTUP_COSTS
    won_so_far = 0.0
    for m in range(1, MONTHS + 1):
        new_total = min(s.first_month_clients + s.monthly_ramp * (m - 1), s.max_new_per_month)
        new = {k: new_total * s.mix[k] for k in PACKAGES}

        # churn applies to the base carried in from last month
        churned = {k: active[k] * s.monthly_churn for k in PACKAGES}
        for k in PACKAGES:
            active[k] = active[k] - churned[k] + new[k]

        active_total = sum(active.values())
        mrr = sum(active[k] * PACKAGES[k]["mrr"] for k in PACKAGES)
        setup_rev = sum(new[k] * PACKAGES[k]["setup"] for k in PACKAGES)
        # pilot discount on the first PILOT_CLIENTS wins
        pilots_this_month = max(0.0, min(new_total, PILOT_CLIENTS - won_so_far))
        if new_total:
            setup_rev -= setup_rev * (pilots_this_month / new_total) * PILOT_SETUP_DISCOUNT
        won_so_far += new_total

        assessments = new_total * s.paid_assessments_per_client
        # credited assessments are netted off the setup fee, so only the uncredited share is extra
        assessment_rev = assessments * ASSESSMENT_PRICE * (1 - ASSESSMENT_CREDIT_RATE)
        training_rev = training_for(s, m)

        revenue = mrr + setup_rev + assessment_rev + training_rev

        recurring_cogs = sum(active[k] * PACKAGES[k]["cogs"] for k in PACKAGES)
        setup_cogs = sum(new[k] * PACKAGES[k]["setup_cost"] for k in PACKAGES)
        training_cogs = training_rev * TRAINING_COGS
        cogs = recurring_cogs + setup_cogs + training_cogs
        gross_profit = revenue - cogs

        # hires: once triggered, they stay
        for role, trigger, threshold, cost in HIRES:
            if role in hired:
                continue
            metric = active_total if trigger == "active_clients" else mrr
            if metric >= threshold:
                hired[role] = m
        staff_cost = sum(cost for role, _, _, cost in HIRES if role in hired)

        marketing = s.marketing_base + s.marketing_per_new_client * new_total
        overheads = sum(BASE_OVERHEADS.values()) + 0.02 * revenue  # 2% payment fees etc.
        opex = s.founder_draw + staff_cost + marketing + overheads
        operating_profit = gross_profit - opex
        cumulative_cash += operating_profit

        rows.append(dict(
            month=m,
            new_clients=new_total,
            active_clients=active_total,
            active_starter=active["Starter"],
            active_growth=active["Growth"],
            active_transformation=active["Transformation"],
            mrr=mrr,
            setup_revenue=setup_rev,
            assessment_revenue=assessment_rev,
            training_revenue=training_rev,
            total_revenue=revenue,
            cogs=cogs,
            gross_profit=gross_profit,
            gross_margin=(gross_profit / revenue) if revenue else 0.0,
            recurring_gross_margin=((mrr - recurring_cogs) / mrr) if mrr else 0.0,
            founder_draw=s.founder_draw,
            staff_cost=staff_cost,
            marketing=marketing,
            overheads=overheads,
            operating_profit=operating_profit,
            cumulative_cash=cumulative_cash,
            headcount=1 + len(hired),
        ))
    return rows, hired


def unit_economics(s: Scenario, rows: list[dict], hired: dict) -> dict:
    arpa = sum(s.mix[k] * PACKAGES[k]["mrr"] for k in PACKAGES)
    margin = sum(s.mix[k] * (PACKAGES[k]["mrr"] - PACKAGES[k]["cogs"]) for k in PACKAGES)
    setup_gp = sum(s.mix[k] * (PACKAGES[k]["setup"] - PACKAGES[k]["setup_cost"]) for k in PACKAGES)
    lifetime_months = 1 / s.monthly_churn
    ltv = margin * lifetime_months + setup_gp
    total_new = sum(r["new_clients"] for r in rows)
    total_marketing = sum(r["marketing"] for r in rows)
    cac_cash = total_marketing / total_new if total_new else float("nan")
    # loaded CAC: also charge half of the client-success/sales hire to acquisition
    sales_role = "Client success & sales executive"
    sales_cost = 0.0
    if sales_role in hired:
        cost = next(c for r, _, _, c in HIRES if r == sales_role)
        sales_cost = cost * 0.5 * (MONTHS - hired[sales_role] + 1)
    founder_time = FOUNDER_SALES_HOURS_PER_WIN * FOUNDER_HOURLY_VALUE * total_new
    cac_loaded = (total_marketing + sales_cost + founder_time) / total_new if total_new else float("nan")
    payback = cac_loaded / margin if margin else float("nan")
    return dict(arpa=arpa, monthly_margin=margin, setup_gp=setup_gp,
                lifetime_months=lifetime_months, ltv=ltv, cac_cash=cac_cash,
                cac_loaded=cac_loaded, ltv_cac=ltv / cac_loaded if cac_loaded else float("nan"),
                payback_months=payback)


def gbp(x: float) -> str:
    sign = "-" if x < 0 else ""
    return f"{sign}£{abs(x):,.0f}"


def first_month(rows, pred):
    for r in rows:
        if pred(r):
            return r["month"]
    return None


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    md = ["# Financial model outputs",
          "",
          "_Generated by `model/financial_model.py`. Do not edit by hand: change the inputs and re-run._",
          "",
          "All figures are **modelled estimates built on stated assumptions**, not forecasts or promises. "
          "Prices exclude VAT. Client counts are expected values.",
          ""]

    summary_rows = []
    for s in SCENARIOS:
        rows, hired = run(s)
        ue = unit_economics(s, rows, hired)

        with open(os.path.join(OUT_DIR, f"{s.name.lower()}_monthly.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            for r in rows:
                w.writerow({k: (round(v, 2) if isinstance(v, float) else v) for k, v in r.items()})

        y1 = rows[:12]
        y2 = rows[12:]
        be = first_month(rows, lambda r: r["operating_profit"] >= 0)
        # sustained break-even: profitable this month and every later month
        sustained = None
        for i, r in enumerate(rows):
            if all(x["operating_profit"] >= 0 for x in rows[i:]):
                sustained = r["month"]
                break
        payback_cash = first_month(rows, lambda r: r["cumulative_cash"] >= 0)
        low_cash = min(r["cumulative_cash"] for r in rows)

        summary_rows.append(dict(
            name=s.name,
            m6_mrr=rows[5]["mrr"], m12_mrr=rows[11]["mrr"], m24_mrr=rows[23]["mrr"],
            m12_clients=rows[11]["active_clients"], m24_clients=rows[23]["active_clients"],
            y1_rev=sum(r["total_revenue"] for r in y1), y2_rev=sum(r["total_revenue"] for r in y2),
            y1_op=sum(r["operating_profit"] for r in y1), y2_op=sum(r["operating_profit"] for r in y2),
            gm_y2=sum(r["gross_profit"] for r in y2) / sum(r["total_revenue"] for r in y2),
            rgm=rows[23]["recurring_gross_margin"],
            be=sustained, be_first=be, payback=payback_cash, low_cash=low_cash,
            headcount=rows[23]["headcount"], ue=ue, hired=hired,
        ))

        md += [f"## {s.name} scenario", "",
               f"- New clients/month: starts at {s.first_month_clients:g}, +{s.monthly_ramp:g} each month, capped at {s.max_new_per_month:g}",
               f"- Package mix (Starter / Growth / Transformation): "
               f"{s.mix['Starter']:.0%} / {s.mix['Growth']:.0%} / {s.mix['Transformation']:.0%}",
               f"- Monthly churn of recurring clients: {s.monthly_churn:.0%}",
               f"- Founder draw: {gbp(s.founder_draw)}/month",
               "",
               "| Month | New | Active | MRR | Revenue | Gross profit | Operating profit | Cumulative cash | Headcount |",
               "|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for r in rows:
            if r["month"] in (1, 2, 3, 4, 5, 6, 9, 12, 15, 18, 21, 24):
                md.append(f"| {r['month']} | {r['new_clients']:.1f} | {r['active_clients']:.1f} | {gbp(r['mrr'])} | "
                          f"{gbp(r['total_revenue'])} | {gbp(r['gross_profit'])} | {gbp(r['operating_profit'])} | "
                          f"{gbp(r['cumulative_cash'])} | {r['headcount']} |")
        md += ["", "Hires triggered: " + (", ".join(f"{k} (month {v})" for k, v in hired.items()) or "none"), ""]

    md += ["## Scenario comparison", "",
           "| Metric | " + " | ".join(r["name"] for r in summary_rows) + " |",
           "|---|" + "---:|" * len(summary_rows)]

    def line(label, fn):
        md.append(f"| {label} | " + " | ".join(fn(r) for r in summary_rows) + " |")

    line("MRR at month 6", lambda r: gbp(r["m6_mrr"]))
    line("MRR at month 12", lambda r: gbp(r["m12_mrr"]))
    line("MRR at month 24", lambda r: gbp(r["m24_mrr"]))
    line("Active recurring clients, month 12", lambda r: f"{r['m12_clients']:.0f}")
    line("Active recurring clients, month 24", lambda r: f"{r['m24_clients']:.0f}")
    line("Year 1 revenue", lambda r: gbp(r["y1_rev"]))
    line("Year 2 revenue", lambda r: gbp(r["y2_rev"]))
    line("Year 1 operating profit (after founder draw)", lambda r: gbp(r["y1_op"]))
    line("Year 2 operating profit (after founder draw)", lambda r: gbp(r["y2_op"]))
    line("Blended gross margin, year 2", lambda r: f"{r['gm_y2']:.0%}")
    line("Recurring (subscription) gross margin", lambda r: f"{r['rgm']:.0%}")
    line("First month operating profit ≥ 0", lambda r: f"Month {r['be_first']}" if r["be_first"] else "Not within 24 months")
    line("Sustained break-even (profitable every month after)", lambda r: f"Month {r['be']}" if r["be"] else "Not within 24 months")
    line("Lowest cumulative cash position (funding needed)", lambda r: gbp(r["low_cash"]))
    line("Cumulative cash payback (incl. startup costs)", lambda r: f"Month {r['payback']}" if r["payback"] else "Not within 24 months")
    line("Headcount at month 24 (incl. founder)", lambda r: str(r["headcount"]))
    line("Average monthly fee per client (ARPA)", lambda r: gbp(r["ue"]["arpa"]))
    line("Monthly gross margin per client", lambda r: gbp(r["ue"]["monthly_margin"]))
    line("Expected client lifetime", lambda r: f"{r['ue']['lifetime_months']:.0f} months")
    line("Customer lifetime value (gross margin, incl. setup)", lambda r: gbp(r["ue"]["ltv"]))
    line("CAC: cash marketing only", lambda r: gbp(r["ue"]["cac_cash"]))
    line("CAC: fully loaded (marketing + half of sales hire + founder selling time)", lambda r: gbp(r["ue"]["cac_loaded"]))
    line("LTV : loaded CAC", lambda r: f"{r['ue']['ltv_cac']:.1f}x")
    line("CAC payback on monthly margin", lambda r: f"{r['ue']['payback_months']:.1f} months")

    md += ["",
           "### Notes on reading this model",
           "",
           "- **Use the fully loaded CAC.** Most early selling is done by the founder. Cash CAC leaves that time out, "
           f"so the loaded figure prices it at {FOUNDER_SALES_HOURS_PER_WIN} hours × {gbp(FOUNDER_HOURLY_VALUE)} per client won.",
           f"- **Pilot pricing:** the first {PILOT_CLIENTS} clients pay {PILOT_SETUP_DISCOUNT:.0%} of the setup fee in return for a case study.",
           "- **Setup fees front-load revenue.** Early months look healthier than recurring revenue alone suggests. "
           "Track MRR separately, because that is what makes the company valuable and stable.",
           "- **Churn is the most sensitive input.** Moving monthly churn from 3% to 5% cuts expected client lifetime "
           "from about 33 months to 20 months. Re-run the model with your real churn after month 6.",
           f"- **Startup costs** of {gbp(STARTUP_COSTS)} are deducted before month 1 in the cumulative cash line.",
           ""]

    with open(os.path.join(OUT_DIR, "financial_model_outputs.md"), "w") as f:
        f.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
