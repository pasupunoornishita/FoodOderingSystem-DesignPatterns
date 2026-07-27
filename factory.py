from models import Pizza, Burger, Sandwich, FrenchFries, Pasta, Subway, Taco

class FoodFactory:
    @staticmethod
    def create_food(food_type):

        if food_type == "pizza":
            return Pizza()

        elif food_type == "burger":
            return Burger()
        
        elif food_type == "sandwich":
            return Sandwich()
        
        elif food_type == "frenchfries":
            return FrenchFries()
        
        elif food_type == "pasta":
            return Pasta()
        
        elif food_type == "subway":
            return Subway()
        
        elif food_type == "taco":
            return Taco()

        else:
            return None