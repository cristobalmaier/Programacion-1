"""
Ejercicio nº 2

Una empresa distribuidora de bebidas desea clasificar a sus comercios según la cantidad de cajones que compran.

- Comercio chico: menos de 50 cajones.
- Comercio mediano: entre 50 y 150 cajones.
- Comercio grande: más de 150 cajones.

Cada cajón cuesta $12000.

Los comercios grandes obtienen un descuento del 7%.

Se desea diseñar un algoritmo que permita ingresar la cantidad de cajones comprados por cada comercio.

La carga finaliza cuando se ingresa 0 cajones.

Al finalizar mostrar:

a) Cantidad total de comercios.
b) Monto total recaudado.
c) Porcentaje de cajones vendidos por categoría.
   (cajones_categoria * 100 / total_cajones)
d) Cantidad total de cajones vendidos.

"""

cajon = 12000
contadorChico = 0
contadorMediano = 0
contadorGrande = 0
acumTotalRecaudado = 0
acumTotalVendidos = 0

cajonesChico = 0
cajonesMediano = 0
cajonesGrande = 0

contaodrCajones = 0

cajones = int(input("Ingrese la cantidad de cajones (0.Salir): "))

while cajones < 0:
    cajones = int(input("ERROR! Ingrese una cantidad positiva: "))

while cajones != 0 :
    if cajones < 50:
        contadorChico += 1
        total = cajones * cajon
        acumTotalRecaudado += total
        acumTotalVendidos += cajones
        cajonesChico += cajones
    elif cajones >= 50 and cajones < 150:
        contadorMediano += 1
        total = cajones * cajon
        acumTotalRecaudado += total
        acumTotalVendidos += cajones
        cajonesMediano += cajones
    else:
        contadorGrande += 1
        total = cajones * cajon
        total *= 0.93
        acumTotalRecaudado += total
        acumTotalVendidos += cajones
        cajonesGrande += cajones
    
    contaodrCajones += 1
    
    cajones = int(input("Ingrese la cantidad de cajones (0.Salir): "))

if contaodrCajones > 0:
    print(f"Cantidad de Comercio Chico: {contadorChico}")
    print(f"Cantidad de Comercio Mediano: {contadorMediano}")
    print(f"Cantidad de Comercio Grande: {contadorGrande}")

    print(f"Monto Total: {acumTotalRecaudado}")

    porcentajeChico = (cajonesChico * 100 / acumTotalVendidos)
    porcentajeMediano = (cajonesMediano * 100 / acumTotalVendidos)
    porcentajeGrande = (cajonesGrande * 100 / acumTotalVendidos)

    print(f"Porcentaje de Comercio Chico: {porcentajeChico}")
    print(f"Porcentaje de Comercio Mediano: {porcentajeMediano}")
    print(f"Porcentaje de Comercio Grande: {porcentajeGrande}")

    print(f"Cantidad de Cajones Vendidos: {acumTotalVendidos}")