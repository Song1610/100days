# Day 8 목차
1.
2.
3.
4.
5.

---

# Function with Inputs

# function review
- `greet()` function 생성
- function 에 3개의 `print()` 작성
- greet() 호출

```py
def greet():
    print("1")
    print("2")
    print("3")

greet()
```


# function with input

```py
def myfunction(something):
    # Do this
    # Then do this
    # Fianlly do this

myfunction(123)
```

호출된 myfunction(123)이 something에 입력되며 아래처럼 출력됨(▼)

```py
def myfunction(something):
    # Do this 123
    # Then do this 123
    # Fianlly do this 123
```


예시(▼)
```py
def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do you do {name}?")

greet_with_name("kim")
```

결과 <br>
![Image](https://github.com/user-attachments/assets/f15c53a1-3672-4e0b-8657-fc7feec6b770)


## Parameter & Argument 비교

| Parameter | Argument |
|:---:|:---:|
| 매개변수 | 인수 |
| 전달되는 데이터의 이름 | 데이터의 실제 값 |
| 함수 안에서 매개변수를 참조하고 작업하기 위해 사용됨 | 실제 데이터 조각으로 호출될 때 함수로 넘겨짐 |



# Life in Weeks
f-String을 사용하여 `life_in_weeks()`라는 함수를 만들어 90세까지 산다면 몇 주가 남았는지 알려줍니다. <br>
현재 나이를 입력으로 받아서 다음 형식으로 남은 시간을 담은 메시지를 출력합니다. <br>

__x주 남았습니다.__

여기서 x는 입력된 나이가 90세까지 남은 실제 계산된 주 수로 대체됩니다.

**경고!** 테스트를 통과하려면 함수 이름을 life_in_weeks로 지정해야 합니다. 또한 출력은 예와 동일한 구두점과 철자를 사용해야 합니다. 마침표도 포함해서요! <br>

_힌트_ <br>
_There are 52 weeks in a year._


```py
def life_in_weeks(age):
    life_age = 90 - age
    weeks = life_age * 52
    print(f"You have {weeks} left.")

life_in_weeks(70)
```