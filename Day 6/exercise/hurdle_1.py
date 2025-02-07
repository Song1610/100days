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

for step in range(6):
move()
jump()

number_hurdles = 6
while number_hurdles > 0:
    move()
    jump()
    number_hurdles -= 1
    print(number_hurdles)
