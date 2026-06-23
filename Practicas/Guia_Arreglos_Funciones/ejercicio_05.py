"""
Cargar dos arreglos paralelos, el nombre y el peso de 10 personas mayores de edad
(18 años)

a. Escribir una función que permita calcular el peso promedio de las personas
e indicar cuántas están por debajo de ese promedio. Mostrar solo los nombres.

b. Mostrar el o los nombres de aquellas personas cuyo peso es el mayor.

c. Ingresar un nombre por teclado y mostrar el peso de esa persona. Si no se
encuentra, mostrar una leyenda.
"""

def peso_promedio(arr_peso):
    acumPeso = 0

    for i in range(len(arr_peso)):
        acumPeso += arr_peso[i]

    promedio = acumPeso / len(arr_peso)
    return promedio

def personas_abajo_promedio(arr_nombres, arr_peso, promedio):
    contador = 0
    print("Personas por debajo del promedio:")

    for i in range(len(arr_peso)):
        if arr_peso[i] < promedio:
            print(arr_nombres[i])
            contador += 1
    return contador

def persona_mayor_peso(arr_peso):
    indiceMayor = 0
    for i in range(len(arr_peso)):
        if arr_peso[i] > arr_peso[indiceMayor]:
            indiceMayor = i

    return indiceMayor

def buscar_elemento(arr_nombres, buscar_dato):
    i = 0
    while i < len(arr_nombres) and arr_nombres[i] != buscar_dato:
        i += 1
    return i


# Programa Principal

nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis","Sofia", "Carlos", "Lucia", "Jorge", "Marta"]

pesos = [70, 60, 80, 55, 90,65, 75, 60, 90, 70]

if len(nombres) > 0:

    # Punto A
    promedio = peso_promedio(pesos)

    print(f"Peso promedio: {promedio}")

    cantidad = personas_abajo_promedio(nombres, pesos,promedio)

    print(f"Cantidad debajo del promedio: {cantidad}")

    # Punto B
    indiceMayor = persona_mayor_peso(pesos)
    mayorPeso = pesos[indiceMayor]

    print("\nPersonas con el mayor peso:")

    for i in range(len(pesos)):
        if pesos[i] == mayorPeso:
            print(nombres[i])

    # Punto C
    buscar = input("\nIngrese un nombre a buscar: ")

    posicion = buscar_elemento(nombres, buscar)

    if posicion < len(nombres):
        print(f"El peso de {buscar} es {pesos[posicion]} kg")
    else:
        print("Nombre no encontrado")