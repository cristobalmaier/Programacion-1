"""
SIMULACRO DE PARCIAL – INTRODUCCIÓN A LA PROGRAMACIÓN

Una empresa de alquiler de autos desea registrar información sobre los clientes que realizan reservas durante el día.

De cada cliente se ingresa:

- Número de reserva (0 para finalizar)
- Nombre del cliente
- Edad
- Tipo de vehículo:
    1 = Económico
    2 = SUV
    3 = Premium
- Cantidad de días de alquiler

Precios por día:

- Económico: $18000
- SUV: $32000
- Premium: $50000

Además:
- Si el alquiler supera los 7 días, se aplica un descuento del 12%.
- Si el vehículo es Premium y el alquiler supera los 14 días,
  se aplica un recargo del 5%.

Se pide:

a) Mostrar por cada cliente:
    - Nombre
    - Tipo de vehículo
    - Total a pagar

b) Informar al finalizar:

1. Cantidad de clientes por tipo de vehículo.
2. Edad del cliente más joven.
3. Promedio de edad de los clientes Premium.
4. Total recaudado por la empresa.
5. Porcentaje de clientes SUV sobre el total.
6. Cantidad total de días alquilados.
7. Porcentaje de días alquilados por categoría:
   (dias_categoria * 100 / total_dias)

Condiciones:
- Validar todos los datos necesarios.
- No usar banderas.
- No usar break.
- Finalizar cuando el número de reserva sea 0.
"""

Econmico = 18000
Suv = 32000
Premium = 50000

contadorEconomico = 0
contadorSuv = 0
contadorPremium = 0
contador = 0
contadorDiasEconmico = 0
contadorDiasSuv = 0
contadorDiasPremium = 0

AcumEdadPremium = 0
AcumTotalRecaudado = 0
AcumDiasAlquilados = 0

numeroReserva = int(input("Ingrese numero de reserva (0. Salir): "))

while numeroReserva != 0:
    nombre = input("Ingrese nombre: ")
    while nombre =="":
        nombre = input("Error! Ingrese nombre del cliente: ")
    edad = int(input("Ingrese edad: "))
    while edad < 0 or edad > 110:
        edad = int(input("Error! Ingrese una edad valida: "))
    tipoVehiculo = int(input("Seleccione 1.Economico 2.Suv 3.Premium: "))
    while tipoVehiculo < 1 or tipoVehiculo > 3:
        tipoVehiculo = int(input("ERROR! Seleccione una opcion valida: "))
    dias = int(input("Ingrese los dias de alquiler: "))
    while dias < 0:
        dias = int(input("ERROR! Ingrese un valor positivo: "))
    
    if tipoVehiculo == 1:
        contadorEconomico += 1
        total = dias * Econmico
            
        if dias > 7:
            total *= 0.88
            
        AcumTotalRecaudado += total
        AcumDiasAlquilados += dias
        contadorDiasEconmico += dias

    elif tipoVehiculo == 2:
        contadorSuv += 1
        total = dias * Suv
            
        if dias > 7:
            total *= 0.88

        AcumTotalRecaudado += total
        AcumDiasAlquilados += dias
        contadorDiasSuv += dias
    else:
        contadorPremium += 1
        total = dias * Premium
        AcumEdadPremium += edad
        
        if dias > 7:
            total *= 0.88
            if dias >= 14:
                total *= 1.05
        
        AcumTotalRecaudado += total
        AcumDiasAlquilados += dias
        contadorDiasPremium += dias

    print(f"Nombre: {nombre}")
    print(f"Tipo de Vehiculo: {tipoVehiculo}")
    print(f"Total a pagar: ${total}")

    if contador == 0:
        mayorEdad = edad
    elif edad < mayorEdad:
        mayorEdad = edad

    contador += 1

    numeroReserva = int(input("Ingrese numero de reserva (0. Salir): "))

if contador > 0:
    print(f"Clientes Econmicos: {contadorEconomico}")
    print(f"Clientes Suv: {contadorSuv}")
    print(f"Clientes Premium: {contadorPremium}")
    print(f"Edad del clientes mas joven: {mayorEdad}")
    print(f"Total Recaudado: {AcumTotalRecaudado}")

    if contadorPremium > 0:
        promedioEdadPremium = AcumEdadPremium / contadorPremium
        print(f"Promedio de edad de los clientes premium: {promedioEdadPremium}")
    porcentajeSuv = (contadorSuv / contador)*100
    print(f"Porcentaje de clientes SUV: {porcentajeSuv}%")
    print(f"Total de Dias alquilados: {AcumDiasAlquilados}")
    porcentajeDiasEconomico = (contadorDiasEconmico/AcumDiasAlquilados)*100
    porcentajeDiasSuv = (contadorDiasSuv/AcumDiasAlquilados)*100
    porcentajeDiasPremium = (contadorDiasPremium/AcumDiasAlquilados)*100
    print(f"Porcentaje de dias de Economico: {porcentajeDiasEconomico}%")
    print(f"Porcentaje de dias de Suv: {porcentajeDiasSuv}%")
    print(f"Porcentaje de dias de Premium: {porcentajeDiasPremium}%")