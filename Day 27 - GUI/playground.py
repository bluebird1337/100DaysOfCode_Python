from tkinter import *


def add(*args):
    summation = 0
    for i in args:
        summation += i
    print(summation)


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.mode = kw.get("mode")


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="A new label", font=("Arial", 24, "normal"))
# Make the component appear on the screen
my_label.grid(column=0, row=0)

# Entry
entry = Entry(width=10)
entry.grid(column=3, row=2)


def button_click():
    res = entry.get()
    my_label["text"] = res


# Button
button = Button(command=button_click)
button["text"] = "click me!"
button.grid(column=1, row=1)
btn2 = Button()
btn2["text"] = "new btn"
btn2.grid(column=2, row=0)

window.mainloop()
