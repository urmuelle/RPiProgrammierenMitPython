# Kapitel 4, 4.13.2, Projekt Pythagorasbaum

from turtle import *
STOP = 5
START = 200

def quadrat(seitenlaenge):
    """Zeichne ein schwarzes Quadrat"""
    down()
    color("black", "black")
    begin_fill()
    for i in range(4):
        fd(seitenlaenge)
        right(90)
    end_fill()
    up()

def uebergang(spaltenbreite):
    """Uebergang zur naechsten Spalte"""
    right(90)
    forward(spaltenbreite)
    left(90)

def zurueck(seitenlaenge):
    """Zurueck zur linken unteren Ecke"""
    left(90)
    forward(2*seitenlaenge/3)
    right(90)

def sierpinski(x):
    """Zeichne Sierpinski-Teppich"""
    if x <= STOP: return
    for i in range(3):      # linke Spalte
        sierpinski(x/3)
        forward(x/3)
    backward(x)
    uebergang(x/3)
    sierpinski(x/3)         # mittlere Spalte
    forward(x/3)
    quadrat(x/3)
    forward(x/3)
    sierpinski(x/3)
    backward(2*x/3)
    uebergang(x/3)
    for i in range(3):      # rechte Spalte
        sierpinski(x/3)
        forward(x/3)
    backward(x)
    zurueck(x)

speed(0)
left(90)
up()
sierpinski(START)
hideturtle()