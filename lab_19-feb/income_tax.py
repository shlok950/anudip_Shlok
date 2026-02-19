income = int(input("Enter your annual income: "))
age = int(input("Enter your age: "))

if income<=250000 :
    tax = 0
    print("Your tax is: ", tax)
elif income<=250001 and income<=500000:
    tax = income*0.05
    print("Your tax is: ", tax)
elif income<=500001 and income<=1000000:
    tax = income*0.2
    print("Your tax is: ", tax) 
else:
        tax = income*0.3
        print("Your tax is: ", tax)

if age<60:
     redemption = 0
elif age>=60:
     redemption=300000
     if tax>redemption:
        tax=tax-redemption
        print("Your tax after redemption is: ", tax)
     else:        
         tax=0
         print("Your tax after redemption is: ", tax)