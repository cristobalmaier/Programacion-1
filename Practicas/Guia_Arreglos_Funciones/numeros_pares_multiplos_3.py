"""
Ingresar valores numéricos enteros hasta cargar un arreglo con los 8 primeros números pares múltiplos de 3.

Mostrarlo.

a. Mostrar los 2 valores más pequeños múltiplos de 6. Si no los hubiese, mostrar una leyenda.

b. Eliminar del arreglo aquellos valores menores a su promedio.

c. Insertar en dicho arreglo después de cada número, su doble
"""

def ingresar_numero():
    numero = int(input("Ingrese un número: "))
    return numero

def cargar(arr):
    while len(arr) < 8:
        numero = ingresar_numero()
        if numero % 2 == 0 and numero % 3 == 0:
            arr.append(numero)

def mostrar(arr):
    for i in range(len(arr)):
        print(arr[i])

def mostrar_multiplos_6(arr):

    if len(arr) < 2:
        print("No hay suficientes valores múltiplos de 6.")
    else:
        indiceMenor = 0

        for i in range(len(arr)):
            if arr[i] < arr[indiceMenor]:
                indiceMenor = i

        indiceSegundoMenor = -1

        for i in range(len(arr)):
            if i != indiceMenor:

                if indiceSegundoMenor == -1:
                    indiceSegundoMenor = i

                elif arr[i] < arr[indiceSegundoMenor]:
                    indiceSegundoMenor = i

        print(f"Los 2 valores más pequeños múltiplos de 6 son: {arr[indiceMenor]} y {arr[indiceSegundoMenor]}")

def eliminar_menores_promedio(arr):

    acum = 0

    for i in range(len(arr)):
        acum += arr[i]

    promedio = acum / len(arr)

    arr_menores = []

    for i in range(len(arr)):
        if arr[i] < promedio:
            arr_menores.append(arr[i])

    for i in range(len(arr_menores)):
        arr.remove(arr_menores[i])

def insertar_doble(arr):

    i = 0

    while i < len(arr):
        arr.insert(i + 1, arr[i] * 2)
        i += 2

# Programa principal

numeros = []

cargar(numeros)

if len (numeros) > 0:
    print("Arreglo original:")
    mostrar(numeros)

    mostrar_multiplos_6(numeros)

    eliminar_menores_promedio(numeros)

    print("Arreglo luego de eliminar los menores al promedio:")
    mostrar(numeros)

    insertar_doble(numeros)

    print("Arreglo final con los dobles insertados:")
    mostrar(numeros)
else:
    print("No se ingresaron números válidos.")