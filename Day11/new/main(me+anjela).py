import random
from art import logo

# hint 4
def deal_card():
    """ 카드를 무작위로 출력 """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# hint 6
"""
user_cards = [], computer_cards = [] 위로 순서 변경한 이유 :
함수를 호출하고 싶은데 함수가 선언되지 않았으므로 호출 할 수 없음
그래서 카드를 나눠주기 전에 호출되어야 함
"""
def calculate_score(cards):
    """
    카드 목록을 가져와서 점수로 반환
    hint 6 ~ 9 
    """
    # hint 7
    if 11 in cards and 10 in cards and len(cards) == 2:
    # if sum(cards) == 21 and len(cards) == 2:
        return 0

    # hint 8
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# hint 13 / 함수를 호출하기 위해서는 우리가 사용하려는 줄 전에 선언되어야 한다.
def compare(u_score, c_score):    # user_score, computer_score : 함수 밖의 파라미터 이름과 똑같아서 변경해주어야함.
    if u_score == c_score:
        return "Draw(비김)"
    elif c_score == 0:
        return "Computer is Blackjack! \nyour lose."
    elif u_score == 0:
        return "User is Blackjack!\n you win."
    elif u_score > 21:
        return "your lose"
    elif c_score > 21:
        return "computer lose."
    elif u_score > c_score:
        return "User win."
    elif u_score < c_score:
        return "Computer win."

def game():     # hint 14, user가 y를 선택하면 게임이 실행되어야 함
    print(logo) # hint 14
    # hint 5
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    """
    1. is_game_over loop 안에서 computer_score 변수 정의 → hint 12의 while loop로 넘어감
    2. 하지만 오류가 있을 경우 or is_game_over loop를 통째로 건너 뜀 →  is_game_over loop의 computer_score에 값이 없음
    3. 빈 변수를 정의한 user_cards, computer_cards 아래에 추가 작성
    기본 값 '0'을 설정불가 : 게임에 블랙잭이 있기때문에 0을 사용할 수 없음

    * user_score도 마찬가지라 computer_score처럼 작성해준다.
    """ 
    is_game_over = False


    for a in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
        """ 아래와 같은 코드
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)
        """

    while not is_game_over: # hint 11 : hint 9와 10을 반복
        # hint 9
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards : {user_cards}, current score : {user_score}")
        print(f"computer first card : {computer_cards[0]}")    # computer는 첫번째 카드만 보여주기


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        # hint 10
        else:
            card_question = input("다른 카드를 받으려면 'y'를 입력하고, 패스하려면 'n'을 입력하세요. ")
            if card_question == "y":
                user_cards.append(deal_card())
            
            else: is_game_over = True


    # hint 12
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())                  # 컴퓨터 카드 추가
        computer_score = calculate_score(computer_cards)    # 컴퓨터 카드 재합산 update, 업데이트 된 컴퓨터 스코어는 calculate_score의 반환 값과 같다.


    print(f"Your final card : {user_cards}, final score : {user_score}")
    print(f"Computer final card : {computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score))

# hint 14

while input("블랙잭 게임을 하시겠습니까? 'y' 또는 'n'을 입력하세요. : ") == "y":
    print("\n" * 10)
    game()
    