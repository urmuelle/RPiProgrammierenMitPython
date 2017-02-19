#----------------------------------------------------------------
# Kapitel 7, 7.3.2 Digitaluhr
#----------------------------------------------------------------

from time import *
from tkinter import *
import _thread

def checkTime():
    while True:
        t = localtime()
        timeText = "Es ist " + str(t.tm_hour) + " Uhr\n"
        timeText += str(t.tm_min) + " Minuten und\n"
        timeText += str(t.tm_sec) + " Sekunden."
        sleep(1)
        timeLabel.config(text=timeText)

window = Tk()
timeLabel = Label(master=window, bg="black",
              font=("Courier", 30), fg="white")
timeLabel.pack()
_thread.start_new_thread(checkTime,())

window.mainloop()