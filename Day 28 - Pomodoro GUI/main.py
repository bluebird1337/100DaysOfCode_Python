from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#2b2e4a"
HEADER_COLOR = "#2f5d62"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    header.config(text="Timer", bg=YELLOW)
    change_whole_color(YELLOW)
    canvas.itemconfig(canvas_text, text="00:00")
    checkmark.config(text="")


# ---------------------------- CHANGE COLOR ------------------------------- #


def change_whole_color(color):
    window.config(bg=color)
    canvas.config(bg=color)
    checkmark.config(bg=color)
    header.config(bg=color)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    if reps == 7:
        header.config(text="Break!")
        change_whole_color(RED)
        count_down(LONG_BREAK_MIN * 60)
        reps = 0
    elif reps % 2 == 0:
        header.config(text="Work")
        change_whole_color(BLUE)
        count_down(WORK_MIN * 60)
        reps += 1
    else:
        header.config(text="Break!")
        change_whole_color(PINK)
        count_down(SHORT_BREAK_MIN*60)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        session = math.floor(reps / 2)
        for _ in range(session):
            mark += "✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
header = Label(text="Timer", bg=YELLOW)
header.config(fg=HEADER_COLOR, font=(FONT_NAME, 35, "bold"))
header.grid(row=0, column=1)

# Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Checkmark
checkmark = Label()
checkmark.config(fg=GREEN)
checkmark.grid(row=2, column=1)

# Button
start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)


window.mainloop()
