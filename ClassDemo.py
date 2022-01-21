# Classes

# A Class is a data type we create that contains multiple variables

# Let's make a class called Student

def printStudentInfo(student):
    print("Student Info:",student.name)
    print("Name:",student.age)
    print("School:",student.school)
    print("GPA:",student.GPA)

class Student:
    name = ""
    age = 0
    school = ""
    GPA = 0.0

Liam = Student()
Liam.name = "Liam"
Liam.age = 18
Liam.school = "Santa Monica College"
Liam.GPA = 3.78

printStudentInfo(Liam)
