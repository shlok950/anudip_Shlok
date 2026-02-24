d = {'a':5, 'b':10, 'c':7}
max_key = max(d, key=d.get)
print(max_key)