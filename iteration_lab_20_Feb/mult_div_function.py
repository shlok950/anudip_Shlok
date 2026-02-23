def calculate_mult(a,b):
    mult_result = a*b
    return mult_result
def calculate_div(a,b):
        if a%b==0:
          div_result = int(a/b)
          return div_result
        else:
            div_result = float(a/b)
            return div_result
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: ")) 
multiplication = calculate_mult(num1, num2)
division = calculate_div(num1, num2)
print("Multiplication =", multiplication)
print("Division =", division) 

    
    