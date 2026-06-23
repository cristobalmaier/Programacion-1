"""
Una empresa de telefonía desea registrar los celulares más vendidos del mes.

De cada celular se almacena:

Modelo
Año de lanzamiento
Cantidad de unidades vendidas
Marca (Samsung, Motorola)

Se pide:

1. Validar todos los datos.
2. Cargar 30 celulares.
3.Mostrar todos los datos.
4.Calcular y retornar el porcentaje de celulares Samsung con más de 500 unidades vendidas y lanzados antes de 2020.
5.Ordenar de mayor a menor según las unidades vendidas.
6.Reemplazar los celulares con 0 ventas por:
    "X" en los arreglos de texto.
    -1 en los arreglos numéricos.
7.Determinar el celular con mayor cantidad de ventas y mostrar toda su información.
8.Ingresar un año y eliminar todos los celulares de ese año.
9.Ingresar una marca y mostrar la primera ocurrencia encontrada.
"""

def ingresar_modelo():
    modelo = input("Ingrese modelo: ")
    while modelo == "":
        modelo = input("Ingrese modelo: ")
    return modelo

def ingresar_año():
    año = int(input("Ingrese año: "))
    while año < 1850 or año > 2026:
        año = int(input("Ingrese año: "))
    return año

def ingresar_cantida_vendidas():
    cantidad_vendidas = int(input("Ingrese cantidad vendidas: "))
    while cantidad_vendidas < 0:
        cantidad_vendidas = int(input("Ingrese cantidad vendidas: "))
    return cantidad_vendidas

def ingresar_marca():
    marca = input("Ingrese marca (Samsung o Motorola): ")
    while marca != "Samsung" and marca != "Motorola":
        marca = input("Ingrese marca (Samsung o Motorola): ")
    return marca

def cargar(arr_modelos,arr_años,arr_cantidad_vendidas,arr_marcas):

    cont = 0
    while cont < 30:
        modelo = ingresar_modelo()
        arr_modelos.append(modelo)

        año = ingresar_año()
        arr_años.append(año)

        cantidades_vendidas = ingresar_cantida_vendidas()
        arr_cantidad_vendidas.append(cantidades_vendidas)

        marca = ingresar_marca()
        arr_marcas.append(marca)

        cont += 1

def mostrar(arr_modelos,arr_años,arr_cantidad_vendidas,arr_marcas):
    for i in range (len(arr_marcas)):
        print("--------------------")
        print(f"Modelo: {arr_modelos[i]}")
        print(f"Año Lanzamiento: {arr_años[i]}")
        print(f"Cantidades Vendidas: {arr_cantidad_vendidas[i]}")
        print(f"Marca: {arr_marcas[i]}")
        print("--------------------")

def calcular_samsung(arr_cantidad_vendidas,arr_años):
    cont = 0
    for i in range (len(arr_años)):
        if arr_años[i] < 2020 and arr_cantidad_vendidas[i] > 500:
            cont += 1
    porcentaje = (cont / len(arr_años)) * 100
    return porcentaje

def intercambiar (arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_modelos,arr_años,arr_cantidad_vendidas,arr_marcas):
    for i in range (len(arr_cantidad_vendidas)):
        for j in range (len(arr_cantidad_vendidas)):
            if arr_cantidad_vendidas[i] > arr_cantidad_vendidas[j]:
                intercambiar(arr_modelos,i,j)
                intercambiar(arr_años,i,j)
                intercambiar(arr_cantidad_vendidas,i,j)
                intercambiar(arr_marcas,i,j)

def reemplazar (arr_modelos,arr_años,arr_cantidad_vendidas,arr_marcas):
    for i in range (len(arr_cantidad_vendidas)):
        if arr_cantidad_vendidas[i] == 0:
            arr_modelos[i] = "X"
            arr_años[i] = -1
            arr_cantidad_vendidas[i] = -1
            arr_marcas[i] = "X"

def celular_mas_ventas (arr_modelos,arr_años,arr_cantidad_vendidas,arr_marcas):
    indice_mayor = 0
    for i in range (len(arr_cantidad_vendidas)):
        if arr_cantidad_vendidas[i] > arr_cantidad_vendidas[indice_mayor]:
            indice_mayor = i
    return indice_mayor

def buscar_por_año(arr_años,buscar):
    i = 0
    while i < len(arr_años) and arr_años[i] != buscar:
        i += 1
    return i

def buscar_por_marca(arr_marcas,buscar):
    i = 0
    while i < len(arr_marcas) and arr_marcas[i] != buscar:
        i += 1
    return i

modelos = []
años = []
cantidades_vendidas = []
marcas = []

cargar(modelos,años,cantidades_vendidas,marcas)

if len(modelos) > 0:
    mostrar(modelos,años,cantidades_vendidas,marcas)
    porcentaje = calcular_samsung(cantidades_vendidas,años)
    print(f"Hay un {porcentaje}% de celulares Samsung con más de 500 unidades vendidas y lanzados antes de 2020")

    ordenar(modelos,años,cantidades_vendidas,marcas)
    print("----- Mostrando Ordenado -----")
    mostrar(modelos,años,cantidades_vendidas,marcas)
    print("----- Mostrando Ordenado -----")

    reemplazar(modelos,años,cantidades_vendidas,marcas)
    print("---- Mostrando con reemplazo ----")
    mostrar(modelos,años,cantidades_vendidas,marcas)
    print("---- Mostrando con reemplazo ----")

    indice_mayor = celular_mas_ventas(modelos,años,cantidades_vendidas,marcas)
    print(f"Modelo: {modelos[indice_mayor]}")
    print(f"Año: {años[indice_mayor]}")
    print(f"Cantidades Vendidas: {cantidades_vendidas[indice_mayor]}")
    print(f"Marca: {marcas[indice_mayor]}")

    buscar_año = int(input("Busqueda por año"))
    indice = buscar_por_año(años,buscar_año)

    while indice < len(años):
        print("---- Encontrado ----")
        print("---- Eliminando informacion ----")

        modelos.pop(indice)
        años.pop(indice)
        cantidades_vendidas.pop(indice)
        marcas.pop(indice)

        indice = buscar_por_año(años,buscar_año)

    buscar_marca = input("Busqueda por marca: ")
    indice_2 = buscar_por_marca(marcas,buscar_marca)

    if indice_2 < len(marcas):
        print("---- Encontrado ----")
        print(f"Modelo: {modelos[indice_2]}")
        print(f"Año: {años[indice_2]}")
        print(f"Cantidad Vendidas: {cantidades_vendidas[indice_2x]}")
        print(f"Marca: {marcas[indice_2]}")
    else:
        print("No se encontro")
else:
    print("No hay datos cargados")