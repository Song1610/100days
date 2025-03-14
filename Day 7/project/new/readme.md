# Hangman Step 목차
1. [step 1](#step-1)
2. [step 2](#step-2)
3. [step 3](#step-3)
4. [step 4](#step-4)
5. [step 5](#step-5)

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


<div align="right">

[목차로](#hangman-step-목차)
</div>

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


<div align="right">

[목차로](#hangman-step-목차)
</div>


---
# Step 3
**TODO-1** <br>
- while 루프를 사용하여 사용자가 다시 추측하게 합니다.
- 루프는 사용자가 선택한 단어의 모든 글자를 추측한 후에만 중지되어야 합니다.
- 그 시점에서 디스플레이에 더 이상 공백("_")이 없습니다. 그러면 사용자에게 승리했다고 알릴 수 있습니다.

_힌트 1_ <br>
`in` 키워드를 사용하여 문자열이나 목록에 특정 항목이 포함되어 있는지 확인할 수 있습니다. <br>
예: Google: 문자열에 글자가 있는지 검색합니다. <br>

**TODO-2** <br> * 살짝 어려웠음
- 이전 추측이 디스플레이 문자열에 추가되도록 for 루프를 업데이트합니다.
- 현재 사용자가 새로운 추측을 하면 이전 추측이 "_"로 바뀝니다. `for loops`를 업데이트하여 이를 수정해야 합니다.

_힌트 2_ <br>
일치하는 글자를 저장하고 elif를 사용하여 글자가 이전에 일치했는지 확인하는 방법에 대해 생각해 보세요.


<div align="right">

[목차로](#hangman-step-목차)
</div>


---

# Step 4
**TODO-1:** <br>
- `lives`라는 변수를 만들어 남은 생명 수를 추적합니다.
- lives를 6으로 설정합니다.

**TODO-2:** <br>
- choose_word에 guess가 없는 경우 lives를 1만큼 줄입니다.
- lives가 0으로 줄어들면 게임이 종료되고 `"You lose"`가 출력됩니다.

_힌트_ <br>
이 todo에서 `not in` 키워드가 친구가 됩니다. 나머지 코드와 완전히 별도로 chosen_word에 무언가가 있는지 확인할 수 있습니다.

**TODO-3:** <br>
사용자의 남은 생명 수에 해당하는 stages 목록에서 ASCII 아트를 출력합니다.


<div align="right">

[목차로](#hangman-step-목차)
</div>


---

# Step 5
[step 5 link](https://github.com/Song1610/100days/blob/main/Day%207/exercise/new/main.py)

**TODO-1:** <br>
단어 목록을 업데이트하여 hangman_words.py의 word_list를 사용합니다.


**TODO-2:**<br>
hangman_art.py 파일의 스테이지를 사용하도록 코드를 업데이트합니다.


**TODO-3:**<br>
hangman_art.py에서 로고를 가져와서 게임 시작 시 인쇄합니다.


**TODO-4:**<br>
사용자가 이미 추측한 글자를 입력한 경우 해당 글자를 인쇄하여 알려줍니다.<br>
여기서는 생명을 차감해서는 안 됩니다.<br>
예를 들어 이미 a를 추측했습니다.


**TODO-5:**<br>
선택한 단어에 해당 글자가 없는 경우 해당 글자를 인쇄하여 해당 단어에 없다고 알려줍니다.<br>
예를 들어 d를 추측했지만 해당 단어에는 없습니다. 생명을 하나 잃습니다.


**TODO-6:**<br>
아래 코드를 업데이트하여 사용자에게 남은 생명 수를 알려줍니다.<br>
```
print("****************************<???>/6 LIVES LEFT********************************")
```


**TODO 7:**<br>
사용자가 추측하려고 했던 올바른 단어를 제공하기 위해 print 문을 업데이트합니다.<br>
예: `IT WAS <Correct Word>! YOU LOSE.`


<div align="right">

[목차로](#hangman-step-목차)
</div>