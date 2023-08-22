#Escriba un programa que calcule el factorial de un número ingresado por el usuario.



def main():

    numero = int (input("ingrese numero: "))
    factorial=1
    for n in range(1,numero+1):
        factorial=factorial*n
        print (factorial)

if __name__ == "__main__":
    main() 