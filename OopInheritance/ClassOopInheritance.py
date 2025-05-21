class TvMobile:
    
    category  = "Electronics"
    def __init__(self, brand, model, price, availability, stock):        
        self.brand = brand
        self.model = model
        self.price = price
        self.availability = availability
        self.stock = stock
        
    def __str__(self):
        return (f"Category: {self.category}, Brand: {self.brand}, Model: {self.model}, price: {self.price}, Available: {self.availability}, Stock: {self.stock}")
    
    def TurnOn (self):
        print (f"Turning on") 
        
    def TurnOff(self):
        print (f"Turning off")
        

