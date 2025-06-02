lst = []

def push(lst, int1, int2):
    lst.append(int1)
    lst.append(int2)
    return lst

def peek(lst):
    print (lst[0])
    
def s_pop(lst):    
    number = lst.pop(0)
    return lst,number
    
print(push(lst, 4, 6))

print(peek(lst))

lst,number = s_pop(lst)
print (lst,number)
    