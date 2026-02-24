set1 = set(map(int, input("Enter elements of first set: ").split(",")))
set2 = set(map(int, input("Enter elements of second set: ").split(",")))

diff_set = set1 - set2
print(diff_set)