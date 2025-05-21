"""
Write a Python function unique_elements(lst) that takes a list as input and returns a set of unique elements in the list. The function should ignore duplicate values and utilize a set to store the unique elements.
"""

def uniqueElements(lst):
    newset = set()
    for i in range (len(lst)):
        newset.add(lst[i])
    print (f"The unique set is: {newset}")

try:
    numbers= []
    size = int (input("Please insert the size of the list: "))
    for i in range (size):
        numbers.append(int(input("Please insert an integer: ")))
except ValueError:
        print ("Eror! Input must be an integer.")

uniqueElements(numbers)    