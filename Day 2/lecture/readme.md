# Data Types
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

## 유형 오류, 유형 검사 및 유형 변환
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

## 파이썬의 수학적 연산
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
| ** | exponents |
| * | multiplication |
| / | division |
| + | addition |
| - | subtraction |

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