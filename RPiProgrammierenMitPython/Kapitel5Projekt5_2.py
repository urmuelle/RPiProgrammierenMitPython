from tkinter import *
from random import randint

def choose():
    zufallszahl = randint(1, 6)
    label.config(text=zufallszahl)

window = Tk()
button = Button(master=window,
                text="Zufallszahl",
                command= choose,
                font=("Arial", 10), fg="blue")

label = Label(master=window,
              font=("Arial", 50),
              text="?",
              width = 3)

label.pack()
button.pack()

window.mainloop()