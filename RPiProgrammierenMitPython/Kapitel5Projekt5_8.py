# Kapitel 5, 5.8, Projekt "Editor mit Pulldown-Menüs"

from tkinter import *

def format_text():
    font = selected_font.get()
    text.config(font=(font,10))

def insert_phrase():
    text.insert(INSERT, selected_phrase.get())

def delete_text():
    text.delete(1.0, END)

window = Tk()
window.title("Texteditor")
scrollbar = Scrollbar(master=window)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text()
text.pack()
scrollbar.config()

# Menue
menubar = Menu(master=window)
window.config(menu=menubar)

# Loeschen
menubar.add_command(label="Loeschen", command=delete_text)

# Menue Schrifttyp
font_menu = Menu(master=menubar)
selected_font = StringVar()
menubar.add_cascade(label="Schrifttyp", menu=font_menu)
for font in ["Arial", "Courier", "Times"]:
    font_menu.add_radiobutton(label=font,
               variable=selected_font, value=font,
               command=format_text)

# Menue Textbausteine
phrase_menu = Menu(master=menubar)
selected_phrase = StringVar()
menubar.add_cascade(label="Textbausteine", menu=phrase_menu)
phrases = ["Die frische Luft tut mir gut.",
           "Ich fuehle mich grossartig.",
           "die Landschaft ist wunderbar hier."]
for ph in phrases:
    phrase_menu.add_radiobutton(label=ph,
               variable=selected_phrase, value=ph,
               command=insert_phrase)
    
window.mainloop()