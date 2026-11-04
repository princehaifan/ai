# ROI calculator: "What is this costing you?"

> Use the **prospect's own numbers**. Present results as a **range** and say clearly that they're estimates, not promises.
> Build it as a Google Sheet for sales meetings and as an interactive page on the website.

---

## Inputs

| Code | Input | Where it comes from |
|---|---|---|
| A | Unanswered calls or enquiries per week | Phone system call log, 2-week sample, or owner estimate (mark as estimate) |
| B | Share of those that are potential new business (%) | Owner estimate; often lower than they think, so be conservative |
| C | Share of new enquiries that normally convert to a customer (%) | Their booking or CRM data |
| D | Average value of a new customer (£): first purchase, or 12-month value if repeat business is typical | Their POS or CRM |
| E | Share of missed enquiries the AI could realistically capture and convert (%) | **Assumption.** Use 30% (low) / 50% (mid) / 70% (high) until you have data from live clients. |
| F | No-shows per week | Booking system |
| G | Average value of a booking (£) | POS |
| H | Expected reduction in no-shows from reminders and deposits (%) | **Assumption.** Use 15% / 25% / 40% until you have client data. |
| I | Staff hours per week on tasks that will be automated | Owner or staff estimate |
| J | Fully loaded hourly staff cost (£) | Payroll (wage + employer NI + pension) |
| K | Share of those hours actually freed (%) | **Assumption.** Use 30% / 50% / 70%. |

## Formulas (monthly; 4.33 weeks per month)

```
Recovered enquiry revenue  = A × B × C × D × E × 4.33
Recovered no-show revenue  = F × G × H × 4.33
Admin time value           = I × J × K × 4.33
Total monthly opportunity  = sum of the above
Net monthly benefit        = total opportunity − Ostler monthly fee
Payback on setup (months)  = setup fee ÷ net monthly benefit
```

> **Revenue is not profit.** For a stricter view, multiply revenue lines by the client's gross margin (e.g. 65% for a restaurant's food and drink margin, as provided by the client).

---

## Worked example (hypothetical numbers, for illustration only)

*An 80-cover restaurant. All inputs are invented to show the method; replace them with real data.*

| Input | Value |
|---|---|
| A: unanswered calls per week | 25 |
| B: share that are bookings | 60% |
| C: share of booking calls that normally convert | 80% |
| D: average spend per booking (party) | £90 |
| E: share the AI captures (low / mid / high) | 30% / 50% / 70% |
| F: no-shows per week | 4 |
| G: average booking value | £90 |
| H: no-show reduction (low / mid / high) | 15% / 25% / 40% |
| I, J, K: admin hours, hourly cost, share freed (low / mid / high) | 5 hrs × £13 × 30% / 50% / 70% |

| Monthly result | Low (E 30%, H 15%, K 30%) | Mid (E 50%, H 25%, K 50%) | High (E 70%, H 40%, K 70%) |
|---|---:|---:|---:|
| Recovered enquiry revenue = 25 × 0.6 × 0.8 × £90 × E × 4.33 | £1,403 | £2,338 | £3,274 |
| Recovered no-show revenue = 4 × £90 × H × 4.33 | £234 | £390 | £624 |
| Admin time value = 5 × £13 × K × 4.33 | £84 | £141 | £197 |
| **Total opportunity (revenue)** | **£1,721** | **£2,869** | **£4,095** |
| At a 65% gross margin | £1,119 | £1,865 | £2,662 |
| Ostler Growth fee | −£495 | −£495 | −£495 |
| **Net monthly benefit (margin basis)** | **£624** | **£1,370** | **£2,167** |
| Payback on £3,500 setup | 5.6 months | 2.6 months | 1.6 months |

---

## How to present it

1. Fill it in **with** the owner, live. People trust numbers they supplied.
2. Lead with the **low** case: "Even on cautious assumptions, this pays for itself in about X months."
3. Explain the assumptions (E, H, K) honestly: "These are estimates; we'll measure the real figures from your baseline and report them monthly."
4. **Never** present the high case as expected, and never guarantee it.

## Measuring actuals after go-live

| Estimated line | What to measure |
|---|---|
| Recovered enquiries | Conversations and calls handled by AI outside staffed capacity; bookings created by AI (tagged in the booking system) |
| No-shows | No-show rate, 4 weeks before vs. after reminders and deposits |
| Admin time | Staff time log sample (1 week before, 1 week after) |
