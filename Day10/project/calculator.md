# Calculator Program

[Demo](https://appbrewery.github.io/python-day10-demo/)

```py
def add(n1, n2):
    return n1 + n2
```

my_favourite_calculation = add <br>
my_favourite_calculation(3, 5) # 8을 반환합니다. <br>
시작 파일에는 계산기가 수행할 수 있는 각 수학 계산을 참조하는 딕셔너리가 있습니다. <br>
계산기를 사용하여 덧셈, 뺄셈, 곱셈, 나눗셈을 수행할 수 있는지 확인해 보세요.


## Puase 1
TODO: 나머지 3가지 함수(뺄셈, 곱셈, 나눗셈)를 작성하세요.

## Puase 2
TODO: 이 4가지 함수를 딕셔너리에 값으로 추가하세요. <br>
keys = "+", "-", "*", "/"

## Puase 3
사전 연산을 사용하여 계산을 수행합니다.<br>
사전을 사용하여 4 * 8을 곱합니다. <br>
```py
print(operations["*"](4, 8))
```

### Function
- 프로그램은 사용자에게 `첫 번째 숫자`를 입력하도록 요청합니다.
- 프로그램은 사용자에게 `수학 연산자("+", "-", "*" 또는 "/")`를 입력하도록 요청합니다.
- 프로그램은 사용자에게 `두 번째 숫자`를 입력하도록 요청합니다.
- 프로그램은 선택한 수학 연산자를 기반으로 결과를 계산합니다.
- 프로그램은 사용자에게 이전 결과로 계속 작업할지 묻습니다.
- `y`인 경우, 프로그램은 이전 결과를 첫 번째 숫자로 사용하기 위해 루프를 돌고 계산 과정을 반복합니다.
- `n`인 경우, 프로그램은 사용자에게 첫 번째 숫자를 다시 묻고 이전 계산에 대한 모든 메모리를 지웁니다.
- art.py에서 로고를 추가합니다.

### Hint
1. 프로그램을 계획하기 위해 순서도를 작성해 보세요.
2. 연산 사전에서 곱셈을 호출하려면 다음과 같이 코드를 작성합니다.
```py
result = operations["*"](n1= 5, n2= 3)
```

---

## 완성

[main.py(new)](https://github.com/Song1610/100days/blob/main/Day10/project/new/solution.py)

[main.py(old)](https://github.com/Song1610/100days/blob/main/Day10/project/old/main.py)