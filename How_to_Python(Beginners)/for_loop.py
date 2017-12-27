""" Author : Juzer Shakir   ||  Created on 10 Nov 2017     ||   Last modified on 10 Dec 2017 7:50pm
Topic : How to loop(for loop) in python"""

"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""1"""
# assigning list with names
names = ["Sushrutha", "Juzer", "Anjali", "Mustafa", "Dhwani", "Mannu"]

# the for loop will print each list's elements
# stored in 'names' variable and prints it
# it also prints the lenght of the elements
# continues to repeat this process until there are no elements left in the list
for name in names:
    print("\nMy name is", name)
    print("Number of character my name has is ", len(name))
print("\n")

# this will print elements value from the list with specific range
for name in names[0:2]:
    print("Someone is in love with", name)
print("\nMay be they both love each other! HAHA!!")

print("\n")
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""


"""2"""
# inviting new operator called break
# this break operator breaks the loop once the condition have been met
# also saves lots of processing time and memory
# giving a value to a variable
n = 51
# this loop will check the number from 0-100
for num in range(101):
    # checks the value of n to num variable
    if num is n:
        # the line of codes print as the conditions meets above
        print("{} is my lucky number".format(n))
# since the condition has already been met and desired statement has been printed...
#..lets break the loop
        break
print("\n")
"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""3"""
# inviting new operator called continue
# this continue operator continues the loop and ignores the rest of the code after it in the loop
# giving a list of numbers
test1 = [1, 3, 5, 7, 9, 11]
# giving a loop to iterate over the the range of numbers, if the number exist in the test1 list...
#...that number will not be printed and loop will continue to the next number
for n in range(1, 13):
    if n in test1:
        continue
    print(n)

"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

# That's it!
print("\nThe END!")
