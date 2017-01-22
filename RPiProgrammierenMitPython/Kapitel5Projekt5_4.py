from tkinter import *

def createStory():
    text = "Es geschah an einem Motagmorgen im "
    text += monthEntry.get() + ". "
    text += nameEntry.get()
    text += " war auf dem Weg zum Bahnhof. Da fuhr ein "
    text += colorEntry.get()
    text += "er Sportwagen an ihm vorbei..."
    story.delete(1.0, END)
    story.insert(END, text)

# Widgets
window = Tk()
button = Button(master=window,
                text="Neue Geschichte",
                command= createStory)
story = Text(master=window,
             width = 30, height = 5, wrap=WORD)
nameLabel = Label(master=window,
                  text="Maennlicher Vorname: ")
monthLabel = Label(master=window, text="Monat: ")
colorLabel = Label(master=window, text="Farbe: ")
nameEntry = Entry(master=window)
monthEntry = Entry(master=window)
colorEntry = Entry(master=window)


# Layout
story.pack()
nameLabel.pack()
monthLabel.pack()
colorLabel.pack()
nameEntry.pack()
monthEntry.pack()
colorEntry.pack()
button.pack()

window.mainloop()