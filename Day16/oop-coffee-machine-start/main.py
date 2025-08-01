from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()

machine = True


while machine:
    options = menu.get_items()
    coffee_question = input(f"커피를 선택하세요. {options}: ")

    if coffee_question == "off":
        machine = False
        print("커피 머신 작동 종료")

    elif coffee_question == "report":
        coffee_maker.report()
    
    elif coffee_question == "espresso" or coffee_question == "latte" or coffee_question == "cappuccino":
        print(coffee_question)
        drink_cost = menu.find_drink(coffee_question)
        print(drink_cost)
        # print(f"{coffee_question}의 금액: ${drink_cost}")
        
        
        # if get
        
        

        # 메뉴 - 완료
        # if 리소스가 많다면(true)
        #     코인 넣기()
        #     if 리소스 체크(ture)
        #         커피만들기