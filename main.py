class Sweet:
    def __init__(self, name, price, flavor, quantity):
    #Raising error if args are not the specified type
        if not isinstance(name, str):
            raise TypeError("The name of the candy must be a string!\n")
        if not isinstance(price, float):
            raise TypeError("The price of the candy must be a number!\n")
        if not isinstance(flavor, str):
            raise TypeError("The flavor of the candy must be a string!\n")
        if not isinstance(quantity, int):
            raise TypeError("The quantity of the candy must be a integer!\n")
        
        
    #Assigning the args to attribs
        self._name = name
        self._price = price
        self._flavor = flavor
        self._quantity = quantity
        
    
    
    #G's
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def flavor(self):
        return self._flavor
    @property
    def quantity(self):
        return self._quantity
     
    #S's
    
    @name.setter
    def name(self, v):
        self._name = v
    @price.setter
    def price(self, v):
        self._price = v
    @flavor.setter
    def flavor(self, v):
        self._flavor = v
    @quantity.setter
    def quantity(self, v):
        self._quantity = v
    
    

    
    
    def restock (self, am):
        if not isinstance(am, int): raise TypeError("The quantity of the candy must be a integer!\n") 
        self._quantity = self._quantity + am
    
    
    def sell (self, ams):
        if not isinstance(ams, int): 
            raise TypeError("The quantity of the candy must be a integer!\n") 
        if (self._quantity >= ams): 
            self._quantity = self._quantity - ams 
        else: 
            print("Not enough in stock, the available quanitty is", self._quantity,"pieces\n") 
    

    def display(self):
            print("This candy's is called", self._name, "and it comes in the flavor of", 
                  self._flavor, "and it's being sold for", 
                  self._price, "$. So better hurry up and get it since there's only", 
                  self._quantity," of them left!!\n")
    


class Chocolate(Sweet):
    def __init__(self, name, price, flavor, quantity, percentage):
        super().__init__(name, price, flavor, quantity)




class Liquorice(Sweet):
    def __init__(self, name, price, flavor, quantity, alcpercentage):
        super().__init__(name, price, flavor, quantity, alcpercentage)
                


class Sour(Sweet):
    def __init__(self, name, price, flavor, quantity):
        super().__init__(name, price, flavor, quantity)
        
        
        
                                
class Gummy(Sweet):
    def __init__(self, name, price, flavor, quantity):
        super().__init__(name, price, flavor, quantity)








tof = Sweet("tofita", 2.5, "strawberry", 400) 
tof.display() 
tof.sell(500)
tof.restock(150)
tof.sell(500)
tof.display()

