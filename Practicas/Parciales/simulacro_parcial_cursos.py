"""
SIMULACRO DE PARCIAL – INTRODUCCIÓN A LA PROGRAMACIÓN

Una empresa de cursos online desea registrar información sobre los alumnos inscriptos durante el mes.

De cada alumno se ingresa:

- Número de inscripción (0 para finalizar)
- Nombre del alumno
- Edad
- Tipo de curso:
    1 = Programación
    2 = Diseño
    3 = Ciberseguridad
- Cantidad de meses contratados

Precios por mes:

- Programación: $25000
- Diseño: $18000
- Ciberseguridad: $40000

Además:
- Si el alumno contrata más de 4 meses, obtiene un descuento del 10%.
- Si el curso es de Ciberseguridad y contrata más de 8 meses,
  se aplica un recargo del 6%.

Se pide:

a) Mostrar por cada alumno:
    - Nombre
    - Tipo de curso
    - Total a pagar

b) Informar al finalizar:

1. Cantidad de alumnos por tipo de curso.
2. Edad del alumno más joven.
3. Promedio de edad de los alumnos de Ciberseguridad.
4. Total recaudado por la empresa.
5. Porcentaje de alumnos de Diseño sobre el total.
6. Cantidad total de meses contratados.
7. Porcentaje de meses contratados por categoría:
   (meses_categoria / total_meses * 100 )

"""
Programación = 25000
Diseño = 18000
Ciberseguridad = 40000

contadorProgramacion = 0
contadorDiseño = 0
contadorCiberseguridad = 0

acumEdadCiberseguridad = 0
acumTotalRecaudado = 0
acumMesesTotalContratados = 0
acumMesesContratadosProgramacion = 0
acumMesesContratadosDiseño = 0
acumMesesContratadosCiberseguridad = 0
contador = 0

numeroInscripcion = int(input("Ingrese numero de inscripcion: "))

while numeroInscripcion != 0:
    nombre = input("Ingrese nombre: ")
    while nombre == "":
        nombre = input("ERROR! Ingrese un nombre: ")
    edad = int(input("Ingrese edad: "))
    while edad < 0 or edad > 110:
        edad = int(input("ERROR! Ingrese una edad valida: "))
    tipoCurso = int(input("Seleccione: 1.Programacion, 2.Diseño, 3.Ciberseguridad: "))
    while tipoCurso < 1 or tipoCurso > 3:
        tipoCurso = int(input("Seleccione una opcion validad: "))
    mesesContratados = int(input("Ingrese meses contratados: "))
    while mesesContratados < 0:
        mesesContratados = int(input("ERROR! Ingrese una cantidad valida: "))
    
    if tipoCurso == 1:
        contadorProgramacion += 1
        total = mesesContratados * Programación
        if mesesContratados > 4:
            total *= 0.90
        
        acumTotalRecaudado += total
        acumMesesTotalContratados += mesesContratados
        acumMesesContratadosProgramacion += mesesContratados
        
    elif tipoCurso == 2:
        contadorDiseño += 1
        total = mesesContratados * Diseño
        if mesesContratados > 4:
            total *= 0.90
        
        acumTotalRecaudado += total
        acumMesesTotalContratados += mesesContratados
        acumMesesContratadosDiseño += mesesContratados
    else:
        contadorCiberseguridad += 1
        total = mesesContratados * Ciberseguridad
        if mesesContratados > 4:
            total *= 0.90
        if mesesContratados > 8:
            total *= 1.06
        
        acumEdadCiberseguridad += edad
        acumTotalRecaudado += total
        acumMesesTotalContratados += mesesContratados
        acumMesesContratadosCiberseguridad += mesesContratados
    
    if contador == 0:
        edadJoven = edad
    elif edad < edadJoven:
        edadJoven = edad
    
    contador += 1

    print(f"Nombre: {nombre}")
    print(f"Tipo de curso: {tipoCurso}")
    print(f"Total a pagar: {total}")

    numeroInscripcion = int(input("Ingrese numero de inscripcion: "))

if contador > 0:
    print(f"Alumnos de Programacion: {contadorProgramacion}")
    print(f"Alumnos de Diseño: {contadorDiseño}")
    print(f"Alumnos de Ciberseguridad: {contadorCiberseguridad}")
    print(f"Alumno mas joven: {edadJoven} de años")

    if contadorCiberseguridad > 0:
        promedioEdadCiberseguridad = acumEdadCiberseguridad / contadorCiberseguridad
        print(f"Edad promedio de ciberseguridad: {promedioEdadCiberseguridad} años")
    
    print(f"Total Recaudado: ${acumTotalRecaudado}")
    porcentajeAlumnosDiseño = (contadorDiseño / contador) * 100
    print(f"Porcentaje de alumnos de diseño: {porcentajeAlumnosDiseño}%")
    print(f"Total de meses contratados: {acumMesesTotalContratados}")

    porcentajeMesesContratadosProgramacion = (acumMesesContratadosProgramacion / acumMesesTotalContratados) * 100
    porcentajeMesesContratadosDiseño = (acumMesesContratadosDiseño / acumMesesTotalContratados) * 100
    porcentajeMesesContratadosCiberseguridad = (acumMesesContratadosCiberseguridad / acumMesesTotalContratados) * 100

    print(f"Porcentaje de meses contratods de programacion: {porcentajeMesesContratadosProgramacion}%")
    print(f"Porcentaje de meses contratods de Diseño: {porcentajeMesesContratadosDiseño}%")
    print(f"Porcentaje de meses contratods de Ciberseguridad: {porcentajeMesesContratadosCiberseguridad}%")
    

    