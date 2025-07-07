# Day 12 목차
- Namespaces & Scope
- Black Scope

---

# Namespaces & Scope
## Local scope
function 안에 존재함

__예시 1__
```py
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
```

결과값

<img width="250" height="62" alt="Image" src="https://github.com/user-attachments/assets/a186a0e8-6cc9-4fa1-9650-eb4aad0c8819" />


__예시 2__
```py
def drink_potion():
    potion_strength = 2
    print(f"potion strength in drink potion : {potion_strength}")

drink_potion()
print(potion_strength) 

```

결과값

<img width="987" height="156" alt="Image" src="https://github.com/user-attachments/assets/e3c7245e-3d88-4fd6-99ba-5188aca94935" />

- potion_strength가 drink_potion() 함수 바깥쪽에 있어서 "NameError: name 'potion_strength' is not defined" 발생
- 새 변수나 다른 함수 안에 새 함수를 만들 때에만 접근할 수 있음
- def 함수 안에 변수가 정의되어 있으면 def 함수 안에서만 local 변수 사용 가능하고 def 밖에선 사용 X
  

## Global scope
**local vs global 차이점**
- 변수나 함수를 어디서 정의하고 어디서 만드느냐의 차이
  
| Local scope | Grobal scope |
|:-|:-|
| 함수 내부에 선언된 변수 | 코드파일의 최상위(들여쓰기X)에 선언된 변수 또는 함수 |
| 같은 코드 블록 내의 다른 코드에서만 볼 수 있음 | 코드 파일의 어디에서나 접근할 수 있음 |


<br>
<br>

**global scope**
```py
player_health = 10          # global 변수

 def drink_potion():
     potion_strength = 2     # local 변수
     print(potion_strength)
     print(player_health)

 drink_potion()
 print(player_health)
 ```

 결과값

 <img width="417" height="86" alt="Image" src="https://github.com/user-attachments/assets/9b95c48a-5cf5-427c-bfe7-032cdabd0a90" />


 - global 변수는 def 함수 밖에 있어도 def 함수 안에서 사용 가능

## Namespace
- 이름을 주는 모든 것에 네임스페이스를 가지고 있음
- 특정 범위에서 유효함
- 코드를 작성하는 곳에서 특정 변수(scope)의 범위를 정의함

```py
def game():
    def drink_potion():
        potion_strength = 2
        print(f"potion strength in drink potion : {potion_strength}")
        print(f"player health : {player_health}")

    drink_potion()

game()
```

결과값

<img width="431" height="73" alt="Image" src="https://github.com/user-attachments/assets/a57f61f4-0091-4319-9c06-8569a52930e2" />