set1 = set(map(int, input("Enter elements of first set: ").split(",")))
set2 = set(map(int, input("Enter elements of second set: ").split(",")))

sym_diff = set1 ^ set2
print(sym_diff)