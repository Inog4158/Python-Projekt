#PythonBuch 5.6
#06.09.2022
#Nico Schlosser
import random
#------------------------------------


#Fahrzeuge = {"wasser": "boot", "flug": "heli", "fahr": "auto"}
#choice = str(input("wasser,flug oder fahr: "))
#print(Fahrzeuge[str(input("wasser,flug oder fahr: "))])

#------------------------------------------
def info():
    print("\n", regal[int(input("Wie vieltes Buch:  "))][input("Welche Info? titel/autor/artikelnummer/preis:  ")], "\n")
    info()

buch1 = {"titel": random.choice(open('titel.txt').read().split()).strip(), "autor": random.choice(open('autor.txt').read().split()).strip(), "artikelnummer": random.randint(100000,999999), "preis": random.randint(500, 2000)/100}
buch2 = {"titel": random.choice(open('titel.txt').read().split()).strip(), "autor": random.choice(open('autor.txt').read().split()).strip(), "artikelnummer": random.randint(100000,999999), "preis": random.randint(500, 2000)/100}
buch3 = {"titel": random.choice(open('titel.txt').read().split()).strip(), "autor": random.choice(open('autor.txt').read().split()).strip(), "artikelnummer": random.randint(100000,999999), "preis": random.randint(500, 2000)/100}
buch4 = {"titel": random.choice(open('titel.txt').read().split()).strip(), "autor": random.choice(open('autor.txt').read().split()).strip(), "artikelnummer": random.randint(100000,999999), "preis": random.randint(500, 2000)/100}
buch5 = {"titel": random.choice(open('titel.txt').read().split()).strip(), "autor": random.choice(open('autor.txt').read().split()).strip(), "artikelnummer": random.randint(100000,999999), "preis": random.randint(500, 2000)/100}
buch6 = {"titel": random.choice(open('titel.txt').read().split()).strip(), "autor": random.choice(open('autor.txt').read().split()).strip(), "artikelnummer": random.randint(100000,999999), "preis": random.randint(500, 2000)/100}
regal = [buch1, buch2, buch3, buch4, buch5, buch6]
info()

