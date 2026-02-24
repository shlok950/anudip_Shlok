d1 = {}
d2 = {}

for _ in range(int(input("Enter number of key-value pairs for first dictionary: "))):
    k, v = input("Enter key and value for first dictionary: ").split(",")
    d1[k] = v

for _ in range(int(input("Enter number of key-value pairs for second dictionary: "))):
    k, v = input("Enter key and value for second dictionary: ").split(",")
    d2[k] = v

for k in d2:
    d1[k] = d2[k]

print(d1)