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


money = 0
off = False


def show_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"money: ${money}")


def calculate_espresso():
    enough = True
    ingredients = MENU['espresso']['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < MENU['espresso']['ingredients'][ingredient]:
            enough = False
    return enough


def calculate_latte():
    enough = True
    ingredients = MENU['latte']['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < MENU['latte']['ingredients'][ingredient]:
            enough = False
    return enough


def calculate_cappuccino():
    enough = True
    ingredients = MENU['cappuccino']['ingredients']
    for ingredient in ingredients:
        if resources[ingredient] < MENU['cappuccino']['ingredients'][ingredient]:
            enough = False
    return enough


def calculate_resources(coffee):
    enough = False
    if coffee == 'espresso':
        enough = calculate_espresso()
    elif coffee == 'latte':
        enough = calculate_latte()
    elif coffee == 'cappuccino':
        enough = calculate_cappuccino()
    return enough


def calculate_coins(quarters, dimes, nickles, pennies):
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


def coins_enough(coffee, coins):
    if coffee == 'espresso':
        if coins < MENU['espresso']['cost']:
            return False
    elif coffee == 'latte':
        if coins < MENU['latte']['cost']:
            return False
    elif coffee == 'cappuccino':
        if coins < MENU['cappuccino']['cost']:
            return False
    return True


def change_money(coffee, coins):
    change = 0
    if coffee == 'espresso':
        change = coins - MENU['espresso']['cost']
    elif coffee == 'latte':
        change = coins - MENU['latte']['cost']
    elif coffee == 'cappuccino':
        change = coins - MENU['cappuccino']['cost']
    return change


def reduce_resources(coffee):
    if coffee == 'espresso':
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    elif coffee == 'latte':
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    elif coffee == 'cappuccino':
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']


def add_money(coins):
    global money
    money += coins


def play_game():
    # off secret word
    global off
    # show coffee choices
    can_produce = False
    while not can_produce:
        coffee = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee == 'report':
            # report
            show_resources()
        elif coffee == 'off':
            # off
            off = True
            return
        else:
            # some coffee chosen
            resources_enough = calculate_resources(coffee)
            if resources_enough:
                # resources enough, end the loop
                can_produce = True
    # insert coins
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    # calculate coins
    coins = calculate_coins(quarters, dimes, nickles, pennies)
    if not coins_enough(coffee, coins):
        # coins not enough
        # refunded
        print("Sorry that's not enough money. Money refunded.")
    else:
        # coins enough
        change = change_money(coffee, coins)
        # give back change
        print(f"Here is ${change} in change.")
        # reduce resources
        reduce_resources(coffee)
        # add money
        add_money(coins)
        # give coffee
        print(f"Here is your {coffee}☕. Enjoy!")
    return


while not off:
    play_game()