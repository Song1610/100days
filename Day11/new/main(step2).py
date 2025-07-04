import random
from art import logo

# Todo 1 : 사용자와 컴퓨터 모두에게 무작위로 선택된 카드 값 2개로 구성된 시작 패를 나눠줍니다.
# hint 4 : 아래 목록을 사용하여 임의의 카드를 반환하는 deal_card() 함수 만들기
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
#
# hint 6 : calculate_score() 함수 생성 : 이 함수는 카드 목록을 입력으로 받고 목록에 있는 모든 카드의 합을 점수로 반환합니다.
def calculate_score(cards):     # 공통 로직 하나로 점수를 계산하는 함수여야 함

    # hint 7 : calculate_score() 내부에서 블랙잭(2장의 카드만 있는 핸드: 에이스(11) + 10)을 확인하고 실제 점수 대신 0을 반환합니다.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    return sum(cards)
#
#     # 0은 게임에서 블랙잭을 나타냅니다.
#     # 카드의 합 21 and 카드가 2장일 때
#     if len(cards) == 2 and sum(cards) == 21:
#         return 0
#
#     # hint 8 : calculate_score() 내부에서 11(에이스)을 확인합니다. 점수가 이미 21을 넘으면 11을 제거하고 1로 바꾸세요.
#     # append() 및 remove()를 이용하세요.
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#         return sum(cards)
#
#     return sum(cards)
#
# # hint 13 : compare()라는 함수를 만들고 user_score와 computer_score를 전달합니다.
# def compare(u_score, computer_score):
#     if u_score == computer_score:
#         print("Draw(비김)")
#     elif computer_score == 0:
#         print("Computer is Blackjack! \nyour lose.")
#     elif u_score == 0:
#         print("User is Blackjack!\nyou win.")
#     elif u_score > 21:
#         print("your lose")
#     elif computer_score > 21:
#         print("computer lose.")
#     elif u_score > computer_score:
#         print("User win.")
#     elif u_score < computer_score:
#         print("Computer win.")
#
# compare(user_score, computer_score)

# hint 5 : deal_card()와 append()를 사용하여 user와 컴퓨터에 각각 2장의 카드를 나눠준다.
user_cards = []
computer_cards = []
not_game_over = False

for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

print(f"User의 카드 : {user_cards}")
print(f"컴퓨터의 첫 번째 카드 : {computer_cards[0]}")


#
#
# # hint 10 : 게임이 끝나지 않았다면 사용자에게 다른 카드를 뽑을지 묻습니다.
# while not_game_over:
#     # hint 9 함수 호출
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#
#     print(f"User 카드 : {user_cards}, 현재 카드 합 : {user_score}" )
#     print(f"Computer의 첫 번째 카드 : {computer_cards[0]}")
#
#     question = input("다른 카드를 받으려면 'y'를 입력하고, 패스하려면 'n'을 입력하세요. ")
#
#     if question == 'y':
#         # hint 10: 뽑을 경우 deal_card() 함수를 사용하여 user_cards 목록에 다른 카드를 추가합니다.
#         new_card = deal_card()
#         user_cards.append(new_card)
#
#         # hint 11 : 새 카드를 뽑을 때마다 점수를 다시 확인해야 하며 게임이 끝날 때까지 힌트 9의 확인을 반복해야 합니다.
#         new_user_card_score = sum(user_cards)
#         print(f"user card : ", user_cards)
#         print(f"user score :", new_user_card_score)
#
#         calculate_score(computer_cards)
#         print(f"computer score : {computer_score}")
#
#     else:
#         # hint 10 : 뽑지 않으면 게임이 종료됩니다.
#         # question == 'n'
#         not_game_over = False
#
#         print("The End")
#
#
# # hint 12: 사용자가 완료하면 컴퓨터가 플레이하도록 할 때입니다. 컴퓨터는 점수가 17점 미만인 한 계속 카드를 뽑아야 합니다.
# while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     new_computer_card_score = sum(computer_cards)
#
#     print(f"computer card : {computer_cards}")
#     print(f"computer score : {new_computer_card_score}")
#
#
#
#
# # hint 14 : 사용자에게 게임을 다시 시작할지 묻습니다. 사용자가 예라고 대답하면 콘솔을 지우고 새로운 블랙잭 게임을 시작하고 art.py의 로고를 표시합니다.
# again_question = input("블랙잭 게임을 하시겠습니까? 'y' 또는 'n'을 입력하세요. : ")
# while again_question == 'y':
#     print("\n" * 10)
#     print(logo)
#     game()
#     compare(user_score, computer_score)
#
#
