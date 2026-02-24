t = tuple(map(int, input("Enter tuple elements: ").split(",")))
element = int(input("Enter element to count: "))

count = 0
for i in t:
    if i == element:
        count += 1

print(count)