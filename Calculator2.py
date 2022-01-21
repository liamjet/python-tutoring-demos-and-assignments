# Make a program that repeats and can do addition, multiplication, subtraction
# and division between two user picked numbers

run = True
while run == True:
    print("This program can do calculations.")
    operator = input("Enter a for addition, enter s for subtraction, enter m for multiplication, enter d for division: ")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    if operator == "a":
        result = number1 + number2

    elif operator == "s":
        result = number1 - number2

    elif operator == "m":
        result = number1 * number2

    elif operator == "d":
        result = number1 / number2

    print("The answer is",result)

    again = input("Would you like to try again? [y/n]")
    if again == "n":
        run = False
