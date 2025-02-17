# 25-02-13 작성

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0,2)


print("user:")
print(image[user_choice])
print("computer:")
print(image[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number. you lose.")
elif user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif user_choice == 2 and computer_choice == 0:
    print("you lose.")
elif user_choice < computer_choice:
    print("you lose.")
elif user_choice > computer_choice:
    print("you win!")