import turtle

FONT = ('Arial', 20, 'normal')


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.Level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f'Level: {self.Level}', font=FONT, align='left')

    def next_level(self):
        self.Level += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', font=FONT, align='center')
