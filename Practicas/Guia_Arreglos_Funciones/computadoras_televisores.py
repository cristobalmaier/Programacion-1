"""
En una tienda de electrónica, se lleva un registro de las ventas diarias de dos productos, televisores y computadoras. 
Al finalizar la semana, se pide realizar los siguientes cálculos:

    - Calcular el total de unidades vendidas de televisores y computadoras (por separado)
    - Calcular el promedio diario de unidades vendidas de televisores y computadoras (juntos)
    - Encontrar el día con la mayor cantidad de unidades vendidas de televisores y computadoras. (juntos)
    - Encontrar el día con la menor cantidad de unidades vendidas de televisores y computadoras. (juntos)
    - Calcular el porcentaje de ventas de televisores y computadoras.
    - Sabiendo que el precio de venta de televisores es de $50000 c/u y el de computadoras es de $200000 c/u
    generar otro registro con los montos monetarios vendido por día para cada producto.
    
    - Obtener a partir de los registros anteriores, el día que más se recaudó (en total).
"""

def calcular_unidades_televisores(arr_televisores):
    acum = 0
    for i in range (len(arr_televisores)):
        acum += arr_televisores[i]
    return acum

def calcular_unidades_computadoras(arr_computadoras):
    acum = 0
    for i in range (len(arr_computadoras)):
        acum += arr_computadoras[i]
    return acum

def calcular_total (arr_televisores, arr_computadoras):
    acumTotal = 0
    for i in range (len(arr_televisores)):
        acumTotal += arr_televisores[i]
        acumTotal += arr_computadoras[i]
    promedio = (acumTotal / len (arr_televisores))
    return promedio

def dia_mayor_ventas (arr_televisores,arr_computadoras):
    indiceMayor = 0
    for i in range (len(arr_televisores)):
        totalDia = arr_televisores[i] + arr_computadoras[i]
        totalMayor = arr_televisores[indiceMayor] + arr_computadoras[indiceMayor]

        if totalDia > totalMayor:
            indiceMayor = i
    
    return indiceMayor

def dia_menor_ventas (arr_televisores,arr_computadoras):
    indiceMenor = 0
    for i in range (len(arr_televisores)):
        totalDia = arr_televisores[i] + arr_computadoras[i]
        totalMenor = arr_televisores[indiceMenor] + arr_computadoras[indiceMenor]

        if totalDia < totalMenor:
            indiceMenor = i
    
    return indiceMenor

def calcular_porcentaje (parte,total):
    porcentaje = (parte/total) * 100
    return porcentaje

def generar_montos_dia (arr1,arr2,monto_TV,monto_C):

    for i in range (len(arr1)):
        monto_dia_TV = arr1[i] * 50000
        monto_TV.append(monto_dia_TV)

        monto_dia_C = arr2[i] * 200000
        monto_C.append(monto_dia_C)
        
def dia_mayor_recaudacion(arr1,arr2):
    indiceMayor = 0
    for i in range (len(arr1)):
        totalDia = arr1[i] + arr2[i]
        totalMayor = arr1[indiceMayor] + arr2[indiceMayor]

        if totalDia > totalMayor:
            indiceMayor = i
    
    return indiceMayor


televisores = [10, 15, 20, 5, 8, 12, 18]
computadoras = [5, 10, 15, 20, 25, 30, 35]
montoTV = []
montoC = []


if len (televisores) > 0:
    cantidadTelevisores = calcular_unidades_televisores(televisores)
    print(f"Televisores: {cantidadTelevisores}")
    cantidadComputadoras = calcular_unidades_computadoras(computadoras)
    print(f"Computadoras: {cantidadComputadoras}")
    promedioDiario = calcular_total(televisores,computadoras)
    print(f"Promedio Diario de unidades vendidas: {promedioDiario}")
    diaMayorVentas = dia_mayor_ventas(televisores,computadoras)
    print(f"El dia que mas se vendio fue: {diaMayorVentas + 1} ")
    diaMenorVentas = dia_menor_ventas(televisores,computadoras)
    print(f"El dia que menos se vendio fue: {diaMenorVentas + 1}")
    TotalCantidad = cantidadTelevisores + cantidadComputadoras
    porcentajeTV = calcular_porcentaje(cantidadTelevisores,TotalCantidad)
    print(f"Televisores: {porcentajeTV:.2f}%")
    porcentajeC = calcular_porcentaje(cantidadComputadoras,TotalCantidad)
    print(f"Computadoras: {porcentajeC:.2f}%")
    generar_montos_dia(televisores,computadoras,montoTV,montoC)
    print(f"Montos diarios de televisores: {montoTV}")
    print(f"Montos diarios de computadoras: {montoC}")
    diaMayorRecaudacion = dia_mayor_recaudacion(montoTV,montoC)
    print(f"Dia con mayor recaudacion: {diaMayorRecaudacion + 1}")