"""
El Ministerio de Salud le solicitó realizar un programa para llevar adelante un censo de salud.
Para ello se tomaron los siguientes datos: peso, edad y sexo.

Se realizan dos encuestas, y los datos fueron tomados en dos estaciones ferroviarias: Retiro y Constitución.

1) Cargar los datos de todas los encuestados. El ingreso concluye cuando el encuestador ingresa un 0 en el peso. Todos los datos deben ser validados.

2) Mostrar los datos cargados.

3) Determinar promediando cuál de las dos estaciones tiene las personas con mayor peso (mayor promedio).

4) Generar un nuevo arreglo con los pesos de ambos lotes que superen el promedio general. Mostrarlo
"""

def ingresar_peso():
    peso = float(input("Ingrese peso: "))
    while peso < 0 :
        peso = float(input("Ingrese peso: "))
    return peso

def ingresar_edad():
    edad = int(input("Ingrese edad: "))
    while edad < 0 or edad > 140:
        edad = int(input("Ingrese edad: "))
    return edad

def ingresar_estacion():
    estacion = input("Ingrese estacion (R o C): ")
    while estacion != "R" and estacion != "C":
        estacion = input("Ingrese estacion (R o C): ")
    return estacion

def ingresar_sexo():
    sexo = input("Ingrese Sexo (M o F): ")
    while sexo != "M" and sexo != "F":
        sexo = input("Ingrese Sexo (M o F): ")
    return sexo

def mostrar(arr_peso, arr_edades, arr_sexo,arr_est):
    for i in range (len(arr_peso)):
        print(f"Peso: {arr_peso[i]} | Edad: {arr_edades[i]} | Sexo: {arr_sexo[i]} | Estacion: {arr_est[i]}")

def promedio_estaciones(arr_peso,arr_est):
    acumtRetiro = 0
    contRetiro = 0
    acumConsti = 0
    contConsti = 0

    for i in range (len(arr_peso)):
        if arr_est[i] == "R":
            acumtRetiro += arr_peso[i]
            contRetiro += 1
        else:
            acumConsti += arr_peso[i]
            contConsti += 1
    
    if contRetiro > 0:
        promedioRetiro = acumtRetiro / contRetiro
    else:
        promedioRetiro = 0
    if contConsti > 0:
        promedioConsti = acumConsti / contConsti
    else:
        promedioConsti = 0
    
    if promedioRetiro > promedioConsti:
        print("Retiro tiene mas promedio de peso")
    elif promedioConsti > promedioRetiro:
        print("Constitucion tiene mas promedio de peso")
    else:
        print("Tiene el mismo promedio de peso")
    
def promedio_general(arr_peso):
    acum = 0
    for i in range (len(arr_peso)):
        acum += arr_peso[i]
    promedioPesoGeneral = acum / len(arr_peso)
    return promedioPesoGeneral

def pesos_mayores_promedio(arr_peso,promedio):
    arr_nuevos = []
    for i in range (len(arr_peso)):
        if arr_peso[i] > promedio:
            arr_nuevos.append(arr_peso[i])
    return arr_nuevos

def cargar(arr_peso, arr_edades, arr_sexo,arr_est):
    peso = ingresar_peso()
    while peso != 0:
        arr_peso.append(peso)
        edad = ingresar_edad()
        arr_edades.append(edad)
        sexo = ingresar_sexo()
        arr_sexo.append(sexo)
        estacion = ingresar_estacion()
        arr_est.append(estacion)
        peso = ingresar_peso()

peso = []
edades = []
sexo = []
estacion = []

cargar(peso,edades,sexo,estacion)

if len(edades) > 0:
    mostrar(peso,edades,sexo,estacion)
    promedio = promedio_general(peso)
    promedio_estaciones(peso,estacion)
    nuevo_arreglo = pesos_mayores_promedio(peso, promedio)
    print(f"Promedio general: {promedio}")
    print("Pesos mayores al promedio:")
    for i in range(len(nuevo_arreglo)):
        print(nuevo_arreglo[i])
