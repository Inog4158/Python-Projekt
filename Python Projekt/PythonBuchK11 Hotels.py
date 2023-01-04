
class Hotels:


    anzahl = 0
    
    def __init__(self, na, st, be, ko):

        self.__Name = na
        self.__Standort = st
        self.__Betten = be
        self.__Kosten = ko

        Hotels.anzahl += 1



    def getName(self):
        return self.__Name
    
    def getStandort(self):
        return self.__Standort
    
    def getBetten(self):
        return self.__Betten

    def getKosten(self):
        return self.__Kosten
    
    def setPreis(self, newPreis):
        self.__Kosten = newPreis

print("anzahl zimmer: ", Hotels.anzahl)
zimmer1 = Hotels("Säntisblick", "Appenzell", 3, 4.0)
print("anzahl zimmer: ", Hotels.anzahl)
zimmer2 = Hotels("Vierwaldstädtersee", "Luzern", 10, 8.0)
print("anzahl zimmer: ", Hotels.anzahl)
print(zimmer1.getName(), zimmer1.getStandort(), zimmer1.getBetten(), zimmer1.getKosten())
print(zimmer2.getName(), zimmer2.getStandort(), zimmer2.getBetten(), zimmer2.getKosten())
print("anzahl zimmer: ", Hotels.anzahl)
