from ClassOopInheritance import TvMobile
class Mobile(TvMobile):
    product = "Mobile"
    
    def __init__(self, brand, model, operating, camera, price, availability, stock):
        super().__init__(brand, model, price, availability, stock)
        self.operating = operating
        self.camera = camera
    
    def __str__(self):
        return (f"Category: {self.category}, Product: {self.product}, Brand: {self.brand}, Model: {self.model}, Operating System: {self.operating}, Camera: {self.camera} Mega Pixel, Price: $ {self.price}, Availability: {self.availability}, Stock: {self.stock}")

    def Call(self):
        print (f"Mobile is calling......") 
        
    def Sms(self):
        print (f"Mobile is sending SMS.")
        




