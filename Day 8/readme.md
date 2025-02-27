# Day 8 목차

---

# Function with Inputs

## function review
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


## function with input

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


### Parameter & Argument 비교

| Parameter | Argument |
|:---:|:---:|
| 매개변수 | 인수 |
| 전달되는 데이터의 이름 | 데이터의 실제 값 |
| 함수 안에서 매개변수를 참조하고 작업하기 위해 사용됨 | 실제 데이터 조각으로 호출될 때 함수로 넘겨짐 |

