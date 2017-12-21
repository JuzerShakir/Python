""" Author : Juzer Shakir   ||  Created on 18 Dec 2017     ||   Last modified on 18 Dec 2017 7:46pm
Topic : Calculates the density of the population"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#defining function with two arguments - area of land(km) and population - to calculate density
def population_density(land_area, population):
    density  = population/land_area
    return density

#calling the function by giving arguments
print("The density of the population is : ",population_density(500, 2000))

#That's it!
print("\nThe END!")
