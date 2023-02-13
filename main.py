from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
optinos = Menu()
is_continue = True
while is_continue :
    print(optinos.get_items())
    choice = input()
    if choice == "report" :
        (coffee_maker.report())
        (money_machine.report())
    if choice == "off" :
        is_continue = False
    else :
        drink = optinos.find_drink(choice)
        response = coffee_maker.is_resource_sufficient(drink) 
        if response :
            cash = money_machine.make_payment(drink.cost)
            if cash :
                coffee_maker.make_coffee(drink)

            
        


