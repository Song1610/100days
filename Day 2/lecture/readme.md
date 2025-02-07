# Data Types
## 1. Data Types
### Subscripting
- 가장 기본적인 데이터 타입
```
print("hello"[4])
```

### String
```
print("123" + "345")
```
* "123"  # "" 안에 있으면 어쨌든 문자로 취급

### integer : 정수

* 123_456_789 → 123456789 로 인식
```
print(123 + 345)
```


### float : 소수
```
print(3.14159)
```

### boolean : 참/거짓
```
print(True)
print(False)
```

## 2. Type Error, Checking and Conversion
### new 버전
#### PAUSE 1
len() 함수를 수정하여 더 이상 경고나 오류가 발생하지 않도록 하세요.
```
len(12345)
→ len("12345")
print(type("12345"))
```

#### PAUSE 2

4가지 데이터 유형을 모두 출력하기 위해 4가지 유형 검사를 작성합니다.

type() 및 print() 함수를 사용하여 출력 영역에 4줄을 출력하세요.

<class 'str'> <class 'int'> <class 'float'> <class 'bool'>

```
print(type("hello"))
print(type(1234))
print(type(3.1235))
print(type(True))
```

### 예전버전
```
num_char = len(input("what is your name?"))
```
* print("your name has " + num_char + " characters.")    error : num_char가 정수가 아님

```
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")
print(type(num_char))
```

```
a = 123
print(type(a))
```

```
print(70 + float("100.5"))
print(str(70) + str(100))
```



## 3. Mathematical Operations
### New(25-02-07)

```
print("My age: " + str(12))
```

연산자(PEMDASLR)
```
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)        # 2.0
print(type(6 / 3))  # result : <class 'float'>
print(6 // 3)       # 2
print(type(6 // 3)) # <class 'int'>
```

지수(2^4)
```
print(2**4)
```


#### pause 1. What is the output of this code?
```
print(3*3+3/3-3)    # 7
```

#### pause 2. Change the code so it outputs 3?
```
print(3*(3+3)/3-3)  # 3
```



### old
### 파이썬의 수학적 연산
```
3 + 5
10 - 3
7 * 4
6 / 3
2**10  # 2의 10승
```

* 같은 코드줄에 하나 이상의 연산을 하면 특정 우선순위가 있음

### pemdaslr
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

```
print(3*3+3/3-3)
print(3*(3+3)/3-3)
```

### rounding numbers(반올림)
```
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

### user scored a point
score = 0
score += 1  #score = score + 1 와 같다.
```
score -= 1     =     score = score - 1
score *= 1     =     score = score * 1
score /= 1     =     score = score / 1
```

### score
```
print(score)
print("your score is " + str(score))

score = 0
height = 1.8
isWinning = True
```

### f-string : 다양한 데이터를 복잡하지 않게 넣을 수 있다.
```
print(
    f"your score is {score}, your heigh is {height}, you are winning is {isWinning}"
)
```

나눗셈 후 나머지 ' % '