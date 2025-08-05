from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
machine = True


while machine:
    options = menu.get_items()
    coffee_question = input(f"커피를 선택하세요.({options}): ")

    if coffee_question == "off":
        machine = False
        print("커피 머신 작동 종료")

    elif coffee_question == "report":
        coffee_maker.report()
        money_machine.report()
    
    elif coffee_question == "espresso" or coffee_question == "latte" or coffee_question == "cappuccino":
        print(coffee_question)
        drink = menu.find_drink(coffee_question)
        sufficient = coffee_maker.is_resource_sufficient(drink)
        if sufficient == True:
            user_coin = money_machine.make_payment(drink.cost)
            if user_coin == True:
                coffee_maker.make_coffee(drink)
    
    else:
        print("잘못 입력하셨습니다.")