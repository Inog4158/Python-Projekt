from tkinter import *

class myButton(Button):

    def rechnenButton (self):
        zahl1 = int(eingabe1.get())
        zahl2 = int(eingabe2.get())
        eingabe1.delete(0, "end")
        eingabe2.delete(0, "end")
        ausgabe.delete(0, "end")
        ausgabe.insert(0, zahl1 + zahl2)

    def checkButton (self):
        if 1 == check.get():
            info = Tk()
            info.geometry("100x50")
            info.title("Hinweis")
            label = Label(info, text="Checkbox Ausgefüllt")
            label.pack(fill="both", expand=1)

rechner = Tk()
rechner.geometry("200x400")
rechner.title("Taschenrechner")
rahmen = Frame(rechner, relief="ridge", borderwidth=10)
rahmen.pack(fill="both", expand=1)
label1 = Label(rahmen, text="Additions Rechner")
label1.place(x=40, y=20)

eingabe1 = Entry(rahmen, bd=2, width=10)
eingabe2 = Entry(rahmen, bd=2, width=10)
ausgabe = Entry(rahmen, bd=2, width=10)
eingabe1.place(x=15, y=50)
eingabe2.place(x=105, y=50)
ausgabe.place(x=60, y=120)

button = myButton(rahmen, text="Ausrechnen")
button["command"] = button.rechnenButton
button.place(x=55, y=80)

check = IntVar()
checkbutton = Checkbutton(rahmen, text="Check", variable = check)
checkbutton.place(x=58, y=175)

button2 = myButton(rahmen, text="Bestätigen")
button2["command"] = button2.checkButton
button2.place(x=55, y=220)


rechner.mainloop
