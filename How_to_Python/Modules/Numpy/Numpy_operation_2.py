""" Author : Juzer Shakir   ||  Created on 19 Dec 2017     ||   Last modified on 19 Dec 2017 10:27am
Topic : How to use numpy module in python (Introduction 2)

What Numpy can do?
#9. Finding sum of rows or columns
#10. Finding sqaure root
#11. Finding Standard deviation
#12. Performing basic arithmetic with arrays(add, substarct, multiply, divide)
#13. Concatinating numpy's vertically and horizontally
#14. Combining all columns into single columns
#15. Exponential and logarithmic function
#16. Linspace function"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])

#----9
#Finding sum of the elemnts by columns
#axis = 0 means column
colsum = a.sum(axis = 0)
print("\nThe sum of all the value in the array by columns are {}".format(colsum))
#Finding sum of the elemnts by rows
#axis = 1 means rows
rowsum = a.sum(axis = 1)
print("\nThe sum of all the value in the array by rows are {}".format(rowsum))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#----10
#Finding sqaure root of each element in the array
sqrt = np.sqrt(a)
print("\nThe sqaure root of each elements are \n{}".format(sqrt))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#----11
#Finding standard deviation of the array
stnd = np.std(a)
print("\nThe standard deviation of array is \n{}".format(stnd))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#lets set another numpy array for performing arithmetic calculations
b = np.array([(10, 11, 12), (13, 14, 15)])
print("\nAnother numpy array given for calculations \n{}".format(b))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#-----12
#Finding the sum of two arrays
asumb = a + b
print("\nThe sum of two arrays are \n{}".format(asumb))
#Finding the substraction of two arrays
aminusb = a - b
print("\nThe substraction of two arrays are \n{}".format(aminusb))
#Finding the multiplication of two arrays
amultib = a * b
print("\nThe multiplication of two arrays are \n{}".format(amultib))
#Finding the division of two arrays
adivb = a / b
print("\nThe division of two arrays are \n{}".format(adivb))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#---13
#Concatinating numpy's vertically
vstack = np.vstack((a, b))
print("\nVertically stacked numpy's \n{}".format(vstack))
#Concatinating numpy's horizontally
hstack = np.hstack((a, b))
print("\nHorizontally stacked numpy's \n{}".format(hstack))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#----14
#Combining columns of a numpy into a single column
single_a = a.ravel()
print("\nThe first numpy array now have a single column\n{}".format(single_a))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#----15
#Exponential function
ex_a = np.exp(a)
print("\nThe elements of the first numpy array raised to the e power =\n{}".format(ex_a))
#logarithmic function
#natural logarithmic (ln)
log_a = np.log(a)
print("\nThe natural log of the elements of the first numpy array =\n{}".format(log_a))
#logarithmic (ln) with base 10 or log
log_a = np.log10(a)
print("\nThe log with base 10 of the elements of the first numpy array =\n{}".format(log_a))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#---16
#the first value passed in the argument will be the value to start with
#second will be the value to end at
#third will be how many numbers do you want in between first and second arguments
al = np.linspace(1, 5, 10)
print("\nThese are 10 numbers in between 1 and 5 \n{}".format(al))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#That's it!
print("\nThe End!")
