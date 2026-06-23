"""
1er EXAMEN PARCIAL DE INTRODUCCIÓN A LA PROGRAMACIÓN

Ejercicio nº 1

Una clínica privada de la Ciudad de Buenos Aires desea registrar información sobre los pacientes que llegan para ser atendidos.

En la clínica existen 3 tipos de atención:

1 = Clínica médica
2 = Pediatría
3 = Traumatología

De cada paciente se conoce la siguiente información:

- Nombre (cadena)
- Edad (entero)
- Tipo de atención (entero de 1 a 3)

Se pide desarrollar un algoritmo que permita:

Por cada paciente:
- Solicitar y mostrar su nombre y el tipo de atención.

Al finalizar informar:

a) La cantidad de pacientes de cada tipo de atención.
b) La edad del paciente más grande (se supone único).
c) El promedio de edades de los pacientes de Traumatología.

Se ingresan datos hasta que el tipo de atención sea 0.

"""

cantidadClinica = 0
cantidadPediatria = 0
cantidadTraumatologia = 0
contador = 0
acumEdadTraumatologia = 0



tipoAtencion = int(input("Ingrese el numero del tipo de atencion (0 para salir): "))
while tipoAtencion < 0 or tipoAtencion > 3:
    tipoAtencion = int(input("ERROR! Ingrese un tipo de atencion valido: "))


while tipoAtencion != 0:
    nombre = input("Ingrese nombre del cliente: ")
    while nombre == "":
        nombre = input("ERROR! Ingrese nombre del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))
    while edad < 0 or edad > 110:
        edad = int(input("ERROR! Ingrese una edad valida: "))
    
    print(f"Nombre: {nombre}")
    print(f"Tipo de atencion: {tipoAtencion}")

    if tipoAtencion == 1:
        cantidadClinica += 1
    elif tipoAtencion == 2:
        cantidadPediatria += 1
    else:
        cantidadTraumatologia +=1
        acumEdadTraumatologia += edad
    
    if contador == 0:
        maximo = edad
    elif edad > maximo:
        maximo = edad
    
    contador += 1

    tipoAtencion = int(input("Ingrese el numero del tipo de atencion (0 para salir): "))

if contador > 0:
    print(f"Cantidad de Pacientes de Clinica Medica: {cantidadClinica}")
    print(f"Cantidad de Pacientes de Pediatria: {cantidadPediatria}")
    print(f"Cantidad de Pacientes de Traumatologia: {cantidadTraumatologia}")
    print(f"El paciente mas grande tiene {maximo} años")

    if cantidadTraumatologia > 0:
        promedio = acumEdadTraumatologia / cantidadTraumatologia
        print(f"El promedio de Edad de los pacientes de Traumatologia es: {promedio}")