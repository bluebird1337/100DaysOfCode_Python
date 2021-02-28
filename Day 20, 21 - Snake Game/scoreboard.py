from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Verdana', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color('white')
        self.ht()
        self.point = 0

    def display(self):
        self.write(f"Score : {self.point}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.point += 1
        self.clear()
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
