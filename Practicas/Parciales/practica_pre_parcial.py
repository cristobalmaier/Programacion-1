"""
Se quiere llevar el control de peajes de una ruta nacional, para lo cual se carga la siguiente información:

  - Tipo de vehículo (moto, auto, camión)

  - Hora (pico - P / no pico - NP)

Se pide:

La carga finaliza cuando se ingresa FIN en tipo de vehículo o se hayan cargado 50 vehículos.
Considerando que el valor en hora no pico para autos es $500, moto $350 y camión $1200 y que en hora pico se incrementa en 25%. Calcular el monto total recaudado por las motos hora pico.
Calcular el porcentaje de camiones en hora no pico sobre el total de vehículos.
Calcular el promedio por vehículo.
"""

contador_vehiculos = 0
contador_camiones_np = 0

total_motos_pico = 0
acum_total = 0

tipo_vehiculo = input("Ingrese el tipo de vehículo: ")

while tipo_vehiculo != "FIN" and contador_vehiculos < 50:

    while tipo_vehiculo != "moto" and tipo_vehiculo != "auto" and tipo_vehiculo != "camión" and tipo_vehiculo != "FIN":
        tipo_vehiculo = input("Error! Ingrese un tipo de vehículo válido: ")

    if tipo_vehiculo != "FIN":

        hora = input("Ingrese la hora (P/NP): ")

        while hora != "P" and hora != "NP":
            hora = input("Error! Ingrese una hora válida (P/NP): ")

        if tipo_vehiculo == "moto":

            if hora == "P":
                monto = 350 * 1.25
                total_motos_pico += monto
            else:
                monto = 350

        elif tipo_vehiculo == "auto":

            if hora == "P":
                monto = 500 * 1.25
            else:
                monto = 500

        elif tipo_vehiculo == "camión":

            if hora == "P":
                monto = 1200 * 1.25
            else:
                monto = 1200
                contador_camiones_np += 1

        acum_total += monto
        contador_vehiculos += 1
        tipo_vehiculo = input("Ingrese el tipo de vehículo: ")

if contador_vehiculos > 0:

    porcentaje_camiones = (contador_camiones_np / contador_vehiculos) * 100
    promedio = acum_total / contador_vehiculos

    print(f"Total recaudado por motos en hora pico: ${total_motos_pico}")
    print(f"Porcentaje de camiones en hora no pico: {porcentaje_camiones}%")
    print(f"Promedio por vehículo: ${promedio}")
else:
    print("No se ingresaron vehículos")