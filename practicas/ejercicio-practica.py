"""
Se desea llevar el control de planes de una prepaga para las localidades más populares CABA y BSAS, y realizar una estadística

Para ello se releva la siguiente información.

    Localidad (CABA o BS AS)
    Tipo de plan: Oro (O), Plata (P)
    Edad del paciente
    Cantidad de consultas realizadas
    Validar los datos de entrada con criterios lógicos
    La carga finaliza cuando se ingresa en cantidad de consultas 0

Se pide:
    Mostrar los datos cargados
    Calcular el promedio de edades de los pacientes
    Determinar que zona tuvo mayor cantidad de consultas
    Calcular el porcentaje de personas mayores a 50 con plan Oro.
"""
import os
os.system ("clear")

contadorCABA = 0
contadorBSAS = 0
contadorMayoresOro = 0
contadorPersonas = 0
acumEdad = 0

consultas = int(input("Ingrese cantidad de consultas: "))
while consultas != 0:
    localidad = input("Ingrese su localidad (CABA o BS AS): ")
    while localidad != "CABA" and localidad != "BS AS":
        localidad = input("Error! Ingrese una localidad validad CABA o BS AS: ")
    
    tipoPlan = input("Ingrese su tipo de plan Oro O o Plata P: ")
    while tipoPlan != "O" and tipoPlan != "P":
        tipoPlan = input("Eror! Ingrese un tipo de plan valido O o P")

    edad = int(input("Ingrese su edad: "))
    while edad < 0 or edad > 110:
        edad = int(input("Error! edad invalidad ingrese un valor valido: "))

    acumEdad += edad
    contadorPersonas += 1

    consultas_actual = consultas

    if localidad == "CABA":
        contadorCABA += consultas_actual
    else:
        contadorBSAS += consultas_actual

    if tipoPlan == "O":
        if edad > 50:
            contadorMayoresOro += 1

    consultas = int(input("Ingrese cantidad de consultas: "))

    print(f"Localidad: {localidad}")
    print(f"Tipo de plan: {tipoPlan}")
    print(f"Edad del paciente: {edad}")
    print(f"Cantidad de Consultas: {consultas_actual}")

if contadorCABA > contadorBSAS:
    print(f"En CABA hubo mas consultas: {contadorCABA} ")
elif contadorBSAS > contadorCABA:
    print(f"En BSAS hubo mas consultas: {contadorBSAS} ")
else:
    print("Ambos tuvieron la misma cantidad de consultas")

if contadorPersonas > 0:
    porcentaje = (contadorMayoresOro / contadorPersonas) * 100
    print(f"Porcentaje de personas mayores a 50 con plan Oro {porcentaje}%")

    promedio = (acumEdad / contadorPersonas)
    print(f"El promedio de la edad de los pacientes es: {promedio}")