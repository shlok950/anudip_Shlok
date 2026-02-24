l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

common = []

for i in l1:
    if i in l2 and i not in common:
        common.append(i)

print(common)