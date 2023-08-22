#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro
#usando la primera función.


def circulo(radio):
    pi = 3.14
    area = (pi * radio**2)
    return (area)

   

def volumen_cilindro(altura, radio):
    pi = 3.14
    volumen = (circulo(radio) * altura)
    return(volumen)


def main():
   radio=int(input("ingrese el valor del area: "))
   altura=int(input("ingrese el valor de la altura: "))

   print(circulo(radio))
   print(volumen_cilindro(altura, radio))



if __name__=="__main__":
     main()