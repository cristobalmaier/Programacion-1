"""
 Se quiere generar el registro de los vinos premiados de una prestigiosa bodega, para lo cual se registra la siguiente información:

    Nombre del vino
    Año de cosecha
    Cantidad de menciones
    Viñedo (Mendoza, Salta)

Se carga información hasta que se registren 50 vinos.

Se pide:

    Validar los datos con criterios lógicos
    Crear una función para mostrar los datos
    Crear una función para calcular y retornar el porcentaje de vinos originarios de Salta con mas de 5 menciones y año de cosecha menor a 1998.
    Ordenar de mayor a menor según la cantidad de menciones
    Reemplazar aquellos vinos que tengan una cantidad de menciones igual a 1, por "X" y -1 en los arreglos que correspondan.
    Calcular utilizando una función el vino que tiene la máxima cantidad de menciones y luego mostrar toda la información asociada.
    Ingresar un año por teclado y eliminar toda la información de los vinos cuya cosecha fue ese año.
"""

def ingresar_nombre():
    nombre = input("Ingrese nombre del vino: ")
    while nombre == "":
        nombre = input("Ingrese nombre del vino: ")
    return nombre

def ingresar_año():
    año = int(input("Ingrese año de cosecha: "))
    while año < 0:
        año = int(input("Ingrese año de cosecha: "))
    return año

def ingresar_cantidad_menciones():
    menciones = int(input("Cantidad de menciones: "))
    while menciones < 0:
        menciones = int(input("Cantidad de menciones: "))
    return menciones

def ingresar_viñedo():
    viñedo = input("Ingrese viñedo: ")
    while viñedo != "Salta" and viñedo != "Mendoza":
        viñedo = input("Ingrese viñedo: ")
    return viñedo

def cargar (arr_vinos,arr_años_cosechas,arr_menciones,arr_viñedos):
    cont = 0
    while cont != 50:  
        nombre = ingresar_nombre()
        arr_vinos.append(nombre)
        año_cosecha = ingresar_año()
        arr_años_cosechas.append(año_cosecha)
        menciones = ingresar_cantidad_menciones()
        arr_menciones.append(menciones)
        viñedo = ingresar_viñedo()
        arr_viñedos.append(viñedo)

        cont += 1

def mostrar(arr_vinos,arr_años_cosechas,arr_menciones,arr_viñedos):
    for i in range (len(arr_vinos)):
        print("--- Mostrando ---")
        print(f"Vino: {arr_vinos[i]}")
        print(f"Años de cosecha: {arr_años_cosechas[i]}")
        print(f"Cantidad de menciones: {arr_menciones[i]}")
        print(f"Viñedo: {arr_viñedos[i]}")

def calcular_porcentaje_vinos_salta (arr_vinos,arr_años_cosechas,arr_menciones,arr_viñedos):
    cont = 0

    for i in range (len(arr_vinos)):
        if arr_viñedos[i] == "Salta" and arr_menciones[i] > 5 and arr_años_cosechas[i] < 1998:
            cont += 1
    
    porcentaje = (cont / len(arr_vinos)) * 100
    return porcentaje

def intercambiar(arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_vinos,arr_años_cosechas,arr_menciones,arr_viñedos):
    for i in range (len(arr_menciones)):
        for j in range (len(arr_menciones)):
            if arr_menciones[i] > arr_menciones[j]:
                intercambiar(arr_vinos,i,j)
                intercambiar(arr_años_cosechas,i,j)
                intercambiar(arr_menciones,i,j)
                intercambiar(arr_viñedos,i,j)

def reemplazar_mencion(arr_vinos,arr_años_cosechas,arr_menciones,arr_viñedos):
    for i in range (len(arr_menciones)):
        if arr_menciones[i] == 1:
            arr_vinos[i] = "X"
            arr_viñedos[i] = "X"
            arr_años_cosechas[i] = -1
            arr_menciones[i] = -1

def calcular_vino_mayor_menciones (arr_vinos,arr_años_cosechas,arr_menciones,arr_viñedos):
    indice_mayor = 0
    for i in range (len(arr_menciones)):
        if arr_menciones[i] > arr_menciones[indice_mayor]:
            indice_mayor = i
    return indice_mayor

def buscar_elemento_eliminar(arr_años_cosechas,buscarElemento):
    i = 0
    while i < len(arr_años_cosechas) and arr_años_cosechas[i] != buscarElemento:
        i += 1
    return i

vinos = []
años_cosechas = []
menciones = []
viñedos = []

cargar(vinos,años_cosechas,menciones,viñedos)

if len(vinos) > 0:
    
    mostrar(vinos,años_cosechas,menciones,viñedos)
    VinosSalta = calcular_porcentaje_vinos_salta (vinos,años_cosechas,menciones,viñedos)
    print(f"{VinosSalta}% de vinos originarios de Salta con mas de 5 menciones y año de cosecha menor a 1998")
    ordenar(vinos,años_cosechas,menciones,viñedos)
    print("---- Ordenados por mayor cantidad de Menciones ----")
    mostrar(vinos,años_cosechas,menciones,viñedos)
    reemplazar_mencion(vinos,años_cosechas,menciones,viñedos)
    print("---- Reemplazando los que tiene 1 mencion ----")
    mostrar(vinos,años_cosechas,menciones,viñedos)
    indiceMayor = calcular_vino_mayor_menciones(vinos,años_cosechas,menciones,viñedos)
    print(f"Mayor cantidad de menciones: {menciones[indiceMayor]}")
    print(f"Vino: {vinos[indiceMayor]}")
    print(f"Año de cosecha: {años_cosechas[indiceMayor]}")
    print(f"Viñedo: {viñedos[indiceMayor]}")

    buscar = int(input("Ingrese año para eliminar producto: "))
    indice = buscar_elemento_eliminar(años_cosechas,buscar)

    if indice == len(años_cosechas):
        print("No existe un vino con ese año")
    else:

        while indice < len(años_cosechas):

            vinos.pop(indice)
            años_cosechas.pop(indice)
            menciones.pop(indice)
            viñedos.pop(indice)

            indice = buscar_elemento_eliminar(años_cosechas,buscar)

        print("Información eliminada")
        mostrar(vinos,años_cosechas,menciones,viñedos)
else:
    print("No se cargaron vinos")