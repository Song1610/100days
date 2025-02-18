# Password Generator

# Instructions

The program will ask:
1. How many letters would you like in your password?
2. How many symbols would you like?
3. How many numbers would you like?

목표는 사용자로부터 이러한 질문에 대한 입력을 받은 다음 임의의 비밀번호를 생성하는 것입니다. Python 목록과 루프에 대한 지식을 사용하여 과제를 완료하세요.

# Easy Version (Step 1)

비밀번호를 순서대로 생성합니다.
* 4 letters
* 2 symbols and
* 3 numbers

4개 문자, 2개 기호, 3개 숫자를 원하면 비밀번호는 다음과 같습니다.

```
fgdx$*924
```
모든 글자가 함께 있는 것을 볼 수 있습니다. 모든 기호가 함께 있고 모든 숫자도 서로 뒤따릅니다. 먼저 이 문제를 풀어보세요.

## Hint
random.choice() 함수를 사용하면 목록에서 무작위 항목을 가져올 수 있다는 걸 기억하세요! 하지만 먼저 random 모듈을 가져와야 합니다.

# Hard Version (Step 2)

쉬운 버전을 완료하면 어려운 버전을 다룰 준비가 된 것입니다.

이 프로젝트의 고급 버전에서는 최종 비밀번호가 패턴을 따르지 않습니다.

따라서 위의 예는 다음과 같습니다.(▼)
```
x$d24g*f9
```
그리고 비밀번호를 생성할 때마다 기호, 숫자, 문자의 위치가 다릅니다.

## Hint
Try googling: "How to shuffle items in a List in Python"

# Solution
1. [https://replit.com/@appbrewery/password-generator-end](https://replit.com/@appbrewery/password-generator-end)
2. 

# demo
[Password Generator Demo](https://appbrewery.github.io/python-day5-demo/)