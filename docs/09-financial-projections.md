# 9. Financial Projections (First 12 Months)

> **Read this first.** These are **projections built from stated assumptions**, not forecasts backed by customer demand. No demand has been validated yet. Every input lives in [`financials/model.py`](../financials/model.py). Change the assumptions and re-run `python3 financials/model.py` to regenerate every table on this page. All figures are GBP, excluding VAT, before corporation tax.

---

## 9.1 Key assumptions

| Assumption | Value | Basis |
|---|---|---|
| Average Sprint price | £5,000 | Blend of £3.5k Starter and £7.5k Growth (proposed prices) |
| Average Build price | £18,000 | Blend of Starter (£8k–£15k) and Growth (£20k–£45k) |
| AI MVP price | £40,000 | Mid-point of Growth MVP range |
| Workshop average | £3,000 | Half/full-day blend |
| Run retainer average | £1,800/month | Mostly Run Starter/low Growth in year 1 |
| Fractional Head of AI | £3,000/month | 2 days/month |
| Build → Run attach rate | 60% / 70% / 80% by scenario | Run is included by default (opt-out) |
| Retainer churn | 3% per month | [Estimate] |
| Delivery cost (COGS) | Sprints 15%, Builds 45%, MVPs 50%, Run 30%, workshops 10%, fractional 5% | Contractors at ~£450–£650/day; client pays LLM/hosting directly |
| Fixed costs | ~£1,030/month (tools £450, PI + cyber insurance £180, accountant £150, misc £250) + marketing £300–£900/month | Estimates: **get real insurance and accountant quotes** |
| One-off set-up | £4,500 in month 1 (contract templates ~£2.5k, brand/website ~£2k) | Estimate |
| Founder pay | £0 for the first 2–4 months, rising to £2k–£4.5k/month | Shown separately so you can see the business's profit before and after paying you |
| Founder capacity | 18 working days/month; 7 days/month always reserved for sales/marketing/admin | Drives the "Founder load" column |
| Revenue timing | Builds recognised 50% in month signed, 50% next month | Cash usually arrives earlier, because deposits are 40–50% upfront |

**Gross margin caveat:** reported gross margins (64–73%) look high because the founder delivers much of the work and **founder pay sits below gross profit**. If you priced founder time at a contractor rate, blended delivery margin would be closer to **45–55%**. That's still healthy for a consultancy. [Estimate]

## 9.2 Scenario results

### Summary of all three scenarios

| Scenario | Year-1 revenue | Gross margin | Month-12 MRR | Retainer clients (m12) | Year-1 net profit after founder pay | Peak cash needed | First profitable month | Cumulative break-even month | Paid engagements | Peak founder load |
|---|---|---|---|---|---|---|---|---|---|---|
| Conservative | £83,166 | 71% | £2,036 | 1.1 | £24,806 | £7,160 | 3 | 6 | 11 | 91% |
| Realistic | £194,860 | 73% | £9,932 | 4.3 | £63,226 | £7,360 | 3 | 4 | 22 | 123% |
| Ambitious | £566,635 | 67% | £23,640 | 11.4 | £197,737 | £6,030 | 2 | 3 | 50 | 166% |

### What the numbers say

1. **Low capital requirement.** Peak cash needed is about **£6k–£7.5k** in every scenario, mainly the set-up costs before the first invoice. **Keep a £15k buffer** (three months of personal costs + business costs) so you never have to take a bad-fit project out of desperation. [Recommendation]
2. **The realistic case is a ~£195k first year with ~£10k MRR exiting month 12.** That's a good, profitable small consultancy, not a venture-scale outcome. That's the right goal for year one.
3. **Founder time is the binding constraint, not demand or cash.** In the Realistic case, founder load passes 100% by month 4–6, even with a part-time delivery lead from month 7. The Ambitious case is only possible with a delivery lead in month 4 and a salaried engineer by month 6, and *still* needs a second hire by month 10. **This is why the Delivery Kit, the contractor bench and the hiring triggers matter more than any marketing tactic.**
4. **Recurring revenue builds slowly.** Even in the Realistic case MRR is under £10k at month 12. The levers: (a) Run included by default in every Build, (b) Fractional Head of AI retainers, (c) a second Build for every happy client. The year-2 target is **MRR covering 100% of fixed costs plus founder pay** (~£8k–£10k), so project revenue becomes profit.
5. **Which scenario is "realistic" depends on you.** The Realistic case assumes a founder with credible AI engineering experience and a reasonable professional network. If you're new to selling consulting or have a thin network, **treat the Conservative case as your realistic plan.**

## 9.3 Break-even

| Measure | Conservative | Realistic | Ambitious |
|---|---|---|---|
| First month with a profit (after founder pay) | Month 3 | Month 3 | Month 2 |
| Cumulative break-even (all set-up costs recovered) | Month 6 | Month 4 | Month 3 |
| Monthly revenue needed to cover fixed costs + target founder pay of £3.5k (at ~65% gross margin) | ~£7.5k/month | ~£7.5k/month | ~£32k/month once hires join (£14.7k/month delivery payroll) |

**Monthly break-even formula:** `(fixed costs + hires + founder pay) ÷ gross margin %`. Example: `(£1,330 + £0 + £3,500) ÷ 0.65 ≈ £7,430/month`.

## 9.4 Customer acquisition cost (CAC)

There's no ad spend in year one, so CAC is mostly **founder time + data tools + partner fees**. [Estimate]

| Channel | Cost inputs | Estimated CAC per new client |
|---|---|---|
| Warm network / referrals | Founder time (~5 hrs), 10% referral fee where applicable | £500–£2,000 |
| Signal-based outbound | Data tools (~£150/month) + ~30 founder hours per win (valued at £75/hour) | £2,500–£4,000 |
| Agency partners | 15–20% referral fee on first project | £2,700–£3,600 on an £18k build |
| Content / inbound | Founder time, freelance editing | Hard to attribute in year 1; falls over time |
| **Blended target** | | **£1,500–£4,000** |

Because every client starts with a **paid** Sprint (£3.5k–£7.5k), **the first invoice usually recovers CAC.** Year-one client value (Sprint + Build + 6–9 months of Run) of **£25k–£60k** gives an LTV:CAC ratio well above 5:1, if delivery quality drives retention. [Estimate]

## 9.5 Sensitivity: what moves the result most

| Change (Realistic case) | Approximate effect on year-1 revenue | Why it matters |
|---|---|---|
| Sprint → Build conversion falls from ~45% to 25% | **−£50k to −£60k** | The most important sales metric. Fix by tightening discovery qualification |
| Average Build price −20% (£14.4k) | ~−£22k | Protect price; cut scope instead |
| First sale slips by 2 months | ~−£40k to −£50k | Warm network in week 3 is critical |
| Run attach rate 30% instead of 70% | ~−£10k in year 1, **much larger in year 2** | Recurring revenue compounds |
| One fixed-price Build overruns by 50% | ~−£4k margin per occurrence | The Sprint, spike gate and change control limit this |

## 9.6 Setting up the finances

- **Company structure:** private limited company (Ltd) for liability protection and credibility. Founder pay as a small salary + dividends: take accountant advice.
- **Business bank account** + accounting software (Xero/FreeAgent) linked from day one.
- **Insurance before the first contract:** Professional Indemnity (typically £1m–£2m cover for tech consultancy; clients may ask for more) and Cyber. Public/Employers' Liability when you hire. Get quotes; the £180/month in the model is a placeholder.
- **VAT:** registration is mandatory above the threshold (currently £90,000 rolling 12-month taxable turnover; check HMRC). The Realistic case crosses it around month 7–8. Consider voluntary registration earlier.
- **Cash discipline:** deposits before work starts; invoices on milestones, not at the end; 14-day terms for Starter clients, 30 days for Enterprise; chase on day 1 overdue.
- **Keep 20–25% of profit aside for corporation tax** and a growing reserve towards 3 months of operating costs.

## Appendix: month-by-month tables (generated by financials/model.py)


### Conservative scenario

_First paid work in month 3, slow referrals, no product builds, no hires._

| Month | Revenue | Recurring (MRR) | Gross profit | Operating costs | Profit before founder pay | Founder pay | Net profit | Cumulative | Founder load |
|---|---|---|---|---|---|---|---|---|---|
| 1 | £0 | £0 | £0 | £5,830 | -£5,830 | £0 | -£5,830 | -£5,830 | 39% |
| 2 | £0 | £0 | £0 | £1,330 | -£1,330 | £0 | -£1,330 | -£7,160 | 39% |
| 3 | £5,000 | £0 | £4,250 | £1,330 | £2,920 | £0 | £2,920 | -£4,240 | 67% |
| 4 | £0 | £0 | £0 | £1,330 | -£1,330 | £0 | -£1,330 | -£5,570 | 39% |
| 5 | £8,000 | £0 | £6,950 | £1,330 | £5,620 | £1,500 | £4,120 | -£1,450 | 78% |
| 6 | £9,000 | £0 | £4,950 | £1,330 | £3,620 | £1,500 | £2,120 | £670 | 61% |
| 7 | £14,000 | £0 | £9,200 | £1,330 | £7,870 | £1,500 | £6,370 | £7,040 | 89% |
| 8 | £6,080 | £1,080 | £5,006 | £1,330 | £3,676 | £1,500 | £2,176 | £9,216 | 69% |
| 9 | £4,048 | £1,048 | £3,433 | £1,330 | £2,103 | £2,000 | £103 | £9,319 | 52% |
| 10 | £15,016 | £1,016 | £9,911 | £1,330 | £8,581 | £2,000 | £6,581 | £15,901 | 91% |
| 11 | £14,986 | £986 | £9,890 | £1,330 | £8,560 | £2,000 | £6,560 | £22,461 | 91% |
| 12 | £7,036 | £2,036 | £5,675 | £1,330 | £4,345 | £2,000 | £2,345 | £24,806 | 71% |

### Realistic scenario

_About one sprint a month from month 3, ~45% of sprints become builds, two fractional retainers, part-time contract delivery lead from month 7._

| Month | Revenue | Recurring (MRR) | Gross profit | Operating costs | Profit before founder pay | Founder pay | Net profit | Cumulative | Founder load |
|---|---|---|---|---|---|---|---|---|---|
| 1 | £0 | £0 | £0 | £5,930 | -£5,930 | £0 | -£5,930 | -£5,930 | 39% |
| 2 | £0 | £0 | £0 | £1,430 | -£1,430 | £0 | -£1,430 | -£7,360 | 39% |
| 3 | £5,000 | £0 | £4,250 | £1,430 | £2,820 | £0 | £2,820 | -£4,540 | 67% |
| 4 | £17,000 | £0 | £11,900 | £1,430 | £10,470 | £2,500 | £7,970 | £3,430 | 100% |
| 5 | £14,000 | £0 | £9,200 | £1,430 | £7,770 | £2,500 | £5,270 | £8,700 | 89% |
| 6 | £18,260 | £4,260 | £12,932 | £1,430 | £11,502 | £2,500 | £9,002 | £17,702 | 108% |
| 7 | £21,132 | £4,132 | £15,520 | £6,430 | £9,090 | £3,000 | £6,090 | £23,792 | 75% |
| 8 | £19,268 | £5,268 | £13,593 | £6,430 | £7,163 | £3,000 | £4,163 | £27,955 | 66% |
| 9 | £19,110 | £5,110 | £13,462 | £6,430 | £7,032 | £3,000 | £4,032 | £31,987 | 65% |
| 10 | £31,217 | £9,217 | £24,016 | £6,430 | £17,586 | £3,500 | £14,086 | £46,073 | 123% |
| 11 | £22,940 | £8,940 | £16,830 | £6,430 | £10,400 | £3,500 | £6,900 | £52,973 | 83% |
| 12 | £26,932 | £9,932 | £20,183 | £6,430 | £13,753 | £3,500 | £10,253 | £63,226 | 96% |

### Ambitious scenario

_Strong network and a working agency-partner channel by month 4; contract delivery lead from month 4, first salaried senior engineer in month 6._

| Month | Revenue | Recurring (MRR) | Gross profit | Operating costs | Profit before founder pay | Founder pay | Net profit | Cumulative | Founder load |
|---|---|---|---|---|---|---|---|---|---|
| 1 | £0 | £0 | £0 | £6,030 | -£6,030 | £0 | -£6,030 | -£6,030 | 39% |
| 2 | £5,000 | £0 | £4,250 | £1,530 | £2,720 | £0 | £2,720 | -£3,310 | 67% |
| 3 | £17,000 | £0 | £11,900 | £1,530 | £10,370 | £3,000 | £7,370 | £4,060 | 100% |
| 4 | £31,000 | £3,000 | £21,250 | £8,730 | £12,520 | £3,000 | £9,520 | £13,580 | 83% |
| 5 | £35,350 | £4,350 | £24,872 | £9,130 | £15,742 | £3,500 | £12,242 | £25,822 | 97% |
| 6 | £56,660 | £5,660 | £35,767 | £16,630 | £19,137 | £3,500 | £15,637 | £41,460 | 44% |
| 7 | £57,930 | £9,930 | £36,785 | £16,630 | £20,155 | £4,000 | £16,155 | £57,615 | 53% |
| 8 | £52,512 | £12,512 | £36,200 | £16,630 | £19,570 | £4,000 | £15,570 | £73,185 | 53% |
| 9 | £58,576 | £13,576 | £41,153 | £16,630 | £24,523 | £4,500 | £20,023 | £93,208 | 82% |
| 10 | £81,049 | £19,049 | £52,994 | £16,630 | £36,364 | £4,500 | £31,864 | £125,072 | 132% |
| 11 | £93,918 | £19,918 | £61,190 | £16,630 | £44,560 | £4,500 | £40,060 | £165,132 | 166% |
| 12 | £77,640 | £23,640 | £53,736 | £16,630 | £37,106 | £4,500 | £32,606 | £197,737 | 135% |

