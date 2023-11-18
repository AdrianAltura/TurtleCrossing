import time
import turtle
import player
import cars
import scoreboard


win = turtle.Screen()
win.setup(width=600, height=600)
win.tracer(0)
win.title('Turtle Crossing')
win.listen()

scoreboard = scoreboard.Scoreboard()
main = player.Player()
cars = cars.Cars()
cars.starting_cars()

win.onkeypress(main.move_up, "Up")
win.onkeypress(main.move_down, "Down")

run = True

while run:
    time.sleep(0.1)
    win.update()

    # Moves cars
    cars.moving_cars()

    # Cars looping
    cars.loop_cars()

    # Main collision to cars
    for car in cars.CARS:
        if main.distance(car) < 20:
            run = False
            scoreboard.game_over()

    # Detect successful cross
    if main.at_finish():
        cars.level_up()
        scoreboard.score_update()
        main.restart_main()
        scoreboard.next_level()

win.exitonclick()
