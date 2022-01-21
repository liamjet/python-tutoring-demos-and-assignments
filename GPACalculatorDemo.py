# GPA Calculator

def AddList(list1):
    total = 0

    for i in range(0,len(list1)):
        total = total + list1[i]
    return total

numClass = int(input("Enter the number of classes: "))
letterGrades = []
numGrades = []

for i in range(0,numClass):
    grade = input("Enter the letter grade for class: ")
    letterGrades.append(grade)

print("These are the letter grades you entered:",letterGrades)
    
for x in letterGrades:
    if x == "A":
        numGrades.append(4.0)
    elif x == "B":
        numGrades.append(3.0)
    elif x == "C":
        numGrades.append(2.0)
    elif x == "D":
        numGrades.append(1.0)
    else:
        numGrades.append(0.0)

print("These are the numerical grades you entered:",numGrades)

sumGrades = AddList(numGrades)

GPA = sumGrades / numClass
print("Your GPA is:",GPA)
