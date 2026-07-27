class Customer:
    def update(self, message):
        print("Notification:", message)

class Order:
    def __init__(self):
        self.observers = []

    def add_customer(self, customer):
        self.observers.append(customer)

    def notify(self, message):
        for customer in self.observers:
            customer.update(message)