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

question = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

user = image[question]
computer = random.choice(image)
print("user:")
print(user)
print("computer:")
print(computer)

if user == computer:
    print("It's a draw!")
if user == 0:
    if computer == 1:
        print("You lose!")
    elif computer == 2:
        print("You win!")
elif user == 1:
    if computer == 0:
        print("You win!")
    elif computer == 2:
        print("You lose!")
elif user == 2:
    if computer == 0:
        print("You lose!")
    elif computer == 1:
        print("You win!")

import random

image = [rock, paper, scissors]

question = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

user = image[question]
computer = random.choice(image)
print("user:")
print(user)
print("computer:")
print(computer)

# and 코드 안먹힘 
if user == computer:
    print("It's a draw!")
elif user == 0 and computer == 2:
    print("you win!")
elif user == 2 and computer == 0:
    print("you lose.")
elif user < computer:
    print("you lose.")
elif user > computer:
    print("you win!")