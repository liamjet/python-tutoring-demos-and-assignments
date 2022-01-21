# GPA Calculator

def AddList(list1):
    total = 0

    for i in range(0,len(list1)):
        total = total + list1[i]

    return total


numClass = int(input("Enter the number the of classes: "))
letterGrades = []
numGrades = []

for i in range(0,numClass):
    grade = input("Enter the letter grade: ")
    letterGrades.append(grade)

for x in letterGrades:
    if x == "A" or x == "a":
        numGrades.append(4.0)
    elif x == "B" or x == "b":
        numGrades.append(3.0)
    elif x == "C" or x == "c":
        numGrades.append(2.0)
    elif x == "D" or x == "d":
        numGrades.append(1.0)
    else:
        numGrades.append(0.0)

sumGrades = AddList(numGrades)

GPA = sumGrades / numClass
print("Your GPA is: ",GPA)
