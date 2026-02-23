# Attendance Tracker
# 1 = Present, 0 = Absent

attendance = list(map(int, input("Enter attendance (1 for Present, 0 for Absent) separated by space: ").split()))

total_days = len(attendance)
present_days = sum(attendance)

# 1. Calculate attendance percentage
percentage = (present_days / total_days) * 100 if total_days > 0 else 0
print("Attendance Percentage:", round(percentage, 2), "%")

# 2. Identify if below 75%
if percentage < 75:
    print("Status: Below 75% Attendance")
else:
    print("Status: Eligible (75% or above)")

# 3. Replace consecutive absences (0 0) with warning flag
modified_attendance = attendance.copy()

for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i + 1] == 0:
        modified_attendance[i] = "⚠"
        modified_attendance[i + 1] = "⚠"

print("Attendance with Warning Flags:", modified_attendance)