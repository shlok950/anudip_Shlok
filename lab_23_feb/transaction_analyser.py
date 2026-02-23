# Bank Transaction Analyzer

# Take transactions input from user (space separated)
# Positive = deposit, Negative = withdrawal
transactions = list(map(float, input("Enter transactions separated by space: ").split()))

print("Transactions:", transactions)

# 1. Calculate total balance
total_balance = sum(transactions)
print("Total Balance:", total_balance)

# 2. Find largest withdrawal (most negative value)
withdrawals = [t for t in transactions if t < 0]

if withdrawals:
    largest_withdrawal = min(withdrawals)   # most negative value
    print("Largest Withdrawal:", largest_withdrawal)
else:
    print("No withdrawals found.")

# 3. Count deposits greater than ₹10,000
large_deposits = [t for t in transactions if t > 10000]
print("Number of Deposits > ₹10,000:", len(large_deposits))