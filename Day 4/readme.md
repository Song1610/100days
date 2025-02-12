# Day 4 목차

---
25-02-12 작성

# 1. random 
❖ [참고링크](https://docs.python.org/3/library/random.html)

## random.randint(a,b)
범위 : a <= n <= b
```
import random

random_int = random.randint(1, 10)
print(random_int)
```
`random 모듈 사용 시 import random 명시 필요`

1 <= n <= 10 이며 *'정수'*이다. 

출력 시, 1 ~ 10 범위의 정수가 출력된다.


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


## random.random()
- 난수 부동 소수점 수를 생성하는 random 모듈
- 범위 : 0.0 <= x <= 1.0
- 파이썬에서 난수를 다룰 때 많이 사용하는 핵심 기술 중 하나
- 0부터 1까지의 숫자 중 부동점 수를 무작위로 생성

```
import random

random_number0_1 = random.random()
print(random_number0_1)

# print 1 = 0.30473346318301686
# print 2 = 0.8813012984957519
```

![Image](https://github.com/user-attachments/assets/8eebfa84-5fb8-43e5-b627-468f0df519ac)

