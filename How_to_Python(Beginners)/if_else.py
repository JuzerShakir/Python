""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 12:07pm
Topic : How to if-else in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# this doesn't has to make sense but you get the idea of what the program does
# Assigning names to variables
my_name = "Juzer"
friend_name = "Huzefa"

# Decision code
# IF 'if', 'elif(else if)' statements return true value, the block of code under those statements is executed
# if statement checking if the variable value is "Juzer" with 'is'
if my_name is "Juzer":
    print("Your name is", my_name)
# if the first if statement is true then the following elif or else will not be checked
elif friend_name is "Huzefa":
    print("Your freind's name is ", friend_name)
else:
    print("So sad! You have no name!:(")

print("\n")
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# defining list
full_name = ["Juzer ", "Shabbir ", "Shakir"]
# checking list elements value to print the name
# checking first element
if full_name[0] is "Juzer ":
    # checking second element
    if full_name[1] is "Shabbir ":
        # checking third element
        if full_name[2] is "Shakir":
            print("Your fullname is Juzer Shabbir Shakir")
# will print if third value is false
        else:
            print("Your half-name is Juzer Shabiir")
# will print if second value is false
    else:
        print("Your name is Juzer")
# will print if first value is false
else:
    print("Sorry! You're not invited!")
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# That's it!
print("\nThe END!")
