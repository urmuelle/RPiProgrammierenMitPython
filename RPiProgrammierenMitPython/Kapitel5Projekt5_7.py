# Kapitel 5, 5.7, Projekt "Farbmixer"

from tkinter import *

def update(event):
    color = "#%02x%02x%02x" \
        % (scale1.get(), scale2.get(), scale3.get())
    label.config(bg=color)

window = Tk()
scale1 = Scale(master=window, orient=VERTICAL,
               label="rot", to=255,
               command=update)
scale1.grid(column=0, row=0)
scale2 = Scale(master=window, orient=VERTICAL,
               label="gruen", to=255,
               command=update)
scale2.grid(column=1, row=0)
scale3 = Scale(master=window, orient=VERTICAL,
               label="blau", to=255,
               command=update)
scale3.grid(column=2, row=0)
label=Label(window, width=20, height=10, bg="black")
label.grid(column=3,row=0)

window.mainloop()