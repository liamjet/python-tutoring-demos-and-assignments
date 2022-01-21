# Program Name: Odd or Even
# Purpose: Prints every odd or even number up to the inputted number

# Request input
print("Enter a number: ")
inputVariable = int(input()) # Cast input as int for for loop
print("Enter [0] to print all even numbers and enter [1] for all odd numbers")
oddOrEven = int(input()) # Cast input as int for if statement

# Conditional for odd or even
if oddOrEven == 0:
    # For loop to print all even numbers
    for i in range(0,inputVariable):
        if i % 2 == 0:
            print(i)
    
else:
    # For loop to print all even numbers
    for i in range(0,inputVariable):
        if i % 2 != 0:
            print(i)
