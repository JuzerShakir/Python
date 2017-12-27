""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 19 Dec 2017 10:36am
Topic : Proof that numpy is better compared to list with examples"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# importing numpy module as np
import numpy as np
# for measuring size taken by an element
import sys
# for measuring time taken to compute program
import time


#-----1. We will prove that numpy takes less memory than list

# giving list with a value ranging from 0 - 999
plist = range(1000)
# multiplying size of one element to the lenght of the list to get the total value occupied by whole list
size_plist_element = sys.getsizeof(1) * len(plist)
print("Size taken by list --> {}".format(size_plist_element))

# giving a numpy list with a value ranging from 0-999
nlist = np.arange(1000)
# multiplying size of one element to the lenght of the numpy list to get the total value occupied by whole list
size_nlist_element = nlist.size * nlist.itemsize
print("Size taken by numpy list --> {}".format(size_nlist_element))
print('\n')
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#-----2. We will prove that numpy takes less time to compute compared to list....
#... and also more convenient to compute

# defining a variable which holds the value of how many elements to be added in both lists
SIZE = 10000000
# giving two normal and two numpy list so that we can add corresponding elements of the lists not concatenate
l1 = range(SIZE)
l2 = range(SIZE)

nl1 = np.arange(SIZE)
nl2 = np.arange(SIZE)

# the start variable will store the amount of time taken to compute the code till now
start = time.time()
# the result variable stores the added value of the corresponding elements of the lists
result = [(x, y) for x, y in zip(l1, l2)]
# the ltime variable will give time taken to add the above list
# time.time() gives total time taken to run the code till here and will substract the time taken to run till variable start.....
#.... This gives us time taken to run the loop to add list
# to see the run time more easily we multiply by more zeroes to move decimal places to the right
list_time = (time.time() - start) * 100
# will print time
print("The time taken to add normal list --> {}".format(list_time))

# the start variable will store the amount of time taken to compute the code till now
start = time.time()
# the result variable stores the added value of the corresponding elements of the numpy lists
result = nl1 + nl2
# this will give the time taken to add above numpy list
ntime = (time.time() - start) * 100
# will print time
print("The time taken to add numpy list --> {}".format(ntime))

print("\nTherefore numpy is fast, convenient and also takes less memory!")
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# That's it!
print("\nThe End!")
