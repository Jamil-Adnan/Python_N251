
"""temp = int (input("What is the temperature today: "))
if temp <= 25:
    print ("Its cold today.")
elif temp >25 and temp < 35:
    print ("its hot today")
else:
    print("Feels like dessert!!")
    
    
subject = []
for i in range (1, 4):    
    question = int (input(f"how much did u score in {subject[i]} : "))
    subject[i].append(question) 
print (subject)


total = 0
avg = 0
counter = 0
while (True):
    number = int (input("Insert a number: "))
    total += number
    counter += 1
    cont = input ("Want to continue?(y/n) : ")
    if cont== "N" or cont =="n":
        avg = total/counter
        print (f"The average is {avg}")
        break

"""

total = 0
count = 0
for i in range (1000):
    number = input ("please enter a number: ")
    if number == "stop":
        break
    else:
        number = int (number)
        total += number   
        count += 1
print (f"Sum of the numbers: {total}, and the Average is {total/count}")
    
    