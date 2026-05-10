"""
Un club de robótica decide preparar un informe sobre los robots presentados en una competencia. 
Para ello, se pide ingresar los siguientes datos hasta que el número de robot sea 0 (cero):

    Número de robot

    Nombre del robot

    Tiempo de autonomía en minutos

Categoría del robot (“rescate”, “sumo”, “seguidor de línea” o “explorador”)

Se pide calcular lo siguiente:

    a) Cantidad de robots ingresados de cada categoría.

    b) El promedio del tiempo de autonomía de cada categoría.
    Ejemplo: “El promedio de autonomía de los robots de rescate es de XXX minutos”.

    c) Mostrar el nombre del robot con mayor tiempo de autonomía.
"""

contadorRobotRescate = 0
contadorRobotSumo = 0
contadorRobotSeguidor = 0
contadorRobotExplorador = 0
acumRobotRescate = 0
acumRobotSumo = 0
acumRobotSeguidor = 0
acumRobotExplorador = 0
contador = 0

numeroRobot = int(input("Ingrese numero de Robot (0. Salir): "))

while numeroRobot != 0:
    nombre = input("Ingrese el nombre: ")
    while nombre == "":
        nombre = input("Erro! Ingrese un nombre: ")
    
    tiempo_autonomia = float(input("Ingrese el tiempo de autonomia (minutos): "))
    while tiempo_autonomia < 0:
        tiempo_autonomia = float(input("Erro!Ingrese un valor positivo en (minutos): "))
    categoria = int(input("Ingrese categoria, 1.Rescate 2.Sumo 3.Seguidor 4.Explorador: "))
    while categoria < 0 or categoria > 5:
        categoria = int(input("Error! Ingrese una categoria valida: "))
    
    if categoria == 1:
        contadorRobotRescate += 1
        acumRobotRescate += tiempo_autonomia
    elif categoria == 2:
        contadorRobotSumo += 1
        acumRobotSumo += tiempo_autonomia
    elif categoria == 3:
        contadorRobotSeguidor += 1
        acumRobotSeguidor += tiempo_autonomia
    else:
        contadorRobotExplorador += 1
        acumRobotExplorador += tiempo_autonomia
    
    if contador == 0:
        mayorAutonomia = tiempo_autonomia
        nombreMayorAutonomia = nombre
        
    else:
        if tiempo_autonomia > mayorAutonomia:
            mayorAutonomia = tiempo_autonomia
            nombreMayorAutonomia = nombre
    contador += 1
    numeroRobot = int(input("Ingrese numero de Robot (0. Salir): "))

if contadorRobotRescate > 0:
    promedioRescate = acumRobotRescate / contadorRobotRescate
    print(f"El promedio de autonomía de los robots de rescate es de {promedioRescate} minutos")
elif contadorRobotSumo > 0:
    promedioSumo = acumRobotSumo / contadorRobotSumo
    print(f"El promedio de autonomía de los robots de sumo es de {promedioSumo} minutos")
elif contadorRobotSeguidor > 0:
    promedioSeguidor = acumRobotSeguidor / contadorRobotSeguidor
    print(f"El promedio de autonomía de los robots de seguidor es de {promedioSeguidor} minutos")
else:
    promedioExplorador = acumRobotExplorador / contadorRobotExplorador
    print(f"El promedio de autonomía de los robots de explorador es de {promedioExplorador} minutos")

if contador > 0:
    print(f"El nombre del Robot con mayor autonomia es: {nombreMayorAutonomia}")