l = [1, 2, 3, 2, 4, 1, 5, 3, 6]
freq = {}

for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)