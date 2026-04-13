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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit  = 0

def print_report():
    """Print current resource levels and profit"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def is_resource_sufficient(drink_name):
    """Check if resource is sufficient to make the drink"""
    ingredients = MENU[drink_name]["ingredients"]
    for item, amount in ingredients.items():
        if resources[item] < amount:
            print("Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Prompt user to insert coins and return total value."""
    print("Please insert coins: ")
    quarters = int(input("How many quarters?: "))
    dimes    = int(input("How many dimes?: "))
    nickles  = int(input("How many nickles?: "))
    pennies  = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def is_transaction_successful(amount_inserted, drink_name):
    """Check if the inserted amount is sufficient to make the drink. Deduct profit or refund"""
    global profit
    cost = MENU[drink_name]["cost"]
    if amount_inserted < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        profit += cost
        change = round(amount_inserted - cost, 2)
        if change > 0:
            print(f"Here is your change: ${change}")
        return True

def make_coffee(drink_name):
    """Deduct ingredients and make a coffee"""
    ingredients = MENU[drink_name]["ingredients"]
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")

def coffee_machine():
    """Main function"""
    machine_on = True
    while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        if choice == "off":
            machine_on = False
        elif choice == "report":
            print_report()

        elif choice in MENU:
            if is_resource_sufficient(choice):
                amount = process_coins()
                if is_transaction_successful(amount, choice):
                    make_coffee(choice)
        else:
            print("Sorry, that's not a valid choice.")


coffee_machine()
