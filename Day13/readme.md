# Day 13 목차
- Debugging
- Describe the Problem
- Reproduce the Bug
- Play Computer


---
# Debugging
코드에서 버그를 제거하는 과정

버그를 재빨리 식별하고 제거하는 방법
1. Describe the Problem : 문제설명
2. Reproduce the Bug : 버그를 다시 만들기

---
# Describe the Problem

아래 코드를 보고 답변을 코멘트로 작성하세요.
```py
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()
```
1. for 루프는 무슨 역할을 하나요?
   - 코드를 반복적으로 실행할 수 있게 함(1부터 20까지(i)를 넣어서 코드를 반복적으로 실행)
2. 이 함수는 언제 "You got it"을 출력하나요?
   - i가 20일 때
3. i의 값에 대해 어떤 가정을 하고 있나요?
   - i가 20일 때 "you got it"을 출력한다.

for i in range(1,20) 은 20까지 실행하지 않고 19까지만 실행한다.

수정된 코드(▼)
```py
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()
```

---
# Reproduce the Bug
일부 버그는 교묘하게 특정 조건에서만 발생합니다. <br>
이러한 버그를 디버깅하려면 버그를 안정적으로 재현하고, 문제를 진단하여 어떤 조건이 버그를 유발하는지 파악해야 합니다.

1. 오류가 발생하도록 코드를 변경하세요.
```py
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
dice_num = 6
print(dice_images[dice_num])
```
1부터 6까지 넣어서 테스트 한다. <br>


오류발생 코드로 수정 결과<br>
<img width="313" height="79" alt="Image" src="https://github.com/user-attachments/assets/73382621-fa83-43a1-a941-60e97513d8a7" />


2. 디버깅 하세요.

```py
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

```

범위는 0부터 시작하므로 randint를 (0,5)로 변경한다.


---

# Play Computer
