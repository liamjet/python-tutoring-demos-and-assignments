# Loops

#run = True
#while run == True:
#    print("INFINITE WORDS")

# DO NOT DO THAT

run = True
while run == True:
    print("This program goes in circles unless you say no.")
    choice = input("Type y to run again, type n to stop: ")
    if choice == "n":
        run = False

