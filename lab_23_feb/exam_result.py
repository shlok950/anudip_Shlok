# Online Exam Result Processor

# Take input from user (space separated scores)
scores = list(map(int, input("Enter student scores separated by space: ").split()))

print("Original Scores:", scores)

# 1. Remove lowest 2 scores
if len(scores) > 2:
    scores.sort()
    removed_scores = scores[:2]
    scores = scores[2:]
    print("Removed Lowest 2 Scores:", removed_scores)
else:
    print("Not enough scores to remove lowest two.")

print("After Removing Lowest Scores:", scores)

# 2. Add grace marks of 5 to those scoring between 30–35
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

print("After Adding Grace Marks:", scores)

# 3. Count number of students passed (≥ 40)
passed_count = sum(1 for s in scores if s >= 40)

print("Number of Students Passed:", passed_count)