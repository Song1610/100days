# 복습
import random
from art import logo

# Todo 1 : 사용자와 컴퓨터 모두에게 무작위로 선택된 카드 값 2개로 구성된 시작 패를 나눠줍니다.

def deal_card():
    """ hint 4
    cards 목록을 사용하여 임의의 카드를 반환하는 함수
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):     # 공통 로직 하나로 점수를 계산하는 함수여야 함
    """
    hint 6 ~ 9
    6 : calculate_score() 함수 생성 : 이 함수는 카드 목록을 입력으로 받고 목록에 있는 모든 카드의 합을 점수로 반환합니다.
        공통 로직 하나로 점수를 계산하는 함수여야 함
    7 : calculate_score() 내부에서 블랙잭(2장의 카드 : 11 + 10)을 확인하고 실제 점수(21) 대신 0을 return
        0 = 블랙잭
        즉, 카드의 합 21 and 카드가 2장일 때 return 0
    8 : calculate_score() 내부에서 11(에이스) 확인, 점수가 21을 넘으면 11을 제거하고 1로 변경
        append(), remove() 사용
    9 : calcuate_score() 호출
        컴퓨터나 사용자가 블랙잭을 가지고 있거나 사용자의 점수가 21을 넘으면 게임이 종료됩니다.
    """
    if sum(cards) == 21 and len(cards) == 2:
        # if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    return sum(cards)

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)



# hint 13 : compare()라는 함수를 만들고 user_score와 computer_score를 전달(u_score, c_score)합니다.
def compare(u_score, c_score):
    if c_score == u_score:
        return f"점수가 같습니다. 비겼습니다.🙃"
    elif c_score == 0:
        return "BlackJack : Computer \nUser가 졌습니다.😭"
    elif u_score == 0:
        return "BlackJack : User, \nUser가 이겼습니다.😆"
    elif u_score > 21:
        return "사용자가 졌습니다.😭"
    elif c_score > 21:
        return "사용자가 이겼습니다.😄"
    elif u_score > c_score:
        return "사용자가 이겼습니다.😄"
    elif u_score < c_score:
        return "사용자가 졌습니다.🥹"


def start_game():
    print(logo)
    # hint 5 : deal_card()와 append()를 사용하여 user와 컴퓨터에 각각 2장의 카드를 나눠준다.
    # 빈 변수를 만드는 부분 이 부분이 게임의 시작부분이 됨
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    # hint 11 : 새 카드를 뽑을 때마다 점수를 다시 확인해야 하며 게임이 끝날 때까지 힌트 9의 확인을 반복해야 합니다.
    while not game_over:
        """
        10 : 게임이 끝나지 않았다면 사용자에게 다른 카드를 뽑을 지 묻습니다.
             뽑을 경우 deal_card() 함수를 사용하여 user_cards 목록에 다른 카드를 추가, 뽑지 않으면 게임 종료
        11 : 새 카드를 뽑을 때마다 점수를 다시 확인해야 하며 게임이 끝날 때 까지 hint 9의 확인을 반복해야합니다.
            while 함수를 이용할 것
    
        """
        # hint 9
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User의 카드 : {user_cards}, User의 카드 점수 : {user_score}")
        print(f"컴퓨터의 첫 번째 카드 : {computer_cards[0]}")

        # hint 10
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else :
            user_question = input("다른 카드를 뽑으시겠습니까? y or n : ")
            if user_question == "y":
                user_cards.append(deal_card())
            else:
                game_over = True


    # hint 12: 사용자가 완료하면 컴퓨터가 플레이하도록 할 때입니다. 컴퓨터는 점수가 17점 미만인 한 계속 카드를 뽑아야 합니다.
    while computer_score < 17 and computer_score != 0 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"User 최종 카드 : {user_cards}, User의 최종 카드 점수 : {user_score}")
    print(f"컴퓨터 최종 카드 : {computer_cards}, 컴퓨터의 최종 카드 점수 : {computer_score}")
    print(compare(user_score, computer_score))

# hint 14 : 사용자에게 게임을 다시 시작할지 묻습니다. 사용자가 예라고 대답하면 콘솔을 지우고 새로운 블랙잭 게임을 시작하고 art.py의 로고를 표시합니다.

while input("게임을 시작하시겠습니까? y or n : ") == "y":
    print("\n" * 10)
    start_game()