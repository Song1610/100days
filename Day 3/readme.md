# Day 3 목차

---

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

---

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

---

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

## 롤러코스터 타기

조건
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