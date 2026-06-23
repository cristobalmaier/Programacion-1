"""
Se quieren cargar las ventas de productos de un kiosco. Se debe cargar el nombre
de productos y la cantidad. Se cargan datos hasta que se ingrese un 0 en cantidad.
Los productos se cargan con códigos de tres letras y números, por ejemplo:
 
A01,B03. Se deben utilizar 2 arreglos para guardar la información.
 
Se pide:

a.Escribir una función que calcule el máximo producto vendido en cantidad y muestre su código.

b.Ordenar de menor a mayor los productos y las cantidades, imprimir la información de ambos arreglos.
"""

def ingresar_nombre():
    nombre = input("Ingrese nombre del producto: ")
    while nombre == "":
        nombre = input("Ingrese nombre del producto: ")
    return nombre

def ingresar_cantidad():
    cantidad = int(input("Ingrese la cantidad: "))
    while cantidad < 0:
        cantidad = int(input("Ingrese la cantidad: "))
    return cantidad

def cargar(arr_nombres,arr_cantidades):

    cantidad = ingresar_cantidad()
    while cantidad != 0:
        arr_cantidades.append((cantidad))
        nombre = ingresar_nombre()
        arr_nombres.append(nombre)
        
        cantidad = ingresar_cantidad()

def calcular_producto_mas_vendido(arr_nombres,arr_cantidades):
    indice_mayor = 0
    for i in range (len(arr_cantidades)):
        if arr_cantidades[i] > arr_cantidades[indice_mayor]:
            indice_mayor = i
    return indice_mayor

def intercambiar (arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_nombres,arr_cantidades):
    for i in range (len(arr_cantidades)):
        for j in range (len(arr_cantidades)):
            if arr_cantidades[i] < arr_cantidades[j]:
                intercambiar(arr_nombres,i,j)
                intercambiar(arr_cantidades,i,j)

def mostrar (arr_nombres,arr_cantidades):
    for i in range (len(arr_nombres)):
        print("---------------------------")
        print(f"Nombre: {arr_nombres[i]}")
        print(f"Cantidades: {arr_cantidades[i]}")
        print("---------------------------")

nombres = []
cantidades = []

cargar(nombres,cantidades)

if len(nombres) > 0:
    indice_mayor = calcular_producto_mas_vendido(nombres,cantidades)
    print(f"Producto mas vendido: {nombres[indice_mayor]} | Cantidad: {cantidades[indice_mayor]}")

    ordenar(nombres,cantidades)
    mostrar(nombres,cantidades)