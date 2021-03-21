from turtle import Turtle


class Scoreboard(Turtle):
    l_point = 0
    r_point = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.display()

    def display(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_point, align="center", font=("Arial", 25, "normal"))
        self.goto(100, 200)
        self.write(self.r_point, align="center", font=("Arial", 25, "normal"))

    def l_score(self):
        self.l_point += 1
        self.display()

    def r_score(self):
        self.r_point += 1
        self.display()
