# lst = []

# lst.append('A')
# lst.append('B')
# lst.append('C')

# print(lst.pop())
# print(lst.pop())
# print(lst.pop())

# print(lst)

def push(lst, element):
    lst.append(element)
    return lst
    

def peek(lst):
    print (lst[-1])

def s_pop(lst):
    elem = lst.pop(-1)
    return lst,elem

lst = []

lst = push(lst, 4)
print (lst)

peek(lst)

lst,elem = s_pop(lst)
print (lst,elem)

