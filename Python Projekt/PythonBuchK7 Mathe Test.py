#PythonBuch 5.6
#06.09.2022
#Nico Schlosser
import random
#------------------------------------

print("{-{-{-{-{Mathe Test!!!}-}-}-}-}")
points = int(0)
plus1 = random.randint(1, 499)
plus2 = random.randint(1, 499)
minus1 = random.randint(1, 499)
minus2 = random.randint(1, minus1)
mal1 = random.randint(1, 10)
mal2 = random.randint(1, 10)
geteilt3 = random.randint(1, 10)
geteilt2 = random.randint(1, 10)
geteilt1 = geteilt3 * geteilt2
Mal1 = random.randint(10, 20)
Mal2 = random.randint(10, 20)

      
plus3 = int(input("{} + {} = ". format(plus1, plus2)))
minus3 = int(input("{} - {} = ". format(minus1, minus2)))
mal3 = int(input("{} * {} = ". format(mal1, mal2)))
geteilt3 = int(input("{} / {} = ". format(geteilt1, geteilt2)))
Mal3 = int(input("{} * {} = ". format(Mal1, Mal2)))


if plus3 == plus1 + plus2:
    points += 1
if minus3 == minus1 - minus2:
    points += 1
if mal3 == mal1 * mal2:
    points += 1
if geteilt3 == geteilt1 / geteilt2:
    points += 1
if Mal3 == Mal1 * Mal2:
    points += 1

print("\n")

if points == 5:
    print("Super! Alle Aufgaben Richtig Gelöst!({} Punkte)".format(points))
elif points > 2:
    print("Gute Leistung!({} Punkte)".format(points))
elif points > 0:
    print("Viele Fehler Weitere Übung Erforderlich!({} Punkte)".format(points))
else:
    print("O Punkte Dringend Nachhilfe Benötigt!({} Punkte)".format(points))

fertig = input("\n\n\nPress to end")

