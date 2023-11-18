import turtle
import random

COLORS = ['blue', 'green', 'yellow', 'red', 'orange', 'brown', 'pink', 'black']
START_SPEED = 5
SPEED_INCREMENTS = 2.5


class Cars:

    def __init__(self):
        self.CARS = []
        self.car_speed = START_SPEED

    def starting_cars(self):
        for i in range(30):
            new_car = turtle.Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_random = random.randint(-250, 250)
            x_random = random.randint(-250, 330)
            new_car.goto(x_random, y_random)
            self.CARS.append(new_car)

    def moving_cars(self):
        for car in self.CARS:
            car.backward(self.car_speed)

    def loop_cars(self):
        for car in self.CARS:
            if car.xcor() < -320:
                car.goto(300, random.randint(-250, 250))

    def level_up(self):
        self.car_speed += SPEED_INCREMENTS
