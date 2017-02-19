#----------------------------------------------------------------
# Kapitel 8, 8.1.1: Anklickbarer Buchstabe
#----------------------------------------------------------------

from tkinter import *
import random

class ClickableLabel:
    letters ="ABCDEFGHIFKLMNOPQRSTUVWXYZ"
    def __init__(self, master):                    #1
        self.master = master
        self.i = random.randint(0,len(self.letters)-1)          #2
        self.label=Label(master=self.master,
                         font=("Arial", 20),
                         text=self.letters[self.i])    #3
        self.label.bind("<1>", self.nextLetter)
    
    def nextLetter(self, event):                            #4
        if self.i < len(self.letters)-1:
            self.i += 1
        else:
            self.i = 0
        self.label.config(text=self.letters[self.i])

    def pack(self):                                #5
        self.label.pack()

class Application:
    def __init__(self):  
        self.window = Tk()
        self.c = ClickableLabel(master=self.window)
        self.c.pack()
        self.window.mainloop()

a = Application()