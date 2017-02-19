#----------------------------------------------------------------
# Kapitel 8, Projekt 8.3: Run animation
#----------------------------------------------------------------
from tkinter import *
#from RPi import GPIO
import random, _thread
from time import sleep

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(10, GPIO.IN)
#GPIO.setup(8, GPIO.IN)

STEP = 0.1
GAMETIME = 120
BWIDTH = 750

class Switch:
    def __init__ (self, nr, window):
        self.nr = nr
        if nr == 0:
            window.bind("<1>", self.switch)
            window.bind("<ButtonRelease-1>", self.unswitch)
        else:
            window.bind("<3>", self.switch)
            window.bind("<ButtonRelease-3>", self.unswitch)       
        self.pressed = False

    def switch(self, event):
        self.pressed = True
        
    def unswitch(self, event):
        self.pressed = False

    def isPressed(self):
        return self.pressed

class Controller:
    def __init__(self, switches, display, clock, runner):
        self.s, self.display = switches, display
        self.clock, self.runner = clock, runner
        _thread.start_new_thread(self.run, ())
        
    def waitUntilClicked(self, s):
        while not s.isPressed():
            sleep(STEP)
        while s.isPressed():
            sleep(STEP)      

    def run(self):
        while True:
            self.display.show("Gehe zum Start!")
            waitUntilClicked(self.s[1])
            self.newRun()
                
    def newRun(self):
        self.clock.reset()
        self.runner.startPosition()
        self.display.show("Starte mit dem rechten Fuß! Renn!")
        while not(self.s[1].isPressed() or self.s[0].isPressed()):
            sleep(STEP)
        self.display.show("")
        self.runner.start()
        self.clock.start()
        self.speed = 0
        while self.clock.ticking:
            self.updateSpeed()
        self.display.show("Ziel erreicht!")
        sleep(2)
        self.display.show("")

    def updateSpeed(self):
        t = 0.1
        while not self.s[1].isPressed() and (t < 1):
            t += STEP/5
            sleep(STEP/5)
        while self.s[1].isPressed() and (t < 1):
            t += STEP/5
            sleep(STEP/5)
        while not self.s[0].isPressed() and (t < 1):
            t += STEP/5
            sleep(STEP/5)
        while self.s[0].isPressed() and (t < 1):
            sleep(STEP/5)
            t += STEP/5 
        self.runner.speed = 10/t - 10
     
class Display:
    def __init__(self, background):
        self.background = background
        self.iD = self.background.create_text(BWIDTH/2, 20,
                    font=("Arial", 20))

    def show(self, text):
        self.background.itemconfig(self.iD, text=text)

class Clock:
  def __init__(self, background):
    self.background = background
    self.ticking = False
    self.time = 0.0
    self.iD = self.background.create_text(40, 20,
                            font=("Arial", 20), fill = "blue",
                            text=str(self.time))
  def tick(self):
      while self.ticking:
        sleep(0.1)
        self.time = round(self.time + 0.1, 2)
        self.background.itemconfig(self.iD, text=str(self.time))

  def reset(self):
      self.time = 0.0
      self.background.itemconfig(self.iD, text=str(self.time))

  def start(self):
      self.ticking = True
      _thread.start_new_thread(self.tick, ())

  def stop(self):
      self.ticking = False
              
class Runner:
    def __init__(self, background, clock):
        self.background = background
        self.clock = clock
        self.runImages = [PhotoImage(file=fn)
                           for fn in ["girl_1.gif", "girl_2.gif", "girl_3.gif",
                                      "girl_7.gif", "girl_8.gif", "girl_3.gif"]]    
        self.standingImage= PhotoImage(file="girl_standing.gif")
        self.iD = self.background.create_image(40, 400, anchor=S, 
                            image=self.standingImage)
        self.speed = 0
              
    def startPosition(self):
        self.x = 40
        self.background.coords(self.iD, self.x, 400)
        self.background.itemconfig(self.iD, image=self.standingImage)

    def start(self):
        self.speed = 0
        _thread.start_new_thread(self.run, ())

    def run(self):
        while self.x < BWIDTH - 120:
            self.background.move(self.iD, self.speed, 0)
            self.x += self.speed
            for i in self.runImages:
                self.background.itemconfig(self.iD, image=i)
                sleep(STEP)
        self.clock.stop()
        self.speed = 0
                               

class Background(Canvas):
    def __init__(self, window):
        self.bg = PhotoImage(file="background.gif")
        Canvas.__init__(self, master=window,
                        width=self.bg.width(),
                        height=self.bg.height())
        self.create_image(0, 0, anchor=NW, image=self.bg)
        self.pack()     
                                                             
class Run:
    def __init__(self):

        self.window = Tk()
        self.background = Background(self.window)
        self.display = Display(self.background)
        self.clock = Clock(self.background)
        self.runner = Runner(self.background, self.clock)
        self.switches =[Switch(i, self.window) for i in [0, 1]]
        #self.control = Controller(self.switches, self.display,
        #                          self.clock, self.runner)
        self.window.mainloop()

Run()  
