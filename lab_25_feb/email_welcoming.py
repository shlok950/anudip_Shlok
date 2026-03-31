Email_id = input("Enter your email id: ")
name = Email_id.split('@')[0]
domain = Email_id.split('@')[1]
print(end="\n")
print(f"Hello! from {domain} to {name}")
print(end="\n")