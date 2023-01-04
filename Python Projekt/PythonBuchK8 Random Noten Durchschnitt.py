#PythonBuch 5.6
#06.09.2022
#Nico Schlosser
import random
#------------------------------------




summe = 0
dic = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
for var in dic:
    summe += var
    print(var)
    
schnitt = summe / len(dic) + 0.5
print(int(schnitt))

fertig = input("\n\n\nPress to end")

