
#PythonBuch 5.6
#21.09.2022
#Nico Schlosser
#------------------------------------
def login(benutzer,passwort):
    angemeldet = False
    per1 = "Paul", "vgen8u3"
    per2 = "Fritz", "8fuh92"
    per3 = "Bob",  "v3d4vw"
    daten = [per1, per2, per3]

    
    for x in daten:
        if x[0] == benutzer and x[1] == passwort:
            print("erfolgreich")
            angemeldet = True

    return angemeldet
