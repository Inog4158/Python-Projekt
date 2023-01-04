name = input("Wen willst du Löschen?(klein geschrieben): ")
f = open("partyliste.txt", "r")
liste = f.readlines()
print(liste)
f.close()
print(liste)


for i in range(len(liste)):
    x = liste[i]
    print(x)
    if x != name:
        new = open("partyliste.txt", "w")
        new.write(x)
    f.close()

    
