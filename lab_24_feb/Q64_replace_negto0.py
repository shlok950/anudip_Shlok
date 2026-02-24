l = list(map(int, input("Enter list elements: ").split(",")))

for i in range(len(l)):
    if l[i] < 0:
        l[i] = 0
print(l)