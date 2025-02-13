# Day 4 목차
1. random
    - [random.randint](#randomrandintab)
    - [module](#module)
    - [random.random](#randomrandom)
    - [random.uniform](#randomuniformab)
    - [Pause 1. head or tail](#pause-1-head-or-tail)
2. List

---
25-02-12 작성

# 1. random 
❖ [참고링크](https://docs.python.org/3/library/random.html)

## random.randint(a,b)
- 범위 : a <= n <= b
- [참고링크](https://docs.python.org/3/library/random.html#random.randint)
```
import random

random_int = random.randint(1, 10)
print(random_int)
```
`random 모듈 사용 시 import random 명시 필요`

1 <= n <= 10 이며 _'정수'_ 이다. 

출력 시, 1 ~ 10 범위의 정수가 출력된다.

<div align="right">

[목차로](#day-4-목차)
</div>


## module
**random 모듈은 파이썬 팀이 만든 모듈이다.**

```
import random
import my_module

random_int = random.randint(1, 10)
print(random_int)

print(my_module.my_favourite_number)
# my_favourite_number = 1.2357
```
모듈파일의 함수를 main.py로 불러오는 것

아래 이미지로 설명 대체
![Image](https://github.com/user-attachments/assets/9a248bb4-64a0-4902-888e-0ed96a88843e)

<div align="right">

[목차로](#day-4-목차)
</div>


## random.random()
- 난수 부동 소수점 수를 생성하는 random 모듈
- 범위 : 0.0 <= x <= 1.0
- 파이썬에서 난수를 다룰 때 많이 사용하는 핵심 기술 중 하나
- 0부터 1까지의 숫자 중 부동점 수를 무작위로 생성
- [참고링크](https://docs.python.org/3/library/random.html#random.random)

```
import random

random_number0_1 = random.random()
print(random_number0_1)

# print 1 = 0.30473346318301686
# print 2 = 0.8813012984957519
```

0.0 <= x <= 10.0 까지 임의의 부동 소수점 수를 생성
```
import random

random_number0_1 = random.random() * 10
print(random_number0_1)

# print 1 = 3.110870060485981
# print 2 = 7.311563937128691
# print 3 = 0.4456769070095645
```

모듈 순서 의미
![Image](https://github.com/user-attachments/assets/8eebfa84-5fb8-43e5-b627-468f0df519ac)

<div align="right">

[목차로](#day-4-목차)
</div>

## random.uniform(a,b)
- 범위 : a <= n <= b
- [참고링크](https://docs.python.org/3/library/random.html#random.uniform)

```
import random

random_float = random.uniform(1,10)
print(random_float)

# print 1 = 8.30030512496964
# print 2 = 3.1639974928791937
# print 3 = 1.8434584518167245
```

### random.random vs random.uniform 차이점
![Image](https://github.com/user-attachments/assets/5af73d9b-31fa-4a38-a499-f7c3c72abf4d)


<div align="right">

[목차로](#day-4-목차)
</div>

##  Pause 1. head or tail
random 모듈을 사용하여 동전의 앞,뒷면이 무작위로 나오게 코드를 작성하세요.

```
import random

h_t = random.randint(0,1)

if h_t == 0:
    print("Heads")
else:
    print("Tails")
```

<div align="right">

[목차로](#day-4-목차)
</div>

---
# 2. List
파이썬에서 그룹화 된 데이터를 정리하고 저장하는 방법(Data Strucrture)

## list 구조
```
fruits = ["item 1", "item 2", "item 3"]
```

[data structure 참고링크](https://docs.python.org/3/tutorial/datastructures.html)

## list index
list 전체 데이터 출력
```
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
```

list 지정 데이터 출력(인덱스) `인덱스 : '0'부터 시작`
```
print(states_of_america[0])

# Delaware
```

list 맨 마지막 데이터 출력  `음극 인덱스 : 숫자에 '-'를 붙여줘야함`
```
print(states_of_america[-1])    # Hawaii
print(states_of_america[-2])    # Alaska
```

## list data 추가
list data 변경
```
states_of_america[1] = "pencillla"

print(states_of_america[1]) # pencillla 출력
```

list data 추가(단수)
```
states_of_america.append("caratland")

print(states_of_america)

['Delaware', 'pencillla', ..., 'Alaska', 'Hawaii', 'caratland']
```
[data 추가 참고링크](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)


list data 추가(복수)
```
states_of_america.extend(["caratland", "jackland", "pioneeland"])

print(states_of_america)

['Delaware', 'pencillla', ..., 'Hawaii', 'caratland', 'jackland', 'pioneeland']

```

## Banker Roulette
친구 목록에서 무작위로 이름을 선택하는 코드를 작성하세요.

* 힌트
    - 작성방법 : 2가지
    - 인덱스를 사용하여 목록에서 항목을 선택하는 난수를 생성하는 방법
    - python docs를 이용하여 데이터를 가져오는 방법

```
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 첫번째 방법
f_index = random.randint(0,4)
print(friends[f_index])

# 두번째 방법
print(random.choice(friends))
```

## Index Error
```
print(len(states_of_america))
```
len 함수로 출력 시 states_of_america 인덱스 개수 = 50

하지만 print(states_of_america[50]) 을 실행하면 인덱스 에러가 뜬다.

`index는 항상 0부터 시작`

[len() 참고링크](https://docs.python.org/3/library/functions.html#len)

print(states_of_america[49])를 출력해야함
- -1을 사용하여 출력하세요.
```
print(states_of_america[49]) 를 출력하는 방법

# No.1
num_america = len(states_of_america)
print(states_of_america[num_america - 1])

# No.2
num_america_2 = len(states_of_america) -1
print(states_of_america[num_america_2])
```

## Nested list
list 안에 list

### 구조
```
list = [list1, list2]
# list = [[list1의 데이터], [list2의 데이터]]
```

### 예시
dirty_dozen의 데이터를 과일/채소로 구분해서 출력
```
# dirty_dozen = ["딸기", "사과", "포도", "배", "치커리", "케일","상추","감자","오이"]

# 과일과 채소를 구분해서 list
fruits = ["딸기", "사과", "포도", "배"]
vegetables = ["치커리", "케일", "상추", "감자", "오이"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
```

위 코드 print 시 결과(▾)
```
[['딸기', '사과', '포도', '배'], ['치커리', '케일', '상추', '감자', '오이']]
```

### 참고: index 안에 index
```
dirty_dozen = ["딸기", "사과", "포도", "배", "치커리", "케일","상추","감자","오이"]
```
기존 `print(dirty_dozen[0])` 출력 시 '딸기' 출력


index 안에 index
```
dirty_dozen = [fruits, vegetables]      # [['딸기', '사과', '포도', '배'], ['치커리', '케일', '상추', '감자', '오이']]
print(dirty_dozen[1][2])                
```
출력 = '상추'

왜냐면 dirty_dozen'[1]'[2] = fruites(0)와 vegetables(1) 중에 vegetables 선택,

dirty_dozen[1]'[2]' = vegetables(1) 내의 "상추"(2) 선택

```
list = [['a', 'b', 'c'], 'e', 'f', 'g']
       ________________
1st         [0]          [1]  [2]  [3]
2rd      [0]  [1]  [2]
```
print(list[0][1]) = b

print(list[1]) = e

둘의 결과값은 전혀 다르다.

---

# 가위바위보 프로젝트
[가위바위보](https://github.com/Song1610/100days/tree/main/Day%204/project)
