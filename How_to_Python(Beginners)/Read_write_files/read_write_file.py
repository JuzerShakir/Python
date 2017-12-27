""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 19 Dec 2017 8:48pm
Topic : How to read & write files in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# opening a file with open function
# giving 'r' parameter to tell python that we only want to read the file
# storing the file in a variable
r = open('read_test.txt', 'r')
# the read function will read the contents of the variable in which the file is stored....
#....and store that content in new variable
r_content = r.read()
# calling the variable that has the contents of the file to print
print(r_content)
# we have to close the file after we have done opeed in order to free up memory
# by giving close function to the variable
r.close()
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# giving second parameter 'w' called write will write the data in the file specified
# CAUTION : this write will delete previous data from the file and write new data
w = open('write_test.txt', 'w')
w.write("Hi! I have been written by write function!")
w.close()
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# giving second parameter 'a' called append will add the data in the file specified
a = open('write_test.txt', 'a')
a.write(" + I have been added by append function!")
a.close()
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# the 'with' function is used if we don't want to use close function for closing files for each file we call
# the 'with' function automatically closes for us
# where 'f' is variable which stores the file
with open('write_test.txt', 'r') as f:
    f_content = f.read()
    print(f_content)
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# That's it!
print("\nThe END!")
