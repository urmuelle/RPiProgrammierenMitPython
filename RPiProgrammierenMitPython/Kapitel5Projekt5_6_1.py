from tkinter import *
from random import shuffle, randint, choice

# globale Variablen
correct = 0

# Funktionen
def new_game():
    points.set(0)
    new_task()

def check():
    if selected.get() == correct:
        points.set(points.get() + 1)
    for ob in option_buttons:
        ob.deselect()
        if ob.cget("value") == correct:
            ob.config(bg="green")

def new_task():
    global correct
    a = randint(2, 20)
    b = randint(2, 10)
    task = "Wie viel ist " + str(a) + " * " + str(b) + "?"
    task_label.config(text=task)
    correct = a*b
    numbers = [a*b, a*b-1, a*b+1, a*b+choice([-2, 2])]
    shuffle(numbers)
    for i in range(4):
        option_buttons[i].config(value=numbers[i],
                             text=numbers[i], bg="white")

# Widgets
window = Tk()
points = IntVar(master=window)
selected = IntVar(master=window)
option_buttons = [
         Radiobutton(master=window,
                     command=check,
                     font=("Arial",20), width=4,
                     variable=selected, value=0,
                     indicatoron=False)
         for i in range(4)]
new_game_button = Button(master=window, text = "Neu",
                         font=("Arial", 12),
                         command = new_game)
new_task_button = Button(master=window, text = "Weiter",
                         font=("Arial", 12),
                         command = new_task)
task_label = Label(master=window, font=("Arial", 12))
points_label = Label(master=window, textvariable=points,
                     font=("Arial", 12), bg="black", fg="white")

# Layout
task_label.grid(column=0, row=0, columnspan=2)
for i, col, row in [(0,0,1),(1,1,1),(2,0,2),(3,1,2)]:
    option_buttons[i].grid(column=col, row=row)
new_task_button.grid(column=0, row=3, sticky=E+W)
points_label.grid(column=1, row=3, sticky = E+W+N+S)
new_game_button.grid(column=2, row=3)
new_task()

window.mainloop()