eshikhon = ["e","s","h","i","k","h","o","n"]    
eshikhon.reverse()                              
print (f"Reversed Order: {eshikhon}")           #reverse prints a list
numbers = [12,23,39,42,57,69,74,88,96]
print (numbers [::-1])                          #reverse prints a list
"""
This is an example of list slicing in Python. Slicing uses the format [start:stop:step], where:start: The index where the slice begins (inclusive). If omitted, it defaults to the beginning of the list. stop: The index where the slice ends (exclusive). If omitted, it defaults to the end of the list. step: The increment between elements. If omitted, it defaults to 1. A negative step means traversing the list in reverse.
In numbers[::-1]:
No start is specified (before the first colon), so it starts from the end of the list.
No stop is specified (between the colons), so it goes all the way to the beginning.
step is -1 (after the second colon), meaning it moves backward one element at a time.
"""

MaxMinNumbers = [14,26,9,47,99,62,13,87,99,3,82]
print (f"\nThe Min value is: {min(MaxMinNumbers)}")
print(f"The Max value is: {max(MaxMinNumbers)}")

MaxMinNumbers.sort()
print (f"\nThe Min value is: {MaxMinNumbers[0]}")
print(f"The Max value is: {MaxMinNumbers[len(MaxMinNumbers)-1]}")

print (f"\nThe sum of all values is: {sum(MaxMinNumbers)}")
average = sum(MaxMinNumbers)/len(MaxMinNumbers)
print (f"\nThe Average of all the values is: {average:.2f}")


counter = (2,45,5,8,32,45,1,2,88,9,45,3,2,67)
print (f"\nThe number 2 appears {counter.count(2)} times in this tuple.")
print (f"\nThe Max value in the tuple is: {max(counter)}")
print (f"The Min value in the tuple is: {min(counter)}")
print ()
print (counter)

# With Loop
number = int (input("Please insert a number from the tuple above (insert  45 for best result): "))
for num in counter:
    if num == number:
        print(f"\nThe number 45 exists in this tuple")
        break;  
      

print (number in (counter))
