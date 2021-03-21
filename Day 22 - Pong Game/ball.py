from turtle import Turtle


class Ball(Turtle):
    horizon = 1
    vertical = 1
    DISTANCE = 10

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width = 20
        self.height = 20
        self.penup()

    def move(self):
        self.goto(self.xcor()+self.DISTANCE*self.horizon, self.ycor()+self.DISTANCE*self.vertical)

    def collide_wall(self):
        self.DISTANCE += 1
        self.vertical *= -1

    def collide_paddle(self):
        self.DISTANCE += 1
        self.horizon *= -1

    def l_reset(self):
        self.DISTANCE = 10
        self.setpos(0, 0)
        self.horizon = -1

    def r_reset(self):
        self.DISTANCE = 10
        self.setpos(0, 0)
        self.horizon = 1
