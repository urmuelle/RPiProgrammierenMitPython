#Kapitel 2, Aufgabe 1, Seite 82

from math import *

hoehe = float(input("Hoehe des Winkelmessers ueber Boden (m): "))
entfernung = float(input("Entfernung zum Turm (m): "))
winkel = float(input("Winkel (Grad): "))

g =  tan(winkel)*entfernung + hoehe;

print("Gebaeudehoehe ", round(g, 2), "m")