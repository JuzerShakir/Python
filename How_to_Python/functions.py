""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 7:17pm
Topic : How to function in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#default argument
#this function takes one arguments of sex
#the value of sex variable will be defined at the time of calling the function by giving value as an argument
#checks wether entered value is male or female
#if not entered, will print the default argument
#defining function by giving an argument with a default value
def get_gender(sex="Unknown"):
    if sex is "m":
        print("You're Male")
    elif sex is "f":
        print("You're Female")
    else:
        print(sex)

#calling function by giving argument
get_gender("m")
get_gender("f")
get_gender()
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#unlimited arguments
#defining function with unlimited arguments
#give an '*' to the varible name (argument)
#this function will sum all numbers given
def add_numbers(*num):
    total = 0
#will loop through each arguments
    for a in num:
        total += a
    return total

#calling function by giving how many arguments i want and printing the result
print("\nThe sum of all numbers are",add_numbers(1, 10, 20))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#That's it!
print("\nThe END!")
