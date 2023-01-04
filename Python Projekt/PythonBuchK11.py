class Regal:

    anzahl = 0
    
    def __init__(self, au, ti, pr, se):

        self.__Autor = au
        self.__Titel = ti
        self.__Preis = pr
        self.__Seiten = se
        

        Regal.anzahl += 1



    def getAutor(self):
        return self.__Autor

        
    def getTitel(self):
        return self.__Titel

        
    def getPreis(self):
        return self.__Preis

        
    def getSeiten(self):
        return self.__Seiten

        
    def setPreis(self, preis_neu):
            self.__Preis = preis_neu

    def __del__(self):
    
        Regal.anzahl -= 1
        print("Auto gelöscht")
        print("noch übrig :", Regal.anzahl)

        
class Roman(Regal):

    def __init__(self, au, ti, pr, se, roman):

        Regal.__init__(self, au, ti, pr, se)
        self.__Roman = roman

    def getRoman(self):
        return self.__Roman


class Schulbuch(Regal):

    def __init__(self, au, ti, pr, se, schulbuch):
        
        Regal.__init__(self, au, ti, pr, se)
        self.__Schulbuch = schulbuch
        
    def getSchulbuch(self):
        return self.__Schulbuch





print("anzahl :", Regal.anzahl)
buch1 = Regal("Arthur", "Märchen", 10, 380)
print("anzahl :", Regal.anzahl, buch1.anzahl)
buch2 = Schulbuch("Bob", "Mathbuch", 4, 120, True)
print("anzahl :", Regal.anzahl, buch1.anzahl)
buch = Roman("Timon", "Star Wars", 55, 279, False)
print("anzahl :", Regal.anzahl)


print(buch1.anzahl, buch2.anzahl, buch.anzahl)

del buch1

print(Regal.anzahl, buch2.anzahl, buch.anzahl)


        
wert = eval(input("Geben sie neuen Preis ein: "))
buch2.setPreis(wert)

print(buch2.getPreis())


print(buch.getPreis())

print(buch.getRoman())

print("------------------------------------------")

print(buch2.getPreis())

print(buch2.getSchulbuch())













