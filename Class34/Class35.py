lst = [4,8,1,3,6,7]
for i in range (len(lst)):
    
    for j in range (len(lst)-1):
        temp = 0
        if lst[j] > lst[j+1] :
            temp = lst[j]
            lst[j] = lst[j+1]        
            lst[j+1] = temp
            
            
print (lst)
