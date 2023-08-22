#Escribir un programa que contenga una función que reciba una lista de palabras y devuelva la
#palabra más larga. Imprimir por pantalla la palabra resultante.


def palabra_larga(lista_palabras):
    palabra_larga = ""
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    return palabra_larga

def main():

    ingresar_palabras = input("ingresa palabras separadas por una coma: ")#no ingresar numeros
    lista_palabras = ingresar_palabras.split(',')

    lista_palabras = [palabra.strip() for palabra in lista_palabras]

    palabra_larga = palabra_larga(lista_palabras)

    print(f"la palabra más larga es: {palabra_larga}")

if __name__=="__main__":
    main()


    
