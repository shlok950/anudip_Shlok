n = int(input("Enter a number: "))
i= int(input("Enter the number of terms in the multiplication table: "))
j = 1
while j <= i:
    print(n, "x", j, "=", n*j)
    j = j + 1