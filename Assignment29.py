# Adds 2 numbers and returns the sum

add = lambda a,b : a+b
a = int (input("Number 1: "))
b = int (input("Number 2: "))
print (add(a,b))

# retruns the greater of 2 numbers

def maximum (a,b):
    return a if a>b else "Equal" if a==b else b  

a = int (input("Number 1: "))
b = int (input("Number 2: "))
print (maximum(a, b))

# returns True if the number is even, otherwise False

def is_even(num):
    return True if num > 0 and num % 2 == 0 else False

num = int (input("Number: "))
print(is_even(num))

# returns the factorial of a number

def factorial(n):
    total = 1
    for i in range(n, 1, -1):        
        total = total * i
    return total

n = int (input("Number : "))
print (f"Factorial of {n} is {factorial(n)}")

# returns the reversed version of an input string

def reverse_string(s):
    reversed_string = ""
    for i in range (len(s)-1,-1,-1):
        reversed_string += s[i]
    return reversed_string

s = input("Insert a string: ")
print (f"The reverse of {s} is {reverse_string(s)}")



        