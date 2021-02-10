from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    instruction = input(f"What do you want to drink today, {menu.get_items()}? ")
    if instruction == 'report':
        coffeemaker.report()
        money_machine.report()
    elif instruction == 'off':
        is_on = False
    else:
        menu_item = menu.find_drink(instruction)
        if coffeemaker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffeemaker.make_coffee(menu_item)





