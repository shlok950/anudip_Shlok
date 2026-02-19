grade12_marks = int(input("Enter the marks obtained in grade 12: "))
is_maths = input("Did the student had mathematics? (yes/no): ").lower()
entrance_exam_marks = int(input("Enter the marks obtained in the entrance exam: "))
if(grade12_marks>=75 and is_maths=="yes" and entrance_exam_marks>=80):
    print("The student is eligible for admission.")
elif(grade12_marks<75):
    print("grade12_marks should be greater than or equal to 75")
elif(is_maths!="yes"):
    print("The student should have had mathematics.")
elif(entrance_exam_marks<80):
    print("entrance_exam_marks should be greater than or equal to 80") 