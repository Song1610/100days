25-02-20 작성
# 로봇(reeborg's world) exercise 목차
1. 
---

# 로봇(reeborg's world) exercise
[exercise file(old)](https://github.com/Song1610/100days/tree/main/Day%206/exercise/old) <br>
[exercise file(new)](https://github.com/Song1610/100days/tree/main/Day%206/exercise/new)
* exercise file(new) : 25-02-18 ~ 25-02-00 작성

## 1. alone
[alone. exercise link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json)

1. 오른쪽 방향 함수 생성 <br>
[turn_right solution](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/alone(turn_right).py)

2. Draw Square <br>
    ![Image](https://github.com/user-attachments/assets/b1883bd7-32e3-4de7-99d9-b564950e22ee) <br>
    [draw square solution](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/alone(DrawSquare).py)


## 2. 허들 1
[허들 1. exercise link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

**문제 : 점프!** <br>
아래 그림처럼 목표에 도달 할 수 있는 코드 작성(▼)

![Image](https://github.com/user-attachments/assets/2a7c6b6d-8f6a-4dd8-a3ce-5cf08761e5c1) <br>
[exercise solution(old)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/old/hurdle_1.py) <br>
[exercise solution(for)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/hurdle_1(for).py) <br>
[exercise solution(while)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/hurdle_1(while).py)

## 3. 허들 2
[허들 2. exercise link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json)

**문제 : 깃발 꽂힌 곳이 랜덤** <br>
아래 그림처럼 목표에 도달 할 수 있는 코드 작성(▼)

![Image](https://github.com/user-attachments/assets/69fde674-a4f0-4f60-915f-0c76fa13c5bc) <br> 
[exercise solution(old)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/old/hurdle_2.py) <br>
[exercise solution(new)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/hurdle_2.py)

## 4. 허들 3
[허들 3. exercise link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json)

**문제 : 벽의 위치가 무작위로 변경** <br>
아래의 함수를 이용할 것 <br>
- move()
- turn_left()
- front_is_clear()
- wall_in_front()
- at_goal()

아래 그림처럼 목표에 도달 할 수 있는 코드 작성(▼) <br>
![Image](https://github.com/user-attachments/assets/f52560bd-5ccc-4ab5-bdea-d22d9f7a35b4) <br>
[exercise solution(old)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/old/hurdle_3.py) <br>
[exercise solution(new)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/hurdle_3.py)

## 5. 허들 4
[허들 4. exercise link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)

**문제 : 다양한 높이의 벽과 허들을 넘어서 목적지에 도달하세요.** <br>
아래의 함수를 이용할 것 <br>
- move()
- turn_left()
- front_is_clear()
- right_is_clear()
- wall_in_front()
- wall_on_right()
- at_goal()

`tip: jump()를 수정하세요.`

아래 그림처럼 목표에 도달 할 수 있는 코드 작성(▼)

![Image](https://github.com/user-attachments/assets/5d2d4723-4d63-4fc8-b235-f559550e308b) <br>
[exercise solution(old)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/old/hurdle_4.py) <br>
[exercise solution(new)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/hurdle_4.py) <br>
[exercise solution(solution)](https://github.com/Song1610/100days/blob/main/Day%206/exercise/new/hurdle_4(solution).py)



## 6. maze
리보그가 출구를 찾을 수 있도록 while/if/elif/else을 사용하여 프로그램을 작성하세요.<br>
비결은 리보그가 미로의 오른쪽 가장자리를 따라가고, 오른쪽으로 돌 수 있으면 오른쪽으로 돌고, 오른쪽으로 돌 수 없으면 직진하고, 마지막 수단으로 왼쪽으로 돌게 하는 것입니다.