# Multi return
* 함수는 return 키워드에서 종료
* return문 아래에 코드를 작성하면 해당 코드는 실행되지 않음
* 하나의 함수에 여러 return이 있을 수 있음

### 조건부 반환(Conditional Returns)
- 제어 흐름이 있는 경우, 즉 특정 조건 검사에 따라 코드가 다르게 동작하는 경우(다른 실행 경로로 이동) 여러 종료(반환)가 발생할 수 있음

#### e.g
def canBuyAlcohol(age):

    if age >= 18:

        return True

    else:

        return False

- 이 뒤에 아무것도 없이 return을 작성할 수 있음
- 함수 종료

