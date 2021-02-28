from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    snake = []

    def __init__(self):
        for i in range(3):
            turtle = Turtle(shape="square")
            turtle.penup()
            turtle.goto(-i * 20, 0)
            turtle.color("white")
            self.snake.append(turtle)

    def extend(self):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(self.snake[-1].position())
        self.snake.append(turtle)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            next_x = self.snake[segment - 1].xcor()
            next_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(next_x, next_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)
