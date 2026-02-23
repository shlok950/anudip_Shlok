rows = int(input("Enter the number of rows: "))
if rows < 1:
    print("Please enter a positive integer.")
    exit()
else:
    for i in range(1, rows+1,2):
     print(" "*int((rows-i/2)) + "*" * i + " "*int((rows-i/2)))
     