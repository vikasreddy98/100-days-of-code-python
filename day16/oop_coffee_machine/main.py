import money_machine
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_menu = Menu()
coffee_machine = CoffeeMaker()
coffee_profits = MoneyMachine()

machine_on = True
while machine_on:
    choice = input(f"What would you like to have? {coffee_menu.get_items()}: ")

    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_machine.report()
        coffee_profits.report()
    else:
        drink = coffee_menu.find_drink(choice)


        if coffee_machine.is_resource_sufficient(drink):
            if coffee_profits.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
        else:
            print("Sorry, That's not a valid choice.")


