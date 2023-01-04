
#PythonBuch 5.6
#21.09.2022
#Nico Schlosser
import random
#------------------------------------
def output(x,y):
    if x < y:
        for z in range(x, y + 1, 2):
            print(z)

    else:
        for z in range(x, y - 1, -2):
            print(z)
            
num1 = eval(input("Erste Zahl: "))
num2 = eval(input("Zweite Zahl: "))
            
output(num1, num2)


