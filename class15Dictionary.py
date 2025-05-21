mydict = {}
mystring = ["4","1","4","4","5","3"]
print (len(mystring))

for i in range(len(mystring)):
    mydict[i+1] = mystring[i]
print (mydict)
