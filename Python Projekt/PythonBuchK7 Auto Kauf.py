#PythonBuch 5.6
#06.09.2022
#Nico Schlosser
import random
#------------------------------------


auto1 = {"marke": "VW", "name": "Golf", "artikelnummer": 589375, "preis": 5000}
auto2 = {"marke": "BMW", "name": "Rover", "artikelnummer": 897435, "preis": 8500}
auto3 = {"marke": "Audi", "name": "Panarama", "artikelnummer": 902383, "preis": 58000}
regal = [auto1, auto2, auto3]

budge = int(input("Wie viel würden sie Zahlen(CHF): "))
if budge >= regal[0]["preis"]:
    print("Marke:", regal[0]["marke"], \
          "/ Name:", regal[0]["name"], \
          "/ Artikelnummer:", regal[0]["artikelnummer"], \
          "/ Preis:", regal[0]["preis"], "CHF")
    
if budge >= regal[1]["preis"]:
    print("Marke:", regal[1]["marke"], \
          "/ Name:", regal[1]["name"], \
          "/ Artikelnummer:", regal[1]["artikelnummer"], \
          "/ Preis:", regal[1]["preis"], "CHF")

if budge >= regal[2]["preis"]:
    print("Marke:", regal[2]["marke"], \
          "/ Name:", regal[2]["name"], \
          "/ Artikelnummer:", regal[2]["artikelnummer"], \
          "/ Preis:", regal[2]["preis"], "CHF")
    
fertig = input("\n\n\nPress to end")
