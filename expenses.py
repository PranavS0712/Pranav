sum = 0
expenses = []
num_expenses = int(input("Enter the no of expenses :"))

# Collecting 7 expenses
for x in range(num_expenses):
    expense = float(input("Enter an expense: "))
    expenses.append(expense)

# Summing the expenses
for i in expenses:
    sum = i + sum  # Accumulate the total

print(f"Total expenses: {sum}")