def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()


# no.1
while not at_goal():
  if wall_in_front():
      turn_left()
      if wall_on_right():
          move()
      else:
          turn_right()
  elif front_is_clear() and right_is_clear():
      jump()
  elif front_is_clear():
      move()

# no.2
def turn_right():
  turn_left()
  turn_left()
  turn_left()
def jump():
  if front_is_clear() and right_is_clear():
      move()
      turn_right()
  elif wall_in_front()
      turn_left()
  else:
      move()

while not at_goal():
 if wall_in_front():
     turn_left()
     if wall_on_right():
         jump()
     else:
         turn_right()
 elif     move()
   turn_right()
   move()
 elif front_is_clear():
     move()
