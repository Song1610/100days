# Day 4 목차

---
25-02-12 작성

# 1. random 
❖ [참고링크](https://docs.python.org/3/library/random.html)

## random.randint(a,b)
a <= n <= b
```
import random

random_int = random.randint(1, 10)
print(random_int)
```
`random 모듈 사용 시 import random 명시 필요`

1 <= n <= 10 이며 *정수*

출력 시, 1 ~ 10 범위의 정수가 출력된다.


## module
`random 모듈은 파이썬 팀이 만든 모듈이다.`

```
import random
import my_module

random_int = random.randint(1, 10)
print(random_int)

print(my_module.my_favourite_number)
# my_favourite_number = 1.2357
```
모듈파일의 함수를 불러오는 것

아래 이미지로 설명 대체
![Image](https://github.com/user-attachments/assets/9a248bb4-64a0-4902-888e-0ed96a88843e)
