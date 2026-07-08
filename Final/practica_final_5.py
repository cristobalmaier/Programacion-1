"""
1. Carga de Datos y Validación
Implementar la carga de datos en arreglos paralelos. El ingreso de datos finalizará cuando en el campo Monto pagado se ingrese el valor -1.

Por cada vehículo, se deberán solicitar y validar los siguientes datos:

Tipo de vehículo: Debe ser estrictamente "AUTO", "MOTO" o "CAMIONETA".

Tiempo de estadía (en horas): Debe ser un valor entero entre 1 y 8.

Monto pagado: No puede ser un valor negativo (a excepción del -1 que actúa como condición de corte).

Número de sector de cochera: Debe ser un valor entero entre 1 y 5.

2. Función de Visualización Individual
Crear una función que reciba como parámetro una posición (índice) y todos los arreglos cargados, y muestre por pantalla de forma ordenada todos los datos relacionados a ese vehículo en particular.

3. Búsqueda por Sector de Cochera
Crear e invocar una función de búsqueda. Una vez finalizada la carga del Punto 1, el sistema debe solicitar al usuario el ingreso de un número de sector por consola.

La función debe buscar dicho sector y retornar la posición del primer vehículo encontrado (o el largo si no existe).

Posteriormente, se deben mostrar todos los datos de ese vehículo utilizando la función del Punto 2 (validando con el if que el índice sea correcto y pasando indice en vez de la variable buscada).

4. Vehículo con Mayor Tiempo de Estadía
Crear e invocar una función que identifique el vehículo que se quedó la mayor cantidad de horas.

La función debe retornar la posición de dicho vehículo.

Luego, se deben mostrar todos sus datos en pantalla utilizando la función del Punto 2.

5. Función de Visualización de Arreglos
Crear una función genérica (mostrar_array) que, dado un arreglo pasado por parámetro, recorra con un bucle y muestre todos sus valores uno abajo del otro de manera limpia.

6. Cálculo de Promedio
Crear e invocar una función que calcule y retorne el promedio de horas de estadía de todos los vehículos registrados.

7. Filtrado de Sectores (Superior al Promedio)
Crear e invocar una función que genere y devuelva un nuevo arreglo. En este se deben almacenar únicamente los números de sector de aquellos vehículos cuyo tiempo de estadía sea estrictamente superior al promedio calculado en el Punto 6 (guardando solo arr[i]).

8. Ordenamiento Descendente
Crear e invocar una función para ordenar todos los datos cargados de manera descendente (de mayor a menor) tomando como criterio el Monto pagado.

Nota: Mantener la correspondencia de los arreglos paralelos utilizando tu método de memoria de doble bucle desde 0 (invirtiendo las variables en el if).

Una vez ordenados, mostrar el contenido de todos los arreglos utilizando la función del Punto 5 (¡nada de usar print(arreglo) directo!).
"""

def ingresar_tipo_vehiculo():
    vehiculo = input("Seleccione tipo de vehiculo (AUTO, MOTO, CAMIONETA): ")
    while vehiculo != "AUTO" and vehiculo != "MOTO" and vehiculo != "CAMIONETA":
        vehiculo = input("Seleccione tipo de vehiculo (AUTO, MOTO, CAMIONETA): ")
    return vehiculo

def ingresar_estadia():
    estadia = int(input("Ingrese tiempo de estadoia (horas): "))
    while estadia < 1 or estadia > 8:
        estadia = int(input("Ingrese tiempo de estadoia (horas): "))
    return estadia

def ingresar_monto():
    monto = int(input("Ingrese monto a pagar: "))
    while monto < 0 and monto != -1:
        monto = int(input("Ingrese monto a pagar: "))
    return monto

def ingresar_cochera():
    cochera = int(input("Ingrese el numero de cochera: "))
    while cochera < 1 or cochera > 5:
        cochera = int(input("Ingrese el numero de cochera: "))
    return cochera

def mostrar(arr_vehiculos,arr_estadias,arr_montos,arr_cochera,posicion):
    print("-- MOSTRAR --")
    print(f"TIPO DE VEHICLO: {arr_vehiculos[posicion]}")
    print(f"TIEMPO DE ESTADIA: {arr_estadias[posicion]}")
    print(f"MONTOS: {arr_montos[posicion]}")
    print(f"NUMERO DE COCHERA: {arr_cochera[posicion]}")

def buscar_por_cochera(arr_cochera,cochera_a_buscar):
    i = 0
    while i < len(arr_cochera) and arr_cochera[i] != cochera_a_buscar:
        i += 1
    return i

def vehiculo_mayor_estadia(arr_estadias):
    posicion_mayor = 0
    for i in range (len(arr_estadias)):
        if arr_estadias[i] > arr_estadias[posicion_mayor]:
            posicion_mayor = i
    return posicion_mayor

def mostrar_array(arr):
    for i in range (len(arr)):
        print(f"{arr[i]}")

def calcular_promedio(arr_estadias):
    acum = 0
    for i in range (len(arr_estadias)):
        acum += arr_estadias[i]
    promedio = acum / len(arr_estadias)
    return promedio

def filtro_sectores(arr_estadias,arr_cochera):
    nuevo_array = []
    promedio = calcular_promedio(arr_estadias)
    for i in range(len(arr_estadias)):
        if arr_estadias[i] > promedio:
            nuevo_array.append(arr_cochera[i])
    return nuevo_array

def intercambiar(arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_vehiculos,arr_estadias,arr_montos,arr_cochera):
    for i in range (len(arr_montos)):
        for j in range (len(arr_montos)):
            if arr_montos[i] > arr_montos[j]:
                intercambiar(arr_vehiculos,i,j)
                intercambiar(arr_estadias,i,j)
                intercambiar(arr_montos,i,j)
                intercambiar(arr_cochera,i,j)

def cargar(arr_vehiculos,arr_estadias,arr_montos,arr_cochera):
    monto = ingresar_monto()
    while monto != -1:
        vehiculo = ingresar_tipo_vehiculo()
        arr_vehiculos.append(vehiculo)

        estadia = ingresar_estadia()
        arr_estadias.append(estadia)

        cochera = ingresar_cochera()
        arr_cochera.append(cochera)

        arr_montos.append(monto)
        monto = ingresar_monto()

tipos_vehiculos = []
tiempo_estadias = []
numeros_cochers = []
montos = []

cargar(tipos_vehiculos,tiempo_estadias,numeros_cochers,montos)

if len(tipos_vehiculos) > 0:
    posicion = int(input("Ingrese una posicion para ver sus datos: "))
    while posicion < 0 or posicion >= len(tipos_vehiculos):
        posicion = int(input("Ingrese una posicion para ver sus datos: "))
    mostrar(tipos_vehiculos,tiempo_estadias,numeros_cochers,montos,posicion)

    numero_cochera_buscar = int(input("Ingrese numero de cochera a buscar: "))
    while numero_cochera_buscar < 1 or numero_cochera_buscar > 5:
        numero_cochera_buscar = int(input("Ingrese numero de cochera a buscar: "))
    indice = buscar_por_cochera(numeros_cochers,numero_cochera_buscar)
    if indice < len(numero_cochera_buscar):
        mostrar(tipos_vehiculos,tiempo_estadias,numeros_cochers,montos,indice)
    else:
        print("NO EXISTE ESE NUMERO DE COCHERA")
        
    posicion_mayor = vehiculo_mayor_estadia(tiempo_estadias)
    print("-- DATOS DEL AUTO CON MAYOR ESTADIA --")
    mostrar(tipos_vehiculos,tiempo_estadias,numeros_cochers,montos,posicion_mayor)

    print("TIPOS VEHICULOS")
    mostrar_array(tipos_vehiculos)
    print("TIEMPO ESTADIAS")
    mostrar_array(tiempo_estadias)
    print("NUMEROS DE COCHERAS")
    mostrar_array(numeros_cochers)
    print("MONTOS A PAGAR")
    mostrar_array(montos)

    promedio = calcular_promedio(tiempo_estadias)
    print(f"EL PROMEDIO DE TIEMPO DE ESTADIA ES: {promedio}")

    nuevo_array = filtro_sectores(tiempo_estadias,numeros_cochers)
    print("LOS NUMEROS DE COCHERAS QUE SUPERAN EL TIEMPO DE ESTADIA PROMEDIO SON: ")
    mostrar_array(nuevo_array)

    ordenar(tipos_vehiculos,tiempo_estadias,numeros_cochers,montos)
    print("TIPOS VEHICULOS")
    mostrar_array(tipos_vehiculos)
    print("TIEMPO ESTADIAS")
    mostrar_array(tiempo_estadias)
    print("NUMEROS DE COCHERAS")
    mostrar_array(numeros_cochers)
    print("MONTOS A PAGAR")
    mostrar_array(montos)

else:
    print("NO HAY DATOS CARGADOS")
