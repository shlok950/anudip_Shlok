a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
if a > b and a > c:
    print("The largest number is : ", a , " -> The First number")
elif b > a and b > c:
    print("The largest number is : ", b, " -> The Second number")
else:
    print("The largest number is : ", c, " -> The Third number")