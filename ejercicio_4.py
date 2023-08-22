#Escriba un programa que pida dos palabras y diga si riman o no. Si coinciden las últimas tres
#letras tiene que decir que riman. Si coinciden sólo las últimas dos tiene que decir que riman un
#poco. Y si no coinciden, decir que no riman. Validar que las palabras tengan al menos tres letras.
#Nota: Utilizar slices.


def validar_palabra(palabra):
    return len(palabra) >= 3

def rima(palabra1, palabra2):
    if not (validar_palabra(palabra1) and validar_palabra(palabra2)):
        return "palabras deben tener al menos tres letras"
    
    if palabra1[-3:] == palabra2[-3:]:
        return "las palabras riman"
    elif palabra1[-2:] == palabra2[-2:]:
        return "las palabras riman un poco"
    else:
        return "las palabras no riman"

def main():
    palabra1 = input("ingresa la primera palabra: ")
    palabra2 = input("ingresa la segunda palabra: ")

    resultado = rima(palabra1, palabra2)
    print(resultado)

if __name__ == "__main__":
    main()
