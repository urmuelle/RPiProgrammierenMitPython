# Kapitel 6, 6.6.3 Karteikasten: Erweiterung des Presenters

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pickle, random

def loadCards():
    global card, cards
    f = filedialog.askopenfile("rb")
    if f:
        try:
            cards = pickle.load(f)
            card = random.choice(cards)
            text.delete(1.0, END)
            text.insert(END, card[0])
            button.config(command=turnCard)
        except:
            messagebox.showerror("", "Kartei unleserlich")
        f.close()

def nextCard():
    global card, cards
    if cards:
        text.delete(0.0, END)
        if learned.get() == 1:
            cards.remove(card)
        if cards:
            card = random.choice(cards)
            text.insert(END, card[0])
            button.config(command=turnCard)
        else:
            text.insert(END, card[0])
        cb.deselect()

def turnCard():
    if cards:
        text.insert(END, "\n" + card[1])
        button.config(command=nextCard)

# Widgets
window = Tk()
learned = IntVar(master=window)
button = Button(master=window, text="Weiter",
                font = ("Arial", 14), command=turnCard)
buttonLoad = Button(master=window, text="Laden",
                    font = ("Arial", 16), command=loadCards)
text = Text(master=window, width=30, height=6,
            font = ("Arial", 14), wrap=WORD)
cb = Checkbutton(master = window, onvalue=1, offvalue=0, 
                 font = ("Arial", 14), variable=learned, text="Gelernt!")
cb.deselect()

# Layout
text.pack(side=LEFT)
cb.pack(side=LEFT)
button.pack(side=LEFT)
buttonLoad.pack(side=LEFT, padx=2, pady=2)
text.insert(END, "Keine Kartei geladen")
window.mainloop()