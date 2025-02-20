while not at_goal():
    if wall_on_right() and wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
    elif front_is_clear():
        move()
    elif right_is_clear():
        turn_left()
    elif wall_in_front():
        right()