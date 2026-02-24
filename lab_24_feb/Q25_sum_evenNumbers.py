n = int(input("Enter a number: "))
i=1
sum=0
while i <= n:
    if i%2==0:
        sum=sum+i
    i=i+1
print("The sum of even numbers from 1 to", n, "is : ", sum)