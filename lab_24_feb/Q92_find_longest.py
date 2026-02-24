s = input("Enter a string: ").split()
longest = s[0]

for word in s:
    if len(word) > len(longest):
        longest = word

print(longest)