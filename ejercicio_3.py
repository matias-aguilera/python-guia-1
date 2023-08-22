#Cree un programa que solicite al usuario un número y determine si el número es primo o no.



def n_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    
    return True

def main():
    numero = int(input("ingresa un numero: "))

    if n_primo(numero):
        print(f"{numero} es un numero primo")
    else:
        print(f"{numero} no es un numero primo")

if __name__ == "__main__":
    main()