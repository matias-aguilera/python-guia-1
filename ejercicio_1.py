#Cree un programa que elija un numero al azar entre 1 y 100, luego le pregunta por un número y
#el programa le debe decir si el numero ingresado es demasiado bajo o demasiado alto, hasta
#que logre dar con el numero generado.


import random

def main():
    numero = random.randint(1, 100)
    
    print("adivina el numero entre 1 y 100")

    while True:
        intento = int(input("ingresa un número: "))

        if intento < numero:
            print("muy bajo")
        elif intento > numero:
            print("muy alto")
        else:
            print("le atinaste, felicidades")
            break

if __name__ == "__main__":
    main()