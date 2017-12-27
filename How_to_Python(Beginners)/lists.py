""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 12:27pm
Topic : How to list in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# defining lists in python
list1 = [1, 2, 3, 4, 5, 6]
print("\nThe elements in the list are", list1)

# displaying 3rd element in list1
# since the list indexing starts at 0
print("Printing the third element in the list", list1[2])

# displaying 2nd element(including) to 4th element(excluding) from list1
print("\nDisplaying specific range of elements")
print(list1[1:3])
# displaying list from one end to other
print(list1[:2])
print(list1[1:])
# displaying whole list
print(list1[:])

# you can also add list to a list
# added by plus(+) operator,joining two elemnts of list
# list1 list won't change, the list is added only for this function(temporary change)
print("\nThis list has new elemnts been added, for temporary", list1 + [7, 8, 9, 10])

# permenant change in list
# append function adds an element to the end of the list, it takes only one argument
list1.append(7)
print("\nThis list has a new list elemnts been added, this time its permenant", list1)

# adding list to list and storing that to another variable
sort_list = list1 + [8, 9, 10, 11, 12]
print("\nThe previous list and new list elements have been added forming this new list", sort_list)

# Changing values of the list by calling the element one by one or in range
sort_list[:6] = [101, 102, 103, 104, 105, 106]
print("\nAssigning new value to the elements to the first half of the list", sort_list)
sort_list[6:] = [107, 108, 109, 110, 111, 112]
print("Assigning new value to the elements to the second half of the list", sort_list)

# will remove all the list elements if range of the list is given value of empty brackets
# removing first half elements
sort_list[:6] = []
print("First half elements of list deleted! ", sort_list)
# removing all elements
sort_list[:] = []
print("All elements of list deleted! ", sort_list)
print('\n')
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# A man wants to buy groceries but unfortunately someone has added entries of the same products twice
# to not buy same products twice we need a program to avoid this
# this is how its done

# giving a list of lists
# giving a list of groceries where each element in 'grocery_list' conatains....
#.... two elemnts where first element is product name and second is it's quantity
grocery_list = [["butter", 2], ["cheese", 3], ["bread", 4], ["tomato", 2], ["egg", 12], ["butter", 2], ["milk", 3],
                ["yoghurt", 5], ["wheat", 2], ["milk", 3], ["cheese", 3]]

# giving two empty list, one for items to buy and other for quantity
grocery_item_list = []
grocery_quantity_list = []

# looping through each grocery in grocery_list
for grocery in grocery_list:
    # checking if the element in 'grocery' of 'grocery_list' is not in 'grocery_item_list'
    if grocery[0] not in grocery_item_list:
        # if not, adding the item from 'grocery' to 'grocery_item_list'
        grocery_item_list.append(grocery[0])
# adding the quantity from 'grocery' to 'grocery_quantity_list'
        grocery_quantity_list.append(grocery[1])

# now we want to print both the list's element in a single line
# this will print how many quantities of groceries we have to buy
for i in range(len(grocery_item_list)):
    print("Buy " + str(grocery_quantity_list[i]) + " quantities of " + grocery_item_list[i])
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# That's it!
print("\n\nThe End!")
