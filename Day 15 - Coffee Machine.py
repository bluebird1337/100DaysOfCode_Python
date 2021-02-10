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
    "money": 0,
}

while True:
    success = False
    # TODO:1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
    instruction = input("What would you like? (espresso/latte/cappuccino) ☕ : ")
    # TODO:2. Turn off the Coffee Machine by entering “off” to the prompt.
    if instruction == 'off':
        break
    # TODO:3. Print report.
    if instruction == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${resources['money']}")
    # TODO:4. Check resources sufficient?
    if instruction == 'espresso':
        if resources['water'] < MENU['espresso']['ingredients']['water'] or resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print("“Sorry there is not enough ingredient")
        else:
            success = True
    elif instruction == 'latte':
        if resources['water'] < MENU['latte']['ingredients']['water'] \
                or resources['milk'] < MENU['latte']['ingredients']['milk']\
                or resources['coffee'] < MENU['latte']['ingredients']['coffee']:
            print("Sorry there is not enough ingredient")
        else:
            success = True
    elif instruction == 'cappuccino':
        if resources['water'] < MENU['cappuccino']['ingredients']['water'] \
                or resources['milk'] < MENU['cappuccino']['ingredients']['milk']\
                or resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry there is not enough ingredient")
        else:
            success = True
    # TODO:5. Process coins.
    if success:
        print(f"The price of {instruction} "
                             f"is {MENU[instruction]['cost']}, please insert coin.")
        quarter = int(input("Quarter(0.25): "))
        dimes = int(input("Dime(0.1): "))
        nickles = int(input("Nickles(0.05): "))
        pennies = int(input("Pennies(0.01): "))
        total_insert = quarter*0.25 + dimes*0.1 + nickles * 0.05 + pennies*0.01
        # TODO:6. Check transaction successful?
        if total_insert < MENU[instruction]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            continue
        # TODO:7. Make Coffee
        else:
            # TODO:8.offer change.
            if total_insert > MENU[instruction]['cost']:
                refund = round(total_insert - MENU[instruction]['cost'], 2)
                print(f"Here is ${refund} dollars in change")
            resources['water'] -= MENU[instruction]['ingredients']['water']
            resources['coffee'] -= MENU[instruction]['ingredients']['coffee']
            if instruction == "latte" or instruction == "cappuccino":
                resources['milk'] -= MENU[instruction]['ingredients']['milk']
            resources['money'] += MENU[instruction]['cost']
            print(f"Here is your {instruction}. Enjoy!")

