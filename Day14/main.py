import random
from art import logo, vs
from game_data import data

#print(logo)

print(logo)

def show_data(information):
    """ A,B 보여주기 """
    name = information['name']
    description = information['description']
    country = information['country']

    return f"{name}, {description}, {country}"


def compare(answer, follow_a, follow_b):
    """A와 B의 팔로우 비교"""
    follower_a = follow_a['follower_count']
    follower_b = follow_b['follower_count']
    if answer == "a":
        return follower_a > follower_b
    elif answer == "b":
        return follower_a < follower_b
    else:
        return False




game_over = False
score = 0

while not game_over:
    """ 게임 시작"""

    b_account = random.choice(data)
    a_account = b_account

    # Print Account
    print(f"A 계정 : {show_data(a_account)}")
    print(vs)
    if a_account == b_account:
        b_account = random.choice(data)
        print(f"B 계정 : {show_data(b_account)}")

    question = input("누구의 팔로우 수가 더 많은가요? A or B : ").lower()

    # 계정 비교 및 점수
    wjatn = compare(question, a_account, b_account)     # wjatn : 점수
    if wjatn :
        score += 1
        print(logo)
        print(f"정답입니다.😍 현재 점수 : {score}")
    else:
        game_over = True
        print(logo)
        print(f"틀렸습니다.😭 최종점수 : {score}")
