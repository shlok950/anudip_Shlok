# Input
units = float(input("Enter electricity units consumed: "))
senior = input("Are you a senior citizen? (yes/no): ")

# Bill calculation
if units <= 100:
    bill = units * 5
    print("Total Electricity Bill: ₹", bill)
elif units <= 300:
  bill = units * 7
  print("Total Electricity Bill: ₹", bill)
else:
    bill = units * 10
    print("Total Electricity Bill: ₹", bill)
# Apply senior citizen discount
if senior.lower() == "yes":
    bill = bill * 0.9   # 10% discount

# Output
print("Total Electricity Bill after age validation is : ₹", bill)
