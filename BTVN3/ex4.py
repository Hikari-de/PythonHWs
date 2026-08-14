
n = int(input("Enter number of expenses: "))

expenses = []

for i in range(n):
    data = input("Enter expense: ").split(",")

    name = data[0].strip()
    amount = int(data[1].strip())
    category = data[2].strip()

    expenses.append((name, amount, category))

print("\nExpense list:")

for expense in expenses:
    print(expense)

total = 0

for expense in expenses:
    total += expense[1]

print("\nTotal expense:", total, "VND")

categories = set()

for expense in expenses:
    categories.add(expense[2])

print("\nStatistics by category:")

for category in categories:
    count = 0
    money = 0

    for expense in expenses:
        if expense[2] == category:
            count += 1
            money += expense[1]

    print("\n" + category + ":")
    print("- Number of expenses:", count)
    print("- Total amount:", money, "VND")

if total > 5000000:
    print("\nWarning: Total expense exceeds 5,000,000 VND.")

largest = expenses[0]

for expense in expenses:
    if expense[1] > largest[1]:
        largest = expense

print("\nLargest expense:")
print(largest)