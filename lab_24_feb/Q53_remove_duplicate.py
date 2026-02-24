lst = [1,2,5,5,3,2,1,4]
unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)