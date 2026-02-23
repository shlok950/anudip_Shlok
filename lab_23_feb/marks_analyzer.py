# Student Marks Analyzer

# Input marks (you can modify this list or take input from user)
marks = [95, 88, 76, 102, -5, 89, 95, 67]

# 1. Remove invalid marks (less than 0 or greater than 100)
valid_marks = [m for m in marks if 0 <= m <= 100]

print("Valid Marks:", valid_marks)

if len(valid_marks) == 0:
    print("No valid marks available.")
else:
    # 2. Calculate average
    average = sum(valid_marks) / len(valid_marks)
    print("Average Marks:", round(average, 2))

    # 3. Find topper(s)
    highest = max(valid_marks)
    toppers = [i for i, m in enumerate(valid_marks) if m == highest]
    print("Highest Marks:", highest)
    print("Topper Position(s) (index-based):", toppers)

    # 4. Display grade based on average
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Grade Based on Average:", grade)