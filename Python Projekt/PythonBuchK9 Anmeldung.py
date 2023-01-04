
#PythonBuch 5.6
#21.09.2022
#Nico Schlosser
import random
import module.k9_anmeldungsvorgang
#------------------------------------  
benutzer = input("Benutzername: ")
passwort = input("Passwort: ")
        
if True == module.k9_anmeldungsvorgang.login(benutzer, passwort):
    print("Willkommen! ")
else:
    print("Anmmeldung fehlgeschlagen")

