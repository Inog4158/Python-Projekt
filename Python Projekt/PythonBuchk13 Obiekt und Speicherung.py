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


#--------------------------------------------------------------


f = open("sortiment.txt","r")
inhalt = f.readlines()
länge = int(len(inhalt)/5)
liste = []

for i in range(länge):
    autor = inhalt[i*5]
    titel = inhalt[i*5+1]
    preis = inhalt[i*5+2]
    seiten = inhalt[i*5+3]
    liste += [Regal(autor, titel, preis, seiten)]

for i in range(länge):
    print("Autor: ", liste[i].getAutor())
    print("Titel: ", liste[i].getTitel())
    print("Preis: ", liste[i].getPreis())
    print("Seiten: ", liste[i].getSeiten(), "\n")




end = input("Press to End")







    



