# blackjack
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.sample(cards, 2)
    print(card)
    return card


user_cards = [deal_card()]
computer_cards = [deal_card()]

sum = sum(user_cards)
