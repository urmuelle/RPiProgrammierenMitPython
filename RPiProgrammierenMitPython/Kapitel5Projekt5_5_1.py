from tkinter import *

def create():
    text = "Hallo!\n"
    text += "Viele Gruesse aus dem Urlaub. "
    text += o1.get() + o2.get()
    greeting.delete(1.0, END)
    greeting.insert(END, text)

window = Tk()

# Kontrollvariablen
o1 = StringVar(window)
o2 = StringVar(window)

# Widgets
button = Button(master=window,
                text="Erzeuge Text",
                command= create)
greeting = Text(master=window,
                width = 40, height = 6, wrap=WORD)
cb1 = Checkbutton(master=window,
                onvalue="Es gibt hier viel zu sehen. ",
                offvalue="",
                text="Viel zu sehen", variable=o1)
cb2 = Checkbutton(master=window,
                onvalue="Das Wetter ist fantastisch. Sonne pur.",
                offvalue="",
                text="Gutes Wetter", variable=o2)
# Layout
greeting.pack()
cb1.pack(anchor=W)
cb2.pack(anchor=W)
button.pack(anchor=E)

window.mainloop()