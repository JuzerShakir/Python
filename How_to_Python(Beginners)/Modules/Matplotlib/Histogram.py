""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 19 Dec 2017 9:18am
Topic : How to use matplotlib module in python (using Histogram)
Result : Results shown in this directory named 'histogram.png'"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# importing module
from matplotlib import pyplot as plt

#'quantities' varaible contains list of numbers measured on y-axis
quantities = [22, 44, 35, 23, 20, 32, 36, 41, 37, 22, 27]
#(x-axis) 'bins' varaible contains list of numbers with Bin size of five in which 'quantities' values will be plotted
bins = [20, 25, 30, 35, 40, 45]
# plotting histogram by giving 'y' value first
plt.hist(quantities, bins, histtype='bar', rwidth=0.9)

# title of graph
plt.title("Histogram")
# labeling x-axis
plt.xlabel("Age")
# labeling y-axis
plt.ylabel("No. of Adults")
# displaying graph
plt.show()


# That's it!
