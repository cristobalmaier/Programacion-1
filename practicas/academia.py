"""
Una academia de deportes quiere hacer un informe sobre los alumnos inscriptos en distintas disciplinas.

Se pide ingresar datos hasta que el número de alumno sea 0:

Número de alumno
Nombre del alumno
Cantidad de horas de entrenamiento por semana
Disciplina ( “fútbol”, “natación”, “tenis” o “atletismo” )

Se pide calcular:

    a) Cantidad de alumnos inscriptos en cada disciplina.

    b) El promedio de horas de entrenamiento por disciplina.
    Ejemplo: “El promedio de horas en natación es de XX horas”.

    c) Mostrar el nombre de la disciplina que tiene mas horas de entrenamiento
"""

contadorFutbol = 0
contadorNatacion = 0
contadorTenis = 0
contadorAtletismo = 0

acumHorasFutbol = 0
acumHorasNatacion = 0
acumHorasTenis = 0
acumHorasAtletismo = 0

contador = 0

numeroAlumno = int(input("Ingrese numero de Alumno: "))

while numeroAlumno != 0:

    nombre = input("Ingrese nombre del alumno: ")
    while nombre == "":
        nombre = input("Error! Ingrese nombre del alumno: ")
    
    horasEntrenamiento = float(input("Ingrese horas de entrenamiento: "))
    while horasEntrenamiento < 0:
        horasEntrenamiento = float(input("Error! Tenes que entrengar minimo 1 hora, ingrese valor: "))
    
    disciplina = input("Seleccione disciplina: Futbol, Natacion, Tenis, Atletismo: ")
    while disciplina != "Futbol" and disciplina != "Natacion" and disciplina != "Tenis" and disciplina != "Atletismo":
        disciplina = input("Error! Seleccione una disciplina valida: Futbol, Natacion, Tenis, Atletismo: ")
    
    if disciplina == "Futbol":
        contadorFutbol += 1
        acumHorasFutbol += horasEntrenamiento
    elif disciplina == "Natacion":
        contadorNatacion += 1
        acumHorasNatacion *= horasEntrenamiento
    elif disciplina == "Tenis":
        contadorTenis += 1
        acumHorasTenis += horasEntrenamiento
    else:
        contadorAtletismo += 1
        acumHorasAtletismo += horasEntrenamiento
    
    if contador == 0:
        mayorHoras = horasEntrenamiento
        mayorDisciplina = nombre
    else:
        if horasEntrenamiento > mayorHoras:
            mayorHoras = horasEntrenamiento
            mayorDisciplina = nombre
        
    contador += 1

    numeroAlumno = int(input("Ingrese numero de Alumno: "))

if contador > 0:
    if contadorFutbol > 0:
        promedioFutbol = acumHorasFutbol / contadorFutbol
        print(f"Alumnos de Futbol: {contadorFutbol}")
        print(f"Proedio de horas de entrenamiento de Futbol: {promedioFutbol}")
    elif contadorNatacion > 0:
        promedioNatacion = acumHorasNatacion / contadorNatacion
        print(f"Alumnos de Natacion: {contadorNatacion}")
        print(f"Promedio de horas de entramiento de Natacion: {promedioNatacion}")
    elif contadorTenis > 0:
        promedioTenis = acumHorasTenis / contadorTenis
        print(f"Alumnos de Tenis: {contadorTenis}")
        print(f"Promedio de horas de entramiento de Tenis: {promedioTenis}")
    else:
        promedioAtletismo = acumHorasAtletismo / contadorAtletismo
        print(f"Alumnos de Atletismo: {contadorAtletismo}")
        print(f"Promedio de horas de entramiento de Atletismo: {promedioAtletismo}")
else:
    print("No se Registraron Alumnos")
