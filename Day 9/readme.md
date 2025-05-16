# Day 9 목차
- Dictionaries
    - dictionaries 모양
    - 검색
    - new key 추가
    - 사전의 value 수정
    - 사전 반복(for in)
  - Garding Program

---
# Dictionaries
| Key | Value |
|---|:---:|
| Bug | An error in a program that prevents the program from running as expected. |
| Function | A piece of code that you can easily call over and over again. |
| Loop | The action of doing something over and over again. |

## dictionaries 모양
```
{key: Value}

{
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
```

## 검색
```
print(programming_dictionary["Bug"])
```
![Image](https://github.com/user-attachments/assets/5ca4b0a5-55ed-4d2a-b770-8f70cc3a777a)


* dictionaries에 없는 키를 print 시, <br>
![Image](https://github.com/user-attachments/assets/8db40fb8-a605-42e9-80f5-25e3e22405a2)

* list[0] & dictionary 차이점 : 사전은 key가 식별하는 요소가 있음


## new key 추가
```
programming_dictionary["Loop"] = " The action of doing something over and over again."
```
![Image](https://github.com/user-attachments/assets/60f48e16-b9bd-4352-b458-bb7219802cce)
<br>

`tip` : 코드를 시작할 때 아무것도 없는 빈 사전으로 시작하는 게 좋다.
```
emty_dictionary : {}
```

## 사전의 value 수정
```
programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary["Bug"])
print(programming_dictionary)
```
![Image](https://github.com/user-attachments/assets/5b815209-7f0d-4830-a506-8592e22b208b)


## 사전 반복(for in)

- print(key) 시 아래처럼 키값만 출력됨
```
for key in programming_dictionary:
    print(key)
```
![Image](https://github.com/user-attachments/assets/c953d3f9-40db-44da-84f5-df8b57600f0b)

<br>

- value를 출력하고 싶으면 아래처럼 작성해야 한다.

```
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
```
![Image](https://github.com/user-attachments/assets/133ff3c8-f334-4faf-abb7-9e2cbca9124f)

---
# Garding Program
