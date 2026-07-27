class MealBuilder:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_food(self, name, price):
        self.items.append(name)
        self.total += price

    def get_total(self):
        return self.total

    def get_items(self):
        return ", ".join(self.items)