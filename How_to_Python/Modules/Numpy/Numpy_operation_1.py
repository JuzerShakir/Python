""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 19 Dec 2017 10:10am
Topic : How to use numpy module in python (Introduction 1)

What Numpy can do?
#1. Find the dimension of the array
#2. Find the byte size of each element
#3. Find the data type of the elements
#4. Find the size of an array (finding total number of elements)
#5. Find the shape of an array (giving you no. of columns and rows)
#6. You can reshape the array
#7. You can slice the array
#8. Finding min, max and sum of the elements in the arrays"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

import numpy as np

#----1
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)
#this will give us the dimension of the numpy variable
dim = a.ndim
print("\nThe dimension of this array is --> {}".format(dim))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#----2
#this will give the byte size of the array
size = a.itemsize
print("\nThe size is --> {} bytes".format(size))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#----3
#this will give the data type the array
data_type = a.dtype
print("\nThe data type of this array is --> {}".format(data_type))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#----4
#this will give the size of the array(no.of elements)
size = a.size
print("\nThe number of elements in this array are --> {}".format(size))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#-----5
#this will give the shape of the array (no. of rows and no. of columns)
shape = a.shape
print("\nThere are {} number of rows and columns respectively.".format(shape))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#-----6
#this will reshape the shape of the array to different rows and columns (arguments - (r,c))
reshape = a.reshape(3, 2)
print("\nThe new shape of the array is \n {}".format(reshape))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#-----7
#this will output a specific number in the elemnts of an array(arguments (r,c))
n = a[0,2]
print("\nThe number at the first row and third column is {}".format(n))
#printing third column of every rows (arguments (r,c))
n3 = a[0: ,2]
print("\nThe number at every row of third column is {}".format(n3))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

#----8
#Finding maximum value in the array
maxn = a.max()
print("\nThe maximum value in this array is {}".format(maxn))
#Finding minimum value in the array
minn = a.min()
print("\nThe minimum value in this array is {}".format(minn))
#Finding sum of all the value in the array
sumn = a.sum()
print("\nThe sum of all the value in the array is {}".format(sumn))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#That's it!
print("\nThe End!")
