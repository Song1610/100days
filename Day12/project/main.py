import random
from art import logo

# todo 1 : 게임 순서대로 알고리즘 먼저 그리기
# todo 2 : 알고리즘대로 코드 작성
# 코드 정리
# 실행
###########################################

def random_number():
    """숫자 랜덤선택"""
    for number in range(1):
        random_num = int(random.randint(1,100))
        #print(f"숫자 : {random_num}")
    return random_num


def mode():
    """모드 선택"""
    mode = input("모드를 선택하세요(easy or hard) : ")
    if mode == "easy":
        choice = 10
        print(f"기회 : {choice}")
    else :
        choice = 5
        print(f"기회 : {choice}")
    return choice


def compare(ran_num, choice_num):   # GPT의 도움을 쪼끔 받았따
    """정답 추측하기"""
    while choice_num > 0:
        guess_num = int(input("추측한 숫자 : "))
        if guess_num > ran_num:
            print(f"{guess_num}보다 높습니다. Down👎👎")

        elif guess_num < ran_num:
            print(f"{guess_num}보다 낮습니다. Up👍👍")

        elif guess_num == ran_num:
            print(f"정답입니다!!! 😍😍😍")
            return

        choice_num -= 1
        print(f"남은 횟수 : {choice_num}번")

    if choice_num == 0:
        print(f"실패!! 정답은 {ran_num}입니다.😭")


def game():
    print(logo)
    print("Up & Down 게임 시작")
    ran_num = random_number()
    choice_num = mode()
    compare(ran_num, choice_num)

    

game()
