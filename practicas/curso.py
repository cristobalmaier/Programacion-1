"""
Se quiere llevar estadística de un curso para ello se pide ingresar el número de legajo, el promedio final, el turno M/T/N.

Se carga la información de 500 alumnos

Se pide:

Calcular el promedio mínimo y a que legajo pertenece
Si el promedio cargado del alumno es mayor a 9 mostrar el mensaje "promedio destacado"
Calcular el porcentaje de alumnos con notas entre 4 y 7.
"""

contadorRango = 0

for i in range (500):

    legajo = int(input("Ingrese numero de legajo: "))
    while legajo < 0:
        legajo = int(input("Erro! Ingrese un lejao mayor a 0: "))
    
    promedioFinal = float(input("Ingrese su promedio final: "))
    while promedioFinal < 0 or promedioFinal > 10:
        promedioFinal = float(input("Error! ingrese un promedio (0-10): "))
    
    turno = input("Ingrese su turno M/T/N: ")
    while turno != "M" and turno != "T" and turno != "N":
        turno = input("Ingrese un turno valido M/T/N: ")

    if promedioFinal > 9:
        print("Promedio Destacado")
    
    if i == 0:
        minimo = promedioFinal
        legajoMinimo = legajo
    else:
        if promedioFinal < minimo:
            minimo = promedioFinal
            legajoMinimo = legajo
    
    if promedioFinal >= 4 and promedioFinal <= 7:
        contadorRango += 1
    

porcentaje = (contadorRango / 500) * 100
print(f"Promedio minimo: {minimo}")
print(f"Legajo del minimo: {legajoMinimo}")
print(f"Porcentaje entre 4 y 7: {porcentaje}%")