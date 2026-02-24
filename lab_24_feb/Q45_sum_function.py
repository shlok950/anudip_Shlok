def sum_digits(n):
    total = 0
    while n > 0:
        total = total + n % 10
        n //= 10
    return total

n = int(input("Enter a number: "))
print(sum_digits(n))