"""
Cargar datos de litros cargados en una estación de servicio y el modelo de auto que corresponde.

Se carga información hasta que los litros consumidos alcancen 1000 litros

Validar el ingreso.

Calcular y retornar el promedio de litros consumidos

Ingresar por teclado un modelo y retornar la primer ocurrencia
"""

def ingresar_litros():
    litros = int(input("Ingrese litros: "))
    while litros <= 0:
        litros = int(input("Ingrese litros: "))
    return litros

def ingresar_auto():
    auto = input("Ingrese modelo de auto: ")
    while auto == "":
        auto = input("Ingrese modelo de auto: ")
    return auto

def calcular_total_litros(arr_litros):
    acum = 0
    for i in range (len(arr_litros)):
        acum += arr_litros[i]
    return acum

def cargar (arr_litros,arr_autos):

    while calcular_total_litros(arr_litros) < 1000:
        litros = ingresar_litros()
        arr_litros.append(litros)

        auto = ingresar_auto()
        arr_autos.append(auto)
        

def calcular_promedio(arr_litros):
    acum = calcular_total_litros(arr_litros)
    promedio = acum / len(arr_litros)
    return promedio 

def buscar_modelo(arr_autos,datoBuscar):
    i = 0
    while i < len(arr_autos) and arr_autos[i] != datoBuscar:
        i += 1
    return i 

litros = []
autos = []

cargar (litros,autos)

if len(litros) > 0:
    promedio = calcular_promedio(litros)
    print(f"Promedio de litros consumidos: {promedio}")

    buscar = input("Ingrese modelo a buscar: ")
    indice = buscar_modelo(autos,buscar)
    if indice < len(autos):
        print(f"---- Auto Encontrado ----")
        print(f"Modelo: {autos[indice]}")
        print(f"Litros: {litros[indice]}")
    else:
        print("No hay ningun modelo de ese auto")
else:
    print("NO se cargaron datos")