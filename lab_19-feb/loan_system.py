# Input from user
credit_score = int(input("Enter credit score: "))
monthly_income = float(input("Enter monthly income (₹): "))
existing_loan_amount = float(input("Enter existing loan amount (₹): "))

# Loan approval logic
if credit_score < 600:
    print("Loan Status: Rejected")

elif credit_score >= 750:
    print("Loan Status: Approved")

else:  # Credit score between 600 and 749
    if monthly_income < 30000 and existing_loan_amount > 500000:
        print("Loan Status: Rejected")
    else:
        print("Loan Status: Approved")
