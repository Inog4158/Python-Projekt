
#PythonBuch 5.6
#06.09.2022
#Nico Schlosser
import random
import module.k9_bsp
#------------------------------------
def loop():
    i = eval(input("Zahl für die Formel wählen: "))
    print(module.k9_bsp.rechnung(i))
    loop()

loop()
