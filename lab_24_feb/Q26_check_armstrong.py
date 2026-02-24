num = int(input("Enter a number : "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num //= 10
if sum == temp:
    print("The given number is an Armstrong number.")
else:
    print("The given number is not an Armstrong number.")