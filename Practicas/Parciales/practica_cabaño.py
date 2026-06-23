"""
La administración del camping comunitario “EcoRío” decide contratarles para organizar y procesar las reservas de parcelas y
alojamientos realizadas durante la temporada. Para eso, les solicitan desarrollar un programa que cumpla con los siguientes
requerimientos:
Carga de datos en arreglos paralelos
Ingresar los siguientes datos en arreglos paralelos hasta que el número de reserva sea 0 (cero):
    -Número de reserva
    -Tipo de alojamiento (valores posibles: “CARPA”, “RODANTE”, “CABAÑA”)
    -Mes de ingreso (valor entre 1 y 12)
    -Días de estadía (valor positivo)
Importante: Realizar la validación de al menos uno de los datos.

- Crear una función para mostrar todos los datos asociados a una reserva, recibiendo como parámetro una posición y
todos los arreglos correspondientes.
- Crear e invocar una función que permita buscar una reserva por número de reserva. Esta función debe devolver la
posición en la que se encuentra. Una vez finalizada la carga de datos del punto 1, ingresar por consola un número de
reserva, invocar la función y luego mostrar los datos correspondientes utilizando la función del punto 2.
- Crear e invocar una función que determine la reserva con mayor cantidad de días de estadía.
La función debe devolver la posición. Luego, mostrar todos los datos de esa reserva utilizando la función del punto 2.
- Crear una función que, dado un arreglo, muestre todos los valores del mismo.
- Crear e invocar una función que permita calcular el promedio de los dìas de estadía
- Crear e Invocar una función que ordene de forma descendente todas las reservas por mes de ingreso.
Luego, mostrar todos los arreglos paralelos invocando las veces que sea necesario, la función del punto 5
"""


def ingresar_numero_reserva():
    numero_reserva = int(input("Ingrese numero de reserva: "))
    while numero_reserva < 0:
        numero_reserva = int(input("Ingrese numero de reserva: "))
    return numero_reserva

def ingresar_alojamiento():
    alojamiento = input("Ingrese alojamiento (CARPA, RODANTE, CABAÑA): ")
    while alojamiento != "CARPA" and alojamiento != "RODANTE" and alojamiento != "CABAÑA":
        alojamiento = input("Ingrese alojamiento (CARPA, RODANTE, CABAÑA): ")
    return alojamiento

def ingresar_mes():
    mes = int(input("Ingrese mes de ingreso (1 - 12): "))
    while mes < 1 or mes > 12:
        mes = int(input("Ingrese mes de ingreso (1 - 12): "))
    return mes

def ingresar_dia_estadia():
    dia_estadia = int(input("Ingrese dia de estadia: "))
    while dia_estadia < 0:
        dia_estadia = int(input("Ingrese dia de estadia: "))
    return dia_estadia

def mostrar_datos_por_posicion(arr_numero_reserva,arr_alojamientos,arr_meses,arr_dias_estadia,posicion):
    

numeros_reserva = []
alojamientos = []
meses = []
dias_estadia = []