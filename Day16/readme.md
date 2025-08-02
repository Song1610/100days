# Day 16 목차
- [Day 16 목차](#day-16-목차)
- [OOP(Object Oriented Programming)](#oopobject-oriented-programming)
- [Procedural Programming](#procedural-programming)
- [How to Use OOP](#how-to-use-oop)
    - [_예시_](#예시)
- [Object(개체)](#object개체)
    - [_예시_](#예시-1)
    - [정리(표)](#정리표)
  - [1. Constructing Objects](#1-constructing-objects)
  - [2. Object Attributes](#2-object-attributes)
  - [3. Object Methods](#3-object-methods)
- [거북이 Challenge](#거북이-challenge)
  - [1. 거북이 컬러 변경](#1-거북이-컬러-변경)
  - [2. 거북이 100걸음 걷게하기](#2-거북이-100걸음-걷게하기)
  - [정리](#정리)
- [Python Packages](#python-packages)
- [Practice Modifying Object Attributes and Calling Methods](#practice-modifying-object-attributes-and-calling-methods)
- [Building the Coffee Machine in OOP](#building-the-coffee-machine-in-oop)


---

# OOP(Object Oriented Programming)
- 객체 지향 프로그래밍

# Procedural Programming
하나의 파일에 코드를 때려 넣으면 코드가 복잡해짐
그럼 코드에서 무슨 일이 벌어지는지 추적하기 어려움


그래서 각각 부분을 다른 모듈로 나눠서 동시에 작업

즉, 큰 작업을 작은 조각으로 나누어서 작업함 → OOP

# How to Use OOP
객체지향 프로그래밍 구현 방법

실제 객체를 모델링하기 위해 사용

### _예시_

model : 웨이터
1. has == __attributes__ (속성)
    ```py
    접시들기 = True
    테이블담당 = [4,5,6]
    ```
    - 보통 변수
    - 모델링 객체와 연관된 변수
    - 모델링의 속성을 변수로 지정


2. dose == __Methods__
    ```py
    def 주문받기(table, order):
        # takes order to chef

    def 계산하기(amount):
        # add money to restaurant
    ```
    - 특정 모델링 개체가 될 수 있는 함수
    - 모델링이 할 수 있는것을 메서드라고 함 <br>
       └ 함수로 모델링


<div align="right">

[목차로](#day-16-목차)
</div>

---

# Object(개체)
- 데이터 조각과 전체적인 기능을 결합
- 같은 유형에서 생성된 여러개의 개체를 가질 수 있다.
- 코드에서 사용할 실제 물건

### _예시_
![Image](https://github.com/user-attachments/assets/f35d9ce7-b3d7-4db4-a975-94fab0b08c7d) <br>
이것을 `blue print` 라고 함
<br>
<br>

### 정리(표)

|class|object|
|:--:|:--:|
|웨이터|남자웨이터 <br> 여자웨이터|


## 1. Constructing Objects
bule print에서 새 오브젝트를 생성하기

![Image](https://github.com/user-attachments/assets/02cace4d-f655-42f4-b9fc-877acca72069) <br>
class와 object 구분하기(▼)
```py
car = CarBlueprint()
```

|class|object|
|:--:|:--:|
|CarBlueprint()|car|

() : object의 구조를 활성화 시킴 

class에서 객체를 생성하기 위해 할 일 : 이름 명명(car)
<br>
<br>

예시 1: 다른모듈 불러오기
```py
import another_module
print(another_module.another_variable)
```
- `another_module.py` 파일을 만들어 `another_variable=12` 변수를 입력 후 `main.py`에서 import 하여 출력
- `main.py` 모듈에서 `another_module`모듈의 변수 값을 사용할 수 있다.


출력 결과(▼)
```
12
```
<br>
<br>

예시 2: 거북이 오브젝트 사용
```py
import turtle               # turtle 모듈 불러오기
timmiy = turtle.Turtle()    # timmiy라는 개체로 저장
```

▲의 `timmiy`를 단순화 하기(▼)
```py
from turtle import Turtle
timmy = Turtle()
```
<br>

결과 출력(▼)
```
<turtle.Turtle object at 0x000001DEE4FA7230>
```

<div align="right">

[목차로](#day-16-목차)
</div>


## 2. Object Attributes
속도나 연료처럼 계속 추적할 수 있는 데이터는 실제 자동차 모델링에 중요한 변수 <br>
이런 특성에 액세스 할 때의 구문(▼)
```py
#차의 속도를 측정하고싶을 때
car.speed
```
|Object|Attribute|
|:--:|:--:|
|car|speed|

가 된다.

<Br>

object와 attribute 구분하기(▼)
```py
from turtle import Turtle, Screen
timmy = Turtle()

my_screen = Screen()
print(my_screen.canvheight)
```
- Screen : 거북이가 나타날 창
- my_screen.canvheight : 거북이가 나타날 창의 크기

- `my_screen.canvheight`의 object와 attribute
    |Object|Attribute|
    |:--:|:--:|
    |my_screen|Canvheight|


결과 출력(▼)
```
<turtle.Turtle object at 0x000001DEE4FA7230>
300
```

<div align="right">

[목차로](#day-16-목차)
</div>


## 3. Object Methods
≒ dose 
car가 할 수 있는 것
```py
def move():
    speed = 60

def stop():
    speed = 0
```
methods : attribute가 연결된 함수(위에처럼)

object와 method 구분하기
```py
car.stop()
```
- `car.stop()`의 object와 Method
    |Object|Method|
    |:--:|:--:|
    |car|stop( )|


거북이 예시 3(▼)
```py
from turtle import Turtle, Screen
timmy = Turtle()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()         # object.method
```

출력결과(▼) <Br>
<img width="980" height="868" alt="Image" src="https://github.com/user-attachments/assets/bf2bedc7-a5eb-483b-8166-39b570356040" />

- 클릭하면 사라짐


거북이 예시 4(▼)
```py
from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")       # 0x000001DEE4FA7230 코드대신 모양으로 출력

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
```

출력결과(▼) <Br>
<img width="469" height="413" alt="Image" src="https://github.com/user-attachments/assets/b734f01a-10fb-452e-b93f-9266497e68a4" />


관련: [거북이 그래픽 사이트](https://docs.python.org/3/library/turtle.html)

<div align="right">

[목차로](#day-16-목차)
</div>

---

# 거북이 Challenge
## 1. 거북이 컬러 변경

- [컬러 참고 사이트](https://cs111.wellesley.edu/reference/colors)

<br>

```py
from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink")     # challenge 1

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
```

출력결과(▼) <Br>
<img width="451" height="401" alt="Image" src="https://github.com/user-attachments/assets/d19e2add-1049-4dde-a1f4-3eaf337bcb1d" />

<br>
<br>


## 2. 거북이 100걸음 걷게하기

```py
from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink")     # challenge 1
timmy.forward(100)          # challenge 2 거북이가 100걸음 걷게하기

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
```

출력결과(▼) <Br>
<img width="463" height="418" alt="Image" src="https://github.com/user-attachments/assets/8d82630a-1200-40ed-b00f-465b138bbc52" />


<div align="right">

[목차로](#day-16-목차)
</div>

---

## 정리

[거북이 코드]()

1. 블루프린트에서 class를 새 object로 만들기
    ```
    car = CarBlueprint()
    ```
2. object.attribute 사용
    ```
    my_screen.canvheight
    ```
3. object.method 사용
    ```py
    timmy.shape("turtle")
    timmy.color("DeepPink")
    timmy.forward(100)
    ```


<div align="right">

[목차로](#day-16-목차)
</div>

---

# Python Packages
[연습 prettytable]()

# Practice Modifying Object Attributes and Calling Methods
```py
from prettytable import PrettyTable

# todo 1: Create a PrettyTable object and save it to a variable called table
table = PrettyTable()

# todo 2: 표 만들기

table.add_column("Pokemon Name", ["피카츄", "꼬부기", "파이리"])
table.add_column("Type", ["전기", "물", "불"])

# todo 3: 중앙정렬에서 좌측정렬로 변경
# table.align["Pokemon Name"] = "l"
# table.align["Type"] = "l"
# table.add_column("Pokemon Name", ["피카츄", "꼬부기", "파이리"], "l")
# table.add_column("Type", ["전기", "물", "불"], "l")
table.align = "l"
# 위의 4개의 줄 = table.aling = "l" 

print(table.align)
print(table)

```


# Building the Coffee Machine in OOP
모듈을 이용해서 커피머신 코드를 재작성하세요.

커피머신 OOP 링크()