from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True




while is_on:
    options = menu.get_items()
    coffee_question = input(f"What would you like?({options})")
    
    if coffee_question == "off":
        is_on = False
    
    elif coffee_question == "report":
        coffee_maker.report()
        money_machine.report()
    
    elif coffee_question == "espresso" or coffee_question == "latte" or coffee_question == "cappuccino":
        drink = menu.find_drink(coffee_question)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

        # if coffee_maker.is_resource_sufficient(drink):
        #     if money_machine.make_payment(drink.cost):
        #         coffee_maker.make_coffee(drink) 와 같다.