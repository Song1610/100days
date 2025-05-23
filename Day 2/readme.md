# Data Types 목차
1. [Data Types](#1-data-types) 
    * Subscripting
    * String
    * integer : 정수
    * float : 소수
    * boolean : 참/거짓
2. [Type Error, Checking and Conversion](#2-type-error-checking-and-conversion)
    * new
    * old
3. [Mathematical Operations](#3-mathematical-operations)
    * New(25-02-07)
    * Old(25-02-07)
4. [Number Manipulation](#4-number-manipulation)
    * New(25-02-07)
    * Old(25-02-07)

---

## 1. Data Types
### Subscripting
- 가장 기본적인 데이터 타입
```
print("hello"[4])
```

### String
```py
print("123" + "345")
```
* "123"  # "" 안에 있으면 어쨌든 문자로 취급


### integer : 정수

* 123_456_789 → 123456789 로 인식
```py
print(123 + 345)
```

### float : 소수
```py
print(3.14159)
```

### boolean : 참/거짓
```py
print(True)
print(False)
```

<div align="right">
  
[목차로](#data-types-목차)

</div>

---

## 2. Type Error, Checking and Conversion
### 2.1 new ▼
#### PAUSE 1
len() 함수를 수정하여 더 이상 경고나 오류가 발생하지 않도록 하세요.
```py
len(12345)
→ len("12345")
print(type("12345"))
```

#### PAUSE 2

4가지 데이터 유형을 모두 출력하기 위해 4가지 유형 검사를 작성합니다.

type() 및 print() 함수를 사용하여 출력 영역에 4줄을 출력하세요.

`<class 'str'> <class 'int'> <class 'float'> <class 'bool'>`

```py
print(type("hello"))
print(type(1234))
print(type(3.1235))
print(type(True))
```

### 2.2 old ▼
```py
num_char = len(input("what is your name?"))
print("your name has " + num_char + " characters.")
```
error : num_char가 정수가 아님

```py
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")
print(type(num_char))
```

```py
a = 123
print(type(a))
```

```py
print(70 + float("100.5"))
print(str(70) + str(100))
```


<div align="right">
  
[목차로](#data-types-목차)

</div>

---

## 3. Mathematical Operations
### New(25-02-07) ▼

```py
print("My age: " + str(12))
```

연산자(PEMDASLR)
```py
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)        # 2.0
print(type(6 / 3))  # result : <class 'float'>
print(6 // 3)       # 2
print(type(6 // 3)) # <class 'int'>
```

| 기호 | 내용 |
|---|:---:|
| () | paresntheses |
| + | addition |
| - | subtraction |
| * | multiplication |
| / | division |
| // | 몫 |
| % | 나머지 |
| ** | exponents(거듭제곱) |

지수(2^4)
```py
print(2**4)
```


#### pause 1. What is the output of this code?
```py
print(3*3+3/3-3)    # 7
```

#### pause 2. Change the code so it outputs 3?
```py
print(3*(3+3)/3-3)  # 3
```
* 같은 코드줄에 하나 이상의 연산을 하면 특정 우선순위가 있음

<div align="right">
  
[목차로](#data-types-목차)

</div>

---

## 4. Number Manipulation
### New(25-02-07) ▼

bmi 추가 코드 `bmi = 84 / 1.65 ** 2`

추가 : 정수(int)로 나타내기
```py
print(int(bmi))         # 30
```

#### Rounding a Number
추가 : 반올림(round)로 나타내기
```py
print(round(bmi))       # 31
print(round(bmi, 2))    # 30.85
```

#### Assignment Operators
User scores a point
```py
score = 0
score += 1
print(score)
```
- score = score + 1 와 같음

#### f-Strings
예시
```py
score = 0
height = 1.8
is_winning = True
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}.")
```


### old ▼
#### rounding numbers(반올림)
```py
print(8 / 3)
print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))
print(round(2.66666666, 2))
print(8 // 3)

result = 4 / 2
result /= 2
print(result)
```

#### user scored a point
score = 0
score += 1  #score = score + 1 와 같다.
```
score -= 1     ==     score = score - 1
score *= 1     ==     score = score * 1
score /= 1     ==     score = score / 1
```

#### score
```py
print(score)
print("your score is " + str(score))

score = 0
height = 1.8
isWinning = True
```

#### f-string : 다양한 데이터를 복잡하지 않게 넣을 수 있다.
```py
print(
    f"your score is {score}, your heigh is {height}, you are winning is {isWinning}"
)
```

나눗셈 후 나머지 ' % '

<div align="right">
  
[목차로](#data-types-목차)

</div>