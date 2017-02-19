#----------------------------------------------------------------
# Kapitel 7, 7.4.3: Digitaler Bilderrahmen
# Benötigt PIL (Python Image Library), läuft nur unter Python 2.7
#----------------------------------------------------------------

from time import *
from tkinter import *
from PIL import Image, ImageTk
from random import choice
import _thread, os, time
BGCOLOR="#933"

month=["Januar", "Februar", "Maerz", "April", "Mai",
       "Juni", "Juli", "August", "September",
       "Oktober", "November", "Dezember"]

def showImages():
    while True:
        # Und hier wäre der Programmteil
        sleep(2)

def finish(event):
    window.destroy()

files = os.listdir(".")
imageFiles = [f for f in files
              if os.path.splitext(filedialog)[1] in {".jpg", ".JPG"}]

window = Tk()
window.overrideredirect(True)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry(str(w) + "x" + str(h) + "+0+0")
window.bind("<Button-1>", finish)

label = Label(master=window, bg="black")
label.pack(expand=True, fill=BOTH)
_thread.start_new_thread(showImages,())

window.mainloop()