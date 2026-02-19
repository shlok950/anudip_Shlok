amount = int(input("Enter the amount to be deposited: "))
account_time = int(input("Enter the time in months: "))
is_international = input("Is the account international? (yes/no): ").lower()

if amount < 200000 or account_time < 6 or is_international != "yes":
    print("The transaction is suspicious.")