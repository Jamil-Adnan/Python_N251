dict = {0:45,1:69,2:3,3:587,4:78,5:105,6:3247,7:52,8:99,9:147,10:30068,11:20154,12:7,13:6547}
max = 0
key = 0
for k,v in dict.items():    # reads all the keys and values in the dictionary
    if dict[k] > max:
        max = dict[k]
        key = k
        
print (f"Maximum number is {max} and index is {key}")