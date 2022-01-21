# Make a program that repeats and can do addition, multiplication, subtraction
# and division between two user picked numbers

run = True
while run == True:
    print("This program can do basic arithmetic.")
    operator = input("Please enter [1] for addition, [2] for subtraction, [3] for multiplication, and [4] for division: ")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    if operator == "1":
        result = number1 + number2
        
    elif operator == "2":
        result = number1 - number2
        
    elif operator == "3":
        result = number1 * number2

    elif operator == "4":
        result = number1 / number2
    
    print("The answer is",result)

    again = input("Would you like to try again? [y/n]")
    if again == "n":
        run = False

print("Goodbye.")
