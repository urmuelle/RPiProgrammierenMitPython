# Kapitel 4, Aufgabe 2, Turm aus Quadraten

from turtle import *

def quadrat(n):
    for i in range(4):    
        forward(n)
        right(90)
    
def figur(n):
    if n > 1:
        quadrat(n)
        forward(n)
        figur(n/2)

clear()
left(90)
speed(0)
figur(100)
hideturtle()