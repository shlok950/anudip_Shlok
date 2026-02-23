# Inventory Management

# Take stock quantities input from user (space separated)
stocks = list(map(int, input("Enter product stock quantities separated by space: ").split()))

print("Original Stock:", stocks)

# 1. Remove items with 0 stock
stocks = [s for s in stocks if s != 0]
print("After Removing 0 Stock Items:", stocks)

# 2. Add restock (add 50 units) to items below 10
for i in range(len(stocks)):
    if stocks[i] < 10:
        stocks[i] += 50

print("After Restocking Low Items:", stocks)

# 3. Find total inventory count
total_inventory = sum(stocks)
print("Total Inventory Count:", total_inventory)
