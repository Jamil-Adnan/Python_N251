from ClassOopInheritance import TvMobile 
class Tv(TvMobile):
    
    product = "Tv"
    
    def __init__(self, brand, model, display, displayType, price, availability, stock):
        super().__init__(brand, model, price, availability, stock)
        self.display = display
        self.displayType = displayType
    
    def __str__(self):
        return (f"Category: {self.category}, Product: {self.product}, Brand: {self.brand}, Model: {self.model}, Display Size: {self.display}, Display Type: {self.displayType}, Price: $ {self.price}, Availability: {self.availability}, Stock: {self.stock}")  
    
    def Channel(self):
        print("Tv is Changing Channel")   
        




