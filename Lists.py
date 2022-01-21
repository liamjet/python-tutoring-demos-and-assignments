# Lists

# Lists are a bunch of variables strung together.

myList = [5,10,35,15,6]
print(myList)
print(myList[3])

# Index - Each piece of a list has a number called an index
# Element - Each value in a list is called an element

# Append adds a number to the end of the list
myList.append(5)
print(myList)

# Insert adds a number at a given index
myList.insert(3,10)
print(myList)

# Remove a given value
myList.remove(35)
print(myList)

# Remove a specific index
myList.pop(1)
print(myList)

myList2 = ["this","list","is","made","of","strings"]
print(myList2)
