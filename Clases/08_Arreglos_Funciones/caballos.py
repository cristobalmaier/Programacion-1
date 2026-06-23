"""
Se quiere determinar el ganador de una carrera de caballos para ello se guarda la siguiente información: 

    - nombre del caballo, tiempo realizado. 

    - Se carga información hasta que en nombre del caballo se ingresa FIN

    - Calcular el minimo y mostrar el caballo a que corresponde el tiempo (funcion)

    - Calcular el promedio de los tiempos obtenidos (funcion)

    - A partir de los tiempos obtenidos generar un nuevo arreglo con los nombres de los caballos que hayan obtenido un tiempo mayor al promedio. 
"""

def ingresar_nombre():
    nombre = input("Ingrese nombre: ")
    while nombre == "":
        nombre = input("Ingrese nombre: ")
    return nombre

def ingresar_tiempo():
    tiempo = float(input("Ingrese el tiempo realizado: "))
    while tiempo < 0:
        tiempo = float(input("Ingrese el tiempo realizado: "))
    return tiempo

def minimo(arr1,arr2):
    indice_menor = 0
    for i in range(len(arr2)):
        if arr2[i] < arr2[indice_menor]:
            indice_menor = i
    return indice_menor

def promedioTiempos(arr1):
    suma = 0
    for i in range(len(arr1)):
        suma += arr1[i]
    promedio = suma / len(arr1)
    return promedio

def caballosMayorPromedio(nombres, tiempos, promedio):
    nuevos = []
    for i in range(len(tiempos)):
        if tiempos[i] > promedio:
            nuevos.append(nombres[i])
    return nuevos

def cargar(arr1,arr2):
    nombre = ingresar_nombre()
    while nombre != "FIN":
        arr1.append(nombre)
        tiempo = ingresar_tiempo()
        arr2.append(tiempo)
        nombre = ingresar_nombre()

## -- Programar Principal ---
caballo = []
tiempo_realizado = []

cargar(caballo,tiempo_realizado)

if len(caballo) > 0:
    indice_menor = minimo(caballo,tiempo_realizado)
    print(f"El caballo {caballo[indice_menor]} tiene el menor tiempo: {tiempo_realizado[indice_menor]}")
    promedio = promedioTiempos(tiempo_realizado)
    print(f"El promedio de tiempo obtenido es: {promedio}")
    caballo_mayor_promedio = caballosMayorPromedio(caballo, tiempo_realizado, promedio)
    print("Caballos con tiempo mayor al promedio:")
    for i in range(len(caballo_mayor_promedio)):
        print(caballo_mayor_promedio[i])
else:
    print("No hay caballos, Por favor Ingreselos para poder ver Informacion")