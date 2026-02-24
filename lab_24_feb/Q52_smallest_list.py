list = [5,8,1,"hello", 3.14, 2, 9]
smallest = list[0]

for i in list:
    if isinstance(i, (int, float)) and i < smallest:
        smallest = i

print(smallest)