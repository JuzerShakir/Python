""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 10 Dec 2017 7:31pm
Topic : How to dictionaries in python"""
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


"""1"""
#dictionaries is defined by curly braces, just as 'sets'
#dictionary has a key and a value, in which key can be a variable and its value is value.
#its like a list but in ecah element you have a key and value
#if you call key, it will print its value
#you can add key and its value by giving 'add' attribute
me = {"Juzer" : "Curious", "Mission" : "Python"}

#the get attribute will find "x" key in dictionary and return its value
#if it cannot find any key 'x' it will return output as 'None'
print(me.get('Age'))
#if you dont want output of the missing key as 'none' and want something else...
#..pass second argument in the form of string which will replace 'none'
print(me.get('Age' , "There\'s no such element!"))
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


"""2"""
#lets give a dictionary which makes sense in real life
#dictionary of grocery list where key will be the product to buy and the value will be its quantity
grocery_list = {'butter' : 2, 'cheese' : 4, 'milk' : 2}

#lets print the key and value of any element in dictionary
print("\nBuy " + str(grocery_list['butter']) + " quantities of butter")
print("\n")

#now lets use loop to print all of the products in the dictionary with key and value
#'k' is for key in dictionary
#'v' is for value in dictionary
for k, v in grocery_list.items():
    print("Buy " + str(v) + " quantities of " + k)
print("\n")
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


"""3"""
#Nesting dictionary
#outer dictionary is name of an individual as key while its value is inner dictionary storing the individuals details
identity = { "Juzer" : {"age" : 22, "weight" : 56, "status" : "single"},
            "Ibrahim" : {"age" : 21, "weight": 55, "status" : "single"}}
#calling the dictionary with specific key
print(identity["Juzer"])
#calling specific dictionary key
print(identity["Ibrahim"]["weight"])
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


#That's it!
print("\nThe END!")
