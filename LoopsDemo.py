# Loops Demonstration

# The simplest loop is the while loop which will repeat until a condition is met.
# For example:

#run = True
#while run == True:
    #print("INFINITE WORDS")

# A more practical use

run = True
while run == True:
    print("This program will repeat itself unless the user says it should not.")
    choice = input("Enter [y] to run again, enter [n] to stop: ")
    if choice == "n":
        run = False
print("You stopped the program.")


# The second loop to learn is the for loop but we'll learn that later
# when we do arrays
