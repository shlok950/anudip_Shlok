n = int(input("Enter the number of students: "))
students = {}

for _ in range(n):
    name, marks = input("Enter name and marks: ").split(",")
    students[name] = int(marks)

topper = max(students, key=students.get)
print("Topper:", topper)