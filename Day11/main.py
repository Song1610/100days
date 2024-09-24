import random

def deal_card():
    """ 랜덤으로 카드를 뽑는다. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# hint 5
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# hint 6
def calculate_score(cards):
    user_sum = user_cards[0] + user_cards[1]
    computer_sum = computer_cards[0] + computer_cards[1]
    print(f"user: {user_sum}")
    print(f"computer: {computer_sum}")

if user_sum or computer_sum == 21:
    if user_sum == 21 and (user_cards[0] or user_cards[1] == 11):
        print("User has blackjack")
    elif computer_sum == 21 and (computer_cards[0] or computer_cards[1] == 11):
        print("Computer has blackjack")

elif user_sum > 21:
    if user_cards[0] or user_cards[1] == 11:
        user_cards[0] or user_cards[1] == 1
        user_sum = user_cards[0] + user_cards[1]
        print(user_sum)

    elif not(user_cards[0] == 11) or not(user_cards[1] == 11):
        print("User has Lose.")