def myDeco(func):
    def Wrapper():
        print("Print Before.")
        func()
        print("Print After.")
    return Wrapper    
@myDeco
def Greetings():
    print("Goodmorning")
    
Greetings()

@myDeco 
def EvenOdd():
    num =12
    print ("Even" if num%2==0 else "Odd")
    
EvenOdd()
