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

#Write your code below this line 👇

import random

image = [rock, paper, scissors]

# user
user_choice = int(input("뭐 낼거니? 0:바위, 1:보, 2:가위\n"))

if user_choice >= 3 or user_choice < 0:
    print("잘못된 입력입니다.")
else:
    user_image = image[user_choice]
    print("user choice : ", user_image)

# computer
computer_choice = random.randint(0, 2)
computer_image = image[computer_choice]
print("computer choice : ", computer_image)

# 확률
if user_choice == 0 and computer_choice == 2:
    print("이겼어")
elif user_choice == 2 and computer_choice == 0:
    print("졌어")
elif user_choice == computer_choice:
    print("비겼어")
elif user_choice > computer_choice:
    print("이겼어")
elif user_choice < computer_choice:
    print("졌어")
