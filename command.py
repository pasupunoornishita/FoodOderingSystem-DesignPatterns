class Kitchen:
    def prepare_food(self):
        print("Food is being prepared")

class OrderCommand:
    def __init__(self, kitchen):
        self.kitchen = kitchen

    def execute(self):
        self.kitchen.prepare_food()