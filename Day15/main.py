# todo : Make 3 hot flavours
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
    "water": 3000,
    "milk": 2000,
    "coffee": 1500,
}


def sufficient(order):
    """재료 확인, 재료가 충분하다면 True, 아니라면 False"""
    for item in order:
        if order[item] > resources[item]:
            print(f"재료가 소진되었습니다.😭")
            return False
        else:
            return True


def process_coin():
    """ 금액 지불 """
    quarter = int(input("quarters 동전을 넣으세요.: ")) * 0.25
    dimes = int(input("dimes 동전을 넣으세요.: ")) * 0.1
    nickel = int(input("nickel 동전을 넣으세요.: ")) * 0.05
    pennies = int(input("pennies 동전을 넣으세요.: ")) * 0.01
    total = quarter + dimes + nickel + pennies

    return total

su_ic = 0
def check(user_money, coffee_cost):
    """지불한 금액이 메뉴 가격보다 큰지 확인, 충분하다면 잔돈 교환 & 수익추가, 아니라면 환불"""
    if user_money >= coffee_cost:
        jandon = round(user_money - coffee_cost, 2)
        print(f"잔돈: ${jandon}")

        global su_ic
        su_ic += coffee_cost
        return True


    elif user_money < coffee_cost:
        print(f"금액이 충분하지 않습니다. 금액을 환불합니다.")
        return False



def make_coffee(drink_name, order):
    """todo : 커피 만들기, 재료 빼기"""
    for item in order:
        resources[item] -= order[item]
    print(f"{drink_name}☕ 완성!")



machine = True

while machine:
    # todo : 커피메뉴 물어보기
    coffee_question = input("커피를 선택하세요.(espresso/latte/cappuccino): ")

    if coffee_question == "off":
        # todo : "off" 입력 시 머신 동작 종료
        machine = False
        print("커피 머신 작동 종료")

    elif coffee_question == "report":
        # todo : "report" 입력 시 재료 잔량 및 판매금액 출력
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']

        print(f"물: {water}ml")
        print(f"우유: {milk}ml")
        print(f"커피: {coffee}g")
        print(f"판매금액: ${su_ic}")
        machine = True


    elif coffee_question == "espresso" or coffee_question == "latte" or coffee_question == "cappuccino":
        drink_choice = MENU[coffee_question]
        drink_resource = drink_choice['ingredients']
        drink_cost = drink_choice['cost']
        print(f"{coffee_question}의 금액: ${drink_cost}")

        if sufficient(drink_resource) == True:
            user_cost = process_coin()
            if check(user_cost, drink_cost) == True:
                make_coffee(coffee_question, drink_resource)

    else :
        print("잘못 입력하셨습니다.")








