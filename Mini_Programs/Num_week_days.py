""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 1:15pm
Topic : Calculating no. of week and days"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#defining function with one argument which will take a whole number(no. of days)
def timetable_week(days):
    #checks whether the number isn't zero
    if days != 0 and days > 0:
        #outputs number of week, result will be whole number
        week = days//7
        #outputs number of days, results will be remainder of the calculation
        remaining_days = days%7
        return "{} week(s) and {} day(s).".format(week, remaining_days)
    else:
        return "Please Input only a whole number other than zero for clean results."

#calling the function by passing the argument
print(timetable_week(1001))

#That's it!
print("\nThe END!")
