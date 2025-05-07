# Cipher 1.

Caesar cipher를 이용해서 암복호화 프로그램 생성

[Demo](https://appbrewery.github.io/python-day8-demo/)

## TODO-1:
Create a function called `encrypt()` that takes `original_text` and `shift_amount` as 2 inputs.

## TODO-2:
`encrypt()` 함수 안에서 `original_text`의 각 문자를 `shift_amount`만큼 알파벳 순으로 이동하고 암호화된 텍스트를 출력합니다.

`index()`를 사용하면 목록에서 항목의 위치를 ​​찾을 수 있습니다.

예:
```
fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
```

예를들어 다음과 같은 값이 있는 경우
```
plain_text = "hello"
shift_amount = 1
```

encrypted output(▼)

```
Here is the encoded result: ifmmp
```

'hello'의 각 글자가 1씩 위로 이동합니다.


힌트 1
- for loop 필요
- 알파벳 목록에서 각 문자의 위치 찾기
- 알파벳 위치 + shift_amount = ?
- index() 필요
- letter 결과 출력




## TODO-3:
encrypt() 함수를 호출하고 사용자 입력을 전달하세요.<br>
코드를 테스트하고 메시지를 암호화할 수 있어야 합니다.

## TODO-4:
'z'를 9만큼 앞으로 옮기면 어떻게 되나요? 코드를 수정할 수 있나요?


힌트 2 
1. 알파벳 글자 목록에 2개 이상의 알파벳 세트를 추가할 수 있습니다.
2. shift_amount를 이동하여 항상 0~25 범위 내에 있고 목록에 맞도록 할 수 있습니다.
3. 나머지를 구하기 위해 모듈로를 사용할 수 있습니다.