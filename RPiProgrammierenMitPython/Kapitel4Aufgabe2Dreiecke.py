# Kapitel 4, Aufgabe 2, Spirale aus Dreiecken

from turtle import *

def spirale(n):
    if n > 2:
        right(60)
        for i in range(3):
            fd(n)
            right(120)
        fd(n)        
        spirale(n/2)

clear()
speed(0)
spirale(200)
hideturtle()