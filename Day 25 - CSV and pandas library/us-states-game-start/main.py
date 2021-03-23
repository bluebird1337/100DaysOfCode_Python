import turtle
import pandas as pd
FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("US states guess game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("50_states.csv")
name = data["state"].tolist()

t = turtle.Turtle()
t.hideturtle()
t.penup()

correct = 0
while correct < 50:
    answer = turtle.textinput(title=f"{correct}/50 States Correct", prompt="Make your answer:")
    answer = answer.title()
    if answer in name:
        name.remove(answer)
        correct += 1
        x_cor = int(data[data.state == answer].x)
        y_cor = int(data[data.state == answer].y)
        t.goto(x_cor, y_cor)
        t.write(answer, False, align="center", font=FONT)

turtle.mainloop()
