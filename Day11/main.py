import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.sample(cards, 2)
    return card


user_cards = deal_card()
computer_cards = deal_card()

print(f"user : {user_cards}")
print(f"computer : {computer_cards}")



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
        11 + [] > 21 -> 1 + [] 으로 변경
    elif user_cards[0] or user_cards[1] not 11:
        print("User has Lose.")