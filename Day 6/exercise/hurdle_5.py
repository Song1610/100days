def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  turn_left()
  while wall_on_right():
    move()
  turn_right()
  move()
  turn_right()
  while front_is_clear():
    move()
  turn_left()


while not at_goal():
  if wall_in_front():
    jump()
  else:
    move()

# 오른쪽 가장자리를 따라가도록 하고 가능하면 우회전 하는걸
while not at_goal():
  if right_is_clear() and not wall_in_front():
    move()
  elif wall_in_front() and wall_on_right():
    turn_left()
  elif wall_in_front() and right_is_clear():
    turn_right()