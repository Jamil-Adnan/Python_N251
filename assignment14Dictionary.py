mydict = {}
word = "alchoholic"
for item in word:
    if item in mydict.keys():
        mydict[item] = mydict [item] + 1
    else:
        mydict [item] = 1
print (mydict)