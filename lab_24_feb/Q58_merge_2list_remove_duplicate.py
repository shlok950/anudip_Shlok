l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

merged = l1 + l2
result = []

for i in merged:
    if i not in result:
        result.append(i)

print(result)