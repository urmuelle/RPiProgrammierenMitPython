# Kapitel 6, 6.5.2 Karteikasten: Der Presenter

from tkinter import *
import pickle, random
PATH = "cards.dat"

def loadCards():
    global card, cards
    try:
        f = open(PATH, "rb")
        cards = pickle.load(f)
        f.close()
        card = random.choice(cards)
        text.insert(END, card[0])
    except:
        text.insert(END, "Sorry, keine Karteikarte vorhanden...")
        cb.destroy()
        button.destroy()

def nextCard():
    global card, cards
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
    text.insert(END, "\n" + card[1])
    button.config(command=nextCard)

# Widgets
window = Tk()
learned = IntVar(master=window)
button = Button(master=window, text="Weiter",
                font = ("Arial", 14), command=turnCard)
text = Text(master=window, width=30, height=6,
            font = ("Arial", 14), wrap=WORD)
cb = Checkbutton(master = window, onvalue=1, offvalue=0, 
                 font = ("Arial", 14), variable=learned, text="Gelernt!")
cb.deselect()

# Layout
text.pack(side=LEFT)
cb.pack(side=LEFT)
button.pack(side=LEFT)

loadCards()
window.mainloop()