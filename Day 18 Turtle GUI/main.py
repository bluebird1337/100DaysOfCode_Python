import turtle
from random import choice

turtle.colormode(255)

color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91),
              (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89),
              (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22),
              (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162),
              (105, 44, 39), (164, 209, 187), (151, 206, 220)]

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.speed(0)
t.hideturtle()

t.setpos(-200, -200)
for i in range(1, 11):
    for j in range(10):
        t.dot(20, choice(color_list))
        t.forward(50)
    t.setpos(-200, -200 + i*50)


my_screen = turtle.Screen()
my_screen.exitonclick()
