# Display art
from art import logo, vs
from game_data import data
import random



def format_data(account):
    """format the account data into printable format.(account 데이터를 출력 가능한 형식으로 변경)"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, 설명: {account_desc}, 국가: {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """use if statement to check if user is correct.(if문을 사용해서 유저의 답이 맞는지 확인)"""
    if 


print(logo)

# Generate a random account from the game data(게임 데이터에서 무작위 계정 생성)
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)


print(f"A 계정 : {format_data(account_a)}")
print(vs)
print(f"B 계정 : {format_data(account_b)}")


# Ask user for a guess.(유저에게 질문하기)
guess = input("Who has more followers? Type 'A' or 'B': ").lower()



# check if user is correct.(유저가 맞는지 확인)
## Get follower count of each account(각 계정의 팔로워 숫자 가져오기)
a_follower_count = account_a["Follower_count"]
b_follower_count = account_b["Follower_count"]

is_correct = check_answer(guess, a_followers_count, b_follower_count)





# give user feedback on their guess(유저의 답에 대한 피드백)

# score kepping(점수 유지)

# make the game repeatable(게임을 반복하게 만들기)

# Making account at position B become the next account at position A(B계정의 위치를 A계정의 위치로 만들기)
