from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def prompt_for_choice():
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    while choice not in ['report','off','espresso','latte','cappuccino']:
        print('Please choose from (espresso/latte/cappuccino/).')
        choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    return choice


def process_money():
    global profit
    quarters = int(input('How many quarters? ')*0.25)
    dimes =    int(input('How many dimes? ')*0.1)
    nickles =  int(input('How many nickles? ')*0.05)
    pennies =  int(input('How many pennies? ')*0.01)
    money = quarters+dimes+nickles+pennies
    return money



def coffee():
    profit = 0
    keep_making_coffee = True
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    while keep_making_coffee:
        choice = prompt_for_choice()
        menu = Menu()
        if choice == "off":
            keep_making_coffee = False
            
        elif choice == 'report':
            coffee_machine.report()
            money_machine.report()
        else:
            menu_item = menu.find_drink(order_name = choice)
            # print(menu_item.cost)

            if coffee_machine.is_resource_sufficient(menu_item):
                
                if money_machine.make_payment(menu_item.cost):
                    coffee_machine.make_coffee(menu_item)
        

coffee()










