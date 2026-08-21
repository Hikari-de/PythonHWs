import numpy as np

revenue = np.array([
    35, 42, 89,
    125, 50, 80,
    120, 200, 150,
    220, 300, 450
])

quarter_revenue = revenue.reshape(4, 3)

print(f"New structure: Shape {quarter_revenue.shape} | Ndim: {quarter_revenue.ndim}")

print("---")
print("Quarterly Report:")

quarter_average = quarter_revenue.mean(axis=1)
quarter_max = quarter_revenue.max(axis=1)

print("Average revenue per quarter:", quarter_average)
print("Highest revenue in each quarter:", quarter_max)

print("---")

filtered_revenue = revenue[(revenue > 80) & (revenue <= 200)]

print("Months satisfying the condition (80 < x <= 200):")
print(filtered_revenue)

print("---")

marketing_budget = np.array([10, 15, 20, 30])

report = np.column_stack((quarter_revenue, marketing_budget))

print("Report after integrating marketing budget:")
print(report)