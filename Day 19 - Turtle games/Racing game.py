from turtle import Turtle, Screen
from random import randint
colour = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
my_screen = Screen()
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race : ")
my_screen.setup(width=500, height=400)

for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle_list.append(turtle)
    turtle_list[i].penup()
    turtle_list[i].color(colour[i])
    turtle_list[i].goto(x=-230, y=-100 + i * 40)

is_on = False
if user_bet:
    is_on = True
while is_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_on = False
            if user_bet == winner:
                print(f"You've win! The winner is{winner}!")
            else:
                print(f"You've lost. The winner is{winner}.")
        speed = randint(0, 10)
        turtle.forward(speed)

my_screen.exitonclick()

