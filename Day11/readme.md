# Day 11 BlackJack Demo Project

* Normal 😎: 아래의 힌트를 모두 사용해서 프로젝트를 완성하기
* Hard 🤔: 힌트 1,2,3만 이용해서 프로젝트 완성
* Extra Hard 😭: 힌트 1,2만 이용해서 프로젝트 완성
* Expert 🤯: 힌트 1만 이용하여 프로젝트 완성

---
## 목차
- [Day 11 BlackJack Demo Project](#day-11-blackjack-demo-project)
  - [목차](#목차)
  - [작성한 파일](#작성한-파일)
  - [blackjack summary](#blackjack-summary)
  - [Our Blackjack Game House Rules](#our-blackjack-game-house-rules)
  - [Hint](#hint)
    - [Hint 1](#hint-1)
    - [Hint 2](#hint-2)
    - [Hint 3](#hint-3)
    - [Hint 4](#hint-4)
    - [Hint 5](#hint-5)
    - [Hint 6](#hint-6)
    - [Hint 7](#hint-7)
    - [Hint 8](#hint-8)
    - [Hint 9](#hint-9)
    - [Hint 10](#hint-10)
    - [Hint 11](#hint-11)
    - [Hint 12](#hint-12)
    - [Hint 13](#hint-13)
    - [Hint 14](#hint-14)


---
## 작성한 파일
[old](https://github.com/Song1610/100days/tree/main/Day11/old) <br>
[new](https://github.com/Song1610/100days/tree/main/Day11/new) <br>
[blackjack summary](https://github.com/Song1610/100days/blob/main/Day11/blackajck_summary.md)
---
## Our Blackjack Game House Rules
* The deck is unlimited in size.
* There are no jokers.
* The Jack/Queen/King = 10.
* The Ace = 11 or 1.
* Use the following list as the deck of cards:
```
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```
* 목록의 카드는 뽑힐 확률: 동일
* 뽑힐 때 카드는 deck에서 제거되지 않음
* 컴퓨터 : 딜러

## Hint 
### Hint 1 
Go to this website and try out the Blackjack game:
https://games.washingtonpost.com/games/blackjack/


Then try out the completed Blackjack project here:
https://appbrewery.github.io/python-day11-demo/

### Hint 2 
프로그램 요구사항의 세부 내용 읽기:
http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

흐름도 만들기

### Hint 3 
흐름도 다운로드 후 읽기:
https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

흐름도
![day 11 blackjack flowchart-32](https://github.com/user-attachments/assets/0bf43b33-4f97-410d-9603-f9c2ae64fc44)


### Hint 4 
아래 목록을 사용하여 임의의 카드를 반환하는 `deal_card()` 함수 만들기:
```
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```
11은 ace이다.

### Hint 5 
`deal_card()`와 `append()`를 사용하여 user와 컴퓨터에 각각 2장의 카드를 나눠준다.
```
user_cards = []
computer_cards = []
```

### Hint 6 
`calculate_score()` 함수 생성 : 이 함수는 카드 목록을 입력으로 받고 목록에 있는 모든 카드의 합을 점수로 반환합니다. sum() 함수를 Google에서 검색하면 도움이 됩니다.

### Hint 7 
`calculate_score()` 내부에서 블랙잭(2장의 카드만 있는 핸드: 에이스 + 10)을 확인하고 실제 점수 대신 0을 반환합니다. 0은 게임에서 블랙잭을 나타냅니다.

### Hint 8 
`calculate_score()` 내부에서 11(에이스)을 확인합니다. 점수가 이미 21을 넘으면 11을 제거하고 1로 바꾸세요. Python 내장 함수 `append()` 및 `remove()`에 대한 설명서를 찾으려면 Google에서 검색해야 할 수도 있습니다.
https://developers.google.com/edu/python/lists#list-methods

### Hint 9 
`calculate_score()` 함수를 호출합니다. 컴퓨터나 사용자가 블랙잭(0)을 가지고 있거나 사용자의 점수가 21을 넘으면 게임이 종료됩니다.

### Hint 10 
게임이 끝나지 않았다면 사용자에게 다른 카드를 뽑을지 묻습니다. 뽑을 경우 `deal_card()` 함수를 사용하여 `user_cards` 목록에 다른 카드를 추가합니다. 뽑지 않으면 게임이 종료됩니다.

### Hint 11 
새 카드를 뽑을 때마다 점수를 다시 확인해야 하며 게임이 끝날 때까지 힌트 9의 확인을 반복해야 합니다.

### Hint 12 
사용자가 완료하면 컴퓨터가 플레이하도록 할 때입니다. 컴퓨터는 점수가 17점 미만인 한 계속 카드를 뽑아야 합니다.

### Hint 13 
`compare()`라는 함수를 만들고 `user_score`와 `computer_score`를 전달합니다.
- 컴퓨터와 사용자의 점수가 같으면 비깁니다.
- 컴퓨터가 블랙잭(0)이면 사용자가 집니다.
- 사용자가 블랙잭(0)이면 사용자가 이깁니다.
- user_score가 21점 이상이면 사용자가 집니다.
- computer_score가 21점 이상이면 컴퓨터가 집니다.
위의 어느 것도 해당되지 않으면 가장 높은 점수를 받은 플레이어가 이깁니다..

### Hint 14 
사용자에게 게임을 다시 시작할지 묻습니다. 사용자가 예라고 대답하면 콘솔을 지우고 새로운 블랙잭 게임을 시작하고 art.py의 로고를 표시합니다.