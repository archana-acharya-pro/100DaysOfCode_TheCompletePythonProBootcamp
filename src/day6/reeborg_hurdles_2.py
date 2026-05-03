def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump_hurdle()



# while at_goal() != True:
#     jump_hurdle()