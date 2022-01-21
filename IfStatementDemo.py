# Take two user values and print the greatest one

number1 = int(input("Enter one number: "))
number2 = int(input("Enter another number: "))
if number1 > number2:
    print("The greater number is",number1)
elif number1 < number2:
    print("The greater number is",number2)
else:
    print("The numbers are equal.")
