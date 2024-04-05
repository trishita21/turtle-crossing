import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move,"Up")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count += 1

    # Detect finish line
    if turtle.has_reached_finish_line():
        score.level_up()
        car_manager.level_up()

    if count == 6:
        car_manager.get_new_car()
        count = 0

    car_manager.move_cars()

    # Detect collision
    for car in car_manager.cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()