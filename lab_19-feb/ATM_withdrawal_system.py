# Initial values (example data)
account_balance = float(input("Enter account balance: ₹"))
withdraw_amount = float(input("Enter withdrawal amount: ₹"))
atm_cash = float(input("Enter ATM available cash: ₹"))

daily_limit = 50000

# Conditions check
if withdraw_amount > daily_limit:
    print("Transaction Failed: Exceeds daily withdrawal limit of ₹50,000.")

elif withdraw_amount > account_balance:
    print("Transaction Failed: Insufficient account balance.")

elif withdraw_amount > atm_cash:
    print("Transaction Failed: ATM has insufficient cash.")

else:
    account_balance -= withdraw_amount
    atm_cash -= withdraw_amount
    print("Withdrawal Successful!")
    print("Remaining Account Balance: ₹", account_balance)
    print("Remaining ATM Cash: ₹", atm_cash)
