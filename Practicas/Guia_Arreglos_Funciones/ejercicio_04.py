"""Haceme una lista de pacientes de una veterinaria. Con nombre, edad y especie. 
Cargar los datos hasta que el nombre sea "FIN". Garantizar que el nombre sea único. 
Mostrar los datos cargados. 
Determinar la persona de mayor y de menor edad y mostrar sus datos. Contar cuántos pacientes hay de cada especie. 
Calcular el promedio de edad de cada especie."""

def ingrese_nombre():
    res = input("Ingrese nombre: ")
    while res == "":
        res = input("Ingrese nombre: ")
    return res

def ingrese_edad():
    res = int(input("Ingrese edad: "))
    while res < 0 or res > 110:
        res = int(input("Ingrese edad: "))
    return res

def ingrese_especie():
    res = input("Ingrese especie: ")
    while res == "":
        res = input("Ingrese especie: ")
    return res

def cargarDatos(x,edades,especies):

    nombre = ingrese_nombre()
    while nombre != "FIN":
        if nombre not in x:
            edad = ingrese_edad()
            especie = ingrese_especie()

            x.append(nombre)
            edades.append(edad)
            especies.append(especie)

        input("Ingrese otro nombre: ")

mascotas = []
años = []
animal = []
veteriania = cargarDatos(mascotas,años,animal)