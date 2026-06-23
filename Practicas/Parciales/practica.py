"""
Se desea realizar un sistema para la gestión de películas disponibles en una plataforma de streaming. Para ello, se
cargará la siguiente información de cada película:
    ● ID de referencia
    ● Género de la película (Ej: ACCIÓN, COMEDIA, DRAMA, etc.)
    ● Duración en minutos
Se pide:
    a) Mostrar el total de minutos de duración acumulados por cada género.
    (Ej.: Las películas de acción tienen un total de X minutos).
    b) Buscar la película que tiene como ID de referencia “107”. Si existe, informar todos sus datos.
    c) Mostrar los datos de la película con menor duración.
    d) Insertar una nueva película en la posición anterior a la película con menor duración, con los siguientes datos:
        ● ID de referencia: 200
        ● Género: "ACCIÓN"
        ● Duración: 125 minutos
    e) Ordenar todas las películas por duración (de menor a mayor) y mostrar todos los arreglos.
"""

def ingresar_id():
    id_referencia = int(input("Ingrese id: "))
    while id_referencia < 0:
        id_referencia = int(input("Ingrese id: "))
    return id_referencia
    
def ingresar_genero():
    genero = input("Ingrese genero (accion, comedia, drama): ")
    while genero != "accion" and genero != "comedia" and genero != "drama":
        genero = input("Ingrese genero (accion, comedia, drama): ")
    return genero

def ingresar_duracion():
    duracion = int(input("Ingrese duracion: "))
    while duracion < 0:
        duracion = int(input("Ingrese duracion: "))
    return duracion

def calcular_total_minutos_accion(arr_generos,arr_duracion):
    acum = 0
    for i in range (len(arr_duracion)):
        if arr_generos[i] == "accion":
            acum += arr_duracion[i]
    return acum

def calcular_total_minutos_comedia(arr_generos,arr_duracion):
    acum = 0
    for i in range (len(arr_duracion)):
        if arr_generos[i] == "comedia":
            acum += arr_duracion[i]
    return acum

def calcular_total_minutos_drama(arr_generos,arr_duracion):
    acum = 0
    for i in range (len(arr_duracion)):
        if arr_generos[i] == "drama":
            acum += arr_duracion[i]
    return acum

def buscar(arr_ids,arr_generos,arr_duracion,buscar_elemento):
    i = 0
    while i < len(arr_ids) and arr_ids[i] != buscar_elemento:
        i += 1
    return i

def calcular_pelicula_con_menor_duracion(arr_ids,arr_duracion,arr_generos):
    indice_menor = 0
    for i in range (len(arr_duracion)):
        if arr_duracion[i] < arr_duracion[indice_menor]:
            indice_menor = i
    return indice_menor

def intercambiar(arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def mostrar(arr_ids,arr_generos,arr_duracion):
    for i in range (len(arr_ids)):
        print("---- Mostrando datos de la pelicula ----")
        print(f"ID: {arr_ids[i]}")
        print(f"Genero: {arr_generos[i]}")
        print(f"Duracion: {arr_duracion[i]}")
        print("----------------------------------------")

def ordenar(arr_ids,arr_generos,arr_duracion):
    for i in range (len(arr_duracion)):
        for j in range (len(arr_duracion)):
            if arr_duracion[i] < arr_duracion[j]:
                intercambiar(arr_ids,i,j)
                intercambiar(arr_generos,i,j)
                intercambiar(arr_duracion,i,j)
    
def cargar(arr_ids,arr_generos,arr_duracion):

    id_referencia = ingresar_id()
    while id_referencia != 0:
    
        arr_ids.append(id_referencia)

        genero = ingresar_genero()
        arr_generos.append(genero)

        duracion = ingresar_duracion()
        arr_duracion.append(duracion)

        id_referencia = ingresar_id()

def insertar(arr_ids,arr_generos,arr_duracion,indice):
    arr_ids.insert(indice,200)
    arr_generos.insert(indice,"accion")
    arr_duracion.insert(indice,125)

ids = []
generos = []
duracion = []

cargar(ids,generos,duracion)

if len(ids) > 0:

    total_minutos_accion = calcular_total_minutos_accion(generos,duracion)
    print(f"Total minutos Genero Accion: {total_minutos_accion}")
    total_minutos_comedia = calcular_total_minutos_comedia(generos,duracion)
    print(f"Total minutos Genero Comedia: {total_minutos_comedia}")
    total_minutos_drama = calcular_total_minutos_drama(generos,duracion)
    print(f"Total minutos Genero Drama: {total_minutos_drama}")

    elemento_a_buscar = int(input("Ingrese ID a buscar: "))
    indice = buscar(ids,generos,duracion,elemento_a_buscar)

    if indice < len(ids):
        print("Id encontrado")
        print("---- Mostrando datos del id buscado ----")
        print(f"ID: {ids[indice]}")
        print(f"Genero: {generos[indice]}")
        print(f"Duracion: {duracion[indice]}")
        print("----------------------------------------")
    else:
        print("El id buscado no existe en la base de datos")
    
    indice_menor = calcular_pelicula_con_menor_duracion(ids,duracion,generos)
    
    print(f"La pelicula con el ID: {ids[indice_menor]}, tiene la menor duracion con {duracion[indice_menor]} minutos, con el genero {generos[indice_menor]}")
    
    insertar(ids,generos,duracion,indice_menor)

    ordenar(ids,generos,duracion)
    mostrar(ids,generos,duracion)
else:
    print("No se han cargado peliculas en la base de datos")