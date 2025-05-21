#number = 54
#print ("Magic Number" if number % 6 == 0 and number % 9 ==0 else "Not a Magic Number")
number = 54

side1 = 5
side2 = 11
side3 = 8
if side1+side2 > side3 and side2+side3 > side1 and side3+side2 > side1:
    if side1 == side2 == side3:
        print("Equilateral")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print ("Isosceles")
    else:
        print ("Scalene")

else:
    print ("Invalid")
    