class Calculator:
    def __init__(self):
        self.total = 5
        self.a = 1
        self.b = 2
        
    def add(self, a, b):
        self.total = a+b
        print (a+b)
        
    def subtract(self, a,b):
        print (a-b)
        
person1 = Calculator()
person1.total = 50
person1.add(1,2)

person2 = Calculator()
print (person2.total) 
person2.total = 99
print (person2.total)
    