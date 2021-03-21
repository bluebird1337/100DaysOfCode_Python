from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

time.sleep(0.1)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player1.go_up, "Up")
screen.onkeypress(player1.go_down, "Down")
screen.onkeypress(player2.go_up, "w")
screen.onkeypress(player2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collide_wall()

    # Detect collision with paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320:
        ball.collide_paddle()
    if ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.collide_paddle()

    # Detect the ball go out of screen
    # Left side win
    if ball.xcor() > 380:
        ball.l_reset()
        scoreboard.l_score()

    # Right side win
    if ball.xcor() < -380:
        ball.r_reset()
        scoreboard.r_score()


screen.exitonclick()
