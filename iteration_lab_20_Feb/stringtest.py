a = [99,100,98,99,97,99,98,95,96]
print(len(a))
a.sort(reverse=True)
for i in range(0,3):
    print(str(i+1) , (a[i]))