# Kapitel 4, Aufgabe 2, Spirale aus Linien

from turtle import *
MAX = 200

def spirale(n):
    if n < MAX:
        forward(n)
        right(90)
        spirale(n+5)
    
clear()
speed(0)
spirale(5)
hideturtle()