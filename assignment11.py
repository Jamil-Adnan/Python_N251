myString = "Eshikhon"
for i in range (len(myString)-1, -1, -1):
   #print ("index", (i), "=>", myString[i])
   print (f"index {i} => {myString[i]}")   # f string format same as c#
   
   for i in range (len(myString)):
      print (myString[i], end = "")    #prints everything on the same line