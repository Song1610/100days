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
