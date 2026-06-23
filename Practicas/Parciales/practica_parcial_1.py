"""
Le encargan un sistema para llevar el control de las estaciones de trabajo de una empresa.
"""

def ingresar_id():
    numID = input("Ingrese ID: ")
    return numID

def ingresar_procesador():
    procesador = input("Ingrese procesador (AMD o INTEL o FIN): ")
    while procesador != "AMD" and procesador != "INTEL" and procesador != "FIN":
        procesador = input("ERROR! Ingrese procesador (AMD o INTEL o FIN): ")
    return procesador

def ingresar_espacio_total():
    espacio = float(input("Ingrese espacio TOTAL (mb): "))
    while espacio <= 0 or espacio > 2000:
        espacio = float(input("ERROR! Ingrese espacio TOTAL (mb): "))
    return espacio

def ingresar_espacio_utilizado(espacio_total):
    espacio_utilizado = float(input("Ingrese espacio utilizado (mb): "))
    while espacio_utilizado < 0 or espacio_utilizado > espacio_total:
        espacio_utilizado = float(input("ERROR! Ingrese espacio utilizado (mb): "))
    return espacio_utilizado

def cargar(arr_id, arr_procesadores, arr_espacioTotal, arr_espacioUtilizado):

    procesador = ingresar_procesador()

    while procesador != "FIN":

        arr_procesadores.append(procesador)

        numID = ingresar_id()
        arr_id.append(numID)

        espacioTotal = ingresar_espacio_total()
        arr_espacioTotal.append(espacioTotal)

        espacioUtilizado = ingresar_espacio_utilizado(espacioTotal)
        arr_espacioUtilizado.append(espacioUtilizado)

        procesador = ingresar_procesador()

def mostrar(arr_id, arr_procesadores, arr_espacioTotal, arr_espacioUtilizado):

    for i in range(len(arr_id)):

        espacioLibre = arr_espacioTotal[i] - arr_espacioUtilizado[i]
        porcentajeLibre = (espacioLibre / arr_espacioTotal[i]) * 100

        print("------------------------")
        print(f"ID: {arr_id[i]}")
        print(f"Procesador: {arr_procesadores[i]}")
        print(f"Espacio Total: {arr_espacioTotal[i]} mb")
        print(f"Espacio Utilizado: {arr_espacioUtilizado[i]} mb")
        print(f"Disponible: {porcentajeLibre:.2f}%")

        if porcentajeLibre < 10:
            print("Se debe eliminar archivos temporales")

def calcular_promedio_amd(arr_procesadores, arr_espacioUtilizado):

    acum = 0
    cont = 0

    for i in range(len(arr_procesadores)):
        if arr_procesadores[i] == "AMD":
            acum += arr_espacioUtilizado[i]
            cont += 1

    if cont > 0:
        return acum / cont

    return 0

def calcular_promedio_intel(arr_procesadores, arr_espacioUtilizado):

    acum = 0
    cont = 0

    for i in range(len(arr_procesadores)):
        if arr_procesadores[i] == "INTEL":
            acum += arr_espacioUtilizado[i]
            cont += 1

    if cont > 0:
        return acum / cont

    return 0

def reemplazar_servidor(arr_id, arr_procesadores, arr_espacioTotal):

    contador = 1

    for i in range(len(arr_id)):

        if arr_procesadores[i] == "INTEL" and arr_espacioTotal[i] == 2000:

            arr_id[i] = f"SERVIDOR_{contador}"
            contador += 1

def calcular_minimo_disponible(arr_espacioTotal, arr_espacioUtilizado):

    indiceMenor = 0

    for i in range(len(arr_espacioTotal)):

        disponibleActual = arr_espacioTotal[i] - arr_espacioUtilizado[i]
        disponibleMenor = arr_espacioTotal[indiceMenor] - arr_espacioUtilizado[indiceMenor]

        if disponibleActual < disponibleMenor:
            indiceMenor = i

    return indiceMenor

def intercambiar(arr, i, j):

    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_id, arr_procesadores, arr_espacioTotal, arr_espacioUtilizado):

    for i in range(len(arr_espacioTotal) - 1):
        for j in range(i + 1, len(arr_espacioTotal)):

            if arr_espacioTotal[i] > arr_espacioTotal[j]:

                intercambiar(arr_id, i, j)
                intercambiar(arr_procesadores, i, j)
                intercambiar(arr_espacioTotal, i, j)
                intercambiar(arr_espacioUtilizado, i, j)

def buscar_id(arr_id, elemento_buscar):

    i = 0

    while i < len(arr_id) and arr_id[i] != elemento_buscar:
        i += 1

    return i

# PROGRAMA PRINCIPAL

ids = []
procesadores = []
espacioTotal = []
espacioUtilizado = []

cargar(ids, procesadores, espacioTotal, espacioUtilizado)

if len(ids) > 0:

    reemplazar_servidor(ids, procesadores, espacioTotal)

    print("ESTACIONES:")
    mostrar(ids, procesadores, espacioTotal, espacioUtilizado)

    promedioAMD = calcular_promedio_amd(procesadores, espacioUtilizado)
    print(f"Promedio espacio utilizado AMD: {promedioAMD:.2f} mb")

    promedioINTEL = calcular_promedio_intel(procesadores, espacioUtilizado)
    print(f"Promedio espacio utilizado INTEL: {promedioINTEL:.2f} mb")

    indiceMenor = calcular_minimo_disponible(espacioTotal, espacioUtilizado)

    print("ESTACION CON MENOR ESPACIO DISPONIBLE")
    print(f"ID: {ids[indiceMenor]}")
    print(f"Disponible: {espacioTotal[indiceMenor] - espacioUtilizado[indiceMenor]} mb")

    buscar = input("Ingrese ID a buscar: ")

    indice = buscar_id(ids, buscar)

    if indice < len(ids):

        print("ID ENCONTRADO")
        print(f"ID: {ids[indice]}")
        print(f"Procesador: {procesadores[indice]}")
        print(f"Espacio Total: {espacioTotal[indice]}")
        print(f"Espacio Utilizado: {espacioUtilizado[indice]}")

        ids.pop(indice)
        procesadores.pop(indice)
        espacioTotal.pop(indice)
        espacioUtilizado.pop(indice)

        print("Registro eliminado.")

    else:
        print("El ID no existe.")

    ordenar(ids, procesadores, espacioTotal, espacioUtilizado)

    print("ORDENADOS POR ESPACIO TOTAL")
    mostrar(ids, procesadores, espacioTotal, espacioUtilizado)

else:
    print("No se cargaron estaciones.")