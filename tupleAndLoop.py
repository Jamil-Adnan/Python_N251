"""
Write a Python function count_occurrences(tpl, target) that takes a tuple of values and a target value as inputs. The function should return the number of occurrences of the target value in the tuple. Use a loop to iterate through the tuple and use the continue statement to skip any non-matching values.
"""

def countOccurences(tpl, target):
    counter = 0
    for element in tpl:
        if element == target:
            counter += 1
        else:
            continue
    return counter
    
    
try:
    tplList = []
    tplSize = int (input("Please insert the size of the tuple: "))
    for i in range (tplSize):
        tplList.append(int(input("Please insert an integer: ")))
    tpl = tuple(tplList)
    
    target = int (input("Please insert the target value: "))    

except ValueError:
        print ("Eror! Input must be an integer.")

print (f"The number of occurrances is :{countOccurences(tpl, target)}")  