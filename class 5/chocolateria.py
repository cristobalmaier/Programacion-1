"""
En un negocio de venta de chocolate hay tres tipos de chocolate: amargo, dulce y con almendras. 

El amargo cuesta $20 el kg, el dulce $25 y con almendras $30 el kg.

Por cada venta, ingresan al sistema:

Nombre del vendedor (Pedro o Pablo – se ingresa como texto)
Cantidad de chocolate vendido (en kg).
Tipo de chocolate (1. amargo, 2. dulce, 3. con almendras)
Día del mes (1 a 30 – nunca trabajan los 31)
Cuando se llega a día =31, quieren ver:

Qué día del mes se registró la mayor venta (en Kg.) y quién realizó la venta.
Qué día del mes se registró la mayor venta (en $) y quién realizó la venta.
Quién facturó más (total en el mes).
Cantidad (total) de Kg. vendidos por tipo de chocolate.
Porcentaje de ventas de Pedro en relación al total (en $).

Validar los ingresos. No usar entradas forzadas a los while. No usar while True, break, continue. No usar banderas.
"""
import os
os.system ("clear")

chocolateAmargo = 20
chocolateDulce = 25
chocolateAlmendras = 30
diaMayorVenta = 0
amargoKG = 0
dulceKG = 0
almendraKG = 0
MayorKG = 0
diaMayorImporte = 0
vendedorMayorKG = ""
mayorImporte = 0
diaMayorKG = 0
vendedorMayorImporte = 0


diaMes = int(input("Ingrese dia del mes: "))

while diaMes != 31:

    while diaMes < 1 or diaMes > 31:
        print("Error! Ingrese un valor correcto")
    
    nombreVendedor = (input("Ingrese nombre del vendedor (Pedro o Pablo): ")).upper()
    while nombreVendedor != "PEDRO" and nombreVendedor != "PABLO":
        print("Error! Ingrese un nombre de vendedor valido!")
    
    cantidadChocolate = float(input("Ingrese la cantidad de chocolate vendido (kg): "))
    while cantidadChocolate < 0:
        print("Error! Cantidad de chocolate negativa, ingrese un valor postivio")

    tipoChocolote = int(input("Ingrese el tipo de chocolate (1. amargo, 2. dulce, 3. con almendras): "))
    while tipoChocolote < 1 and tipoChocolote > 3:
        print("Erro! Tipo de chocolate invalido, Reingrese uno valido")
    
    if tipoChocolote == 1:
        total = cantidadChocolate * chocolateAmargo
        amargoKG += cantidadChocolate
    elif tipoChocolote == 2:
        total = cantidadChocolate * chocolateDulce
        dulceKG += cantidadChocolate
    else:
        total = cantidadChocolate * chocolateAlmendras
        almendraKG += cantidadChocolate
    
    if nombreVendedor == "Pedro":
        totalPedro += total
    else:
        totalPablo += total

    if cantidadChocolate > MayorKG:
        MayorKG = cantidadChocolate
        diaMayorKG = diaMes
        vendedorMayorKG = nombreVendedor
    
    if total > mayorImporte:
        mayorImporte = total
        diaMayorImporte = diaMes
        vendedorMayorImporte = nombreVendedor

    diaMes = int(input("Ingrese dia del mes: "))

cantidadTotal = totalPablo + totalPedro

if cantidadChocolate > 0:
    porcentajePedro = (totalPablo/cantidadTotal) * 100
else:
    porcentajePedro = 0

print(f"Mayor venta en KG: {MayorKG}, Dia: {diaMayorKG}, Vendedor: {vendedorMayorKG}")
print(f"Mayor venta en $: {mayorImporte}, Dia: {diaMayorImporte}, Vendedor: {vendedorMayorImporte}")

if totalPedro > totalPablo:
    print(f"Pedro facturo mas: ${totalPedro}")
else:
    print(f"Pablo facturo mas: ${totalPablo}")

print(f"Amargo KG: {amargoKG}")
print(f"Dulce KG: {dulceKG}")
print(f"Almendra KG: {almendraKG}")

print(f"Cantidad vendida total: ${cantidadTotal}")
print(f"Porcentaje de Pedro: {porcentajePedro}")