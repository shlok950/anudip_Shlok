# Input
age = int(input("Enter patient age: "))
heart_rate_status = input("Is heart rate abnormal? (yes/no): ")
severe_injury = input("Is there a severe injury? (yes/no): ")
condition = input("Enter condition (critical/moderate/normal): ")

# Triage decision
if heart_rate_status.lower() == "yes" or severe_injury.lower() == "yes":
    print("Priority: Critical")

elif condition.lower() == "moderate":
    if age > 65:
        print("Priority: Critical (Upgraded due to age)")
    else:
        print("Priority: Moderate")

else:
    print("Priority: Normal")
