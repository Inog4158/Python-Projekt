def zahl():
    try:
        x = int(input("Geben sie eine ganze Zahl ein: "))
        y = int(input("Geben sie die 2 Zahl ein: "))

        
    except ValueError:
        print("Nur ganze Zahlen!")
        zahl()

    except ZeroDivisionError:
        print("Kann nicht durch 0 Geteilt werden")
        zahl()

    print(x/y)
zahl()
