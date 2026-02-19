# Input
rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment = 0

# Performance based increment
if rating == 5:
    increment += 10
elif rating == 4:
    increment += 7
elif rating == 3:
    increment += 5
elif rating == 2:
    increment += 3
else:
    increment += 0

# Experience bonus
if experience >= 5:
    increment += 3
elif experience >= 2:
    increment += 2

# Attendance bonus
if attendance >= 90:
    increment += 2
elif attendance >= 75:
    increment += 1

# Output
print("Total Increment Percentage:", increment, "%")