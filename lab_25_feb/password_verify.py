password = input("Enter your password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
    exit()
    if (char.isupper() for char in password if char.islower() for char in password if char.isdigit() for char in password):
        print("Password is valid.")
    else:
        print("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")