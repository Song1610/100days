# Day 10 목차
- [Function with Outputs]()
- [Multiple Return Values]()
- [Docstrings]()
---

# Function with Outputs

## Function 정리
### 1. function()
```
def my_function():
    # Do this
    # Then do this
    # Finally do this

my_function()
```


### 2. function(something)
```
def my_function(something):
    # Do this something
    # Then do this something
    # Finally do this something

my_function(123)
```
something = 123

### 3. Functions with outputs
함수가 완성되면 출력을 얻게 해주는 함수
```
def my_function():
    result = 3*2
    return result

my_function()
```
my_function() result = 6 이지만 출력되지 않음 <br>
![Image](https://github.com/user-attachments/assets/02cc042a-9ab2-4112-96be-2bb352184bca)

print(my_function()) 로 해야 값(6) 출력<br>
![Image](https://github.com/user-attachments/assets/eeab8797-22c8-4520-88e4-aaf81cf54929)

**return** : 출력을 가진 함수
- 코드의 다른 지점에서 그 함수를 호출하기로 결정하면
- 일단 함수가 실행되면 반환이나 출력된 것이 함수 호출을 대체
- 마지막에 이 변수 출력물이 output을 저장


#### return example

- todo.1 `f_name`,`l_name`의 입력을 받는 `format_name()` 함수 생성
- todo.2 `title()` 함수를 사용하여 f_name과 l_name 매개변수를 대소문자(Template Case)로 수정


1. print 사용
```
# Todo.1
def format_name(f_name, l_name):
    # Todo.2
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"{formated_f_name}, {formated_l_name}")

format_name("mingyu", "KIM")
```
결과 <br>
![Image](https://github.com/user-attachments/assets/40551978-234a-4d11-8c73-52e786283651)


2. return 사용
```
def format_name(f_name, l_name):
    # Todo.2
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name}, {formated_l_name}"

print(format_name("mingyu", "KIM"))
```
결과 <br>
![Image](https://github.com/user-attachments/assets/40551978-234a-4d11-8c73-52e786283651)


print()와 return을 사용했을 때의 결과는 같지만 코드의 내용이 다르다.
<br>
<br>
<br>


#### Print vs Output
|return|print|
|----|----|
|함수에서 나중에 사용할 수 있는 값을 반환하는데 사용|프로그래머가 볼 수 있도록 콘솔에 값을 표시함|

#### 반환함수(return)의 동작 예시
```
def function_1(text):
    return text + text

def function_2(text):
    return text.title()


output = function_2(function_1("hello "))
print(output)
```

---

# Multiple Return Values
return : 함수실행의 끝  ending
```py
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return f"name value is null"        # early return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(f_name = input("Your first name : "), l_name = input("Your last name : ")))

```

---
# Docstrings
- 기본적으로 문서 조각을 만드는 방법
- 함수나 다른 코드 블록을 코딩할 때 사용

```py
def format_name(f_name, l_name):
    """
    Docstring test
    format_name is first name, last name.
    f_name : first name
    l_name : last name
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)
```
위 코드에서 """ """ 부분이 Docstring(▲) <br>
아래 Docstring가 보임(▼) <br>

![Image](https://github.com/user-attachments/assets/b489b70b-73d2-444f-bdd6-edfffe16a177)