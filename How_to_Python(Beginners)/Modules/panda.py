""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 18 Dec 2017 11:15pm
Topic : Experimenting pandas module in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# importing pandas module and renaming it as 'pd'
import pandas as pd

# defining a dictionary
XYZ_web = {'Day': [1, 2, 3, 4, 5, 6],
           'Visiotrs': [1000, 700, 6000, 1000, 400, 350], 'Bounce_rate': [20, 20, 23, 15, 10, 34]}
# making that dictionary a datatframe with pandas and storing it in a variable
df = pd.DataFrame(XYZ_web)
# printing dataframe
print(df)

#--- SLicing dataframes ---
print('\nSlice')
#'head' function prints the first number of rows(as passed by argument) of the dataframe
print(df.head(2))
#'tail' function prints the last number of rows(as passed by argument) of the dataframe
print(df.tail(1))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#---Merging---
# only rows which have like values in two variables will be printed
print('\nmerge')
# defining 2 variables with a dataframes
ABC_web = pd.DataFrame({'Day': [1, 2, 3, 4, 5, 6], 'Visiotrs': [
                       1000, 700, 6000, 1000, 400, 350], 'Bounce_rate': [20, 20, 23, 15, 10, 34]})
DEF_web = pd.DataFrame({'Day': [1, 2, 3, 4, 10, 6], 'Visiotrs': [
                       10000, 700, 6000, 1000, 400, 350], 'Bounce_rate': [20, 20, 23, 15, 10, 33]})
# merging two dataframes by giving the variables as argument
merge = pd.merge(ABC_web, DEF_web)
# only the cells which have like values in two variables will be printed
print(merge)

# this variable will print only merging the day column
merge1 = pd.merge(ABC_web, DEF_web, on="Day")
# only the rows which have like values in 'Day' column of two variables will be printed
print(merge1)
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#---Joining---
print('\nJoining')
# defining 2 variables with a dataframes
ABC = pd.DataFrame({'Int_rate': [1, 2, 3, 4, 5, 6], 'Int_GDP': [
                   1000, 700, 6000, 1000, 400, 350]}, index=[2001, 2002, 2003, 2004, 2005, 2006])
DEF = pd.DataFrame({'Low_tier_HPI': [8, 10, 13, 14, 110, 16], 'Unemployment': [
                   10000, 7000, 60000, 10000, 4000, 3500]},  index=[2001, 2002, 2003, 2004, 2005, 2006])
# joining two dataframes
join = ABC.join(DEF)
# only the cells which have like values in two variables will be printed
print(join)
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


# That's it!
print("\nThe END!")
