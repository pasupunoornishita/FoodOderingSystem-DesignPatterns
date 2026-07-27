class CheeseDecorator:
    def __init__(self, food):
        self.food = food

    def get_price(self):
        return self.food.get_price() + 50
    
class MushroomDecorator:
    def __init__(self, food):
        self.food = food

    def get_price(self):
        return self.food.get_price() + 40


class CornDecorator:
    def __init__(self, food):
        self.food = food

    def get_price(self):
        return self.food.get_price() + 30
    
class OnionDecorator:
    def __init__(self, food):
        self.food = food
        
    def get_price(self):
        return self.food.get_price() + 20