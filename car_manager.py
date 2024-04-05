from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def get_new_car(self):
        color = random.choice(COLORS)
        seg = Turtle("square")
        seg.color(color)
        seg.penup()
        seg.shapesize(stretch_wid=1, stretch_len=2)
        new_ycor = random.randint(-250,250)
        seg.goto(300,new_ycor)
        seg.setheading(180)
        self.cars.append(seg)

    def move_cars(self):
        for seg in self.cars:
            new_xcor = seg.xcor() - self.move_distance
            if new_xcor < -280:
                new_xcor = 280
            seg.goto(new_xcor, seg.ycor())

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

