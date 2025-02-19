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
1. def 이용 기능 지정
2. 함수에 이름 부여( my_function(): )
3. 코드 작성(# Do this ~ )
    * def기능이 트리거 될 때 실행된 함수로 들어감
4. 함수 호출( my_function() )

```
"move"
"turn left"
"tun right"
"move"
"move"
...
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

## 로봇(reeborg's world) exercise
[exercise file(old)](https://github.com/Song1610/100days/tree/main/Day%206/exercise)

### alone
[exercise link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json)

1. 오른쪽 방향 함수 생성
```py
def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_right()
```

2. Draw Square

![Image](https://github.com/user-attachments/assets/b1883bd7-32e3-4de7-99d9-b564950e22ee)

```py

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Draw Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
```

### 2. 허들 1
[exercise link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

[exercise file(old)](https://github.com/Song1610/100days/tree/main/Day%206/exercise)

