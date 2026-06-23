"""
Se desea generar el registro de los libros más solicitados de una biblioteca.

De cada libro se registra:

Título del libro
Año de publicación
Cantidad de préstamos realizados
Género (Novela, Historia)

Se carga información hasta registrar 50 libros.

Se pide:
    Validar todos los datos con criterios lógicos.
    Crear una función para mostrar todos los datos cargados.
    Crear una función que calcule y retorne el porcentaje de libros del género Historia con más de 20 préstamos y publicados antes del año 2000.
    Ordenar de mayor a menor según la cantidad de préstamos realizados.
    Reemplazar aquellos libros cuya cantidad de préstamos sea igual a 0 por:
        "X" en los arreglos de texto.
        -1 en los arreglos numéricos.
    Crear una función que determine el libro con mayor cantidad de préstamos y mostrar toda su información.
    Ingresar un año por teclado y eliminar toda la información de los libros publicados en ese año.
"""

def ingresar_nombre():
    nombre = input("Ingrese titulo del libro: ")
    while nombre == "":
        nombre = input("Ingrese titulo del libro: ")
    return nombre

def ingresar_año_publicacion():
    año = int(input("Ingrese año de publicacion: "))
    while año < 0:
        año = int(input("Ingrese año de publicacion: "))
    return año

def ingresar_cantidad_prestamos():
    cantidad_prestamos = int(input("Ingrese la cantidad de prestamos: "))
    while cantidad_prestamos < 0 :
        cantidad_prestamos = int(input("Ingrese la cantidad de prestamos: "))
    return cantidad_prestamos

def ingresar_genero():
    genero = input("Ingrese genero (Novela o Historia): ")
    while genero != "Novela" and genero != "Historia":
        genero = input("Ingrese genero (Novela o Historia): ")
    return genero

def verificar_carga(arr_libros):
    acumulador = 0
    for i in range (len(arr_libros)):
        if arr_libros[i] != "":
            acumulador += 1
    return acumulador

def cargar (arr_libros, arr_año_publicacion,arr_cantidad_prestamos,arr_generos):
    
    while verificar_carga(arr_libros) < 50:
        nombre = ingresar_nombre()
        arr_libros.append(nombre)
        año = ingresar_año_publicacion()
        arr_año_publicacion.append(año)
        cantidad_prestamos = ingresar_cantidad_prestamos()
        arr_cantidad_prestamos.append(cantidad_prestamos)
        genero = ingresar_genero()
        arr_generos.append(genero)

def mostrar (arr_libros,arr_año_publicacion,arr_cantidad_prestamos,arr_generos):
    for i in range (len(arr_libros)):
        print(f"Libro: {arr_libros[i]}")
        print(f"Año de publicacion: {arr_año_publicacion[i]}")
        print(f"Cantidad de prestamos: {arr_cantidad_prestamos[i]}")
        print(f"Genero: {arr_generos[i]}")
        print("-------------------")

def calcular_porcentaje_historia(arr_año_publicacion,arr_cantidad_prestamos,arr_generos):
    cont = 0
    for i in range (len(arr_año_publicacion)):
        if arr_generos[i] == "Historia" and arr_año_publicacion[i] < 2000 and arr_cantidad_prestamos[i] > 20:
            cont += 1
    porcentaje = (cont / len(arr_año_publicacion)) * 100
    return porcentaje

def intercambiar (arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_libros,arr_año_publicacion,arr_cantidad_prestamos,arr_generos):
    for i in range (len(arr_cantidad_prestamos)):
        for j in range (len(arr_cantidad_prestamos)):
            if arr_cantidad_prestamos[i] > arr_cantidad_prestamos[j]:
                intercambiar(arr_libros,i,j)
                intercambiar(arr_año_publicacion,i,j)
                intercambiar(arr_cantidad_prestamos,i,j)
                intercambiar(arr_generos,i,j) 

def reemplazar_libros (arr_libros,arr_año_publicacion,arr_cantidad_prestamos,arr_generos):
    for i in range (len(arr_cantidad_prestamos)):
        if arr_cantidad_prestamos[i] == 0:
            arr_libros[i] = "X"
            arr_año_publicacion[i] = -1
            arr_cantidad_prestamos[i] = -1
            arr_generos [i] = "X"
        else:
            print(f"el libro {arr_libros[i]} tiene prestamos realizados")

def calcular_libro_mayor_prestamos(arr_libros,arr_año_publicacion,arr_cantidad_prestamos,arr_generos):
    indiceMayor = 0
    for i in range (len(arr_cantidad_prestamos)):
        if arr_cantidad_prestamos[i] > arr_cantidad_prestamos[indiceMayor]:
            indiceMayor = i
    return indiceMayor

def buscar_elemento(arr_libros,arr_año_publicacion,arr_cantidad_prestamos,arr_generos,dato_a_buscar):
    i = 0
    while i < len(arr_año_publicacion) and arr_año_publicacion[i] != dato_a_buscar:
        i += 1
    return i

libros = []
años_publicacion = []
cantidad_prestamos = []
generos = []

cargar(libros,años_publicacion,cantidad_prestamos,generos)

if len (libros) > 0:
    print("---- Mostrando ----")
    mostrar(libros,años_publicacion,cantidad_prestamos,generos)
    porcentaje = calcular_porcentaje_historia(años_publicacion,cantidad_prestamos,generos)
    print(f"Hay un {porcentaje:.2f}% de libros del género Historia con más de 20 préstamos y publicados antes del año 2000")
    ordenar(libros,años_publicacion,cantidad_prestamos,generos)
    print("---- Mostrando por mayor cantidad de prestamos ----")
    mostrar(libros,años_publicacion,cantidad_prestamos,generos)

    indice_mayor = calcular_libro_mayor_prestamos(libros,años_publicacion,cantidad_prestamos,generos)
    print(f"El libro {libros[indice_mayor]} tiene {cantidad_prestamos[indice_mayor]} la mayor cantidad de prestamos, {años_publicacion[indice_mayor]} | {generos[indice_mayor]}")

    buscar = int(input("Ingrese el libro del año a buscar: "))
    indice = buscar_elemento(libros,años_publicacion,cantidad_prestamos,generos,buscar)

    while indice < len(años_publicacion):
        print("Libro encontrado")
        print("Procediendo a eliminar la informacion del libro")
        
        libros.pop(indice)
        años_publicacion.pop(indice)
        cantidad_prestamos.pop(indice)
        generos.pop(indice)

        print("Se elimino exitosamente la informacion")
        mostrar(libros,años_publicacion,cantidad_prestamos,generos)
        indice = buscar_elemento(libros,años_publicacion,cantidad_prestamos,generos,buscar)

    reemplazar_libros(libros,años_publicacion,cantidad_prestamos,generos)
    mostrar(libros,años_publicacion,cantidad_prestamos,generos)
else:
    print("No hay libros cargados")
