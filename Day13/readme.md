# Day 13 목차
- [Day 13 목차](#day-13-목차)
- [Debugging](#debugging)
- [Describe the Problem](#describe-the-problem)
- [Reproduce the Bug](#reproduce-the-bug)
- [Play Computer](#play-computer)
- [Fix the Errors](#fix-the-errors)
  - [origin code](#origin-code)
    - [pause 1. print error 디버깅](#pause-1-print-error-디버깅)
    - [pause 2. try - except 디버깅](#pause-2-try---except-디버깅)
    - [pause 3. print 출력](#pause-3-print-출력)
- [Use Print](#use-print)
  - [pause 1. print()를 이용해서 디버그](#pause-1-print를-이용해서-디버그)
  - [pause 2. 코드 수정](#pause-2-코드-수정)
- [Use a Debugger](#use-a-debugger)
  - [디버거 사용법](#디버거-사용법)
  - [PAUSE 1](#pause-1)
  - [Debugging Final Tips](#debugging-final-tips)
- [Code Challenge](#code-challenge)


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

<div align="right">

[목차로](#day-13-목차)
</div>

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

<div align="right">

[목차로](#day-13-목차)
</div>


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

<div align="right">

[목차로](#day-13-목차)
</div>

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


<div align="right">

[목차로](#day-13-목차)
</div>


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


<div align="right">

[목차로](#day-13-목차)
</div>


---

# Use a Debugger
Debugger : Pycharm과 같은 IDE(지능형 개발 환경)에 내장되어 있는 디버깅 도구

## 디버거 사용법
1. 중단점 정의 : 디버그 실행 중에 특정 줄에 있는 코드에서 일시정지 <br>
아래 그림처럼 코드의 줄 번호가 있는 곳에 `중단점(빨간 점)`을 설정할 수 있음 <br>
<img width="465" height="188" alt="Image" src="https://github.com/user-attachments/assets/e74f98bb-a098-47f9-b1de-f46e295cfb01" /> <br>


2. 스텝 오버(step over) : 코드를 한 줄 씩 실행함 <br>
<img width="194" height="142" alt="Image" src="https://github.com/user-attachments/assets/5c026be6-badf-4de3-99ee-a7c7547ce7c9" /> <br>


3. 스텝 인투(step into) : 코드가 참조하는 다른 모듈의 실행을 보여줌 (예 : random 모듈) <br>
<img width="191" height="85" alt="Image" src="https://github.com/user-attachments/assets/acb49832-42c9-445e-bfd8-7cd60a7a455c" /> <br>
- 코드의 문제점을 알아내는데 도움이 되는 힌트를 제공하기도 함 <br>


4. Step Into My Code : Step Into와 동일한 기능을 수행하지만, 적용 범위가 자신의 프로젝트 코드로 제한되고 random과 같은 라이브러리 코드는 무시함 <br>
<img width="284" height="103" alt="Image" src="https://github.com/user-attachments/assets/608c3cb1-42da-419f-a5df-c6c8a5e7d805" /> <br>

5. [filename] 다시실행 : 디버그 실행을 다시 시작하고 중단점에서 멈춤 <br>
<img width="203" height="110" alt="Image" src="https://github.com/user-attachments/assets/c4e5e895-a4f0-4e58-b43d-3efd209d2df7" /> <br>

6. 스레드와 변수 : 작업 중인 변수의 값을 보여주어 값 추적 가능 <br>
<img width="370" height="196" alt="Image" src="https://github.com/user-attachments/assets/cedd4fa0-9f69-407f-a0ea-abcf248d8ec2" /> <br>



## PAUSE 1
PyCharm 디버거를 사용하여 아래 시작 코드의 문제를 파악하고 해결하세요.

__original code__

```py
import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
```

`b_list` 결과값(▼)

```
[41]
```

`b_list`가 for _ in 함수에 들어가 있지 않아 마지막 결과값만 출력된다.

<br> <br> 

__디버깅한 코드(▼)__

```py
import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

```

디버깅 코드 결과값(▼)
```
[6, 8, 12, 18, 27, 41]
```


## Debugging Final Tips 
- Take a Break : 머리가 안돌아가면 잠시 쉬세요. ㅋㅋㅋ
- Ask a Friend : 그래도 안되면 누군가에게 물어보세요.
- Run often : 코드를 짜면 자주 run 하세요.


<div align="right">

[목차로](#day-13-목차)
</div>

---

# Code Challenge
코드를 읽고 문제를 찾아 수정하여 프로그램을 실행하세요.

1. [Debugging Odd or Even](https://github.com/Song1610/100days/blob/main/Day13/exercise/Debugging%20Odd%20or%20Even.py)
2. [Debugging Leap Year](https://github.com/Song1610/100days/blob/main/Day13/exercise/Debugging%20Leap%20Year.py)
3. [Debugging FizzBuzz](https://github.com/Song1610/100days/blob/main/Day13/exercise/Debugging%20FizzBuzz.py)

<div align="right">

[목차로](#day-13-목차)
</div>