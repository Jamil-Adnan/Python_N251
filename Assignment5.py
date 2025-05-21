"""
program-1 : takes a number as input and checks if it is negative, positive or zero
"""
number1 = float (input ("Please  insert a number: "))
if number1 < 0:
    print("The number is negative.")
elif number1 == 0:
    print ("The number is Zero.")
else :
    print ("The number is positive.")
    
"""
Program-2: takes a number (age) as an input and prints statements according to age category. 
"""
    
age = float (input("Please insert your age: "))
if age <= 0:
    print("You are not born yet.")
elif age >0 and age < 13:
    print ("Child.")
elif age >= 13 and age <= 19:
    print ("Teenager.")
else :
    print ("<Adult.")
    
"""
Program-3: takes a number as input and checks if it an odd or even number     
"""

number2= int (input("Please enter an integer: "))
if number2 % 2 == 0:
    print ("The number is even.")
else :
    print ("The number is odd.")
    
"""
Program-4: Takes a letter as input and checks if it is a vowel or consonant     
"""
letter = input ("Please insert a letter: ")
if letter == 'a' or letter == 'A':
    print ("It is a vowel.")
elif letter == 'e' or letter == 'E':
    print ("It is a vowel.")
elif letter == 'i' or letter == 'I':
    print ("It is a vowel.")
elif letter == 'o' or letter == 'O':
    print ("It is a vowel.")
elif letter == 'u' or letter == 'U':
    print ("It is a vowel.")
else:
    print ("It is a consonant.")
    
"""
Program-5: takes a number as input (marks) and prints grade according to the number    
"""
    
marks = float (input("How much did you score on python course: "))
if marks > 100:
    print("Please insert a valid input.")
elif marks >= 90 and marks <= 100:
    print ("Your grade is 'A'.")
elif marks >= 80 and marks < 90:
    print ("Your grade is 'B'.")
elif marks >= 70 and marks < 80:
    print ("Your grade is 'C'.")
elif marks >= 60 and marks < 70:
    print ("Your grade is 'D'.")
elif marks >= 0 and marks < 60:
    print ("You got 'F'. Try harder next time.")
else :
    print ("Invalid input!!")
    
    