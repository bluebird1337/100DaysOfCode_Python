from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        ycor = random.randint(-250, 250)
        self.setpos(290, ycor)
        self.setheading(180)
        self.add_speed = level

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(self.add_speed - 1))


