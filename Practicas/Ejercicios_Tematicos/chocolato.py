"""
Ejercicio adicional para que practiquen. No requiere entrega.

En un negocio de venta de chocolate hay tres tipos de chocolate: amargo, dulce y con almendras. 

El amargo cuesta $20 el kg, el dulce $25 y con almendras $30 el kg.

Por cada venta, ingresan al sistema:

Nombre del vendedor (Pedro o Pablo  se ingresa como texto)
Cantidad de chocolate vendido (en kg).
Tipo de chocolate (1. amargo, 2. dulce, 3. con almendras)
Día del mes (1 a 30  nunca trabajan los 31)
Cuando se llega a día =31, quieren ver:

    Qué día del mes se registró la mayor venta (en Kg.) y quién realizó la venta.
    Qué día del mes se registró la mayor venta (en $) y quién realizó la venta.
    Quién facturó más (total en el mes).
    Cantidad (total) de Kg. vendidos por tipo de chocolate.
    Porcentaje de ventas de Pedro en relación al total (en $).

Validar los ingresos. No usar entradas forzadas a los while. No usar while True, break, continue. No usar banderas.
"""

amargo = 20
dulce = 25
almendras = 30
acumAlmendras = 0
acumAmargo = 0
acumDulce = 0
acumTotal = 0
totalPablo = 0
totalPedro = 0

contador = 0

dia = int(input("Ingrese el dia del Mes"))
while dia < 0 or dia > 31:
    dia = int(input("Error! Ingrese un dia valido:"))

while dia != 31:
    nombre = input("Ingrese nombre del venedor (Pedro/Pablo): ").upper()
    while nombre != "Pedro" and nombre != "Pablo":
        nombre = input("ERORR! Ingrese un nombre valido (Pedro / Pablo): ")
    
    cantidad = float(input("Ingrese la cantidad de chocolate (kg): "))
    while cantidad < 0:
        cantidad = float(input("EROR! Ingrese la cantidad de chocolate (kg): "))

    tipoChocolate = int(input("Seleccione el tipo de Chocolate -> 1. Amargo 2.Dulce 3.Alemndras: "))
    while tipoChocolate != 1 and tipoChocolate != 2 and tipoChocolate != 3:
        tipoChocolate = int(input("ERROR! Seleccione un tipo de chocolate valido -> 1. Amargo 2.Dulce 3.Alemndras: "))
    
    if nombre == "Pedro":
        totalPedro += total
    else:
        totalPablo += total
    
    if tipoChocolate == 1:
        total = amargo * cantidad
        acumAlmendras += cantidad
        
    
    elif tipoChocolate == 2:
        total = dulce * cantidad
        acumDulce += cantidad
    
    else:
        total = almendras * cantidad
        acumAlmendras += cantidad
    
    if contador == 0:
        mayorDia = dia
        mayorNombre = nombre
        mayorTotal = acumTotal
    elif dia > mayorDia:
        mayorDia = dia
        mayorNombre = nombre
        mayorTotal = total
    