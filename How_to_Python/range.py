""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 1:15pm
Topic : How to use range in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# this range function creates a loop without a list
# this range function will print values from 0 - 9, which are 10
print("Prints value form 0-9")
for numbers in range(10):
    print(numbers)

# we can give specific range to print from-to
# this range function will print values from 10 - 20,
print("Prints values form 10-20")
for numbers in range(10, 21):
    print(numbers)

# we can not only give specific range to print from-to
# but also increament the value by x
# this range function will print values from 10 - 50 with increament of 5 in each execution
print("Prints numbers from 10-50, increaments the value by 5")
for numbers in range(10, 51, 5):
    print(numbers)

# we can also give a string to repeat x times
print("Prints this message 3 times")
for reminder in range(3):
    print("This is range function in business!")


# That's it!
print("\nThe END!")
