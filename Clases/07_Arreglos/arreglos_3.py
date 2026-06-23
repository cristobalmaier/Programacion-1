# DECLARACION DE FUNCIONES

def ingresar_edad ():

    edad = int(input("Ingrese la edad: "))
    while edad < 0 or edad > 120:

        edad = int(input("Ingrese la edad: "))
    return edad

def ingresar_nombre():

    nombre = input("Ingrese el nombre: ")
    while nombre == "":

        nombre = input("Ingrese el nombre: ")
    return nombre

def ingresar_sexo():

    sexo = input("Ingrese el sexo").upper()
    while sexo != "F" and sexo!="M":

        sexo = input("Ingrese el sexo").upper()
    return sexo

def ingresar_indice(tamanio):
    indice = int(input("Ingrese un indice: "))
    while indice < 0 or indice >= tamanio:
        indice = int(input("error..Ingrese un indice: "))
    return indice

def mostrar_datos(arr_nombres, arr_edades, arr_sexos):

    for i in range(len(arr_nombres)):
        print(f"{arr_nombres[i]} => {arr_edades[i]} => {arr_sexos[i]}")

def calcular_maximo(arr_edades):

    indice_mayor = 0

    for i in range(len(arr_edades)):

        if arr_edades[i] > arr_edades[indice_mayor]:

            indice_mayor = i

    return indice_mayor


def calcular_minimo(arr_edades):
    indice_menor = 0

    for i in range(len(arr_edades)):

        if arr_edades[i] < arr_edades[indice_menor]:
            indice_menor = i

    return indice_menor

def calcular_minimo_piola(arr_edades):
    indice_menor = arr_edades[0]

    for i in range(len(arr_edades)):

        if arr_edades[i] < arr_edades[indice_menor]:
            indice_menor = i

    return indice_menor

def contar_mayores (arr_edades):
    cont = 0
    for i in range(len(arr_edades)):
        if arr_edades[i] >= 18:
            cont+=1
    
    return cont

def calcular_promedio(arr_edades, arr_sexos, sexo):
    acum = 0
    cont = 0
    for i in range(len(arr_edades)):
        if arr_sexos[i] == sexo:
            acum += arr_edades[i]
            cont += 1   
    return acum/cont

def buscar(arreglo, dato):
    i = 0
    while i < len(arreglo) and arreglo[i] != dato:
        i+=1
    return i 

def intercambiar(arreglo, i, j):
    aux = arreglo[i]
    arreglo[i] = arreglo[j]
    arreglo[j] = aux

def cargar(arr_nombres, arr_edades, arr_sexos):

    nombre = ingresar_nombre()

    while nombre != "FIN":

        if buscar(arr_nombres, nombre) == len(arr_nombres):
            edad = ingresar_edad()
            sexo = ingresar_sexo()

            arr_nombres.append(nombre)
            arr_edades.append(edad)
            arr_sexos.append(sexo)
        
        else:
            print("Esa persona ya fue cargada")

        nombre = ingresar_nombre()

# PROGRAMA PRINCIPAL

nombres = []
edades = []
sexos = []

# Cargar datos hasta que nombre sea "FIN", garantizar que sea unico
cargar(nombres, edades, sexos)

if len(nombres) > 0:

    # Mostrar los datos cargados
    mostrar_datos(nombres, edades, sexos)

    # Determinar la persona de mayor y de menor edad y mostrar sus datos
    indice_mayor = calcular_maximo(edades)
    print(f"La persona mayor es {nombres[indice_mayor]}, tiene {edades[indice_mayor]} y es del sexo {sexos[indice_mayor]}")
    
    indice_menor = calcular_minimo(edades)
    print(f"La persona menor es {nombres[indice_menor]}, tiene {edades[indice_menor]} y es del sexo {sexos[indice_menor]}")

    # Contar la cantidad de personas mayores de edad
    cantidad_personas_mayores = contar_mayores(edades)
    print("La cantidad mayores de edad son:", cantidad_personas_mayores)

    # Promedio de edades de mujeres
    indice_f = buscar(sexos, "F")
    if indice_f < len(sexos):
        promedio = calcular_promedio(edades, sexos, "F")
    else:
        print("No hay mujeres")

    # Solicitar al usuario 2 valores e intercambiar los datos
    indice_1 = ingresar_indice(len(nombres))
    indice_2 = ingresar_indice(len(nombres))
    intercambiar(nombres, indice_1, indice_2)
    intercambiar(edades, indice_1, indice_2)
    intercambiar(sexos, indice_1, indice_2)

else:
    print("No se cargaron datos")