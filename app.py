from flask import Flask, render_template, request

from adapter import UPIService, PaymentAdapter
from builder import MealBuilder
from command import Kitchen, OrderCommand
from decorator import *
from facade import OrderFacade
from factory import FoodFactory
from observer import Customer, Order
from singleton import Database
from strategy import CreditCard, UPI, DebitCard, NetBanking, CashOnDelivery
from template_method import CustomerOrder

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    # Singleton Pattern
    db = Database()

    result = ""

    if request.method == "POST":
        food_types = request.form.getlist("food")
        if not food_types:
            return render_template("index.html", result="Please select at least one food item.")                                          
        payment = request.form["payment"]
        size = request.form["size"]

        # Factory Pattern + Builder Pattern
        meal = MealBuilder()
        amount = 0

        for food_type in food_types:
            food = FoodFactory.create_food(food_type)
            if food:
                food_price = food.get_price()

                # Size Pricing only for Pizza and Burger
                if food_type in ["pizza", "burger"]:
                    if size == "medium":
                        food_price += 50

                    elif size == "full":
                        food_price += 100

                amount += food_price
                meal.add_food(food_type.capitalize(), food_price)
        
        # Decorator Pattern - Toppings
        if "cheese" in request.form:
            amount += 50
            meal.add_food("Cheese", 50)

        if "mushroom" in request.form:
            amount += 40
            meal.add_food("Mushroom", 40)

        if "corn" in request.form:
            amount += 30
            meal.add_food("Corn", 30)

        if "onion" in request.form:
            amount += 20
            meal.add_food("Onion", 20)

        # Extras
        if "coke" in request.form:
            amount += 40
            meal.add_food("Coke", 40)

        if "icecream" in request.form:
            amount += 60
            meal.add_food("Ice Cream", 60)

        # Strategy Pattern
        if payment == "card":
            pay = CreditCard()
            
        elif payment == "debit":
            pay = DebitCard()

        elif payment == "netbanking":
            pay = NetBanking()

        elif payment == "cod":
            pay = CashOnDelivery()

        else:
            pay = PaymentAdapter(UPIService())

        result = pay.pay(amount)
        
        # Facade Pattern
        facade = OrderFacade()
        facade.complete_order()
        
        # Observer Pattern
        customer = Customer()
        order = Order()
        
        order.add_customer(customer)
        order.notify("Order Placed Successfully!")
        
        # Command Pattern
        kitchen = Kitchen()
        command = OrderCommand(kitchen)
        command.execute()
        
        # Template Method Pattern
        process = CustomerOrder()
        process.process_order()
        
        # Backend Output
        print("Foods:", food_types)
        print("Size:", size)
        print("Payment:", payment)
        
        if "cheese" in request.form:
            print("Extra Cheese Added")
            
        if "mushroom" in request.form:
            print("Mushroom Added")

        if "corn" in request.form:
            print("Corn Added")

        if "onion" in request.form:
            print("Onion Added")

        if "coke" in request.form:
            print("Coke Added")

        if "icecream" in request.form:
            print("Ice Cream Added")
            
        print("Meal Items:", meal.get_items())
        print("Meal Total:", meal.get_total())
        
        print("Final Amount:", amount)
        print("Result:", result)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)