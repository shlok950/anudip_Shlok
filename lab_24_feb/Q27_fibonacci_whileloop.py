n = int(input("Enter the number of terms in the Fibonacci series: "))
a = 0
b =  1
print(a, end=" ")
print(b, end=" ")

count = 0
while count < n - 2:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        count = count + 1