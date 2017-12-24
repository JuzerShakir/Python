""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 19 Dec 2017 9:18am
Topic : How to use matplotlib module in python (using Scatter plot)
Result : Results shown in this directory named 'scatter_plot.png'"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# importing module
from matplotlib import pyplot as plt
from matplotlib import style

# displays background grids with default white color
style.use("ggplot")

# co-ordinates of the points
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [20, 25, 30, 15, 18, 11, 24, 30, 20, 13]
# plotting points on the graph
plt.scatter(x, y, label="xyz", color='g')

# title of graph
plt.title("Scatter Plot")
# labeling x-axis
plt.xlabel("Age")
# labeling y-axis
plt.ylabel("Brain Cells")
# changing the grid lines color
plt.grid(True, color='k')
# displaying graph
plt.show()


# That's it!
