import random
numero = random.randint (0, 99)

def intro():
    print ("Adivina el número del 0 al 99")

def juega():
    intentos = 0
    while True:
        numUsuario = int(input("Inserta un número: "))
        if numUsuario > numero:
            intentos += 1
            print("Demasiado grande")
        elif numUsuario < numero:
            intentos +=1
            print("Demasiado pequeño")
        else:
            intentos +=1
            print(f"Ha ganado! Lo ha conseguido en el intento numero {intentos}")
            break


intro()
juega()