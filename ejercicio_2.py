#Cree un programa conversor de unidades, donde muestre una serie de unidades a convertir y la
#opción de terminar el programa. Si se selecciona la opción de terminar el programa, se debe
#terminar la ejecución del mismo. Por ejemplo:
#a. ¿Que conversión desea realizar?
#b. 1) centímetros -> pulgadas
#c. 2) metros -> kilometros
#d. 3) onzas -> gramos
#e. 4) milla -> kilometro
#f. 5) celcius -> fahrenheit
#g. 6) Salir


def cm_a_in (a):
    return a * 0.39

def mts_a_km (a):
    return a/1000

def onzas_a_gr (a):
    return a*28.34

def milla_a_km (a):
    return a*1.609

def celcius_a_fahrenheit (a):
    return (a * 9/5) + 32

    

def main():
        mensaje = """ 
        transformaciones
        1- centímetros -> pulgadas
        2- metros -> kilometros
        3- onzas -> gramos
        4- milla -> kilometro
        5-celcius -> fahrenheit
        6- salir

       """ 
        print(mensaje)

        opcion = int (input("ingrese una opcion: "))

        while opcion != 6 :
             valor_1=int(input("ingrese numero 1: "))
             

             if opcion==1:
                  resultado = cm_a_in(valor_1)
             elif opcion==2:
                  resultado = mts_a_km(valor_1)    
             elif opcion==3:
                  resultado = onzas_a_gr(valor_1) 
             elif opcion==4:
                  resultado = milla_a_km(valor_1)
             elif opcion==5:
                  resultado = celcius_a_fahrenheit(valor_1)        
             else:
                  resultado=""
                  print("la opcion no es valida")    

             print(f"el resultado de la operacion es : {resultado}") 

             opcion = int (input("ingrese una opcion: ")) 

             print(mensaje)       


if __name__=="__main__":
        main()