""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 10:58pm
Topic : How to use module in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# importing a function name randrange from module named random
# randrange prints a random integer from (a <= N <= b)
from random import randrange

# defining a variable which will store random integer
x = randrange(1, 100)
print(x)
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# Download any image on the internet with a link
# downloads an image of the url given and saves with a new name with a random number from 1 - 1000
import urllib.request

# defining a function


def download_image(url):
    # this variable will have any random num from 1-1000
    name = randrange(1, 1000)
# adding an exension of an image file to the 'name' variable so that it has supoorted format to display image
    full_name = str(name) + ".jpg"
# this function will change the name
    urllib.request.urlretrieve(url, full_name)


# calling the function and argument as a link
download_image()
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# That's it!
print("\nThe END!")
