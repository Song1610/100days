# 가위바위보 만들기
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
# 사용해야할 거 : if/else, random, list
################ 이미지 없음!! ################
# import random

# user1_choice = input("what do you choose? Rock,Paper,Scissors.\n").lower()
# rps = ["rock", "paper", "scissors"]  # 0 1 2
# user1_index = rps.index(user1_choice)

# # 컴퓨터
# user2_index = random.randint(0, 2)
# user2_choice = rps[user2_index]
# print("Computer choose : ", user2_choice)

# # 바위 = 0, 보 = 1, 가위 = 2
# if user1_index == 0 and user2_index == 2:  #바위>가위
#     print("이겼어!!")
# elif user1_index == 2 and user2_index == 0:  #가위<바위
#     print("졌어!!")
# elif user1_index == user2_index:  # 가위=가위, 바위=바위, 보=보
#     print("비겼어!")
# elif user1_index < user2_index:  # 보<가위, 보<바위
#     print("졌어!!")
# elif user1_index > user2_index:  # 가위>보, 보>바위
#     print("이겼어!!")

# else:
#     print("잘못된 입력입니다.")

################ 이미지 있음 ################
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
