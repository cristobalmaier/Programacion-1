"""
Una empresa de turismo desea registrar información sobre los pasajeros que compran paquetes de viaje.

De cada pasajero se ingresa:

- Número de reserva (0 para finalizar)
- Nombre del pasajero
- Edad
- Tipo de paquete:
    1 = Nacional
    2 = Internacional
    3 = Premium
- Cantidad de días del viaje

Los precios por día son:

- Nacional: $15000
- Internacional: $30000
- Premium: $50000

Además:
- Si el viaje dura más de 10 días, se aplica un descuento del 10%.

Se pide:

a) Mostrar por cada pasajero:
    - Nombre
    - Tipo de paquete
    - Total a pagar

b) Informar al final:
    - Cantidad de pasajeros de cada tipo de paquete
    - Edad del pasajero más joven
    - Promedio de edad de los pasajeros Premium
    - Total recaudado por la empresa
    - Porcentaje de pasajeros de tipo Internacional sobre el total
    - Cantidad total de días vendidos
"""

nacional = 15000
internacional = 30000
Premium = 50000
contador_paquete1 = 0
contador_paquete2 = 0
contador_paquete3 = 0
contador = 0
acumPasajerosPremium = 0
acumDinero = 0
acumDias = 0


numero_reserva = int(input("Ingrese numero de Reserva (0. Salir): "))
while numero_reserva != 0:
    nombre = input("Ingrese nombre del pasajero: ")
    edad = int(input("Ingrese la edad del pasajero: "))
    while edad < 0 or edad > 110:
        edad = int(input("Erro! Ingrese una edad validad del pasajero: "))
    tipo_paquete = int(input("Seleccione el tipo de Paquete 1. Nacional 2.Internacional 3.Premium: "))
    while tipo_paquete < 0 or tipo_paquete > 4:
        tipo_paquete = int(input("Erro! Seleccione un paquete valido: 1. Nacional 2.Internacional 3.Premium: "))
    dias = int(input("Ingrese la cantidad de dias: "))
    while dias < 0:
        dias = int(input("Error! No se puede ingresar dias negativos, Ingrese la cantidad de dias: "))

    if tipo_paquete == 1:
        contador_paquete1 += 1
        total = dias * nacional
        
        if dias >= 10:
            total *= 0.90
        
        acumDinero += total
        acumDias += dias

    elif tipo_paquete == 2:
        contador_paquete2 += 1
        total = dias * internacional
        
        if dias >= 10:
            total *= 0.90
        
        acumDinero += total
        acumDias += dias
    else:
        contador_paquete3 += 1
        acumPasajerosPremium += edad
        total = dias * Premium
        if dias >= 10:
            total *= 0.90
        
        acumDinero += total
        acumDias += dias

    if contador == 0:
        minimo = edad
    elif edad < minimo:
            minimo = edad
    
    contador += 1

    print(f"Nombre del pasajero: {nombre}")
    print(f"Tipo de Paquete: {tipo_paquete}")
    print(f"Total a pagar: {total}")
    numero_reserva = int(input("Ingrese numero de Reserva (0. Salir): "))

if contador > 0:
    print(f"Pasajeros de tipo Nacional: {contador_paquete1}")
    print(f"Pasajeros de tipo Internacional: {contador_paquete2}")
    print(f"Pasajeros de tipo Premium: {contador_paquete3}")
    print(f"Pasajero mas joven: {minimo} años")
    if contador_paquete3 > 0:
        promedio = (acumPasajerosPremium / contador_paquete3)
        print(f"Promedio de los pasajeros Premium: {promedio}")
    print(f"Total Recaudado: {acumDinero}")
    porcentaje = (contador_paquete2 / contador) * 100
    print(f"El porcentaje de Tipo internacional sobre el total es: {porcentaje}")
    print(f"Cantidad total de dias vendidos: {acumDias}")