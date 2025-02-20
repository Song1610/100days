# maze

def turn_right():
   turn_left()
   turn_left()
   turn_left()

while not at_goal():
   if right_is_clear():
      turn_right()
      move()
   elif front_is_clear():
      move()
   else:
      turn_left()

# 이후의 디버그는 day 15 완료 후 해볼 것 