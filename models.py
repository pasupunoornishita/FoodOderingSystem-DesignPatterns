class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Pizza(FoodItem):
    def __init__(self):
        super().__init__("Pizza", 200)


class Burger(FoodItem):
    def __init__(self):
        super().__init__("Burger", 150)
 
        
class Sandwich(FoodItem):
    def  __init__(self):
        super().__init__("Sandwich", 120)
        

class FrenchFries(FoodItem):
    def __init__(self):
        super().__init__("FrenchFries", 100)
        
        
class Pasta(FoodItem):
    def __init__(self):
        super().__init__("Pasta", 180)
        
        
class Subway(FoodItem):
    def __init__(self):
        super().__init__("Subway", 160)
        
        
class Taco(FoodItem):
    def __init__(self):
        super().__init__("Taco", 140)
        