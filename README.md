# E-commerce Performance Analysis — Customer Retention (2024)

**Email (verification): 23f2004940@ds.study.iitm.ac.in**

This PR analyzes 2024 quarterly customer retention against the industry target (85%).  
It includes code, visualization, and a data-driven narrative for executives.

## Key Findings
- **Average 2024 retention:** **72.56%** (computed from Q1–Q4: 72.88, 72.98, 71.23, 73.16)
- **Gap to target (85%):** **12.44 percentage points**
- **Quarterly trend:** Mild improvement in Q4 vs. Q3 low (71.23%), but the year remains well below target.
- **Risk:** Prolonged sub-target retention increases churn, depresses LTV, and raises CAC pressure to replace lost customers.

## Business Implications
- **Revenue & LTV:** Lower retention reduces cohort LTV and dampens compounding effects of repeat purchases.
- **Marketing Efficiency:** Greater reliance on acquisition budgets to offset churn.
- **Planning:** Inventory and staffing forecasts become less predictable with declining loyalty.

## Recommendations — Primary Solution
**Implement targeted retention campaigns** focused on:
1. **At-risk segmentation:** Predict churn propensity (RFM, recency windows, support signal, browse-abandon patterns) and trigger timely re-engagement.
2. **Lifecycle messaging:** Personalized post-purchase sequences, loyalty tiers, and win-back flows (offers calibrated to price sensitivity).
3. **Experience levers:** Improve delivery speed/accuracy and returns experience—common drivers for churn in e-commerce.
4. **Value reinforcement:** Bundles/subscriptions for sticky categories; attach rate boosts via cross-sell/upsell nudges.

**Operational Targets (next 2–3 quarters):**
- Lift high-risk cohorts by **+6–8 pp** via win-back & loyalty programs.
- Lift all-customer average by **+12.44 pp** to reach **85%** through iterative testing.

## How to Reproduce
```bash
pip install -r requirements.txt
python analysis.py
# Output: figures/retention_trend.png
```

## Files
- `analysis.py` — data processing + visualization
- `figures/retention_trend.png` — trend chart with benchmark line
- `requirements.txt`

## LLM Assistance

This analysis and code were prepared with the help of Jules (ChatGPT Codex) / LLM tooling.
See `llm_assistance.md` for prompts & responses used during development.