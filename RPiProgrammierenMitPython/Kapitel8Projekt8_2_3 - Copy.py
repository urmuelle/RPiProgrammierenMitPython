#----------------------------------------------------------------
# Kapitel 8, Projekt 8.2.3: Pong - ohne RaspberryPi, Maustasten
#----------------------------------------------------------------
from tkinter import *
import random, time, _thread

STEP = 0.05

class Ball:
    def __init__(self, canvas, points):
        self.canvas, self.points = canvas, points
        self.img = PhotoImage(file='ball.gif')
        self.iD = self.canvas.create_image(0, 0, image=self.img)
        self.start()

    def start(self):
        x = int(self.canvas['width'])/2
        self.canvas.coords(self.iD, x, 1)
        self.vy = random.randint(2,6)
        self.vx = random.choice([-3, 3])
        _thread.start_new_thread(self.run, ())

    def bounce(self):
        if self.vx > 0:
            self.vx = -self.vx -1
        else:
            self.vx = -self.vx +1
        self.canvas.move(self.iD, self.vx, self.vy)

    def run(self):
        x, y = self.canvas.coords(self.iD)
        while 0 < int(x) < int(self.canvas['width']):
            self.canvas.move(self.iD, self.vx, self.vy)
            x, y = self.canvas.coords(self.iD)
            if not(0 < int(y) < int(self.canvas['height'])):
                self.vy = - self.vy
            time.sleep(STEP)       
        if int(x) <= 0: winner = 1
        else: winner = 0
        self.points.count(winner)    
        self.canvas.after(3000, self.start)

class Bat:
    def __init__(self, canvas, ball, x, pin):
        self.canvas, self.ball, self.pin = canvas, ball, pin
        self.y = 0
        self.direction = 1
        self.img = PhotoImage(file='bat.gif')
        self.iD = self.canvas.create_image(x, 0, anchor=NW, image=self.img)
        self.canvas.bind(pin, self.changeDir)
        _thread.start_new_thread(self.run, ())

    def run(self):
        while True:
            if (self.direction == 1) and (self.y > 0):
                self.canvas.move(self.iD, 0, -5)
                self.y -= 5
            elif self.y < int(self.canvas['height']) - 30:
                self.canvas.move(self.iD, 0, 5)
                self.y += 5
            x1, y1, x2, y2  = self.canvas.bbox(self.iD)
            if self.ball.iD in self.canvas.find_overlapping(x1, y1, x2, y2):
                self.ball.bounce()
            time.sleep(STEP)
    
    def changeDir(self, event):
        self.direction *= -1
    
class Points:
    def __init__(self, canvas):
        self.points =[0, 0]
        self.canvas = canvas
        x = int(canvas.cget('width'))/2
        self.iD = self.canvas.create_text(x, 50,
                                    font=("Arial", 50),
                                    fill = "white",
                                    text="0 : 0")
    def count(self, player):
        self.points[player] += 1
        text = str(self.points[0]) + " : " + str(self.points[1])
        self.canvas.itemconfigure(self.iD, text=text)
                                                             
class Pong:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(master=self.window, bg="black", 
                             width=800, height=450)
        self.canvas.pack()
        self.points = Points(self.canvas) 
        self.ball = Ball(self.canvas, self.points )
        self.leftBat = Bat(self.canvas, self.ball, 20, "<1>")
        self.rightBat = Bat(self.canvas, self.ball, 760, "<3>")
        self.window.mainloop()

Pong()  
