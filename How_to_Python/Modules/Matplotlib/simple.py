""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 19 Dec 2017 9:58am
Topic : How to use matplotlib module in python (using Bar Graph)
Result : Results shown in this directory named 'simple.png'"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#importing module
from matplotlib import pyplot as plt
from matplotlib import style

#this will add box like style in background
style.use("ggplot")

#defining list and will import this as an argument to plot function
#co-ordinates of 'first data'
x = [1, 2, 3, 4, 5, 6]
y = [5, 12, 6, 14, 17, 7]
#co-ordinates of 'second data'
x2 = [1, 2, 3, 4, 5, 6]
y2 = [3, 10, 16, 5, 12, 8]

#giving list as an argument to plt on graph
#plotting 'first data'
plt.plot(x,y, color = 'y', label = "first data", linewidth = 1)
#plotting 'second data'
plt.plot(x2,y2, color = 'g', label = "second data", linewidth = 1)

#printing the legend in the graph
plt.legend()
#giving the title to the graph
plt.title('Graph')
#labeling x and y axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#this will trigger the lines of the grid in the background by giving the color you want
plt.grid(True, color = 'k')
#outputs the graph
plt.show()


#That's it!
