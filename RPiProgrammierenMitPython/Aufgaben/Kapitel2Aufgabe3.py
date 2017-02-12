# Kapitel 2, Aufgabe 3, Seite 83
punkte = 0

print("Wofuer steht das \"Pi\" des Raspberry Pi?")
print("(P)ython Interpreter")
print("(K)reiszahl Pi")
print("Public (I)nternet")
antwort = input("Antwort: ")

if (antwort == "P") or (antwort == "p"):
    punkte += 1;
    print("Richtig.")
else:   
    print("Falsch.")

print("Welches Betriebssystem funktioniert auf dem RPi nicht?")
print("(R)isc OS")
print("(W)indows 8")
print("(A)rch Linux")
antwort = input("Antwort: ")

if (antwort == "W") or (antwort == "w"):
    punkte += 1;
    print("Richtig.")
else:    
    print("Falsch.")

print("In welchem Land wurde der RPi entwickelt?")
print("(D)eutschland")
print("(E)ngland")
print("(U)SA")
antwort = input("Antwort: ")

if (antwort == "E") or (antwort == "e"):
    punkte += 1;
    print("Richtig.")
else:
    print("Falsch.")

if (punkte == 3):
    print("Alles richtig beantwortet! ", end="")

print("Danke fuers Mitmachen")