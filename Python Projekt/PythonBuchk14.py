from tkinter import *

class myButton(Button):
    
    def rightButton (self):
        print("Rechter Knopf gedrückt")
    def bestätigung (self):
        name = eingabe.get()
        print(name)
        eingabe.delete(0,"end")

    def bestätigung2 (self):
        print(var.get())

        
objekt = Tk()
objekt.geometry("300x350")
objekt.title("Willkommen zun Python-Kurs!")

rahmen = Frame(objekt, relief="ridge", borderwidth=5)
rahmen.pack(fill="both", expand=1)

label = Label(rahmen, text="Willkommen zun Python-Kurs!")

label.place(x=60, y=5)

button1 = Button(rahmen, text="Left", command=objekt.destroy, width=10)
button2 = myButton(rahmen, text="Right", width=10)
button2["command"] = button2.rightButton


button1.place(x=40, y=25)
button2.place(x=170, y=25)

eingabe = Entry(rahmen, bd=2, width=22)
eingabe.place(x=30, y=60)
button3 = myButton(rahmen, text="Eingabe")
button3["command"] = button3.bestätigung
button3.place(x=200, y=60)

var = IntVar()
checkbutton = Checkbutton(rahmen, text="Bestätigen", variable = var)
checkbutton.place(x=50, y=100)
button4 = myButton(rahmen, text="Eingabe")
button4["command"] = button4.bestätigung2
button4.place(x=200, y=100)

scrollbar = Scrollbar(rahmen)
liste = Listbox(rahmen, yscrollcommand = scrollbar.set)
for i in range(25):
    liste.insert(END, "Zeile " + str(i))
scrollbar.config(command=liste.yview)
liste.place(x=30, y=150)
scrollbar.pack(side="left", fill="y")



objekt.mainloop
