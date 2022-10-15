MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_enough(order_ingredients):
    """Returns True when order can be made because the resources are sufficient,
    returns False if the resources aren't enough"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item} to make your desired coffee")
            is_enough = False  # same as writing return False
    return is_enough  # same as writing return True

def process_coins():
    """Returns the Total amount of coins inserted"""
    print("Please insert coins")
    Total = int(input("How many quarters?: ")) * 0.25
    Total += int(input("How many dimes?: ")) * 0.1
    Total += int(input("How many nickels?: ")) * 0.05
    Total += int(input("How many pennies?: ")) * 0.01
    return Total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted and False if money received isn't enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you do not have enough money to purchase your desired cup of coffee. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct ingredients from resources after a drink is made"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}. Enjoy")


should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        should_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        # here we're calling our is_resources func, and we're getting our order ingredients from drink,
        # then we pass in the key "ingredients" to access the quantities
        if is_resources_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
