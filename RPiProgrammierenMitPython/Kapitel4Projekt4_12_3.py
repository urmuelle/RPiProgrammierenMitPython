# Kapitel 4, 4.13.2, Projekt Pythagorasbaum

from turtle import *
from math import sqrt

def baum(c):
    a = c/sqrt(2)    
    if c < 10:
        right(90)
        fd(c)
        right(90)
    else:
        fd(c)
        left(45)
        baum(a)
        left(90)
        baum(a)
        left(45)
        fd(c)

speed(0)
left(90)
baum(40)