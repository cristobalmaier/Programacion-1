"""
1. Ingresar los siguientes datos en arreglos paralelos hasta que el número de reserva sea 0 (cero):

-Número de reserva

-Categoría del libro ("FICCIÓN", "NO FICCIÓN", "INFANTIL")

-Mes de la reserva (valor numérico entre 1 y 12):

-Días de duración de la reserva:

Se debe validar el ingreso correcto de los datos:
    el número de reserva y los días de duración deben ser mayores a cero;
    la categoría debe ser una de las tres mencionadas;
    el mes debe ser un valor entero entre 1 y 12.

2. Crear una función para mostrar todos los datos asociados a una reserva,
recibiendo como parámetro una posición y todos los arreglos correspondientes.

3. Crear e invocar una función que permita buscar una reserva por número. Esta función debe devolver la posición en la que se encuentra.

Una vez finalizada la carga de datos del punto 1, ingresar por consola un número de reserva, invocar la función y luego mostrar los datos correspondientes utilizando la función del punto 2.

4. Crear e invocar una función que permita encontrar la reserva con mayor duración.
Esta función debe devolver la posición. Luego mostrar todos los datos relacionados a la reserva utilizando la función del punto 2.

5. Crear una función que, dado un arreglo, muestre todos los valores del mismo.

6. Crear e invocar una función que devuelva un nuevo arreglo del mismo tamaño que los anteriores.
Este arreglo debe contener "1" en las posiciones donde la duración sea mayor a 15, y "0" en las demás.

(Nota manuscrita sobre el punto 6: "ipos > 15 and > 0")

7. Invocar una función que ordene de forma descendente todas las reservas por mes de reserva. 
Luego, mostrar todos los arreglos paralelos utilizando la función del punto 5.
"""

def ingresar_numero_reserva():
    numero_reserva = int(input("Ingrese numero de reserva: "))
    
    while numero_reserva == "":
        numero_reserva = int(input("Ingrese numero de reserva: "))
    return numero_reserva

def ingresar_categoria_libro():
    categoria_libro = input("Seleccione FICCION, NO_FICCION, INFANTIL: ")
    while categoria_libro != "FICCION" and categoria_libro != "NO_FICCION" and categoria_libro != "INFANTIL":
        categoria_libro = input("Seleccione FICCION, NO_FICCION, INFANTIL: ")
    return categoria_libro

def ingresar_mes_reserva():
    mes_reserva = int(input("Ingrese mes de reserva: "))
    while mes_reserva < 1 or mes_reserva > 12:
        mes_reserva = int(input("Ingrese mes de reserva: "))
    return mes_reserva

def ingresar_dias_duracion_reserva():
    dias_duracion_reserva = int(input("Ingrese dias de duracion de reserva: "))
    while dias_duracion_reserva < 1 or dias_duracion_reserva > 30:
        dias_duracion_reserva = int(input("Ingrese dias de duracion de reserva: "))
    return dias_duracion_reserva

def cargar_datos(arr_numeros_reservas, arr_categorias_libros, arr_meses_reservas, arr_dias_duracion_reservas):
    numero_reserva = ingresar_numero_reserva()
    while numero_reserva != 0:
        categoria_libro = ingresar_categoria_libro()
        mes_reserva = ingresar_mes_reserva()
        dias_duracion_reserva = ingresar_dias_duracion_reserva()

        arr_numeros_reservas.append(numero_reserva)
        arr_categorias_libros.append(categoria_libro)
        arr_meses_reservas.append(mes_reserva)
        arr_dias_duracion_reservas.append(dias_duracion_reserva)

        numero_reserva = ingresar_numero_reserva()

# Funcion para mostrar todos los datos asociados a una reserva

def mostrar_datos_reserva(arr_numeros_reservas, arr_categorias_libros, arr_meses_reservas, arr_dias_duracion_reservas, posicion):
    print(f"Numero de reserva: {arr_numeros_reservas[posicion]}")
    print(f"Categoria de libro: {arr_categorias_libros[posicion]}")
    print(f"Mes de reserva: {arr_meses_reservas[posicion]}")
    print(f"Dias de duracion de reserva: {arr_dias_duracion_reservas[posicion]}")


def buscar_reserva_por_numero(arr_numeros_reservas, numero):
    i = 0
    while i < len(arr_numeros_reservas) and arr_numeros_reservas[i] != numero:
        i += 1
    return i

def buscar_reserva_mayor_duracion(arr_dias_duracion_reservas):
    posicion_mayor = 0
    for i in range(len(arr_dias_duracion_reservas)):
        if arr_dias_duracion_reservas[i] > arr_dias_duracion_reservas[posicion_mayor]:
            posicion_mayor = i
    return posicion_mayor

def mostrar_arreglo(arr):
    for i in range(len(arr)):
        print(arr[i])

def crear_arreglo_duracion_mayor_15(arr_dias_duracion_reservas):
    arr_duracion_mayor_15 = []
    for i in range(len(arr_dias_duracion_reservas)):
        if arr_dias_duracion_reservas[i] > 15:
            arr_duracion_mayor_15.append(1)
        else:
            arr_duracion_mayor_15.append(0)
    return arr_duracion_mayor_15

def intercambiar_elementos(arr, i, j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar_reservas_por_mes(arr_numeros_reservas, arr_categorias_libros, arr_meses_reservas, arr_dias_duracion_reservas):
    for i in range(len(arr_meses_reservas)):
        for j in range(len(arr_meses_reservas)):
            if arr_meses_reservas[i] > arr_meses_reservas[j]:
                intercambiar_elementos(arr_numeros_reservas, i, j)
                intercambiar_elementos(arr_categorias_libros, i, j)
                intercambiar_elementos(arr_meses_reservas, i, j)
                intercambiar_elementos(arr_dias_duracion_reservas, i, j)

numeros_reservas = []
categorias_libros = []
meses_reservas = []
dias_duracion_reservas = []

cargar_datos(numeros_reservas, categorias_libros, meses_reservas, dias_duracion_reservas)

if len(numeros_reservas) > 0:
    print("--- Punto 2 ----")
    posicion = int(input("Ingrese la posicion de la reserva que desea mostrar: "))
    if posicion >= 0 and posicion < len(numeros_reservas):
        mostrar_datos_reserva(numeros_reservas, categorias_libros, meses_reservas, dias_duracion_reservas, posicion)
    else:
        print("Posicion invalida")
    1
    print("--- Punto 3 ----")
    numero = int(input("Ingrese el numero de reserva que desea buscar: "))
    indice = buscar_reserva_por_numero(numeros_reservas, numero)
    if indice < len(numeros_reservas):
        mostrar_datos_reserva(numeros_reservas, categorias_libros, meses_reservas, dias_duracion_reservas, indice)
    else:
        print("No se encontro la reserva con ese numero")
    
    print("--- Punto 4 ----")
    posicion_mayor_duracion = buscar_reserva_mayor_duracion(dias_duracion_reservas)
    mostrar_datos_reserva(numeros_reservas, categorias_libros, meses_reservas, dias_duracion_reservas, posicion_mayor_duracion)

    print("--- Punto 5 ----")
    print("Numeros de reservas: ")
    mostrar_arreglo(numeros_reservas)
    print("Categorias de libros: ")
    mostrar_arreglo(categorias_libros)
    print("Meses de reservas: ")
    mostrar_arreglo(meses_reservas)
    print("Dias de duracion de reservas: ")
    mostrar_arreglo(dias_duracion_reservas)

    print("--- Punto 6 ----")
    arr_duracion_mayor_15 = crear_arreglo_duracion_mayor_15(dias_duracion_reservas)
    print("Arreglo de duracion mayor a 15: ")
    mostrar_arreglo(arr_duracion_mayor_15)

    print("--- Punto 7 ----")
    ordenar_reservas_por_mes(numeros_reservas, categorias_libros, meses_reservas, dias_duracion_reservas)
    print("Numeros de reservas ordenados por mes: ")
    mostrar_arreglo(numeros_reservas)

else:
    print("No se cargaron reservas")