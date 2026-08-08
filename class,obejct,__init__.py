class Student:

    School = "Delhi public school"
    def __init__(self, name, marks, attendance):
        self.name=name
        self.marks=marks
        self.attendance=attendance

    def Calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"    

s1 = Student("Rohit", 85, 90)
s2 = Student("Karan", 75, 92)
print(s1.name)
print(s2.name)
print(s1.Calculate_grade())
print(Student.School)
