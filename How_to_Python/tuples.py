""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 7:00pm
Topic : How to tuples in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# Tuples are like list, you can give multiple values to it that are always gonna be used together
# example dimensions of a box, latitude and longitude of a place..etc
# when giving tuples, parathesis to the value is optional
dimensions = 100, 20, 35
# tuple Unpacking
# tuple unpacking will store the values to these 3 variables corresponding to the values given to 'dimensions'
length, width, height = dimensions
print("The dimensions of the box are {} x {} x {}".format(length, width, height))

# giving a tuple inside a dictionary as a key
world_heritage_locations = {(13.4125, 103.866667): "Angkor Wat",
                            (25.73333, 32.6): "Ancient Thebes",
                            (30.330556, 35.4433330): "Petra",
                            (-13.116667, -72.583333): "Machu Picchu"}
# will print the value of this key
print(world_heritage_locations[25.73333, 32.6])


# That's it!
print("\nThe END!")
