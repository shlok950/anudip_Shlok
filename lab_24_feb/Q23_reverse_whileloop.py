n = int (input("Enter a number: "))
while n > 0:
    rev = n%10
    print(rev, end="")
    n = n//10