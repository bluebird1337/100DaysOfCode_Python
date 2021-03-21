from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    level = 1

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.display()

    def display(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
