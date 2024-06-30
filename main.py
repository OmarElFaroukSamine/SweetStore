import unittest

class Sweet:
    def __init__(self, name, price, flavor):
        if not isinstance(name, str):
            raise TypeError("The name of the candy must be a string!\n")
        if not isinstance(price, float):
            raise TypeError("The price of the candy must be a number!\n")
        if not isinstance(flavor, str):
            raise TypeError("The flavor of the candy must be a string!\n")
        
        self._name = name
        self._price = price
        self._flavor = flavor
    
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

    # Main methods that will overriden
    def display(self):
        print(f"\nThis candy is called {self._name}, it comes in the flavor of {self._flavor},"
              f" and it's being sold for ${self._price}.",  end =" ")
    
    def make(self, store, quantity):
        raise NotImplementedError("Please use this method with the correct class")





#The sweets subclasses which are Chocolate, Liquorice, Gummy and Sour


class Chocolate(Sweet):
    def __init__(self, name, price, flavor, percentage):
        super().__init__(name, price, flavor)
        self._percentage = percentage


    #G's & S's for percentage attribute
    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def pecentage(self, v):
        self._percentage = v


    #Overriding display() to display the additional attribute
    def display(self):
        super().display()
        print(f"It contains {self.percentage}% cocoa.",  end =" ")
    
    
    #make() method that takes in 2 args, and uses creates the wanted sweet using the ingredients that are needed, and then adds this quantity of sweets  to the inventory of the store that is a dictionary tha contains the object and its quantity
    def make(self, store, quantity):
        ingNeed = {'cocoa': 2, 'sugar': 1}
        for ingredient, amount in ingNeed.items():
            totalNeed = amount * quantity
            if store._ingStock.get(ingredient, 0) < totalNeed:
                print(f"Not enough ingredients to make {self._name}")
                return
        
        for ingredient, amount in ingNeed.items():
            totalNeed = amount * quantity
            store._ingStock[ingredient] -= totalNeed
        
        if self._name in store.inventory:
            store.inventory[self._name][1] += quantity
        else:
            store.inventory[self._name] = [self, quantity]
        print(f"Made {quantity} units of {self._name}")


class Liquorice(Sweet):
    def __init__(self, name, price, flavor, alcPercentage):
        super().__init__(name, price, flavor)
        self._alcPercentage = alcPercentage


    #G'S and S's for alcohol percentage attribute
    @property
    def alcPercentage(self):
        return self._alcPercentage

    @alcPercentage.setter
    def alcPercentage(self, v):
        self._alcPercentage = v



    #Overriding display() to display the additional attribute
    def display(self):
        super().display()
        print(f"Be careful!! since it contains {self._alcPercentage}% alcohol.",  end =" ")
    


    def make(self, store, quantity):
        ingNeed = {'sugar': 3, 'flavoring': 1, 'alcohol': 1}
        for ingredient, amount in ingNeed.items():
            totalNeed = amount * quantity
            if store._ingStock.get(ingredient, 0) < totalNeed:
                print(f"Not enough ingredients to make {self._name}")
                return
        
        for ingredient, amount in ingNeed.items():
            totalNeed = amount * quantity
            store._ingStock[ingredient] -= totalNeed
        
        if self._name in store.inventory:
            store.inventory[self._name][1] += quantity
        else:
            store.inventory[self._name] = [self, quantity]
        print(f"Made {quantity} units of {self._name}")


class Sour(Sweet):
    def __init__(self, name, price, flavor):
        super().__init__(name, price, flavor)
    


    def make(self, store, quantity):
        ingNeed = {'sugar': 2, 'citricAcid': 1}
        for ingredient, amount in ingNeed.items():
            totalNeed = amount * quantity
            if store._ingStock.get(ingredient, 0) < totalNeed:
                print(f"Not enough ingredients to make {self._name}")
                return
        
        for ingredient, amount in ingNeed.items():
            totalNeed = amount * quantity
            store._ingStock[ingredient] -= totalNeed
        
        if self._name in store.inventory:
            store.inventory[self._name][1] += quantity
        else:
            store.inventory[self._name] = [self, quantity]
        print(f"Made {quantity} units of {self._name}")




class Gummy(Sweet):
    def __init__(self, name, price, flavor):
        super().__init__(name, price, flavor)
    


    def make(self, store, quantity):
        ingNeed = {'gelatin': 2, 'sugar': 1, 'flavoring': 1}
        for ingredient, amount in ingNeed.items():
            totalNeed = amount * quantity
            if store._ingStock.get(ingredient, 0) < totalNeed:
                print(f"Not enough ingredients to make {self._name}")
                return
        
        for ingredient, amount in ingNeed.items():
            totalNeed = amount * quantity
            store._ingStock[ingredient] -= totalNeed
        
        if self._name in store.inventory:
            store.inventory[self._name][1] += quantity
        else:
            store.inventory[self._name] = [self, quantity]
        print(f"Made {quantity} units of {self._name}")




#Ingredient class that is used when trying to add ingredients to the ingredient stock, consists of two attributes name and quantity.
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} units"




#The store itself that has all the functionality of the program. Its attributes consist of an inventory, a ingredients stock and a cash register
class SweetStore:
    def __init__(self):
        self.inventory = {}
        self._ingStock = {}
        self.cashRegister = 0.0


    #addsweet method that makes it so you have to go through the store if you want to make a sweet, and it uses the make() method depending on which sweet you give it
    def addSweet(self, sweet, quantity):
        sweet.make(self, quantity)


    #addIngredient method that replaces the restock method, it instead adds the ingredient to the ingStock with it's quantity, but before that it checks if it exists there before and if yes just adds the quantity
    def addIngredient(self, ingredient):
        if ingredient.name in self._ingStock:
            self._ingStock[ingredient.name] += ingredient.quantity
        else:
            self._ingStock[ingredient.name] = ingredient.quantity


    #sell method that checks the inventory and sells the sweet if available, and deducts the quantity of the sweet from the inventory, and adds the money that was made to the cash register, this is if the purchase is possible ofc
    def sell(self, sweetName, quantity):
        if sweetName in self.inventory and self.inventory[sweetName][1] >= quantity:
            totalPrice = self.inventory[sweetName][0].price * quantity
            self.inventory[sweetName][1] -= quantity
            if self.inventory[sweetName][1] == 0:
                del self.inventory[sweetName]
            self.cashRegister += totalPrice
            print(f"Sold {quantity} units of {sweetName} for ${totalPrice:.2f}")
        else:
            print(f"Not enough {sweetName} in inventory to sell {quantity} units")


    #show inventory, i think the name is a good enough description :)
    def showInventory(self):
        for name, (sweet, quantity) in self.inventory.items():
            print(f"{name}: {quantity} units")


    #Same here
    def showingStock(self):
        for ingredient, quantity in self._ingStock.items():
            print(f"{ingredient}: {quantity} units")
    
    #also showing, but rounding up and only showing 2 decimals  
    def showCashRegister(self):
        print(f"Cash Register: ${self.cashRegister:.2f}")


#Now to test if this program works
class TestSweetClasses(unittest.TestCase):

    def setUp(self):
        self.choco = Chocolate("Dark Chocolate", 2.5, "Bitter", 70)
        self.candy = Liquorice("Liquorice", 1.5, "Anise", 10)
        self.sour = Sour("Sour Candy", 0.5, "Lemon")
        self.gummy = Gummy("Gummy Bears", 0.75, "Fruity")
        self.store = SweetStore()
        self.store.addIngredient(Ingredient("cocoa", 50))
        self.store.addIngredient(Ingredient("sugar", 100))
        self.store.addIngredient(Ingredient("flavoring", 50))
        self.store.addIngredient(Ingredient("citricAcid", 20))
        self.store.addIngredient(Ingredient("gelatin", 50))
        self.store.addIngredient(Ingredient("alcohol", 30))

    def test_sweet_initialization(self):
        with self.assertRaises(TypeError):
            Sweet(123, 1.0, "Sweet")
        with self.assertRaises(TypeError):
            Sweet("Candy", "price", "Sweet")
        with self.assertRaises(TypeError):
            Sweet("Candy", 1.0, 123)
        
        sweet = Sweet("Candy", 1.0, "Sweet")
        self.assertEqual(sweet.name, "Candy")
        self.assertEqual(sweet.price, 1.0)
        self.assertEqual(sweet.flavor, "Sweet")

    def testChocolateInit(self):
        self.assertEqual(self.choco.name, "Dark Chocolate")
        self.assertEqual(self.choco.price, 2.5)
        self.assertEqual(self.choco.flavor, "Bitter")
        self.assertEqual(self.choco.percentage, 70)

    def testLiquoriceInit(self):
        self.assertEqual(self.candy.name, "Liquorice")
        self.assertEqual(self.candy.price, 1.5)
        self.assertEqual(self.candy.flavor, "Anise")
        self.assertEqual(self.candy.alcPercentage, 10)

    def testSourInit(self):
        self.assertEqual(self.sour.name, "Sour Candy")
        self.assertEqual(self.sour.price, 0.5)
        self.assertEqual(self.sour.flavor, "Lemon")

    def test_gummy_initialization(self):
        self.assertEqual(self.gummy.name, "Gummy Bears")
        self.assertEqual(self.gummy.price, 0.75)
        self.assertEqual(self.gummy.flavor, "Fruity")

    def test_chocolate_make(self):
        self.store.addSweet(self.choco, 10)
        self.assertEqual(self.store.inventory["Dark Chocolate"][1], 10)
        self.assertEqual(self.store._ingStock["cocoa"], 30)
        self.assertEqual(self.store._ingStock["sugar"], 90)

    def test_liquorice_make(self):
        self.store.addSweet(self.candy, 20)
        self.assertEqual(self.store.inventory["Liquorice"][1], 20)
        self.assertEqual(self.store._ingStock["sugar"], 40)
        self.assertEqual(self.store._ingStock["flavoring"], 30)
        self.assertEqual(self.store._ingStock["alcohol"], 10)

    def test_sour_make(self):
        #this test is supposed to fail becaues we know that the ingredient amount is not enough to create these sour candies.
        self.store.addSweet(self.sour, 50)
        self.assertEqual(self.store.inventory["Sour Candy"][1], 50)
        self.assertEqual(self.store._ingStock["sugar"], 0)
        self.assertEqual(self.store._ingStock["citricAcid"], 0)

    def test_gummy_make(self):
        #same for this test.
        self.store.addSweet(self.gummy, 50)
        self.assertEqual(self.store.inventory["Gummy Bears"][1], 50)
        self.assertEqual(self.store._ingStock["gelatin"], 0)
        self.assertEqual(self.store._ingStock["sugar"], 50)
        self.assertEqual(self.store._ingStock["flavoring"], 0)

    def test_sell(self):
        self.store.addSweet(self.choco, 10)
        self.store.sell("Dark Chocolate", 5)
        self.assertEqual(self.store.inventory["Dark Chocolate"][1], 5)
        self.assertEqual(self.store.cashRegister, 12.5)

        self.store.sell("Dark Chocolate", 5)
        self.assertNotIn("Dark Chocolate", self.store.inventory)
        self.assertEqual(self.store.cashRegister, 25.0)

    def test_sell_not_enough_inventory(self):
        self.store.addSweet(self.choco, 10)
        self.store.sell("Dark Chocolate", 15)
        self.assertEqual(self.store.inventory["Dark Chocolate"][1], 10)
        self.assertEqual(self.store.cashRegister, 0.0)

    def test_show_inventory(self):
        self.store.addSweet(self.choco, 10)
        self.store.addSweet(self.candy, 20)
        self.assertEqual(len(self.store.inventory), 2)
        self.assertIn("Dark Chocolate", self.store.inventory)
        self.assertIn("Liquorice", self.store.inventory)

    def testShowIngStock(self):
        self.assertEqual(len(self.store._ingStock), 6)
        self.assertIn("cocoa", self.store._ingStock)
        self.assertIn("sugar", self.store._ingStock)
        self.assertIn("flavoring", self.store._ingStock)
        self.assertIn("citricAcid", self.store._ingStock)
        self.assertIn("gelatin", self.store._ingStock)
        self.assertIn("alcohol", self.store._ingStock)

    def testShowCashRegister(self):
        self.assertEqual(self.store.cashRegister, 0.0)

if __name__ == '__main__':
    unittest.main()
