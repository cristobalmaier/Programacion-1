"""
Se quiere llevar la estadística navideña de rendimiento de los renos, para eso se carga la siguiente información:

    nombre del reno

    cantidad de comida consumida

    cantidad de km que voló con el trineo

La carga finaliza cuando en el nombre de reno se escribe FIN o cuando se alcanzó la cantidad de 12 renos.

    Calcular usando una función el promedio de comida consumida

    Calcular usando una función el maximo de km recorridos y el nombre del reno al que pertenece.

    Ordenar de menor a mayor los nombres de los renos y la cantidad de km recorridos

    Crear una función que dado el nombre de un reno ingresado, retorne la cantidad de kilómetros que ha recorrido.
"""

def ingresar_nombre ():
    nombre = input("Ingresa nombre del reno: ")
    while nombre == "":
        nombre = input("Ingresa nombre del reno: ")
    return nombre

def ingresar_comida():
    comida = int(input("Ingresar cantidad de comida: "))
    while comida < 0:
        comida = int(input("Ingresar cantidad de comida: "))
    return comida

def ingresar_km():
    km = float(input("Ingrese cantidad de km que volo con el trineo: "))
    while km < 0:
        km = float(input("Ingrese cantidad de km que volo con el trineo: "))
    return km

def cargar(arr_nombres,arr_comidas,arr_kms):

    nombre = ingresar_nombre()
    while nombre != "FIN" and len(arr_nombres) < 12:
        arr_nombres.append(nombre)
        cantidad_comida = ingresar_comida()
        arr_comidas.append(cantidad_comida)
        km = ingresar_km()
        arr_kms.append(km)

        nombre = ingresar_nombre()

def promedio_comida (arr_comidas):
    acum = 0
    for i in range (len(arr_comidas)):
        acum += arr_comidas[i]
    promedio = acum / len(arr_comidas)
    return promedio

def calcular_maximo_kms(arr_nombres,arr_kms):
    indice_mayor = 0
    for i in range (len(arr_kms)):
        if arr_kms[i] > arr_kms[indice_mayor]:
            indice_mayor = i
    return indice_mayor

def intercambiar (arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar (arr_nombres,arr_kms):
    for i in range (len(arr_nombres)):
        for j in range (len(arr_nombres)):
            if arr_nombres[i] < arr_nombres[j]:
                intercambiar(arr_nombres,i,j)
                intercambiar(arr_kms,i,j)

def mostrar (arr_nombres,arr_kms):
    for i in range (len(arr_nombres)):
        print(f"Nombre: {arr_nombres[i]}")
        print(f"Kms: {arr_kms[i]}")

def buscar_elemento(arr_nombres,arr_kms,buscar_elemento):
    i = 0
    while i < len(arr_nombres) and arr_nombres[i] != buscar_elemento:
        i += 1
    return i

nombres = []
cantidad_comidas = []
kms = []

cargar (nombres,cantidad_comidas,kms)

if len(nombres) > 0:
    Promedio_comida = promedio_comida(cantidad_comidas)
    print(f"El promedio de comida consumida es: {Promedio_comida}")

    indice_mayor = calcular_maximo_kms(nombres,kms)
    print(f"Maximo kms: {kms[indice_mayor]} | Nombre: {nombres[indice_mayor]}")

    ordenar (nombres,kms)
    mostrar (nombres,kms)

    buscar = input("Ingrese reno a buscar para saber km: ")
    indice = buscar_elemento(nombres,kms,buscar)
    if indice < len(nombres):
        print("---- Reno Encontrado ----")
        print(f"Kms: {kms[indice]}")
    else:
        print("Ese reno no existe")

else:
    print("No hay datos cargados")