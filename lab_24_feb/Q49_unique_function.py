def unique(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

lst = list(map(int, input("Enter the list elements : ").split()))
print(unique(lst))