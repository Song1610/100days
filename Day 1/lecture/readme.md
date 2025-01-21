# 강의 정리

### printing
##### 기본
```
# Write your code below this line 👇
print("Hello World!")
print("Hello World!)  # print 구문에 '', ""가 없으면 출력되지 않음
```

##### print("she said:"hello" and then left.")
""가 있으면 안됨
```
print('she said:"hello" and then left.')
print("she saide: \"hello\" and then left.")
```

##### enter 작성
```
print("hello! \nhello! \nhello!")
```

##### 문자열 결합
```
print("hello" + "mingyu")
print("hello " + "mingyu")
print("hello" + " mingyu")
print("hello" + " " + "mingyu")
```

##### 입력함수
```
input("what is your name?")
print("hello" + input("what is your name?"))
```


### variables
##### input
```
name = input("What is your name?")
print(name)

name = "Jack"
print(name)

name = "mingyu S2"
print(name)
```

##### 변수 설정
print(len(input("What is your name?")))
```
name = input("What is your name?")
length = len(name)
print(length)
```