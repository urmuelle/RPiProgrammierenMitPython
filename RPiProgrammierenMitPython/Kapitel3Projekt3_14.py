G = {"A":[("B", 2), ("C", 5)],
     "B":[("C", 1), ("D", 5)],
     "C":[("A", 5), ("E", 1)],
     "D":[("C", 1), ("E", 2)],
     "E":[]}

start = input("Start: ")
ziel = input("Ziel: ")
nicht_besucht = G.keys()
entfernung = {k:10000 for k in G.keys()}
entfernung[start] = 0
vorgaenger = dict()

while nicht_besucht:
    weglaenge, knoten = min([(entfernung[k], k) for k in nicht_besucht])
    nicht_besucht -= {knoten}
    for nachbar, distanz in G[knoten]:
        if (nachbar in nicht_besucht) and (weglaenge + distanz < entfernung[nachbar]):
            vorgaenger[nachbar] = knoten
            entfernung[nachbar] = weglaenge + distanz

# Weg berechnen
knoten = ziel
weg = []
while knoten in vorgaenger.keys():
    weg = [knoten] + weg
    knoten = vorgaenger[knoten]

# Ausgabe
print(start, end=" ")
for k in weg:
    print("-->", k, end=" ")