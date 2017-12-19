""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 1:15pm
Topic : How to sets in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#before we go explore the sets function lets take an example of grocery_list function
#lets first give a simple list of groceries
#it was written in hurry furry by my worker, so it might have items which are being repeated twice
#in order to prevent buying one stuff twice, we will give another empty list, loop through grocery_list and remove...
#...items that are repeated
grocery_list = ["butter", "cheese", "bread", "tomato", "egg", "butter", "milk",
            "yoghurt", "wheat", "milk", "cheese"]
#defining empty list
grocery_list_right = []

print("This is the messed up grocery list :",grocery_list)

#looping through 'grocery_list'
for groceries in grocery_list:
#checking if the item already exist in the 'grocery_list_right'
    if groceries not in grocery_list_right:
#if not, then an item is added to the 'grocery_list_right'
        grocery_list_right.append(groceries)
print("\nThis is the correct grocery list using loop:")
print(grocery_list_right)
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#now lets try this same problem by giving 'sets'
#sets is a type of list in which the element can't be repeated
#defining a new list to store the the new values of the list
grocery_set_right = set(grocery_list)
#the sets function will not print out the values as given in order in the list
#also sets are defined by curly braces not square brackets as list
#printing out the list
print("\nThis is the correct grocery list using sets:")
print(grocery_set_right)
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#That's it!
print("\nThe END!")
