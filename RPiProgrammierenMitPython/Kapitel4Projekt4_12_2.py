# Kapitel 4, 4.12.2, Projekt Eine rekursive Spirale aus Quadraten

from turtle import *

def quadrat(n):
    #begin_fill()
    for i in range(4):
        forward(n)
        right(90)
    #end_fill

def spirale(n):
    if n > 5:
        quadrat(n)
        right(15)
        spirale(n*0.9)

clear()
speed(0)
#color("black", "white")
spirale(100)
#hideturtle()