# Love Calculator
💪 이건 어려운 도전이에요!💪

두 이름 사이의 호환성을 테스트하는 `calculate_love_score()`라는 함수를 작성하려고 합니다.
두 사람 사이의 사랑 점수를 계산하려면:

1. 두 사람의 이름을 모두 가져와 TRUE라는 단어의 글자가 나오는 횟수를 확인합니다.
2. 그런 다음 LOVE라는 단어의 글자가 나오는 횟수를 확인합니다.
3. 그런 다음 이 숫자를 합쳐서 2자리 숫자를 만들고 출력합니다.


예: `name1 = "Angela Yu" name2 = "Jack Bauer"`


T가 0번 발생 <br>
R이 1번 발생 <br>
U가 2번 발생 <br>
E가 2번 발생 <br>

__합계 = 5__


L이 1번 발생 <br>
O가 0번 발생 <br>
V가 0번 발생 <br>
E가 2번 발생 <br>

__합계 = 3__

__Love Score = 53__


#### 입력 예시
```py
calculate_love_score("Kanye West", "Kim Kardashian")
```

#### 출력 예시
```
42
```


__코드를 테스트하고 출력을 확인하는 방법은?__

Udemy 코딩 연습에는 콘솔이 없으므로 `input()` 함수를 사용할 수 없습니다. <br>
다음과 같이 하드코딩된 값으로 함수를 호출해야 합니다.

```py
def calculate_love_score(name1, name2):
    # 여기에 코드를 입력하세요

# 하드코딩된 값으로 함수를 호출하세요
calculate_love_score("Kanye West", "Kim Kardashian")
```



# Hint
1. count(): [참고링크](https://www.w3schools.com/python/ref_list_count.asp)
2. lower() : [참고링크](https://www.w3schools.com/python/ref_string_lower.asp)
