class Vehicle:
    wheels = 4
    
    def __init__(self, car_name):
        self.window = 2
        self.seat = 2
        self.name = car_name
        
        
    def __str__(self):
        return self.name 
        
    def sound(self):
        print ("beep beep")
        
    def start(self):
        print ("The car started")
        
    def Stop(self):
        print ("The car stopped")
        
        
class Bus (Vehicle):
    def Brake(self):
        print ("Braking the bus")
        
    def start(self):
        print ("The bus started")


Hanif = Bus("Hanif Bus")
Hanif.Brake()
    
# bus = Vehicle("Bus")
# bus.Sound()
# print (bus.wheels)
# bus.wheels = 6
# print (bus.wheels)

# car = Vehicle("Car")
# car.Start()

# Vehicle.wheels = 12
# print (Vehicle.wheels)
