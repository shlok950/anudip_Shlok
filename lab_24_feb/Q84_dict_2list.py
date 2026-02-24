keys = input("Enter keys separated by spaces: ").split(",")
values = list(map(int, input("Enter values separated by spaces: ").split(",")))
d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)