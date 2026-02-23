# Salary Processing System

# Minimum wage value
MIN_WAGE = 15000  

# Take salary input from user (space separated)
salaries = list(map(float, input("Enter employee salaries separated by space: ").split()))

# 1. Remove salaries below minimum wage
valid_salaries = [s for s in salaries if s >= MIN_WAGE]
print("After Removing Below Minimum Wage:", valid_salaries)

# 2. Add 5% bonus to employees with salary > 50000
updated_salaries = []
for s in valid_salaries:
    if s > 50000:
        bonus = s * 0.05
        s += bonus
    updated_salaries.append(s)

print("After Adding Bonus:", updated_salaries)

# 3. Sort salaries in descending order
updated_salaries.sort(reverse=True)
print("Sorted Salaries (Descending):", updated_salaries)

# 4. Display top 3 highest salaries
top_3 = updated_salaries[:3]
print("Top 3 Highest Salaries:", top_3)
