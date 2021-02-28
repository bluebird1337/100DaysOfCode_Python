from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    scoreboard.display()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check collision with the food:
    if snake.snake[0].distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.update_score()

    # Detect collision with wall:
    if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 \
            or snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
        is_on = False
        scoreboard.game_over()

    # Detect collision with its body:
    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            is_on = False
            scoreboard.game_over()


screen.exitonclick()
