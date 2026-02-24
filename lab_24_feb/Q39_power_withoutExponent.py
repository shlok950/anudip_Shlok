a = int(input("Enter the base number: "))
b = int(input("Enter the exponent: "))
result = 1
for i in range(b):
    result = result * a
print(result)