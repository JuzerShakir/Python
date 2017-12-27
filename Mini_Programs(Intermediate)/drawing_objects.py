""" Author : Juzer Shakir   ||  Created on 20 Nov 2017     ||   Last modified on 25 Dec 2017 10:13am
Topic : To do draw a Circle with sqaure in python using classes"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# turtle is a module which has many funtions inside each class
import turtle


def draw_circle():
    # a varibale is given to store all of the functions of the class 'Turtle' of a module 'turtle'
    sqaure = turtle.Turtle()
# this shape function changes the pointers shape in turtle
    sqaure.shape('turtle')
# Increaing the speed of execution of drawing
    sqaure.speed(10)

# we need to know how many sqaures of equal dimentions we need to make a circle
# in order to know that, we need to decided how much degrees we should rotate in
# a circle is 360 degree round figure, so if we rotate the pointer 10 degrees after a sqaure is drawn ...
#....to make another square, we have to make 36 sqaure such.
# because 10(degrees rotated) * 36(number of sqaures) = 360 degree(angle of a circle)
# so lets define some variables

# number of sqaure drawn
    current_sqaure = 0
# total number of sqaures needed
    total_sqaure = 36

# giving loop to a sqaure to make a circle
    while current_sqaure < total_sqaure:
        # number of lines in sqaure is 4
        lines_in_sqaure = 0
# giving loop to lines of a sqaure to make a sqaure
        while lines_in_sqaure < 4:
            # the function 'forward' moves the turtle cursor forward by the value passed in the parameters
            sqaure.forward(100)
            # the 'right' function rotates the cursor right by 90 degrees since the sqaures interior angles are 90 degrees
            sqaure.right(90)
            # so by moving forward by x as changing the turtle cursor position by 90 degrees we have made a line
            # so now lets increament its value
            lines_in_sqaure += 1
# after making a sqaure, the pointer will rotate to 10 degrees to make another sqaure
        sqaure.right(10)
# since we have made a sqaure, lets increament its value
        current_sqaure += 1


# calling function to execute the diagram
draw_circle()

# That's it!
