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
    "money": 0
}


# Calculates total coins and returns the value entered
def calculate_coins():
    print("Please insert coins")
    total = 0;
    quarter = float(input("How many Quarters: "))
    dimes = float(input("How many Dimes: "))
    nickels = float(input("How many Nickels: "))
    pennies = float(input("How many Pennies: "))
    total += quarter * .25 + dimes * .10 + nickels * .05 + pennies * .01
    return total


# User drink analyzed
def coffee_type(drink):
    water_use = MENU[drink]['ingredients']['water']
    coffee_use = MENU[drink]['ingredients']['coffee']
    milk_use = MENU[drink]['ingredients']['coffee']
    if water_use > resources['water']:
        print("Not enough water in the machine.")
    elif coffee_use > resources['coffee']:
        print("Not enough coffee in the machine")
    elif milk_use > resources['milk']:
        print("Not enough milk in the machine.")
    else:
        total_coins = calculate_coins()
        if total_coins >= MENU[drink]['cost']:
            resources['money'] += MENU[drink]['cost']
            change = total_coins - MENU[drink]['cost']
            resources['water'] -= water_use
            resources['coffee'] -= coffee_use
            resources['milk'] -= milk_use
            print(f'Here is your {drink} and {"{:.2f}".format(change)} dollars in change')
        else:
            print(f"Must put in more money.")


def run_machine():
    machine_power = True
    while machine_power:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            machine_power = False
        # espresso uses fewer ingredients, so it isn't using coffee_type function
        elif user_choice == "espresso":
            water_use = MENU['espresso']['ingredients']['water']
            coffee_use = MENU['espresso']['ingredients']['coffee']
            if water_use > resources['water']:
                print("Not enough water in the machine.")
            elif coffee_use > resources['coffee']:
                print("Not enough coffee in the machine")
            else:
                total_coins = calculate_coins()
                if total_coins >= MENU['espresso']['cost']:
                    resources['money'] += MENU['espresso']['cost']
                    change = total_coins - MENU['espresso']['cost']
                    resources['water'] -= water_use
                    resources['coffee'] -= coffee_use
                    print(f'Here is your espresso and {"{:.2f}".format(change)} dollars in change')
                else:
                    print(f"Must put in more money.")
        elif user_choice == "latte":
            coffee_type(user_choice)
        elif user_choice == "cappuccino":
            coffee_type(user_choice)
        elif user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        else:
            continue


run_machine()
