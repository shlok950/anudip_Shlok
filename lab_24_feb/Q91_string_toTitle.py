s = input("Enter a string: ").split()
title_case = ""

for word in s:
    title_case += word[0].upper() + word[1:].lower() + " "

print(title_case.strip())