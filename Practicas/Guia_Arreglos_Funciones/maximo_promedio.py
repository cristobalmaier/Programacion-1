# Cargar un arreglo con positivos hasta que se ingrese 0

# Calcular la posicion del valor maximo del arreglo

# Calcular, retornar y mostrar la cantidad de ocurrencias del maximo dentro del arreglo

# Calcular y retornar el promedio del arreglo

# A partir del dato anterior, sumar dicho promedio a los valores maximos

def cargar(arr_numeros):
    num = int(input("Ingrese numero: "))
    while num != 0:
        arr_numeros.append(num)
        num = int(input("Ingrese numero: "))

def calcular_maximo (arr_numeros):
    indiceMayor = 0
    for i in range (len(arr_numeros)):
        if arr_numeros[i] > arr_numeros[indiceMayor]:
            indiceMayor = i
    return indiceMayor

def calcular_ocurrencias (arr_numeros,maximo):
    cont = 0
    for i in range (len(arr_numeros)):
        if arr_numeros[i] == maximo:
            cont += 1
    return cont

def calcular_promedio (arr_numeros):
    acum = 0
    for i in range (len(arr_numeros)):
        acum += arr_numeros[i]
    promedio = acum / len(arr_numeros)
    return promedio

def sumar_promedio_maximo (arr_numeros,maximo,promedio):
    for i in range (len(arr_numeros)):
        if arr_numeros[i] == maximo:
            arr_numeros[i] += promedio
    return arr_numeros

numeros = []

cargar(numeros)

indiceMayor = calcular_maximo(numeros) #INDICE MAYOR
maximo = numeros[indiceMayor] #DEVUELVE EL VALOR DEL INDCIE MAYOR
print(f"Valor maximo: {numeros[indiceMayor]}")

ocurrencias = calcular_ocurrencias(numeros,maximo)
print(f"Cantidad de veces que se repite el valor maximo es: {ocurrencias}")

promedio = calcular_promedio(numeros)
print(f"Promedio del los valores del arreglo es: {promedio}")

Suma_promedio_al_maximo = sumar_promedio_maximo(numeros,maximo,promedio)
print(f"quedaria asi: {Suma_promedio_al_maximo}")