l = [1,5,7,1,6,45,8,56,3,2]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print(l)