"""
Un dentista de la zona, le solicito que realizar un programa para poder llevar su agenda de turnos.

En el mismo debe existir un menú para que la secretaria pueda realizar sus tareas con facilidad,
ya que según lo que ella misma informa " La computadora no es su amiga" 

En el menú deben visualizarse las siguientes opciones:

    1- Ingresar turnos 

    2- Ver turnos 

    3- Eliminar turnos cancelados

    4- Ver estadísticas

    5- Salir 

En cada ítem del menú deberá:

1- Ingresar turnos:

El doc. solo atiende 23 pacientes por día, los datos que se registran de cada paciente son los siguientes: 

·        Nombre

·        Número de socio 

·        Horario ( de 8 a 20hs)

·        Tratamiento ( Control, arreglo de caries, ortodoncia, extracción) 

2- Ver turnos:

Debe mostrar todos los turnos ordenados de menor a mayor según el horario asignado mostrando todos los datos de cada paciente en forma prolija y clara ( DAR FORMATO) 

3- Eliminar turnos

Si un cliente llama para eliminar el turno, la secretaria le pedirá su número de socio y se eliminará el turno. 

4- Ver estadísticas:

·        Porcentaje de todos los pacientes que se realizan ortodoncia

·        Cantidad de pacientes a atender antes de las 16hs
"""

def ingresar_nombre():
    nombre = input("Ingrese nombre: ")
    while nombre == "":
        nombre = input("Ingrese nombre: ")
    return nombre

def ingresar_numero_socio(arr_numeros_socios):
    
    num_socio = int(input("Ingrese numero de socio: "))
    while num_socio < 0:
        num_socio = int(input("Ingrese numero de socio: "))
    
    while num_socio in arr_numeros_socios:
        print("Ese numero de socio ya existe, ingrese otro")
        num_socio = int(input("Ingrese numero de socio: "))
        while num_socio < 0:
            num_socio = int(input("Ingrese numero de socio: "))
    
    return num_socio

def calcular_pacientes_ortodoncia(arr_tratamientos):
    cont = 0
    for i in range (len(arr_tratamientos)):
        if arr_tratamientos[i] == "ortodoncia":
            cont += 1
    porcentaje = (cont / len(arr_tratamientos)) * 100
    return porcentaje
    
def ingresar_horario ():
    horario = int(input("Ingrese horario (de 8 a 20): "))
    while horario < 8 or horario > 20:
        horario = int(input("Ingrese horario (de 8 a 20): "))
    return horario

def ingresar_tratamiento():
    tratamiento = input("Ingrese tratamiento (Control, arreglo de caries, ortodoncia, extracción): ")
    while tratamiento != "Control" and tratamiento != "arreglo de caries" and tratamiento != "ortodoncia" and tratamiento != "extracción":
        tratamiento = input("Ingrese tratamiento (Control, arreglo de caries, ortodoncia, extracción):")
    return tratamiento

def intercambiar(arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_nombres,arr_numeros_socios,arr_horarios,arr_tratamientos):
    for i in range (len(arr_horarios)):
        for j in range (len(arr_horarios)):
            if arr_horarios[i] < arr_horarios[j]:
                intercambiar(arr_nombres,i,j)
                intercambiar(arr_numeros_socios,i,j)
                intercambiar(arr_horarios,i,j)
                intercambiar(arr_tratamientos,i,j)

def mostrar (arr_nombres,arr_numeros_socios,arr_horarios,arr_tratamientos):
    for i in range (len(arr_nombres)):
        print("-----------------------------")
        print(f"Nombre: {arr_nombres[i]}")
        print(f"Numero de socio: {arr_numeros_socios[i]}")
        print(f"Horario: {arr_horarios[i]}")
        print(f"Tratamiento: {arr_tratamientos[i]}")
        print("-----------------------------")

def calcular_pacientes_16hs(arr_horarios):
    cont = 0
    for i in range (len(arr_horarios)):
        if arr_horarios[i] < 16:
            cont += 1
    return cont

def ingresar_turno(arr_nombres,arr_numeros_socios,arr_horarios,arr_tratamientos):
    
    if len(arr_nombres) < 23:
        nombre = ingresar_nombre()
        arr_nombres.append(nombre)
        num_socio = ingresar_numero_socio(arr_numeros_socios)
        arr_numeros_socios.append(num_socio)
        horario = ingresar_horario()
        arr_horarios.append(horario)
        tratamiento = ingresar_tratamiento()
        arr_tratamientos.append(tratamiento)
    else:
        print("No se pueden ingresar mas turnos, el doctor solo atiende 23 pacientes por dia")

def eliminar_turno(arr_numeros_socios,dato_a_buscar):
    i = 0
    while i < len(arr_numeros_socios) and arr_numeros_socios[i] != dato_a_buscar:
        i += 1
    return i

def menu(arr_nombres,arr_numeros_socios,arr_horarios,arr_tratamientos):
    

    print("----- Menu ----")
    print("1. Ingresar Turno")
    print("2. Ver Turnos")
    print("3. Eliminar Turnos")
    print("4. Estadisticas")
    print("5. Salir")
    
    opc = int(input("Ingrese una opcion: "))

    while opc != 5:
        if opc == 1:
            ingresar_turno(arr_nombres,arr_numeros_socios,arr_horarios,arr_tratamientos)
        elif opc == 2:
            if len(arr_nombres) > 0:
                ordenar(arr_nombres,arr_numeros_socios,arr_horarios,arr_tratamientos)
                print("---- Datos Ordenados por horario ----")
                mostrar(arr_nombres,arr_numeros_socios,arr_horarios,arr_tratamientos)
            else:
                print("NO HAY DATOS PARA MOSTRAR")
        elif opc == 3:
            datoBuscar = int(input("para eliminiar el turno, ingrese numero de socio: "))
            indice = eliminar_turno(arr_numeros_socios,datoBuscar)
            if indice < len(arr_numeros_socios):
                print("Dato Encontrado")
                arr_nombres.pop(indice)
                arr_numeros_socios.pop(indice)
                arr_horarios.pop(indice)
                arr_tratamientos.pop(indice)
                print("Turno Eliminado")
                mostrar(arr_nombres,arr_numeros_socios,arr_horarios,arr_tratamientos)
            else:
                print("No existe ese numero de socio")
        elif opc == 4:
            if len(arr_tratamientos) > 0:
                porcentaje_pacientes_ortodoncia  = calcular_pacientes_ortodoncia(arr_tratamientos)
                print(f"porcentaje de pacientes de ortodoncia: {porcentaje_pacientes_ortodoncia:.2f}%")
            else:
                print(f"No hay pacientes con ortodoncia")
            pacientes_antes_16hs = calcular_pacientes_16hs(arr_horarios)
            print(f"Cantidad de pacientes antes de las 16hs: {pacientes_antes_16hs}")
        else:
            print("Opcion invalida")

        print("----- Menu ----")
        print("1. Ingresar Turno")
        print("2. Ver Turnos")
        print("3. Eliminar Turnos")
        print("4. Estadisticas")
        print("5. Salir")
        opc = int(input("Ingrese una opcion: "))

nombres = []
numeros_socios = []
horarios = []
tratamientos = []

menu(nombres,numeros_socios,horarios,tratamientos)