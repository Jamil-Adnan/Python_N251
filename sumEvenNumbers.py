def sumEvenNumbers(lst):
    sum = 0
    for i in range (len(lst)):
        if numbers[i]%2==0:
            sum += numbers[i]
        else:
            continue
    print (f"The Sum of the even nunbers is {sum}")

try:
    numbers= []
    size = int (input("Please insert the size of the list: "))
    for i in range (size):
        numbers.append(int(input("Please insert an integer: ")))
except ValueError:
        print ("Eror! Input must be an integer.")

sumEvenNumbers(numbers)       
    



    
    