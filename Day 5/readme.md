# Day 5 목차

---

25-02-18 작성

# Loops

## For Loop
구조
```
for item in list_of_item:
    # Do something to each item
```
- 같은 코드 라인을 여러번 실행함

예시 1. fruits 목록을 1개씩 출력하고 싶을 때
```
fruits = ["Apple", "Peach", "Pear"]
for f in fruits:
    print(f)
```

f 출력 시, fruits 목록의 과일들이 출력된다.(▼)

![Image](https://github.com/user-attachments/assets/3366f5a6-fffd-42d5-bcb3-2d2fcaee32e0)


예시 2. fruits + pie를 붙여서 출력하고 싶을 때
```
for f in fruits:
    print(f)
    print(f + " pie")
```
f 출력 시, fruits + 'fruits[] + pie' 출력(▼)

![Image](https://github.com/user-attachments/assets/845aedfb-7a1c-4431-84db-c750d1478b53)


예시 3. 들여쓰기
```
for f in fruits:
    print(f)
    print(f + " pie")
    # print(fruits)
```
f와 f + pie의 출력이 끝날 때 마다 ['Apple', 'Peach', 'Pear']를 출력함(▼)

(fruits list를 3번 출력한단 소리)

![Image](https://github.com/user-attachments/assets/785b810b-7653-4bd3-b89b-cb6737b31d27)


예시 3.1 fruits list를 1번만 출력하고 싶다면 for문 안에 넣지 말 것
```
for f in fruits:
    print(f)    # print 1. Apple 2. Peach 3. Pear
    print(f + " pie")   # print 1. Apple pie 2. Peach pie  3. Pear pie

print(fruits)
```
출력 시(▼)

![Image](https://github.com/user-attachments/assets/a60a1c40-3fe1-457a-b537-a104584cb8bc)