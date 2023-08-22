
#Escribe un programa que le pida al usuario una palabra y una letra. El programa debe contar
#cuántas veces aparece la letra en la palabra usando un ciclo for.

def main():

    palabra = input("ingresa una palabra: ")
    letra = input("ingresa una letra: ")

    contador = 0

    for i in palabra:
        if i == letra:
            contador += 1

    print(f"la letra '{letra}' aparece {contador} veces en la palabra '{palabra}'")

if __name__ == "__main__":
    main()