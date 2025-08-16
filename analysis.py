# analysis.py
# E-commerce Retention Analysis (2024)
# Author / verification email: 23f2004940@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ----------------------------
# 1) Data
# ----------------------------
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "RetentionRate": [72.88, 72.98, 71.23, 73.16],  # %
}
target = 85.0

df = pd.DataFrame(data)
df["QuarterIndex"] = range(1, len(df) + 1)

avg = df["RetentionRate"].mean()
avg_2dp = round(avg, 2)  # should be 72.56
gap = round(target - avg_2dp, 2)

print("=== E-commerce Retention (2024) ===")
print(df)
print(f"\nAverage retention (two decimals): {avg_2dp}")
print(f"Industry target: {target}")
print(f"Gap to target: {gap} percentage points")

# Hard guard for the assignment’s required average (avoid accidental edits)
assert avg_2dp == 72.56, f"Expected 72.56 average, got {avg_2dp}"

# ----------------------------
# 2) Visualization
# ----------------------------
outdir = Path("figures")
outdir.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid", context="talk")

fig, ax = plt.subplots(figsize=(10, 6))
# Trend line
sns.lineplot(
    data=df, x="Quarter", y="RetentionRate",
    marker="o", linewidth=3, ax=ax, color="#1f77b4"
)

# Benchmark line
ax.axhline(y=target, color="#d62728", linestyle="--", linewidth=2, label=f"Target = {target}%")

# Average annotation
ax.axhline(y=avg, color="#2ca02c", linestyle=":", linewidth=2, label=f"Average = {avg_2dp}%")
ax.text(3.55, avg + 0.2, f"Avg {avg_2dp}%", color="#2ca02c")

# Titles & labels
ax.set_title("Customer Retention Rate — 2024 Quarterly Trend vs. Industry Target", pad=16)
ax.set_xlabel("Quarter")
ax.set_ylabel("Retention Rate (%)")
ax.set_ylim(65, 90)
ax.legend(loc="lower right", frameon=True)

# Annotate the widest dip
q3_val = float(df.loc[df["Quarter"] == "Q3", "RetentionRate"].iloc[0])
ax.annotate(
    f"Q3 low: {q3_val}%",
    xy=("Q3", q3_val),
    xytext=("Q3", q3_val - 4),
    arrowprops=dict(arrowstyle="->", color="gray"),
    ha="center",
    color="gray"
)

fig.tight_layout()
fig.savefig(outdir / "retention_trend.png", dpi=120)
plt.close(fig)