# Kapitel 2, Aufgabe 4, Seite 84

from math import pi

wiederholung = True

while (wiederholung):

    # Eingabe
    eingabe_durchmesser = input("Durchmesser in m: ")
    eingabe_hoehe = input("Hoehe in m: ")

    # Verarbeitung
    d = float(eingabe_durchmesser)
    h = float (eingabe_hoehe)
    volumen = pi * (d/2)**2 * h

    # Ausgabe
    print("Der Zylinder hat folgendes Volumen (Kubikmeter)")
    print(round(volumen, 2))

    r = input("Noch eine Rechnung (j/n)?")

    if (r == "N") or (r == "n"):
        wiederholung = False;

print("Auf Wiedersehen")