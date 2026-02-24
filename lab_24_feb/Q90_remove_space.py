s = input("Enter a string: ")
no_spaces = ""

for ch in s:
    if ch != " ":
        no_spaces += ch

print(no_spaces)