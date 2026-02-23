def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
addition, difference = calculate(num1, num2)
print("Addition =", addition)
print("Difference =", difference)