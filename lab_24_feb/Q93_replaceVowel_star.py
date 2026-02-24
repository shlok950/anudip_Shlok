s = input("Enter a string: ")
vowels = "aeiouAEIOU"
res = ""

for ch in s:
    if ch in vowels:
        res += "*"
    else:
        res += ch

print(res)