# Kapitel 6, 6.9.4 Staumelder

from tkinter import *
from urllib.request import *
import re
WWW="http://www.wdr.de"
MESSAGE="""die aktuelle Verkerhslage in NRW.
Gesamte Staulaenge: {km} km. Betroffene Strassen:
{streets}."""

def findStau():
    wdrText = str(urlopen(WWW).read(), encoding="utf-8")
    finds1 = re.findall("<span>\d+ km Stau</span>", wdrText)
    km = int(re.findall("\d+", finds1[0])[0])
    finds2 = re.findall("<strong>\d+ km Stau</strong>", wdrText)
    streets = [re.findall("[AB]\d+", t)[0] for t in finds2]
    stNames = ", ".join(streets)
    label.config(text=MESSAGE.format(km=km, streets=stNames))
#    if km < 10:
#        image = images[0]
#    elif km < 20:
#        image = images[1]
#    else:
#        image = images[2]
#    labelImage.config(image=image)

# Widgets
window = Tk()
# images = [PhotoImage(master = window, file = fn) for fn in ["one.gif", "two.gif", "three.gif"]]
label = Label(master=window, font=("Arial", 16), bg="white")
label.pack()
labelImage = Label(master=window, bg="white")
Label(master=window, font=("Arial", 8), bg="white",
      text="Datenquelle: WDR Koeln").pack(fill=X)
findStau()
window.mainloop()