class UPIService:
    def pay_amount(self, amount):
        return f"Paid ₹{amount} using UPI"

class PaymentAdapter:
    def __init__(self, service):
        self.service = service

    def pay(self, amount):
        return self.service.pay_amount(amount)