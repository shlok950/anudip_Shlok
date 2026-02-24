n = int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print("The number is divisible by both 3 and 5.")
elif n%3==0:
    print("The number is divisible by 3 only.")
elif n%5==0:
    print("The number is divisible by 5 only.")
else:
    print("The number is divisible neither by 3 nor 5.")