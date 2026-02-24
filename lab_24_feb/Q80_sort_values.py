d = {'a':3, 'b':1, 'c':2}
for k in sorted(d, key=d.get):
    print(k, ":", d[k])