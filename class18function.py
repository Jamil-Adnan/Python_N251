def makeSquare (x):
    result = []
    for numbers in x:
        result.append(numbers*numbers)
    return result   
    
    
x = [2,3,4,5]
print (makeSquare(x))
square = makeSquare(x)
print (square)


def evenOrOdd(number):
    if number%2 == 0:
        return "even"
    else:
        return "odd"


input = int (input("Please insert a number: "))
print (evenOrOdd(input))