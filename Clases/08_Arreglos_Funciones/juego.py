"""
Se quiere llevar el control de preguntas para un nuevo juego. Para lo que se debe generar un sistema que cumpla con las siguientes características.

    Cargar preguntas y sus puntajes (se deben usar arreglos paralelos)
    La carga Finaliza cuando en pregunta se ingresa "FIN" o que la suma de los puntajes ingresados haya llegado a 150.
    El puntaje que corresponde a cada pregunta debe ser mayor 0 y menor o igual a 25.

Se pide:

    Crear una función que determine el mínimo puntaje ingresado y mostrar la pregunta a la que corresponde.
    Crear una función que calcule el puntaje promedio de las preguntas y  retorne la cantidad de preguntas cuyo puntaje superen ese promedio.
    Crear una función que muestre las preguntas y su puntaje
    Ordenar las preguntas de menor a mayor segun su puntaje. Luego mostrar.puntuajes  te amo criss<3"""
    
def ingresar_pregunta():
    pregunta = input("Ingrese la pregunta: ")
    while pregunta == "":
        pregunta = input("Ingrese la pregunta: ")
    return pregunta

def ingresar_puntaje():
    puntaje = int(input("Ingrese el puntaje: "))
    while puntaje <= 0 or puntaje > 25:
        puntaje = int(input("Ingrese el puntaje: "))
    return puntaje

def promedio(arr1):
    acumSuma = 0
    cont = 0
    for i in range (len(arr1)):
        acumSuma += arr1[i]
    prom = acumSuma / len(arr1)
    
    for i in range (len(arr1)):
        if arr1[i] > prom:
            cont += 1
    return cont

def acumularPuntajes(arr1):
    acumSuma = 0
    for i in range (len(arr1)):
        acumSuma += arr1[i]
    return acumSuma

def mostrar(arr1,arr2):
    for i in range(len(arr1)):
        print(f"Pregunta: {arr1[i]} | Puntaje: {arr2[i]}")

def minimo(arr1,arr2):
    indiceMenor = 0
    for i in range (len(arr2)):
        if arr2[i] < arr2[indiceMenor]:
            indiceMenor = i
    return indiceMenor

def intercambiar(arr1,i,j):
    aux = arr1[i]
    arr1[i] = arr1[j]
    arr1[j] = aux

def ordenar(arr1,arr2):
    for i in range (len(arr1)):
        for j in range (len(arr2)):
            if arr2[i] < arr2[j]:
                intercambiar(arr1,i,j)
                intercambiar(arr2,i,j)

def cargar(arr1,arr2):
    pregunta = ingresar_pregunta()
    while pregunta != "FIN" and acumularPuntajes(arr2) < 150:
        puntaje = ingresar_puntaje()
        arr1.append(pregunta)
        arr2.append(puntaje)

        if acumularPuntajes(arr2) < 150:
            pregunta = ingresar_pregunta()

## Codigo principal
preguntas = []
puntuajes = []

cargar(preguntas,puntuajes)

if len(preguntas) > 0:
    mostrar(preguntas,puntuajes)
    indice_minimo = minimo(preguntas,puntuajes)
    print(f"La pregunta con el puntaje menor es: {preguntas[indice_minimo]} con un puntaje de {puntuajes[indice_minimo]}")  
    print(f"La cantidad de preguntas que superan el puntaje promedio es: {promedio(puntuajes)}")
    ordenar(preguntas,puntuajes)
    print("Preguntas ordenadas por puntaje:")
    mostrar(preguntas,puntuajes)
else:
    print("No se han ingresado preguntas")