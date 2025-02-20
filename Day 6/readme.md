# 목차
25-02-18 작성

---

# Functions
함수 정의 방법 및 구조
```py
def my_function():
    # Do this
    # Then do this
    # finally do this

my_function()
```
<br>

1. def 이용 기능 지정
2. 함수에 이름 부여( my_function(): )
3. 코드 작성(# Do this ~ )
    * def기능이 트리거 될 때 실행된 함수로 들어감
4. 함수 호출( my_function() ) <br>

```
"move"
"turn left"
"tun right"
"move"
"move"
```

이렇게 많은 함수를 def를 사용해서 동시에 참조할 수 있다.(▼) 

```py
def get():
    "move"
    "turn left"
    "tun right"
    "move"
    "move"
```

# Indentation(들여쓰기)
들여쓰기 : 4칸, 스페이스바 : 1칸

```py
def myfunction():
√√√√print("hello")
print("bye")
```

print("hello") : myfunction() 안에 포함된 함수 <br>
print("bye") : myfunction()에 포함되지 않은 함수


```py
def myfunction():
√√√√if sky == 'clear':
√√√√√√√√print("blue")
    else:
        print("red")
```
함수블록(들여쓰기)를 잘 봐야함!


# While Loop
## 구조
특정 조건이 참이면 거짓이 될 때까지 코드가 반복 실행 됨

```py
while something_is_true:
    # Do this
    # Then do this
    # the do this
``` 

## 비교(for, while)
| for | while |
|---|---|
| for item in list_of_items: <br>   # Do something to each item  | while something_is_true: <br>   # Do something repeateldy |
| for numver in range(a,b): <br>   print(number) | - |
| list[] 안의 item을 반복하고 싶을 때 사용 <br> or <br> range(a,b)를 이용해서 반복작업을 해야할 때 사용 | 설정한 어떤 조건을 따를 때까지 반복 |
| 반복 횟수를 지정할 수 있음 | 특정 조건이 거짓으로 바뀔 때까지 반복 실행 |

[while()을 이용한 허들1 code](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/hurdle_1(while).py)

## Infinite Loop
조건이 참이면 무한 반복
<br>
예시:

```py
while 5 > 3:
    # Do this
    jump()
```
위 while()은 5>3 조건이 참이기 때문에 jump를 무한대로 반복한다.

## 로봇(reeborg's world) exercise
[robot exercise](https://github.com/Song1610/100days/tree/main/Day%206/exercise)
