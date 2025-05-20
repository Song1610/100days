# Day 8 목차
1. Function with Inputs
    - [PAUSE 1. function review](#pause-1-function-review)
    - [function with input](#function-with-input)
     - [Parameter \& Argument 비교](#parameter--argument-비교)
2. [Life in Weeks](#life-in-weeks)
  
3. 위치 인수(Positional Argument) \& 키워드 인수(Keyworkd Argument)
     - [Positional Argument](#positional-argument)
       - [PAUSE 2. functions with more than 1 input](#pause-2-functions-with-more-than-1-input)
     - [Keyword Argument](#keyword-argument)
4. [Love Calculator](#love-calculator)
5. [Cipher](#cipher)

---

# Function with Inputs

# PAUSE 1. function review
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

<div align="right">

[목차로](#day-8-목차)
</div>

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
|:---|:---|
| 매개변수 | 인수 |
| 전달되는 데이터의 이름 | 데이터의 실제 값 |
| 함수 안에서 매개변수를 참조하고 작업하기 위해 사용됨 | 실제 데이터 조각으로 호출될 때 함수로 넘겨짐 |

<div align="right">

[목차로](#day-8-목차)
</div>

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
<div align="right">

[목차로](#day-8-목차)
</div>


# 위치 인수(Positional Argument) & 키워드 인수(Keyworkd Argument)
## Positional Argument

```py
def myfunction(a,b,c):
    # Do this with a
    # Then do this with b
    # Finally do this with C

myfunction(1,2,3)
```
a = 1 <br>
b = 2 <br>
c = 3 <br>

함수의 호출에서 argument의 순서를 변경하면,

```py
def myfunction(a,b,c):
    # Do this with a
    # Then do this with b
    # Finally do this with C

myfunction(3,1,2)
```
a = 3 <br>
b = 1 <br>
c = 2 <br>


### PAUSE 2. functions with more than 1 input
```py
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")

greet_with("MG", "paris")
```

결과(▼) <br>
<img width="214" alt="Image" src="https://github.com/user-attachments/assets/30de0532-beb9-4b32-9f90-01ee776eba77" />


입력데이터의 순서를 바꿔서 출력 시
```py
greet_with("paris", "MG")
```
결과(▼) <br>
<img width="185" alt="Image" src="https://github.com/user-attachments/assets/d7f8fef8-839d-40c6-91c4-d3602e631b95" /> <br>

함수를 지정할 때 특정 매개변수를 지정하지 않았기 때문에 "mg"는 location에 할당되고 "paris"는 name에 할당되어 나옴 

<div align="right">

[목차로](#day-8-목차)
</div>

## Keyword Argument

함수호출에 매개변수와 인수를 매핑하여 출력한다.

```py
def myfunction(a,b,c):
    # Do this with a
    # Then do this with b
    # Finally do this with C

myfunction(c = 3,a = 1,b = 2)
```
a = 1 <br>
b = 2 <br>
c = 3 <br>
으로 출력 된다.

```py
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")

greet_with(location="paris", name="mg")
```

결과(▼) <br>

<img width="221" alt="Image" src="https://github.com/user-attachments/assets/f0a8cfcc-de31-450d-b72d-dc13d40472c7" />

<div align="right">

[목차로](#day-8-목차)
</div>


# Love Calculator
[Exercise Link](https://github.com/Song1610/100days/tree/main/Day%208/exercise/love_calculator)

<div align="right">

[목차로](#day-8-목차)
</div>

# Cipher
**[Demo link](https://appbrewery.github.io/python-day8-demo/) <br>**

[cipher1]() <br>
[cipher2]() <br>
[cipher3]() <br>

<div align="right">

[목차로](#day-8-목차)
</div>