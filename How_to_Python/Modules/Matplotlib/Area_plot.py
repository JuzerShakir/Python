""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 19 Dec 2017 9:18am
Topic : How to use matplotlib module in python (using area plot)
Result : Results shown in this directory named 'area_plot.png'"""

"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#importing module
from matplotlib import pyplot as plt

#x-axis
days = [1, 2, 3, 4, 5, 6, 7]
#y-axis
#all corresponding variales values should add upto equal value
sleeping = [8, 9, 8, 7, 7.5, 6.5, 8.5]
exercise = [2, 2, 3, 1.5, 2.5, 1, 2]
studying = [6, 6, 7, 8, 5, 7, 6]
playing = [8, 7, 6, 7.5, 9, 9.5, 7.5]

#each plot for each list
plt.plot([],[], color = 'm', label = "sleeping", linewidth = 3)
plt.plot([],[], color = 'k', label = "exercise", linewidth = 3)
plt.plot([],[], color = 'y', label = "studying", linewidth = 3)
plt.plot([],[], color = 'g', label = "playing", linewidth = 3)

#will stack the plot on top of each other on a single graph
plt.stackplot(days, sleeping, exercise, studying, playing, colors = ['m','k','y','g'])

#title of graph
plt.title("Area Scatter Plot")
#labeling x-axis
plt.xlabel("Days")
#labeling y-axis
plt.ylabel("Spending time")
#displaying graph
plt.show()


#That's it!
