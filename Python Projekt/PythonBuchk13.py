"""
f = open("sortiment.txt", "w")

nummer = input("nummer: ")
preis = input("preis: ")

f.write(nummer+"\n")
f.write(preis+"\n")
f.write("\n")
f.close()


f = open("sortiment.txt", "r")
inhalt = f.read()
print(inhalt)
"""

f = open("sortiment.txt", "r")
inhalt = f.readlines()
