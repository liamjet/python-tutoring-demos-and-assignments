# Lists Demo

# Lists are essentially a bunch of variables of one type strung together.
# A list can only have one type. So an integer list, a string list, or float list
# Each value in a list is called an element
# Each element has an index, starting from 0.

myList = [1,2,3,4,5]
print(myList)

# To access individual elements

print(myList[0]) # 0 is the first element in the list
print(myList[1]) # 1 is the second element in the list

# List elements can otherwise be used as normal variables with arithmetic
# Lists can be declared even without values in them

myList2 = []
print(myList2)

#To add values to a list

# Append adds it to the end
myList2.append(5)
myList2.append(7)
print(myList2)

# Insert adds it at a given index
myList2.insert(1,50)
print(myList2)

# To remove an item
myList2.remove(50)
print(myList2)

# To remove a specific index
myList2.pop(0)
print(myList2)
