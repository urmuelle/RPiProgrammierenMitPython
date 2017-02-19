#----------------------------------------------------------------
#----------------------------------------------------------------
"""Dieses Modul ist eine Beispielimplementation
   zur Lösung Aufgabe 1, Kapitel 2

"""

from math import *

hoehe = float(input("Hoehe des Winkelmessers ueber Boden (m): "))
entfernung = float(input("Entfernung zum Turm (m): "))
winkel = float(input("Winkel (Grad): "))

g =  tan(winkel)*entfernung + hoehe;

print("Gebaeudehoehe ", round(g, 2), "m")