from tkinter import *
from random import randint

sayings = [("Du siehst heute gut aus", "You look great"),
           ("Kopf hoch!", "Cheer up"),
           ("Du schaffst das!","You will make it")]

def pick():
    nr = randint(0, len(sayings)-1)
    t = sayings[nr]
    label.config(text = t[language.get()])

window = Tk()

# Kontrollvariablen
language = IntVar(window)

# Widgets
button = Button(master=window,
                text="Neu",
                command= pick)
label = Label(master=window,
              width = 30, font=("Arial", 12))
german_rb = Radiobutton(master=window,
                value=0,
                text="Deutsch", 
                variable=language)
english_rb = Radiobutton(master=window,
                value=1,
                text="Englisch", 
                variable=language)

# Layout
label.pack(anchor=W)
german_rb.pack(anchor=W)
english_rb.pack(anchor=W)
german_rb.select();
button.pack(anchor=W)

window.mainloop()