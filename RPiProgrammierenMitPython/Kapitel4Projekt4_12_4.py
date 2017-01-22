# Kapitel 4, 4.13.2, Projekt Koch Schneeflocke

from turtle import *
STOP = 2
START = 200

def seite(n):
    if n <= STOP:        
        fd(n)
    else:
        seite(n/3)
        left(60)
        seite(n/3)
        right(120)
        seite(n/3)
        left(60)
        seite(n/3)

speed(0)
left(60)
for i in range(3):
    seite(START)
    right(120)
hideturtle()