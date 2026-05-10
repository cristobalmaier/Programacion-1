import os
os.system("clear")

chocolateAmargo = 20
chocolateDulce = 25
chocolateAlmendras = 30
totalPedro = 0
totalPablo = 0
amargoKG = 0
dulceKG = 0
almendraKG = 0
mayorKG = 0
diaMayorKG = 0
vendedorMayorKG = ""
mayorImporte = 0
diaMayorImporte = 0
vendedorMayorImporte = ""

diaMes = int(input("Ingrese dia del mes: "))

while diaMes != 31:

    while diaMes < 1 or diaMes > 30:
        diaMes = int(input("Reingrese dia valido: "))

    nombreVendedor = input("Ingrese nombre del vendedor (Pedro o Pablo): ").upper()
    while nombreVendedor != "PEDRO" and nombreVendedor != "PABLO":
        nombreVendedor = input("Error. Ingrese PEDRO o PABLO: ").upper()

    cantidadChocolate = float(input("Ingrese la cantidad de chocolate vendido (kg): "))
    while cantidadChocolate <= 0:
        cantidadChocolate = float(input("Error. Ingrese cantidad positiva: "))

    tipoChocolate = int(input("Ingrese el tipo de chocolate (1-3): "))
    while tipoChocolate != 1 and tipoChocolate != 2 and tipoChocolate != 3:
        tipoChocolate = int(input("Error. Ingrese 1, 2 o 3: "))

    if tipoChocolate == 1:
        total = cantidadChocolate * chocolateAmargo
        amargoKG += cantidadChocolate
    elif tipoChocolate == 2:
        total = cantidadChocolate * chocolateDulce
        dulceKG += cantidadChocolate
    else:
        total = cantidadChocolate * chocolateAlmendras
        almendraKG += cantidadChocolate

    if nombreVendedor == "PEDRO":
        totalPedro += total
    else:
        totalPablo += total

    if cantidadChocolate > mayorKG:
        mayorKG = cantidadChocolate
        diaMayorKG = diaMes
        vendedorMayorKG = nombreVendedor

    if total > mayorImporte:
        mayorImporte = total
        diaMayorImporte = diaMes
        vendedorMayorImporte = nombreVendedor

    diaMes = int(input("Ingrese dia del mes: "))

cantidadVendidaTotal = totalPedro + totalPablo

if cantidadVendidaTotal > 0:
    porcentajePedro = (totalPedro / cantidadVendidaTotal) * 100
else:
    porcentajePedro = 0

print(f"Mayor venta en KG: {mayorKG}, Dia: {diaMayorKG}, Vendedor: {vendedorMayorKG}")
print(f"Mayor venta en $: {mayorImporte}, Dia: {diaMayorImporte}, Vendedor: {vendedorMayorImporte}")

if totalPedro > totalPablo:
    print(f"Pedro facturo mas: ${totalPedro}")
else:
    print(f"Pablo facturo mas: ${totalPablo}")

print(f"Amargo KG: {amargoKG}")
print(f"Dulce KG: {dulceKG}")
print(f"Almendra KG: {almendraKG}")

print(f"Cantidad vendida total: ${cantidadVendidaTotal}")
print(f"Porcentaje de Pedro: {porcentajePedro}")