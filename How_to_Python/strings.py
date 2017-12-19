""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 1:15pm
Topic : How to output string in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#Assigning a string to a variable
first_name = "Juzer "
middle_name = "Shabbir "
surname = "Shakir "

#then add these variables to a single variable
full_name = first_name + middle_name + surname

#printing name on the screen
print("\nYour full name is \'{}\'.".format(full_name))

#name will be printed multiple times
print("\nYour name will be printed 3 times ",full_name * 3)

#printing out file location in python
print("\nPrinting the path of this file")
#since file location has '\' in the path name, it has different meaning in python
#we type 'r' before we start a string with file location
#we type 'r' so that it doesn't apply '\' characteristics and knows it's a file location to print
print(r"How_to_Python\strings.py")
print("\n")

#the 'len' function calculates the lenght of a string
print ("The lenght of my name ",len(full_name))
print("\n")

#slicing strings
#we can print from where to where the characters should be printed of the variable
#prints from start to the 3th character of the string
print(first_name[:3])
#prints from 3rd character to the last character of the string
print(middle_name[2:])
#prints from start to the 4th character of the string
print(surname[0:4])
print("\n")
#print from start to the end character of the string
print(full_name[:])


#That's it!
print("\nThe END!")
