# Cipher 2
Caesar cipher를 이용해서 암복호화 프로그램 생성2

## TODO-1:
`original_text`와 `shift_amount`를 2개의 입력으로 받는 `decrypt()`라는 함수를 만듭니다.


## TODO-2:
`decrypt()` 함수 내부에서 `original_text`의 각 문자를 알파벳 순서에서 `shift_amount`만큼 앞으로 이동한 후 복호화된 텍스트를 출력합니다.

__힌트 1__ <br>
어떤 수에 -1을 곱하면 음수가 됨

## TODO-3:
`encrypt()` 와 `decrypt()` 함수를 `caesar()` 함수로 합칩니다.


사용자가 선택한 방향 변수의 값을 사용하여 사용할 기능을 결정합니다.

`encrypt/decrypt` 대신 `Caesar` 함수를 호출하고 `direction/text/shift` 세 변수를 모두 전달합니다.

<br>

**힌트 2** <br>
숫자에 -1을 곱하면 부호가 반전된다.
```
3 + ( 5 * -1) is the same as 3 - 5.
```

<br>

**힌트 3** <br>
```
Here is the encoded result: XXX
or
Here is the decoded result: XXX
```