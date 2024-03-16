from menu import Menu, MenuItems
from coffee import Coffeemaker
from money_machine import MoneyMachine

items_menu = Menu() 
coffee_machine = Coffeemaker()
money_machine = MoneyMachine()

def report(): 
    coffee_machine.report()
    money_machine.report()
# items_menu.get_items()

# Prompt for the user by asking "What would you like to have"?(espresso/latte/cappuccino)

machine_ON = True
while machine_ON:
    customer_choice = input(f"\n\nType REPORT to see if the ingredients are enpugh." +
                            f"\n Type OFF if you want to turn the machine off"
                            f"\n What would you like to have?{items_menu.get_items()}\n").lower()
    
    if customer_choice == 'report':
        report()
    elif customer_choice == 'off':
        machine_ON = False

    else:
        drink = items_menu.find_drink(customer_choice)
        if coffee_machine.is_resources_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)
        else:
            break


