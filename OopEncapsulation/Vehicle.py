class Vehicle:
    driver = 1
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return (f"Name: {self.name}, Driver: {self.driver}")    