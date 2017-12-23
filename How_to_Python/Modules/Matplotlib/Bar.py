""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 19 Dec 2017 9:18am
Topic : How to use matplotlib module in python (using Bar Graph)
Result : Results shown in this directory named 'bar.png'"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# importing module
from matplotlib import pyplot as plt

# plotting bars of two topics, cars and bikes
# giving two lists where first list contains values of 'x' and second of 'y'
plt.bar([1, 3, 5], [2, 6, 4], color='g', label="cars", width=0.1)
plt.bar([2, 4, 6], [10, 5, 3], color='b', label="bikes", width=0.1)

# title of graph
plt.title("Cars vs Bikes")
# displays legend on the graph
plt.legend()
# labeling x-axis
plt.xlabel("days")
# labeling y-axis
plt.ylabel("Accidents")
# displaying graph
plt.show()


# That's it!
