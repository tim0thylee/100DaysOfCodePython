from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_machine = CoffeeMaker()
cashier = MoneyMachine()
machine_on = True

while machine_on:
    user_choice = input(f"What would you like? {coffee_menu.get_items()}: ")
    if user_choice == 'report':
        coffee_machine.report()
        cashier.report()
    elif user_choice == 'off':
        break
    else:
        coffee_type = coffee_menu.find_drink(user_choice)
        if coffee_type != None:
            if coffee_machine.is_resource_sufficient(coffee_type):
                if cashier.make_payment(coffee_type.cost):
                    coffee_machine.make_coffee(coffee_type)



