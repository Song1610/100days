import random
import my_module  # 모듈 불러오기

print(my_module.pi)

random_integer = random.randint(1, 15)
print(random_integer)

random_float = random.random()  # 0,1사이의 값 출력 0.0000 - 0.99999999
print(random_float)

random_decimal = random.uniform(0, 5)
print(random_decimal)

score = random.randint(1, 100)
print(f"Your score is {score}")

# list
'''
data structure : 데이터를 정리하고 저장하는 방법
'''

states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# states_of_america[1] = "Pencilvania"

# #데이터를 마지막에 추가하고 싶을 때
# states_of_america.append("SVT")
# states_of_america.append("Caratland")
# states_of_america.extend(["Scoups", "JH", "Joshua", "Jun"])

# ame = len(states_of_america)
# print(states_of_america[ame - 1])
# dirty_dozen = [ "Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = [
    "Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
    "Pears"
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(
    dirty_dozen[1][2]
)  # dirty_dozen[1] = fruites(0)와 vegetables(1) 중에 1, dirty_dozen[1][2] = vegetables(1) 내의 Tomatoes(2)

# list = [['a', 'b', 'c'], 'e', 'f', 'g']
#       __________________
# 1st         [0]          [1]  [2]  [3]
# 2rd      [0]  [1]  [2]

# print(list[0][1]) = b // print(list[1]) = e
