#----------------------------------------------------------------
# Kapitel 7, 7.3.3 Vollbildmodus
#----------------------------------------------------------------

from time import *
from tkinter import *
import _thread
BGCOLOR="#933"

month=["Januar", "Februar", "Maerz", "April", "Mai",
       "Juni", "Juli", "August", "September",
       "Oktober", "November", "Dezember"]

def checkTime():
    while True:
        t = localtime()
        timeText = "Heute ist der " + str(t.tm_mday) + ". "
        timeText += month[t.tm_mon - 1] + " "
        timeText += str(t.tm_year) + ".\n"
        timeText += "Es ist " + str(t.tm_hour) + " Uhr\n"
        timeText += str(t.tm_min) + " Minuten und\n"
        timeText += str(t.tm_sec) + " Sekunden."
        label.config(text=timeText)
        sleep(1)

window = Tk()

window.overrideredirect(True)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry(str(w) + "x" + str(h) + "+0+0")

frame = Frame(master=window, bg=BGCOLOR)
label = Label(master=frame, bg=BGCOLOR,
              font=("Courier", 30), fg="white")
button = Button(master=frame, text="X", bg=BGCOLOR,
                fg="white", command=window.destroy)
frame.pack(expand=True, fill=BOTH)
label.pack(expand=True, fill=BOTH)
button.pack(side=RIGHT)
_thread.start_new_thread(checkTime,())

window.mainloop()