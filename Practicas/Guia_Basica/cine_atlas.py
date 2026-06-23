"""
El cine Atlas de Flores decide digitalizar el control de ventas de entradas para las películas infantiles que estarán en cartelera durante las vacaciones de invierno.

Para la venta de las entradas se pide al usuario que ingrese la siguiente información:

    Cantidad de entradas vendidas. (valor entero)
    Nombre de película. (cadena de caracteres)

Se pide:

    Generar un arreglo con las peliculas guardando la cantidad de entradas vendidas en un arreglo paralelo.
    La carga finaliza cuando en cantidad se ingresa un 0.
    En una función calcular y retornar la pelicula que mas vendió.

PLUS: buscar si la pelicula ingresada ya existe en el arreglo, y si es así, acumular la cantidad de entradas para esa pelicula.
"""

def ingresar_entrada():
    cantidad = int(input("Ingrese cantidad de entradas vendidas: "))
    while cantidad < 0:
        cantidad = int(input("Ingrese cantidad de entradas vendidas: "))
    return cantidad

def ingresar_pelicula():
    pelicula = input("Ingrese nombre de película: ")
    while pelicula == "":
        pelicula = input("Ingrese nombre de película: ")
    return pelicula

def buscar_elemento(arr_peliculas, buscar_elemento):
    i = 0

    while i < len(arr_peliculas) and arr_peliculas[i] != buscar_elemento:
        i += 1

    return i

def cargar(arr_entradas, arr_peliculas):

    cantidad = ingresar_entrada()

    while cantidad != 0:

        pelicula = ingresar_pelicula()

        indice = buscar_elemento(arr_peliculas, pelicula)

        if indice < len(arr_peliculas):
            arr_entradas[indice] += cantidad
        else:
            arr_entradas.append(cantidad)
            arr_peliculas.append(pelicula)

        cantidad = ingresar_entrada()

def calcular_pelicula_mas_vendio(arr_entradas):
    indice_mayor = 0

    for i in range(len(arr_entradas)):
        if arr_entradas[i] > arr_entradas[indice_mayor]:
            indice_mayor = i

    return indice_mayor

entradas = []
peliculas = []

cargar(entradas, peliculas)

if len(entradas) > 0:

    indice_mayor = calcular_pelicula_mas_vendio(entradas)

    print("---- Película con más ventas ----")
    print(f"Película: {peliculas[indice_mayor]}")
    print(f"Entradas vendidas: {entradas[indice_mayor]}")

    buscar = input("Ingrese película a buscar: ")

    indice = buscar_elemento(peliculas, buscar)

    if indice < len(peliculas):
        print("Película encontrada")
        print(f"Película: {peliculas[indice]}")
        print(f"Entradas vendidas: {entradas[indice]}")
    else:
        print("La película no existe en el arreglo")

else:
    print("No se cargaron datos")