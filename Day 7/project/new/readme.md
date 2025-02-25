# Hangman Step 목차
1. [step 1](#step-1)
2. [step 2](#step-2)

---

# Hangman Step
## Step 1
목표는 Python 프로그래밍에 대해 배운 모든 것을 사용하여 행맨 게임을 만드는 것입니다.

**데모 최종 프로젝트** <br>
https://appbrewery.github.io/python-day7-demo/ <br>

프로젝트는 5가지 주요 단계로 나뉩니다. 각 단계에는 여러 개의 TODO가 있습니다. 목표는 각 todo를 순서대로 살펴보고 완료하는 것입니다. <br>

PyCharm에서 View -> Tool Windows -> TODOs로 이동하여 모든 todo를 쉽게 볼 수 있습니다. <br>

**TODO-1** <br>
word_list에서 단어를 무작위로 선택하여 `chosen_word`라는 변수에 할당합니다. 그런 다음 인쇄합니다.

**TODO-2** <br>
사용자에게 문자를 추측하도록 요청하고 해당 답변을 `guess`라는 변수에 할당합니다. `guess`에 저장된 문자열을 소문자로 만듭니다.

_힌트 1_ <br>
_Google에서 Python의 `lower()` 함수를 검색합니다._

**TODO-3** <br>
사용자가 추측한 문자가 `chosen_word`의 문자 중 하나인지 확인합니다. `chosen_word`의 각 글자를 반복하고 글자가 일치하면 "Right"를, 일치하지 않으면 "Wrong"을 출력합니다.

_힌트 2_ <br>
_문자열을 반복하는 방법은 리스트를 반복하는 것과 같습니다. `for in` 루프를 사용하면 됩니다. 구글링해 보세요: "Loop through strings python"_

---

## Step 2
**TODO-1** <br>
- `placeholder`라는 빈 문자열을 만듭니다.
- chosen_word의 각 문자에 대해 placeholder에 `_`를 추가합니다.
- 따라서 chosen_word가 "apple"인 경우 placeholder는 추측할 각 문자를 나타내는 5개의 "_"가 있는 `_ _ _ _ _`이어야 합니다.
- hint를 출력합니다.

_힌트 1_ <br>
_반복문 내에서 `range()` 함수를 사용하여 특정 횟수만큼 작업을 수행할 수 있습니다._


**TODO-2** <br>
- "display"라는 빈 문자열을 만듭니다.
- chosen_word의 각 문자를 반복합니다.
- 해당 위치의 문자가 guess와 일치하면 해당 위치의 display에 해당 문자를 표시합니다.
- 예를 들어 사용자가 "p"를 추측했고 선택한 단어가 "apple"인 경우 display는 `_ p p _ _`이어야 합니다.
- display를 출력하면 추측한 문자가 올바른 위치에 표시됩니다.
- 하지만 일치하지 않는 모든 문자는 "_"로 표시됩니다.

_힌트 2_ <br>
_for 루프는 선택한 단어의 각 문자를 순서대로 살펴봅니다. 이 사실을 사용하여 문자나 "_"를 추가하여 새 문자열을 만들 수 있습니다._