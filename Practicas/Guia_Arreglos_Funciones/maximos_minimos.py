"""
Cargar un arreglo de números enteros hasta que se ingrese un 0.

    Calcular y mostrar el valor máximo cargado en el arreglo
    Calcular y mostrar el valor mínimo cargado en el arreglo

"""

def calcular_minimo(arr_numeros):
    indiceMenor = 0
    for i in range (len(arr_numeros)):
        if arr_numeros[i] < arr_numeros[indiceMenor]:
            indiceMenor = i
    return indiceMenor

def calcular_maximo(arr_numeros):
    indiceMayor = 0
    for i in range (len(arr_numeros)):
        if arr_numeros[i] > arr_numeros[indiceMayor]:
            indiceMayor = i
    return indiceMayor

def cargar(arr_numeros):
    num = int(input("Ingrese un numero: "))
    while num != 0:
        arr_numeros.append(num)
        num = int(input("Ingrese un numero: "))

numeros = []

cargar(numeros)
indiceMenor = calcular_minimo(numeros)
print(f"El numero menor del arreglo es: {numeros[indiceMenor]}")
indiceMayor = calcular_maximo(numeros)
print(f"El numero mayor del arreglo es: {numeros[indiceMayor]}")