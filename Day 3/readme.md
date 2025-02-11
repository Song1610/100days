# Day 3 목차
1. [if else](#1-if-else)
2. [Modulo](#2-modulo-)
3. [Nested if/else](#3-nested-if--else)
4. [Multiple if](#4-multiple-if)
5. [Python Pizza](#5-python-pizza)
6. [Logical Operators](#6-logical-operators)
7. [Project(Treasure Island)](#7-treasure-island-project)

---

25-02-08 작성

# 1. if else
특정 조건에 따라 A나 B를 선택함
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride.")
else:
    print("Sorry you can't ride.")
```

비교연산자
| 기호 | 내용 |
|---|:---:|
| > | Greater than |
| < | Less than |
| >= | greater than or equal to |
| <= | less than or equal to |
| == | equal to |
| != | not equal to |

<div align="right">

[목차로](#day-3-목차)
</div>


# 2. Modulo (%)
숫자 / 2 = '나머지'
```
10 % 2 == 0
10 % 3 == 1
```

## pause 2 : check odd or even
입력한 숫자가 홀수인지 짝수인지 확인하는 코드를 작성하세요.

`홀수 : odd, 짝수 : even 출력`

```
number = int(input("check number : "))

num = number % 2
if num == 0:
    print("number is even.")
else :
    print("number is odd.")
```

<div align="right">

[목차로](#day-3-목차)
</div>

# 3. Nested if / else
if 안에 또 if
```
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
```

if / elif / else
```
if condition 1:
    do A
elif condition 2:
    do B
else:
    do this
```

## 3.1 롤러코스터 타기
**조건**
1. height >= 120 이상일 때 나이 확인
2. age
    - 12세 이하 : $5
    - 18세 이하 : $7
    - 18세 이상 : $12

```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))
    if age <= 12:
        print("pay $5")
    elif age <= 18:
        print("pay $7")
    else:
        print("pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
```

## 3.2 bmi
**조건**
1. if / elif / else 사용
2. 세부 조건
    - bmi is under 18.5 (not including), print out "underweight"
    - bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
    - bmi is 25 (including) or over, print out "overweight"
```
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi <= 18.5 or bmi < 25:
    print("normal weight")
else:
    print("overweight")
```
* bmi(old) : https://github.com/Song1610/100days/tree/main/Day%203/exercise/bmi

<div align="right">

[목차로](#day-3-목차)
</div>


# 4. Multiple if
if 조건이 모두 참이라면 a,b,c, 모두 실행된다.
```
if condition 1:
    do A
if condition 2:
    do B
if condition 3:
    do C
```

롤러코스터 예시 : https://github.com/Song1610/100days/blob/main/Day%203/lecture/multiple-if.py

<div align="right">

[목차로](#day-3-목차)
</div>


# 5. Python Pizza
pizza : https://github.com/Song1610/100days/tree/main/Day%203/exercise/pizza\

<div align="right">

[목차로](#day-3-목차)
</div>

# 6. Logical Operators
```
if condition 1 & condition 2 & condition 3:
    do this
else:
    do this
```
논리 연산자 3가지
1. and
2. or
3. not
![Image](https://github.com/user-attachments/assets/de699711-19c6-47bb-80bb-32acfdfec166)

exercise : 기존 롤러코스터 코드에서 45 <= age <= 55 사이의 사람들에게는 무료로 티켓을 줄 수 있게 코드를 작성하세요.

exercise link : https://github.com/Song1610/100days/blob/main/Day%203/lecture/my.py

<div align="right">

[목차로](#day-3-목차)
</div>


# 7. Treasure Island Project
link : https://github.com/Song1610/100days/tree/main/Day%203/project

<div align="right">

[목차로](#day-3-목차)
</div>