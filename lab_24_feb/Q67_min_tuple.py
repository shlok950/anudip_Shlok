t = tuple(map(int, input("Enter tuple elements: ").split(",")))
minimum = t[0]

for i in t:
    if i < minimum:
        minimum = i

print(minimum)