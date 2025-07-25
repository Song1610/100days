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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine = True

# todo : Prompt user by asking
# todo : Turn off the Coffee Machine by entering “ off ” to the prompt
coffee_question = input("커피를 선택하세요.(espresso/latte/cappuccino): ")
if coffee_question == "off":
    machine = False
    print("머신 작동 종료")

# todo : Print report.
elif coffee_question == "report":
    print(resources)
# todo : Check resources sufficient
# todo : Process coin
# todo : Check transaction successful
# todo : Make Coffee