class FoodOrder:
    def process_order(self):
        self.select_food()
        self.make_payment()
        self.deliver()

    def select_food(self):
        pass

    def make_payment(self):
        print("Payment Successful")

    def deliver(self):
        print("Order Delivered")


class CustomerOrder(FoodOrder):
    def select_food(self):
        print("Food Selected")