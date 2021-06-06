from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- Reading data ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    # Switch to the front window
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_item, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # Flip the card after 3 sec
    window.after_cancel(flip_timer)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- Create a file to save the Progress ------------------------------- #


def is_known():
    to_learn.remove(current_card)
    next_card()
    words = pandas.DataFrame(to_learn)
    words.to_csv("data/words_to_learn.csv", index=False)

# ---------------------------- UI ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_item = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_btn = Button(image=check_image, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)

# ---------------------------- Flip the card / Timer ------------------------------- #


def flip_card():
    # Switch to the back window
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_item, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


flip_timer = window.after(3000, func=flip_card)

# ---------------------------- Main ------------------------------- #


next_card()
window.mainloop()
