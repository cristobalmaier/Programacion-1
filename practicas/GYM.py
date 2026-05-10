"""
Un gimnasio desea registrar la información de las personas que se inscriben a distintas actividades.

De cada socio se ingresa:

- Número de socio (0 para finalizar)
- Nombre
- Edad
- Tipo de actividad:
    1 = Musculación
    2 = Spinning
    3 = Crossfit
- Cantidad de meses contratados

Los precios por mes son:

- Musculación: $18000
- Spinning: $22000
- Crossfit: $30000

Además:
- Si contrata más de 6 meses, obtiene un descuento del 12%.

Se pide:

a) Mostrar por cada socio:
    - Nombre
    - Tipo de actividad
    - Total a pagar

b) Informar al finalizar:
    - Cantidad de socios de cada actividad
    - Edad del socio más grande
    - Promedio de edad de los socios de Crossfit
    - Total recaudado por el gimnasio
    - Porcentaje de socios de Spinning sobre el total
    - Cantidad total de meses contratados
"""

cantidadMasculacion = 0
cantidadSpinning = 0
cantidadCrossfit = 0

acumEdadCrossfit = 0
acumTotal = 0

contador = 0

musculacion = 18000
spinning = 22000
crossfit = 30000

numeroSocio = int(input("Ingrese numero de socio (0. Salir): "))

while numeroSocio != 0:
    nombre = input("Ingrese su nombre: ")
    while nombre == "":
        nombre = input("Error! Ingrese un nombre valido: ")
    edad = int(input("Ingrese su Edad: "))
    while edad < 0 or edad > 110:
        edad = int(input("Error! Ingrese una edad valida: "))
    tipoActividad = int(input("Selecciona el tipo de actividad: 1. Musculacion 2.Spinning 3.Crossfit: "))
    while tipoActividad != 1 and tipoActividad != 2 and tipoActividad != 3:
        tipoActividad = int(input("Error! Ingrese un tipo de actividad valido: 1.Musculacion 2.Spinning 3.Crossfit"))
    cantidadMeses = int(input("Ingrese la cantidad de meses: "))
    while cantidadMeses < 0:
        cantidadMeses = int(input("Error! Ingrese un numero valido: "))

    if tipoActividad == 1:
        cantidadMasculacion += 1
        total = musculacion * cantidadMeses
        if cantidadMeses >= 6:
            total *= 0.88
        
        acumTotal += total
        
    elif tipoActividad == 2:
        cantidadSpinning += 1
        total = spinning * cantidadMeses
        if cantidadMeses >= 6:
            total *= 0.88
        acumTotal += total
    else:
        cantidadCrossfit += 1
        total = crossfit * cantidadMeses
        acumEdadCrossfit += edad
        if cantidadMeses >= 6:
            total *= 0.88
        acumTotal += total
    

    if contador == 0:
        edadMaxima = edad
        mesesMaximo = cantidadMeses
    else:
        if edad > edadMaxima:
            edadMaxima = edad
        elif cantidadMeses > mesesMaximo:
            mesesMaximo = cantidadMeses


    contador += 1

    print(f"Nombre del socio: {nombre}")
    print(f"Tipo de Actividad: {tipoActividad}")
    print(f"Total a pagar: {total}")

    numeroSocio = int(input("Ingrese numero de socio (0. Salir): "))