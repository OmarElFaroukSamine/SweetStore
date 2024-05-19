class Candy: 
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
        self.name = name 
        self.price = price 
        self.flavor = flavor 
        self.quantity = quantity 
    
    
    def restock (self, am): 
        if not isinstance(am, int): raise TypeError("The quantity of the candy must be a integer!\n") 
        self.quantity = self.quantity + am 
    
    
    def sell (self, ams): 
        if not isinstance(ams, int): 
            raise TypeError("The quantity of the candy must be a integer!\n") 
        if (self.quantity >= ams): 
            self.quantity = self.quantity - ams 
        else: 
            print("Not enough in stock, the available quanitty is", self.quantity,"pieces\n") 
    

    def display(self): 
            print("This candy's is called ", self.name, "and it comes in the flavor of ", 
                  self.flavor, "and it's being sold for", 
                  self.price, "$. So better hurry up and get it since there's only ", 
                  self.quantity," of them left!!\n")

tof = Candy("tofita", 2.5, "strawberry", 400) 
tof.display() 
tof.sell(500)
tof.restock(150)
tof.sell(500)
tof.display()
