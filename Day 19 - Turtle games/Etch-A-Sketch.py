from turtle import Turtle, Screen

turtle = Turtle()
my_screen = Screen()


def movebackward():
    turtle.bk(10)


def clockwise():
    turtle.right(10)


def counterclock():
    turtle.left(10)


def moveforward():
    turtle.forward(10)


def clear():
    turtle.home()
    turtle.clear()


my_screen.listen()
my_screen.onkey(key="a", fun=counterclock)
my_screen.onkey(key="d", fun=clockwise)
my_screen.onkey(key="w", fun=moveforward)
my_screen.onkey(key="s", fun=movebackward)
my_screen.onkey(key="space", fun=clear)

my_screen.exitonclick()

