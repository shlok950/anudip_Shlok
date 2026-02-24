num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))
num_4 = int(input("Enter the fourth number: "))
if num_1 > num_2 and num_1 > num_3 and num_1 > num_4:
    print("The greatest number is:", num_1)
elif num_2 > num_1 and num_2 > num_3 and num_2 > num_4:
    print("The greatest number is:", num_2)
elif num_3 > num_1 and num_3 > num_2 and num_3 > num_4:
    print("The greatest number is:", num_3)
else:
    print("The greatest number is:", num_4)