MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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
    'money': 0
}

def check_resources_are_enough(coffee_type):
    water_required =  MENU[coffee_type]['ingredients']['water']
    milk_required =  MENU[coffee_type]['ingredients']['milk']
    coffee_required =  MENU[coffee_type]['ingredients']['coffee']
    resources_required = []
    ingredients = MENU[coffee_type]['ingredients']
    for item in ingredients:
        if resources[item] - ingredients[item] < 0:
            resources_required.append(item)
            return False, resources_required
            
    return True,[]
    
    
    
def serve(coffee_type):
    water_required =  MENU[coffee_type]['ingredients']['water']
    milk_required =  MENU[coffee_type]['ingredients']['milk']
    coffee_required =  MENU[coffee_type]['ingredients']['coffee']
    resources['water'] -= water_required
    resources['milk'] -= milk_required
    resources['coffee'] -= coffee_required
    print(f'Here is your {coffee_type} ☕. Enjoy!')
    
def process_coins(coffee_type):
    print('Please enter coins.')
    quarters = int(input(f'How many quarters? '))*0.25
    dimes = int(input(f'How many dimes? '))*0.1
    nickles = int(input(f'How many nickles? '))*0.05
    pennies = int(input(f'How many pennies? '))*0.01
    money_received = quarters+dimes+pennies+nickles
    
    return money_received

def is_transaction_successful(money_received,cost):
    
    if money_received >= cost:
        
        return_money = money_received - cost
        resources['money'] += cost
        print(f"Here is ${round(return_money,2)} dollars in change")
        
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(resources['money'],2)}")


stop_coffee_machine = False

while not stop_coffee_machine:
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while user_prompt not in ["espresso","latte","cappuccino","off","report"]:
        user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    
    if user_prompt == 'off':
        stop_coffee_machine = True
    elif user_prompt == 'report':
        print_report()
    else:
        resources_enough, resources_required = check_resources_are_enough(user_prompt)
        if resources_enough:
            money_received = process_coins(user_prompt)
            cost = MENU[user_prompt]['cost']
            if is_transaction_successful(money_received, cost):
                serve(user_prompt)
        else:
            print(f'Sorry there is not enough {resources_required[0]}.')
            
    

    
    
    




















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












































