liste = []
newliste = []
loop = True
while loop == True:
    name = input("Person hinzufügen(mit 'beenden' wird die Liste gefüllt): ")
    if name == "beenden":
        loop = False
    else:
        liste += name

        
print("Neue Namen: ")
for i in range(len(liste)):
    print(liste[i])


    
f = open("partyliste.txt","a")

for i in range(len(liste)):
    x = liste[i]
    f.write("\n"+x)
    
f.close()



f = open("partyliste.txt", "r")

partyliste = f.readlines()

print("Partyanmeldungen: ")
for i in range(len(partyliste)):
    print(partyliste[i])
    
f.close()


 
end = input("Press to End")
