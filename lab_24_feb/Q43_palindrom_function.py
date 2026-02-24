def is_palindrome(s):
    return s == s[::-1]

s = input("Enter a string: ")
if is_palindrome(s):
    print("String is Palindrome")
else:
    print("String is Not Palindrome")
