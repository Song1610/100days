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
    
hurdles = 6
while hurdles > 0:
    move()
    jump()
    hurdles -= 1
    print(hurdles)