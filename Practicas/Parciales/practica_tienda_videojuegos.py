"""
Una tienda de videojuegos desea registrar los juegos más vendidos del mes.

De cada juego se almacena:

Nombre del juego
Año de lanzamiento
Cantidad de copias vendidas
Plataforma (PC, PlayStation)

La carga finaliza cuando se registran 50 juegos.

Se pide:

a)Validar todos los datos con criterios lógicos.

b)Crear una función para mostrar todos los datos cargados.

c)Crear una función que calcule y retorne el porcentaje de juegos de PC que:
    hayan vendido más de 1000 copias y hayan sido lanzados antes de 2015
d)Ordenar de mayor a menor según la cantidad de copias vendidas.

e)Reemplazar aquellos juegos cuya cantidad de copias vendidas sea igual a 0 por:

    "X" en los arreglos de texto
    -1 en los arreglos numéricos

f)Crear una función que determine el juego con mayor cantidad de copias vendidas y mostrar toda su información.

g)Ingresar un año por teclado y eliminar toda la información de los juegos lanzados en ese año.

h) (Plus) Ingresar un nombre de juego por teclado y mostrar la primera ocurrencia encontrada.
"""


def ingresar_nombre():
    nombre = input("Ingrese nombre: ")
    while nombre == "":
        nombre = input("Ingrese nombre: ")
    return nombre

def ingresar_año():
    año = int(input("Ingrese año de lanzamiento: "))
    while año < 0:
        año = int(input("Ingrese año de lanzamiento: "))
    return año

def ingresar_copias_vendidas():
    copias_vendidas = int(input("Ingrese cantida de copias vendidas: "))
    while copias_vendidas < 0:
        copias_vendidas = int(input("Ingrese cantida de copias vendidas: "))
    return copias_vendidas

def ingresar_plataforma():
    plataforma = input("Ingrese plataforma (Playstation o PC): ")
    while plataforma != "Playstation" and plataforma != "PC":
        plataforma = input("Ingrese plataforma (Playstation o PC): ")
    return plataforma

def cargar(arr_nombres,arr_años,arr_copias_vendidas,arr_plataformas):

    while len(arr_nombres) < 50:

        nombre = ingresar_nombre()
        arr_nombres.append(nombre)

        año_lanzamiento = ingresar_año()
        arr_años.append(año_lanzamiento)

        copias_vendidas = ingresar_copias_vendidas()
        arr_copias_vendidas.append(copias_vendidas)

        plataforma = ingresar_plataforma()
        arr_plataformas.append(plataforma)

def mostrar(arr_nombres,arr_años,arr_copias_vendidas,arr_plataformas):
    for i in range (len(arr_nombres)):
        print("-------------------------------")
        print(f"Nombre: {arr_nombres[i]}")
        print(f"Año de Lanzamiento: {arr_años[i]}")
        print(f"Copias Vendidas: {arr_copias_vendidas[i]}")
        print(f"Plataforma: {arr_plataformas[i]}")
        print("-------------------------------")

def calcuar_porcentaje_juegos_pc(arr_copias_vendidas,arr_años,arr_plataformas):
    cont = 0
    for i in range (len(arr_plataformas)):
        if arr_plataformas[i] == "PC" and arr_años[i] < 2015 and arr_copias_vendidas[i] > 1000:
            cont +=1
    porcentaje = (cont / len(arr_plataformas)) * 100
    return porcentaje

def intercambiar (arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_nombres,arr_años,arr_copias_vendidas,arr_plataformas):
    for i in range (len(arr_copias_vendidas)):
        for j in range (len(arr_copias_vendidas)):
            if arr_copias_vendidas[i] > arr_copias_vendidas[j]:
                intercambiar(arr_nombres,i,j)
                intercambiar(arr_años,i,j)
                intercambiar(arr_copias_vendidas,i,j)
                intercambiar(arr_plataformas,i,j)

def reemplazar(arr_nombres,arr_años,arr_copias_vendidas,arr_plataformas):
    for i in range (len(arr_copias_vendidas)):
        if arr_copias_vendidas[i] == 0:
            arr_nombres[i] = "X"
            arr_años[i] = -1
            arr_copias_vendidas[i] = -1
            arr_plataformas[i] = "X"

def calcular_juego_mas_vendido(arr_nombres,arr_años,arr_copias_vendidas,arr_plataformas):
    indice_mayor = 0
    for i in range (len(arr_copias_vendidas)):
        if arr_copias_vendidas[i] > arr_copias_vendidas[indice_mayor]:
            indice_mayor = i
    return indice_mayor

def buscar_elemento(arr_años,elemento_a_buscar):
    i = 0
    while i < len(arr_años) and arr_años[i] != elemento_a_buscar:
        i += 1
    return i

def buscar_elemento_por_nombre(arr_nombres,elemento_a_buscar):
    i = 0
    while i < len(arr_nombres) and arr_nombres[i] != elemento_a_buscar:
        i += 1
    return i

nombres = []
años_lanzamientos = []
copias_vendidas = []
plataformas = []

cargar(nombres,años_lanzamientos,copias_vendidas,plataformas)

if len (nombres) > 0:
    mostrar(nombres,años_lanzamientos,copias_vendidas,plataformas)

    porcentaje_juegos_pc = calcuar_porcentaje_juegos_pc(copias_vendidas,años_lanzamientos,plataformas)
    print(f"Hay un {porcentaje_juegos_pc}% que hayan vendido más de 1000 copias y hayan sido lanzados antes de 2015")

    ordenar(nombres,años_lanzamientos,copias_vendidas,plataformas)
    print("------ Mostrando Ordenado ------")
    mostrar(nombres,años_lanzamientos,copias_vendidas,plataformas)
    print("------ Mostrando Ordenado ------")


    indice_mayor = calcular_juego_mas_vendido(nombres,años_lanzamientos,copias_vendidas,plataformas)
    print(f"Juego mas vendido: {nombres[indice_mayor]}")
    print(f"Año: {años_lanzamientos[indice_mayor]} ")
    print(f"Copias Vendidas: {copias_vendidas[indice_mayor]}")
    print(f"Plataforma: {plataformas[indice_mayor]}")
    
    reemplazar(nombres,años_lanzamientos,copias_vendidas,plataformas)
    mostrar(nombres,años_lanzamientos,copias_vendidas,plataformas)



    elemento_a_buscar = int(input("Buqueda por año: "))
    indice = buscar_elemento(años_lanzamientos,elemento_a_buscar)

    while indice < len(años_lanzamientos):
        
        print("---- Dato encontrado ----")
        print("---- Eliminando informacion ----")
        nombres.pop(indice)
        años_lanzamientos.pop(indice)
        copias_vendidas.pop(indice)
        plataformas.pop(indice)

        indice = buscar_elemento(años_lanzamientos,elemento_a_buscar)
    

    busqueda_por_nombre = input("Ingrese el nombre del juego a buscar: ")
    indice_2 = buscar_elemento_por_nombre(nombres,busqueda_por_nombre)
    if indice_2 < len(nombres):
        print(f"Nombre: {nombres[indice_2]}")
        print(f"Año de lanzamiento: {años_lanzamientos[indice_2]}")
        print(f"Copias Vendidas: {copias_vendidas[indice_2]}")
        print(f"Plataforma: {plataformas[indice_2]}")
    else:
        print("No existe ese juego")
    
    mostrar(nombres,años_lanzamientos,copias_vendidas,plataformas)

else:
    print("No hay juegos cargados")