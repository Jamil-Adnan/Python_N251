"""
def Greetings (n):
    if n==0:
        return
    else:
        print ("Eid Mubarak")
        print (n)
        Greetings (n= n-  1)

Greetings(4)
print ("The End!")

"""
def Message(n):
    if n >= 5:
        return
    else:
        print (f"Hello World - {n}")
        Message (n + 1)


Message (0)
print ("The end!")