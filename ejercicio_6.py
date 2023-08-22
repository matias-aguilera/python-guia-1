#Escriba un programa que pida al usuario una palabra y la imprima al revés. El programa debe
#continuar pidiendo palabras hasta que el usuario ingrese salir

def main():
    palabra=input("ingrese nombre: ")

    while palabra.lower() != "salir":
        
        reves = palabra[::-1]
        print(f"Palabra al reves es: {reves}")
        palabra=input("ingrese nombre: ")

if __name__ == "__main__":
    main()    