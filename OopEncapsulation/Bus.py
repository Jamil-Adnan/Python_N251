from Vehicle import Vehicle
class Bus(Vehicle):
    def __init__(self, name, wheel):
        super().__init__(name)
        self.name = name
        self.wheel = wheel
        self.__sit = 0
        
    def get__sit(self):
        return self.__sit
    
    def set__sit(self, sit):
        self.__sit= sit
        return self.__sit
    
    def __str__(self):
        return (f"Name: {self.name}, Driver: {self.driver}, Number of sits: {self.get__sit()}, Number of Wheels: {self.wheel}")