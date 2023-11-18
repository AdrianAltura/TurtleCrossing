import turtle

STARTING_POSITION = (0, -280)
MOVEMENT = 15


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.y = MOVEMENT
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.restart_main()

    def move_up(self):
        self.forward(MOVEMENT)

    def move_down(self):
        self.backward(MOVEMENT)

    def restart_main(self):
        self.goto(STARTING_POSITION)

    def at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False
