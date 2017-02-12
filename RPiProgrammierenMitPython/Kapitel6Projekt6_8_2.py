# Kapitel 6, 6.8.2 Goethe oder Schiller

from tkinter import *
import random, time

def createBook(filename):
    f = open(filename, "r", encoding="utf-8")
    text = f.read()
    f.close()
    text = text.replace("\n", " ")
    raw = text.split(". ")
    sentences = [s.strip() for s in raw
                 if (len(s) > 100) and ("(" not in s)\
                 and ("_" not in s)]
    return sentences

def newQuote():
    global author
    if answer.get():
        author = random.choice(["Goethe", "Schiller"])
        if author == "Goethe":
            quote = random.choice(bookGoethe) + "."
        else:
            quote = random.choice(bookSchiller) + "."
        text.delete(1.0, END)
        text.insert(1.0, quote)
        label.config(text="Von wem stammt dieser Text?")
        for rb in radiobuttons: rb.deselect()
        answer.set("")

def check():
    if author == answer.get():
        response = "Richtig! "
    else:
        response = "Falsch! "
    label.config(text=response + "Das stammt von " + author)

# Widgets
window = Tk()
answer = StringVar(master=window, value="x")
label = Label(master=window, font=("Arial", 16))
radiobuttons=[Radiobutton(master=window, text=a, value=a,
                          font = ("Arial", 16),
                          variable=answer,
                          command=check,
                          indicatoron=False) for a in ("Goethe", "Schiller")]
button = Button(master=window, text="Naechstes Zitat",
                font = ("Arial", 16), command=newQuote)
text = Text(master=window, width=50, height=8,
            font = ("Arial", 14), wrap=WORD)

# Layout
label.pack()
text.pack()
for rb in radiobuttons: rb.pack(side=LEFT)
button.pack(side=LEFT)
bookGoethe = createBook("faust.txt")
bookSchiller = createBook("raeuber.txt")
window.mainloop()