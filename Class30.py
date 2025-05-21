class Mobile:
    def __init__(self, name):
        self.model = name #public
        self._sim = 2 # protected
        self.__camera = 3 #private
        
    def get__camera(self):      #gets/imports/reads a value
        return self.__camera
    
    def set__camera(self, num):     #sets a value
        self.__camera = num
        return self.__camera
        
    def call(self):
        print ("Calling....")
        
Samsung_S24 = Mobile("S24")
print(Samsung_S24.model) 

Samsung_S24.set__camera(5)      #setting the value to 5
print(Samsung_S24.get__camera())        #reading the set value