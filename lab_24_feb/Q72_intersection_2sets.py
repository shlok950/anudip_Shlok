set1 = set(map(int, input("Enter elements of first set: ").split(",")))
set2 = set(map(int, input("Enter elements of second set: ").split(",")))

intersection_set = set1 & set2
print(intersection_set)