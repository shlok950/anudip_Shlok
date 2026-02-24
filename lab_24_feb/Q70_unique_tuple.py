t = tuple(map(int, input("Enter tuple elements: ").split(",")))

unique = True

for i in range(len(t)):
    for j in range(i + 1, len(t)):
        if t[i] == t[j]:
            unique = False

if unique:
    print("Unique")
else:
    print("Not Unique")