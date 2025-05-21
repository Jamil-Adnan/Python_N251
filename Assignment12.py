even = []
odd = []
for i in range (1,101):
    if i % 2 ==0 :
        even.append(i)
    else:
        odd.append(i)
        
for  number in even:
    print (f"{number}", end = "")
print ("\n")
for number in odd:
    print (f"{number}", end = "")
#print (even)
#print (odd)