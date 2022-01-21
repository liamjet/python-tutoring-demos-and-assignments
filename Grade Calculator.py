# Grade Calculator

def WhatIsYourGrade():
    grade = float(input("Enter your grade: "))
    if grade >= 90:
        print("You have an A!")
    elif grade >= 80:
        print("You have a B!")
    elif grade >= 70:
        print("You have a C!")
    elif grade >= 60:
        print("You have a D!")
    else:
        print("You have an F.")


run = True
while run == True:
    
    WhatIsYourGrade()

    choice = input("Type Y to continue, type N to quit: ")
    if choice == "N":
        run = False
