# BlackJack Summary
힌트 코드 재작성 및 정리
# Hint 4 
아래 목록을 사용하여 임의의 카드를 반환하는 `deal_card()` 함수 만들기:
```
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

__작성 코드(▼)__
```py
 def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.chioce(cards)
    return card
```

<br><br>

# Hint 5 
`deal_card()`와 `append()`를 사용하여 user와 컴퓨터에 각각 2장의 카드를 나눠준다.
```
user_cards = []
computer_cards = []
```
__작성 코드(▼)__
```py
user_cards = []
computer_cards = []

for c in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
```

<br><br>


# Hint 6 
`calculate_score()` 함수 생성 : 이 함수는 카드 목록을 입력으로 받고 목록에 있는 모든 카드의 합을 점수로 반환합니다.
- sum() 함수를 Google에서 검색하면 도움이 됩니다.

__작성 코드(▼)__
```py
 def calcuate_score(cards):
    return sum(cards)
```


<br><br>


# Hint 7 
`calculate_score()` 내부에서 블랙잭(2장의 카드만 있는 핸드: 에이스 + 10)을 확인하고 실제 점수 대신 0을 반환합니다.
* 0은 게임에서 블랙잭을 나타냅니다.
* 11은 에이스이다.

__작성 코드(▼)__
```py
  def calcuate_score(cards):

    if 11 in cards and 10 in cards and len(2):
        return 0

    return sum(cards)
```
or 
```py
  def calcuate_score(cards):

    if sum(cards) == 21 and len(2):
        return 0

    return sum(cards)
```

<br><br>


# Hint 8 
1. `calculate_score()` 내부에서 11(에이스)을 확인합니다.
2. 점수가 이미 21을 넘으면 11을 제거하고 1로 바꾸세요.
   
* Python 내장 함수 `append()` 및 `remove()`에 대한 설명서를 찾으려면 Google에서 검색해야 할 수도 있습니다.
https://developers.google.com/edu/python/lists#list-methods

__작성 코드(▼)__
```py
   def calcuate_score(cards):

    if 11 in cards and 10 in cards and len(2):
        return 0

    
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)


    return sum(cards)
```

<br><br>


# Hint 9 
1. `calculate_score()` 함수를 호출합니다.
   - 호출 시 print()도 작성
2. 컴퓨터나 사용자가 블랙잭(0)을 가지고 있거나 사용자의 점수가 21을 넘으면 게임이 종료됩니다.

__작성 코드(▼)__
```py
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"User의 카드 : {user_cards}, User의 현재 카드 점수 : {user_score}")
print(f"Computer의 카드 : {computer_cards}, Computer의 현재 카드 점수 : {computer_score}")

if computer_score == 0 or user_score == 0 or user_score > 21:
    game_over = True
```

game_over 가 `True`가 되기 위해 calculate_score() 함수 전에 `game_over = False` 선언을 해야함 <br>
hint 5의 코드 안에 `game_over = False`를 추가 해준다.


```py
user_cards = []
computer_cards = []
game_over = False

for c in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
```


<br><br>


# Hint 10 
게임이 끝나지 않았다면 사용자에게 다른 카드를 뽑을지 묻습니다. 뽑을 경우 `deal_card()` 함수를 사용하여 `user_cards` 목록에 다른 카드를 추가합니다. 뽑지 않으면 게임이 종료됩니다.

__작성 코드(▼)__
```py
else :
    question = input("다른 카드를 뽑으시겠습니까? y or n: ")
    
    if question == "y":
        user_card.append(deal_card())
    else : 
        game_over = True
```

## Hint 9와 10을 합쳤을 때
```py
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if computer_score == 0 or user_score == 0 or user_score > 21:
    game_over = True

else :
    question = input("다른 카드를 뽑으시겠습니까? y or n: ")
    
    if question == "y":
        user_card.append(deal_card())
    else : 
        game_over = True
```

## 현재까지 작성된 코드(hint 4 ~ 10)
```py
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.chioce(cards)
    return card

def calcuate_score(cards):
    if 11 in cards and 10 in cards and len(2):
    return 0

    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
return sum(cards)

user_cards = []
computer_cards = []
game_over = False

for c in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"User의 카드 : {user_cards}, User의 현재 카드 점수 : {user_score}")
print(f"Computer의 카드 : {computer_cards}, Computer의 현재 카드 점수 : {computer_score}")


if computer_score == 0 or user_score == 0 or user_score > 21:
    game_over = True

else :
    question = input("다른 카드를 뽑으시겠습니까? y or n: ")
    
    if question == "y":
        user_card.append(deal_card())
    else : 
        game_over = True
```

<br><br>


# Hint 11 
새 카드를 뽑을 때마다 점수를 다시 확인해야 하며 게임이 끝날 때까지 힌트 9의 확인을 반복해야 합니다.

__작성 코드(▼)__
```py
while not game_over:
    # hint 9
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if computer_score == 0 or user_score == 0 or user_score > 21:
        game_over = True
    
    # hint 10
    else :
        question = input("다른 카드를 뽑으시겠습니까? y or n : ")
        
        if question == "y":
            user_card.append(deal_card())
        else : 
            game_over = True  
```


<br><br>


# Hint 12 
사용자가 완료하면 컴퓨터가 플레이하도록 할 때입니다. 컴퓨터는 점수가 17점 미만인 한 계속 카드를 뽑아야 합니다.

__작성 코드(▼)__
```py
while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)

```
computer_score != 0
- 이 조건을 추가하지않으면 computer score가 블랙잭일 때도 멈추지않고 카드를 계속 뽑는다.

computer_score = calculate_score(computer_cards)
- 이 전 점수 → 새 점수로 리셋


## 추가 내용 

함수가 `while computer_score < 17 and computer_score != 0:` 에 도달하기 전에 이미 `computer_score`의 값이 정해져 있음 <br>
하지만 오류가 있을 경우 `computer_score`에 값이 없다.
  
- 이럴 경우 에러가 날 수 있어 `computer_score`를 정의해야 함
- `user_score`도 마찬가지로 값을 정의해준다.
- user_cards, computer_cards 아래에 값을 정의해준다.

### 세부 설명
1. is_game_over loop 안에서 computer_score 변수 정의 → hint 12의 while loop로 넘어감
2. 하지만 오류가 있을 경우 or is_game_over loop를 통째로 건너 뜀 →  is_game_over loop의 computer_score에 값이 없음
3. 빈 변수를 정의한 user_cards, computer_cards 아래에 추가 작성
   - 기본 값 '0'을 설정불가 : 게임에 블랙잭이 있기때문에 0을 사용할 수 없음

* user_score도 마찬가지라 computer_score처럼 작성해준다.


```py
user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
game_over = False
```

<br><br>


# Hint 13 
`compare()`라는 함수를 만들고 `user_score`와 `computer_score`를 전달합니다.
- 컴퓨터와 사용자의 점수가 같으면 비깁니다.
- 컴퓨터가 블랙잭(0)이면 사용자가 집니다.
- 사용자가 블랙잭(0)이면 사용자가 이깁니다.
- user_score가 21점 이상이면 사용자가 집니다.
- computer_score가 21점 이상이면 컴퓨터가 집니다.
위의 어느 것도 해당되지 않으면 가장 높은 점수를 받은 플레이어가 이깁니다.

__작성 코드(▼)__
```py
def compare(user_score, computer_score):
    if computer_score == user_score:
        return "비김"
    elif computer_score == 0:
        return "User lose"
    elif user_score == 0:
        return "User win"
    elif user_score > 21:
        return "User lose."
    elif computer_score > 21:
        return "User Win!"
    elif user_score > computer_score:
        return "User Win!!"
    elif user_score < computer_score:
        return "User Lose."
```

user_score, computer_score는 이미 위에 다른 코드에서 사용하고 있기 때문에 다른 명칭으로 변경해준다. <br>
ex : u_score, c_score

__수정 코드(▼)__
```py
def compare(u_score, c_score):
    if c_score == u_score:
        return f"점수가 같습니다. 비겼습니다.🙃"
    elif c_score == 0:
        return "BlackJack : Computer \nUser가 졌습니다.😭"
    elif u_score == 0:
        return "BlackJack : User, \nUser가 이겼습니다.😆"
    elif u_score > 21:
        return "사용자가 졌습니다.😭"
    elif c_score > 21:
        return "사용자가 이겼습니다.😄"
    elif u_score > c_score:
        return "사용자가 이겼습니다.😄"
    elif u_score < c_score:
        return "사용자가 졌습니다.🥹"
```

## 추가내용
hint 12의 while문 아래에 최종 점수를 볼 수 있게 다음과 같이 작성한다.
- compare()를 호출하는 함수를 작성
- 최종 스코어를 볼 수 있게 print() 추가 작성

```py
print(f"User 최종 카드 : {user_cards}, User의 최종 카드 점수 : {user_score}")
print(f"컴퓨터 최종 카드 : {computer_cards}, 컴퓨터의 최종 카드 점수 : {computer_score}")
print(compare(user_score, computer_score))
```

<br><br>


# Hint 14 
사용자에게 게임을 다시 시작할지 묻습니다. 사용자가 예라고 대답하면 콘솔을 지우고 새로운 블랙잭 게임을 시작하고 art.py의 로고를 표시합니다.

__작성 코드(▼)__
```py
while input("게임을 시작하시겠습니까? y or n : ") == "y":
    print("\n" * 10)
    start_game()
```

위의 코드를 마지막 줄에 작성 후 작성한 코드에서 `start_game()`을 정의한다.

- **def()가 while()보다 윗쪽에 정의되어야 함**
- computer_score의 빈 변수를 정의한 부분부터 새 카드를 뽑는 부분까지 `start_game()`으로 정의

- __def | while 순서 세부 설명__ <br>
    user_cards = [], computer_cards = [] 위로 순서 변경한 이유 : <br>
    함수를 호출하고 싶은데 함수가 선언되지 않았으므로 호출 할 수 없음 <br> 
    그래서 카드를 나눠주기 전에 호출되어야 함


```py
def start_game():
    # 현재까지 작성된 코드 중 일부 
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for c in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"User의 카드 : {user_cards}, User의 현재 카드 점수 : {user_score}")
    print(f"Computer의 카드 : {computer_cards}, Computer의 현재 카드 점수 : {computer_score}")

    # hint 11 
    while not game_over:
        # hint 9
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        
        # hint 10
        else :
            question = input("다른 카드를 뽑으시겠습니까? y or n : ")
            
            if question == "y":
                user_card.append(deal_card())
            else : 
                game_over = True  
```




<br><br>

# 최종 코드 정리
[Step 2](https://github.com/Song1610/100days/blob/main/Day11/new/main(step2).py)
or 
[me+anjela.ver](https://github.com/Song1610/100days/blob/main/Day11/new/main(me%2Banjela).py)


# 노트 정리
![Image](https://github.com/user-attachments/assets/9ca5ecba-c68e-4334-b96e-af4028c2fdf3)

![Image](https://github.com/user-attachments/assets/6444625f-1816-4042-b148-4bcef1564100)