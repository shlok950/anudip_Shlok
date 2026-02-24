t = tuple(map(int, input("Enter tuple elements: ").split(",")))
maximum = t[0]

for i in t:
    if i > maximum:
        maximum = i
print(maximum)