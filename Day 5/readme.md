# Day 5 목차

---

25-02-18 작성

# Loops

# 1. For Loop
## 구조
```py
for item in list_of_item:
    # Do something to each item
```
- 목록의 항목을 살펴보고 각각 항목으로 작업을 수행할 수 있음
- 같은 코드 라인을 여러번 실행함

## 예시 1. fruits 목록을 1개씩 출력하고 싶을 때
```py
fruits = ["Apple", "Peach", "Pear"]
for f in fruits:
    print(f)
```

f 출력 시, fruits 목록의 과일들이 출력된다.(▼)

![Image](https://github.com/user-attachments/assets/3366f5a6-fffd-42d5-bcb3-2d2fcaee32e0)


## 예시 2. fruits + pie를 붙여서 출력하고 싶을 때
```py
for f in fruits:
    print(f)
    print(f + " pie")
```
f 출력 시, fruits + 'fruits + pie' 출력(▼)

![Image](https://github.com/user-attachments/assets/845aedfb-7a1c-4431-84db-c750d1478b53)


## 예시 3. 들여쓰기
```py
for f in fruits:
    print(f)
    print(f + " pie")
    # print(fruits)
```
f와 f + pie의 출력이 끝날 때 마다 ['Apple', 'Peach', 'Pear']를 출력함(▼)

(fruits list를 3번 출력한단 소리)

![Image](https://github.com/user-attachments/assets/785b810b-7653-4bd3-b89b-cb6737b31d27)


### 예시 3.1 fruits list를 1번만 출력하고 싶다면 for문 안에 넣지 말 것
```py
for f in fruits:
    print(f)    # print 1. Apple 2. Peach 3. Pear
    print(f + " pie")   # print 1. Apple pie 2. Peach pie  3. Pear pie

print(fruits)
```
출력 시(▼)

![Image](https://github.com/user-attachments/assets/a60a1c40-3fe1-457a-b537-a104584cb8bc)

## Highest Score
[high_score link](https://github.com/Song1610/100days/tree/main/Day%205/exercise/high_score)


---
# 2. Range
range(a,b)는 다른 함수와 함께 사용됨

## 구조
```
for number in range(a,b):
    print(number)
```

## 숫자 출력 시
```py
for num in range(1,10):
    print(num)
```
![Image](https://github.com/user-attachments/assets/04925565-0e93-4e81-a835-2c9c5558ff32)


## 숫자 건너 뛰기
```py
for num in range(1,12,3):
    print(num)
```
3씩 건너 뛰어서 출력한다.

![Image](https://github.com/user-attachments/assets/04eddcfe-3b2f-42e1-9561-91f8ff33cdbe)

## PAUSE 1 - The Gauss Challenge
range를 이용해 1부터 100까지 숫자 더하기
```py
# PAUSE 1 - The Gauss Challenge
total = 0
for number in range(1, 101):
    total += number
    print(total)            # 더해진 값 확인용 / 없어도 됨
print(f"total : {total}")
```
출력 값 : `total : 5050`


## fizzbuzz
[fizzbuzz link](https://github.com/Song1610/100days/tree/main/Day%205/exercise/fizzbuzz)


# Password Generator Project
1. [Password Generator Demo](https://appbrewery.github.io/python-day5-demo/)
2. [Password Generator Project](https://github.com/Song1610/100days/tree/main/Day%205/project)