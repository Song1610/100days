# Cipher 3

## TODO-1:
프로그램이 시작되면 art.py에서 로고를 가져와서 출력

## TODO-2:
사용자가 알파벳 리스트에 없는 숫자/기호/공백을 입력하면 어떻게 되나요? <br>
텍스트가 인코딩/디코딩될 때 숫자/기호/공백이 유지되도록 코드를 수정할 수 있나요?


예시
```
original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"
```
<br>

**힌트 1** <br>
If it's not a letter in the List alphabet, maybe you can just add it to the end of cipher_text as the unmodified character?


## TODO-3:
Can you figure out a way to restart the cipher program?


예시
```
Type 'yes' if you want to go again. Otherwise, type 'no'.
```

'yes'를 입력하면 direction/text/shift를 다시 묻고 caesar() 함수를 다시 호출합니다.


**힌트 2** <br>
사용자가 'yes'를 입력하면 프로그램을 계속 실행하는 while 루프를 만들어 보세요.