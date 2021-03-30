from tkinter import *

window = Tk()
window.title("Pounds to Kilogram program")
window.minsize(width=500, height=300)


def convert():
    pounds = int(entry.get())
    kilo = pounds * 0.453592
    kilogram["text"] = round(kilo)


entry = Entry()
entry.grid(row=0, column=1)

pound = Label(text="Pounds")
pound.grid(row=0, column=2)

equal_str = Label(text="is equal to")
equal_str.grid(row=1, column=0)

kilogram = Label(text="0")
kilogram.grid(row=1, column=1)

kilogram_str = Label(text="Kilograms")
kilogram_str.grid(row=1, column=2)

convert_btn = Button(text="Calculate", command=convert)
convert_btn.grid(row=2, column=1)

window.mainloop()
