#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa
#debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida
#terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el
#siguiente formato:


def lista_compra(carrito):
    print("\n lista de la compra: ")
    total = 0
    for articulo, precio in carrito.items():
        print(f"{articulo}: {precio}")
        total += precio
    print(f"coste total: {total}")

carrito_compra = {}

while True:
    articulo = input("ingresa el nombre del artículo ( escriba 'salir' para finalizar): ")
    
    if articulo.lower() == 'salir':
        break
    
    precio = int(input(f"ingresa el precio del artículo '{articulo}': "))
    
    carrito_compra[articulo] = precio

lista_compra(carrito_compra)
