# Day 13 목차
- Debugging
- Describe the Problem
- Reproduce the Bug
- Play Computer
- Fix the Errors
- Use Print
- Use a Debugger 



---
# Debugging
코드에서 버그를 제거하는 과정

버그를 재빨리 식별하고 제거하는 방법
1. Describe the Problem : 문제설명
2. Reproduce the Bug : 버그를 다시 만들기

---
# Describe the Problem

아래 코드를 보고 답변을 코멘트로 작성하세요.
```py
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()
```
1. for 루프는 무슨 역할을 하나요?
   - 코드를 반복적으로 실행할 수 있게 함(1부터 20까지(i)를 넣어서 코드를 반복적으로 실행)
2. 이 함수는 언제 "You got it"을 출력하나요?
   - i가 20일 때
3. i의 값에 대해 어떤 가정을 하고 있나요?
   - i가 20일 때 "you got it"을 출력한다.

for i in range(1,20) 은 20까지 실행하지 않고 19까지만 실행한다.

수정된 코드(▼)
```py
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()
```

---
# Reproduce the Bug
일부 버그는 교묘하게 특정 조건에서만 발생합니다. <br>
이러한 버그를 디버깅하려면 버그를 안정적으로 재현하고, 문제를 진단하여 어떤 조건이 버그를 유발하는지 파악해야 합니다.

1. 오류가 발생하도록 코드를 변경하세요.
```py
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
dice_num = 6
print(dice_images[dice_num])
```
1부터 6까지 넣어서 테스트 한다. <br>


오류발생 코드로 수정 결과<br>
<img width="313" height="79" alt="Image" src="https://github.com/user-attachments/assets/73382621-fa83-43a1-a941-60e97513d8a7" />


2. 디버깅 하세요.

```py
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

```

범위는 0부터 시작하므로 randint를 (0,5)로 변경한다.


---

# Play Computer
아래의 코드를 실행하면 1994년생은 어떤 것도 출력되지 않는 에러가 발생함

```py
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
```

결과

<img width="266" height="82" alt="Image" src="https://github.com/user-attachments/assets/5a699a7f-358e-4381-8645-8062c7cd55db" />

<br><br>

코드 줄을 하나씩 실행해 보고 각각의 코드를 보고 논리적으로 평가한 뒤, 1994의 세대가 출력되도록 디버깅 하세요. <br>

```py
year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

```

결과 <br>

<img width="285" height="103" alt="Image" src="https://github.com/user-attachments/assets/f30a54f1-e1ae-4d92-95c1-95a9dc2481bc" />


---

# Fix the Errors

- 코드를 실행하기 전에 편집기에 표시되는 `모든 오류(빨간색 밑줄)`를 확인
- `경고(노란색 밑줄)` : 선택적인 수정사항, 추후에 문제를 일으킬 수도 있음

## origin code
```py
age = int(input("How old are you? "))
if age > 18:
print("You can drive at age {age}")
```

### pause 1. print error 디버깅
origin code에서 print 부분이 오류가 나지 않게 수정

```py
age = int(input("How old are you? "))
if age > 18:
    print("You can drive at age {age}")
```

### pause 2. try - except 디버깅


```py
age = int(input("How old are you? "))
if age > 18:
    print("You can drive at age {age}")
```

<br>
age에 `seventeen`과 같은 문자열을 넣으면 아래와 같은 `ValueError`가 발생
<br>

```
age = int(input("How old are you? "))
ValueError: invalid literal for int() with base 10: 'seventeen'
```

- 제공된 문자열을 `int`정수로 구문 분석할 수 없음
- `int()`안에 들어갈 값이 문자열은 맞지만 그 값이 int로 변환할 수 없어 생기는 오류

<br>
잠재적인 오류(ValueError)를 잡아 코드가 충돌하지 않게 하고 코드가 다운되는 대안 경로를 제공함


```py
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in a an invalid number. Please try again.")
    age = int(input("How old are you? "))

if age > 18:
    print("You can drive at age {age}.")
```

실행결과(▼) <br>
<img width="471" height="105" alt="Image" src="https://github.com/user-attachments/assets/a5c8748c-a086-417a-bf5d-81e4d0b23858" />




### pause 3. print 출력
print 명령문이 출력 영역에 올바른 age 값을 표시하도록 디버깅

```py
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in a an invalid number. Please try again.")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")
```

결과<br>
<img width="219" height="63" alt="Image" src="https://github.com/user-attachments/assets/8ebc18db-975c-4e0e-bedd-103729fdc83d" />


---

# Use Print
`print()`는 코드를 디버깅하는 데 많은 도움이 된다.

__origin code__

```py
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

결과값

<img width="264" height="73" alt="Image" src="https://github.com/user-attachments/assets/2a18a15d-cbd1-49bc-950c-d8f362e72df1" />

total_word가 0이 된다.

## pause 1. print()를 이용해서 디버그
사용자가 제공하는 변수의 실제 값을 프린트

```py
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

print(f"페이지 : {pages}")
print(f"워드 페이지 : {word_per_page}")

```


결과

<img width="259" height="137" alt="Image" src="https://github.com/user-attachments/assets/69781c51-d58c-440a-944b-de173d786398" />


워드페이지의 값이 `0`인 것을 확인할 수 있음

## pause 2. 코드 수정
최종 총합이 프린트 될 수 있게 수정

```py
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

print(f"페이지 : {pages}")
print(f"워드 페이지 : {word_per_page}")
```

결과

<img width="259" height="121" alt="Image" src="https://github.com/user-attachments/assets/e24b9805-c6bf-49b3-a25e-a1c1f379314c" />


---

# Use a Debugger