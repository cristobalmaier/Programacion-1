"""
Se quieren cargar las ventas de productos de un kiosco. Se debe cargar el nombre de productos y la cantidad.

    Se cargan datos hasta que se ingrese un 0 en cantidad.
    Los productos se cargan con códigos de tres letras y números por ejemplo: A01, B03
    Se deben utilizar 2 arreglos para guardar la información.

Se pide:

Crear una función que calcule el máximo producto vendido en cantidad y muestre su código

Ordenar de menor a mayor los productos y las cantidades, imprimir la información de ambos arreglos.
"""

def ingresar_producto():
    producto = input("Ingrese producto: ")
    while producto == "":
        producto = input("Ingrese producto: ")
    return producto

def ingresar_cantidad():
    cantidad = int(input("Ingrese cantidad: "))
    while cantidad < 0:
        cantidad = int(input("Ingrese cantidad: "))
    return cantidad

def cargar(arr_productos,arr_cantidad):
    cantidad = ingresar_cantidad()
    while cantidad != 0:
        arr_cantidad.append(cantidad)
        producto = ingresar_producto()
        arr_productos.append(producto)
        cantidad = ingresar_cantidad()

def calcular_maximo (arr_productos,arr_cantidad):
    indiceMayor = 0
    for i in range (len(arr_cantidad)):
        if arr_cantidad[i] > arr_cantidad[indiceMayor]:
            indiceMayor = i
    return indiceMayor

def intercambiar(arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar (arr1,arr2):
    for i in range (len(arr1)):
        for j in range (len(arr2)):
            if arr2[i] < arr2[j]:
                intercambiar(arr1,i,j)
                intercambiar(arr2,i,j)

def mostrar (arr1,arr2):
    for i in range (len(arr1)):
        print(arr1[i],arr2[i])

productos = []
cantidad = []

cargar(productos,cantidad)

if len(productos) > 0:
    productoMaximo = calcular_maximo(productos, cantidad)
    print(f"EL producto que vendio mas por cantidad es: {productos[productoMaximo]}")
    ordenar(productos,cantidad)
    mostrar(productos,cantidad)