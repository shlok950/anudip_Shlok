# E-Commerce Cart System

# Take product prices input from user (space separated)
prices = list(map(float, input("Enter product prices separated by space: ").split()))

# 1. Remove duplicate items
unique_prices = list(set(prices))

print("Unique Product Prices:", unique_prices)

# 2. Calculate total
total = sum(unique_prices)
print("Total before discount:", total)

# 3. Apply 10% discount if total > 5000
if total > 5000:
    discount = total * 0.10
    total -= discount
    print("Discount Applied (10%):", discount)
else:
    print("No Discount Applied")

print("Total after discount:", total)

# 4. Add GST 18%
gst = total * 0.18
final_amount = total + gst

print("GST (18%):", round(gst, 2))
print("Final Payable Amount:", round(final_amount, 2))