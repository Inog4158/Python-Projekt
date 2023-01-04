#PythonBuch 5.6
#06.09.2022
#Nico Schlosser
#------------------------------------
def rechnung():
    num1 = int(input("Erste Zahl der Addition eingeben: "))
    num2 = int(input("Zweite Zahl der Addition eingeben: "))
    print(num1, " + ", num2, " ergibt = ", num1 + num2)
    rechnung()



rechnung()
