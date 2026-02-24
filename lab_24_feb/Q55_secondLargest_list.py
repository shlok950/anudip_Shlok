lst = [5, 8, 1, "hello", 3.14, 2, 9]

largest = second = float('-inf')

for num in lst:
    if isinstance(num, (int, float)) and num > largest:
        second = largest
        largest = num
    elif isinstance(num, (int, float)) and num > second and num != largest:
        second = num

print(second)