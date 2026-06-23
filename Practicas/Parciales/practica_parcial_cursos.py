"""
Se desea realizar un sistema para la gestión de cursos online de una plataforma educativa. Para ello, se cargará la siguiente información de cada curso:

Código del curso
Categoría del curso (PROGRAMACION, DISEÑO o MARKETING)
Cupo máximo de alumnos
Cantidad de alumnos inscriptos

Se pide:

a) Cargar:

Registrar cursos: Código, Categoría, Cupo máximo e Inscriptos -> 4 arreglos.

Ingresar datos hasta que en categoría se ingrese "FIN".

Validar los datos de entrada con criterio lógico.

b) Mostrar los datos de todos los cursos cargados (Código, Categoría y Cupo máximo) junto con su porcentaje de ocupación.

Si este es mayor al 90%, mostrar un mensaje indicando que el curso está próximo a completarse.

c) Calcular el promedio de alumnos inscriptos, tanto para los cursos de PROGRAMACION como para los de DISEÑO (por separado).

d) Reemplazar con PREMIUM_i en Código, los cursos de PROGRAMACION con cupo máximo de 50 alumnos.

i debe ser un número único.

(Ej: PREMIUM_1, PREMIUM_2, PREMIUM_3, etc.)

e) Calcular y mostrar los datos del curso con mayor cantidad de vacantes disponibles.

f) Solicitar al usuario un Código y, si existe, mostrar todos los datos asociados y eliminarlo.

Caso contrario, informar que no existe.

g) Solicitar los datos de un nuevo curso e insertarlo en la posición anterior al curso con menor cantidad de alumnos inscriptos.

h) Ordenar de mayor a menor según la cantidad de alumnos inscriptos.
"""

def ingresar_codigo():
    codigo = input("Ingrese codigo: ")
    while codigo == "":
        codigo = input("Ingrese codigo: ")
    return codigo

def ingresar_categoria():
    categoria = input("Ingrese categoria (PROGRAMACION, DISEÑO, MARKETING): ")
    while categoria != "PROGRAMACION" and categoria != "DISEÑO" and categoria != "MARKETING" and categoria != "FIN":
        categoria = input("Ingrese categoria (PROGRAMACION, DISEÑO, MARKETING): ")
    return categoria

def ingresar_cupos_maximos():
    cupo_maximo = int(input("Ingrese cupos maximos: "))
    while cupo_maximo < 1 or cupo_maximo > 50:
        cupo_maximo = int(input("Ingrese cupos maximos: "))
    return cupo_maximo

def ingresar_alumnos_inscriptos(cupo_maximo):
    alumnos_inscriptos = int(input("Ingrese la cantidad de alumnos inscriptos: "))
    while alumnos_inscriptos < 0  or alumnos_inscriptos > cupo_maximo:
        alumnos_inscriptos = int(input("ERROR! Ingrese la cantidad de alumnos inscriptos: "))
    return alumnos_inscriptos

def cantidad_alumnos_inscriptos_programacion(arr_categorias):
    cont = 0
    for i in range (len(arr_categorias)):
        if arr_categorias[i] == "PROGRAMACION":
            cont +=1
        else:
            print("No hay alumnos de PROGRAMACION")

def cantidad_alumnos_inscriptos_diseño(arr_categorias):
    cont = 0
    for i in range (len(arr_categorias)):
        if arr_categorias[i] == "DISEÑO":
            cont +=1
        else:
            print("No hay alumnos de DISEÑO")

def cantidad_alumnos_inscriptos_marketing(arr_categorias):
    cont = 0
    for i in range (len(arr_categorias)):
        if arr_categorias[i] == "MARKETING":
            cont +=1
        else:
            print("No hay alumnos de MARKETING")

def mostrar(arr_codigos,arr_categorias,arr_cupos_maximos,arr_alumnos_inscriptos):
    for i in range (len(arr_codigos)):
        porcentaje = calcular_porcentaje_ocupacion(arr_cupos_maximos[i],arr_alumnos_inscriptos[i])
        print("---------------------")
        print(f"Codigo: {arr_codigos[i]}")
        print(f"Categoria: {arr_categorias[i]}")
        print(f"Cupos Maximos: {arr_cupos_maximos[i]}")
        print(f"Alumnos Insciptos: {arr_alumnos_inscriptos[i]}")
        print(f"Ocupacion: {porcentaje}%")
        print("---------------------")

def calcular_porcentaje_ocupacion(cupo_maximo,alumnos_inscriptos):
    porcentaje = (alumnos_inscriptos / cupo_maximo) * 100
    return porcentaje


def calcular_mayor_cantidad_vacantes(arr_codigos,arr_categorias,arr_cupos_maximos,arr_alumnos_inscriptos):
    indice_mayor = 0
    
    for i in range (len(arr_alumnos_inscriptos)):
        vacantes_actual = (arr_cupos_maximos[i], arr_alumnos_inscriptos[i])
        vacante_mayor = (arr_cupos_maximos[indice_mayor] - arr_alumnos_inscriptos[i])

        if vacantes_actual > vacante_mayor:
            indice_mayor = i
    return indice_mayor

def calcular_promedio_inscriptos_programacion(arr_categorias,arr_alumnos_inscriptos):
    cont = 0
    acum = 0
    for i in range (len(arr_alumnos_inscriptos)):
        if arr_categorias[i] == "PROGRAMACION":
            acum += arr_alumnos_inscriptos[i]
            cont += 1
    promedio = acum / cont

    return promedio

def calcular_promedio_inscriptos_diseño(arr_categorias,arr_alumnos_inscriptos):
    cont = 0
    acum = 0
    for i in range (len(arr_alumnos_inscriptos)):
        if arr_categorias[i] == "DISEÑO":
            acum += arr_alumnos_inscriptos[i]
            cont += 1
    promedio = acum / cont
    return promedio

def reemplazar_codigo_programacion(arr_categorias,arr_cupos_maximos,arr_codigos):
    cont = 1
    for i in range (len(arr_categorias)):
        if arr_categorias[i] == "PROGRAMACION" and arr_cupos_maximos[i] == 50:
            arr_codigos[i] = f"PREMIUM_{cont}" 
            cont += 1
        else:
            print("NO se reemplazo el codigo")



def cargar(arr_codigos,arr_categorias,arr_cupos_maximos,arr_alumnos_inscriptos):

    codigo = ingresar_codigo()
    categoria = ingresar_categoria()
    while categoria != "FIN":
        arr_codigos.append(codigo)
        arr_categorias.append(categoria)

        cupo_maximo = ingresar_cupos_maximos()
        arr_cupos_maximos.append(cupo_maximo)

        alumnos_inscriptos = ingresar_alumnos_inscriptos(cupo_maximo)
        arr_alumnos_inscriptos.append(alumnos_inscriptos)
        
        codigo = ingresar_codigo()
        categoria = ingresar_categoria()

codigos = []
categorias = []
cupos_maximos = []
alumnos_inscriptos = []