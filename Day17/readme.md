# Day 17 목차

---
# Class

```py
class User:
    pass    

user_1 = User()
```

pass : 함수 선언이나 class선언 시, 함수나 클래스 안의 코드 실행을 비워두고 다음 코드를 실행하고 싶을 때 사용

Class name : 첫 글자가 `대문자`여야함 <br>
→ Pascal Case

## 대소문자 종류
1. Pascal Case
   - 첫글자만 대문자
   - Class 사용
2. camel Case
   - 첫 단어는 소문자
   - python에선 잘 사용하지 않음
3. snake_case
   - 단어는 소문자지만 밑줄로 구분
   - class 이외의 모든 name에 사용

---

# Attribute
class가 선언되었으니 attribute를 만들자.

attribute 형태
```py
class Car:
    def __init__(self, seats):
        self.seats = seats
```

`__init__`
- 초기화되거나 생성되는 실제 객체
- 원하는만큼  매개변수를 추가할 수 있음(self, seats, cheel...)

**(self, ...)**
- 객체가 구성될 때 전달
- 데이터를 받으면 개체의 특성을 설정할 수 있음


init 예시
```py
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "alicia")
print(user_1.username, user_1.id, user_1.followers)
```

결과 <br>
<img width="136" height="65" alt="Image" src="https://github.com/user-attachments/assets/5a9a1d9a-1bee-498a-ad88-06335cf6df16" />

<br>

**self.followers = 0**
- __init__()에 follower를 적지 않더라도 기본값으로 제공할 수 있다.


---

# Methods
