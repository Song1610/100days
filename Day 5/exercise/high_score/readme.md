# Instructions
You are going to write a program that calculates the highest score from a List of scores.

#### e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
### Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

### Example Output
The highest score in the class is: 91


---
25-02-18(new)

Python에는 숫자를 다루는 데 도움이 되는 내장 함수가 많이 있습니다. 그 중 하나는 합계(총계)를 계산하는 데 도움이 됩니다. 예를 들어
```
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)
```

하지만 sum()은 내부적으로 어떻게 작동할까요? 이 코드는 Python을 개발한 사람들이 작성했으며 다음과 같습니다.

```
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
sum += score

print(sum)
```

PAUSE 1 - Max

max() 및 min()이라는 내장 Python 메서드도 있는데, 이를 사용하면 숫자 목록을 전달하면 가장 높은 숫자나 가장 낮은 숫자를 알려줍니다.

여러분의 작업은 Python 프로그래머가 루프와 조건문을 사용하여 이 기능을 어떻게 구축했을지 알아내는 것입니다.

max()를 사용하지 않고 이 챌린지를 완료하세요.

시험 점수 목록이 주어지고 목록에서 가장 높은 점수를 출력해야 합니다. 

학생 점수 목록에서 가장 높은 점수를 출력하려면 목록, For 루프 및 조건문에 대해 배운 내용을 사용해야 합니다.

예를 들어, 점수가 다음과 같다면:

```
8 65 89 86 55 91 64 89
```

코드는 다음을 출력해야 합니다.
```
91
```
