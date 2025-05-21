# import module library

import math

print (math.sqrt(36))   # prints the square root
print (math.pow(6,2))   # prints the power on a number, here 6 is the number and 2 is the power
print (math.factorial(5))   # prints the factorial
print(math.ceil(4.6897))
print(math.floor(4.6897))


import math as m    # imports math library and use as object m
print (m.sqrt(25))

from datetime import datetime, date
print (datetime.now())
print (date.today())
print (datetime.now().month)
print (datetime.now().year)

"""
We are going to create a file, open and read it. first creating a separate text file named test.txt
"""
file = open ("test.txt", "r").read()
file = open ("test.txt", "r").readline()
file = open ("test.txt", "r").readlines()
print (file)