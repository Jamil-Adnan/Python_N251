"""List practice"""
numbers = [12,54,25,36,44,78,21,98]
for i in range (0, len(numbers), +1):
    if numbers [i] % 2== 0:
        print (f"{numbers[i]} = even")
    else:
        print (f"{numbers[i]} = odd")
        
numbers [2] = 31        # changes thevalue of index 2
numbers.append(63)  #adds a value at the end of the list
