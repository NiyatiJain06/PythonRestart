#Before OOPs come same problem's are occur on our code, understand with example
#Example: School Managment System

#Student1 data
s1_name = "Om"
s1_marks = 85
s1_attendance = 90

#Student2 data
s2_name = "Arun"
s2_marks = 92
s2_attendance = 88

def Check_grades(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    else:
        return "Fail"

def Update_Marks(old_marks, new_marks):
    return new_marks

print("Student:", s1_name)
print("Marks:", s1_marks)
print("Grade:", Check_grades(s1_marks))
print("Attendance:", s1_attendance)
print()

print("Student:", s2_name)
print("Marks:", s2_marks)
print("Grade:", Check_grades(s2_marks))
print("Attendance:", s2_attendance)
print()

s1_marks = Update_Marks(s1_marks, 99)

print("After Update")
print("Student:", s1_name)
print("Marks:", s1_marks)
print("Grade:", Check_grades(s1_marks))
print("Attendance:", s1_attendance)
print()

