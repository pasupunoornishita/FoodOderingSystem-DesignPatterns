class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"

class UPI(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ₹{amount} using UPI"
    
class DebitCard(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ₹{amount} using Debit Card"
    
class NetBanking(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ₹{amount} using Net Banking"


class CashOnDelivery(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ₹{amount} using Cash on Delivery"