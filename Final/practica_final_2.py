"""
1. Carga de Datos y Validación
Implementar la carga de datos de los clientes en arreglos paralelos. El ingreso de datos finalizará cuando en el campo Precio del abono se ingrese el valor -1.

Por cada cliente, se deberán solicitar y validar los siguientes datos:

    Tipo de abono: Debe ser estrictamente "CARDIO", "MAQUINAS" o "PREMIUM".

    Cantidad de días de entreno por semana: Debe ser un valor entero entre 1 y 7.

    Precio del abono: No puede ser un valor negativo (a excepción del -1 que actúa como condición de corte).

    Código del cliente: Debe ser un valor entero entre 1 y 5.

2. Función de Visualización Individual
Crear una función que reciba como parámetro una posición (índice) y todos los arreglos cargados, y muestre por pantalla de forma ordenada todos los datos relacionados a ese cliente en particular.

3. Búsqueda por Código de Cliente
Crear e invocar una función de búsqueda. Una vez finalizada la carga del Punto 1, el sistema debe solicitar al usuario el ingreso de un código de cliente por consola.

La función debe buscar dicho código y retornar la posición en la que se encuentra.

Posteriormente, se deben mostrar todos los datos del cliente encontrado utilizando la función desarrollada en el Punto 2.

4. Cliente con Mayor Asistencia
Crear e invocar una función que identifique al cliente que entrena la mayor cantidad de días a la semana.

La función debe retornar la posición de dicho cliente.

Luego, se deben mostrar todos sus datos en pantalla utilizando la función del Punto 2.

5. Función de Visualización de Arreglos
Crear una función genérica que, dado un arreglo pasado por parámetro, recorra y muestre todos sus valores en pantalla.

6. Cálculo de Promedio
Crear e invocar una función que calcule y retorne el promedio de la cantidad de días de entrenamiento de todos los clientes registrados.

7. Filtrado de Clientes (Superior al Promedio)
Crear e invocar una función que genere y devuelva un nuevo arreglo. En este se deben almacenar únicamente los códigos de aquellos clientes cuya cantidad de días de entrenamiento sea estrictamente superior al promedio calculado en el Punto 6.

8. Ordenamiento Descendente
Crear e invocar una función para ordenar todos los datos cargados de manera descendente tomando como criterio el Precio del abono (del más caro al más barato).

Nota: Al tratarse de arreglos paralelos, recuerde mantener la correspondencia de los índices al realizar los intercambios.

Una vez ordenados, mostrar el contenido de todos los arreglos utilizando la función del Punto 5.
"""

def ingresar_tipo_abono():
    tipo_abono = input("Seleccion tipo de abono (CARDIO, MAQUINAS, PREMIUM): ")
    while tipo_abono != "CARDIO" and tipo_abono != "MAQUINAS" and tipo_abono != "PREMIUM":
        tipo_abono = input("Seleccion tipo de abono (CARDIO, MAQUINAS, PREMIUM): ")
    return tipo_abono

def ingresar_cantidad_dias_por_semana():
    cantidad_dias_por_semana = int(input("Ingrese la cantidad de dias de entreno por semana: "))
    while cantidad_dias_por_semana < 1 or cantidad_dias_por_semana > 7:
        cantidad_dias_por_semana = int(input("Ingrese la cantidad de dias de entreno por semana: "))
    return cantidad_dias_por_semana

def ingresar_precio_abono():
    precio_abono = float(input("Ingrese precio de abono: "))
    while precio_abono < 0 and precio_abono != -1:
        precio_abono = float(input("Ingrese precio de abono: "))
    return precio_abono

def ingresar_codigo_cliente():
    codigo_cliente = int(input("Ingres codigo de cliente: "))
    while codigo_cliente < 1 or codigo_cliente > 5:
        codigo_cliente = int(input("Ingres codigo de cliente: "))
    return codigo_cliente

def mostrar_por_cliente(arr_tipos_abonos,arr_cantidades_dias_por_semana,arr_precios_abonos,arr_codigos_clientes,posicion):
    print(f"Tipo Abono: {arr_tipos_abonos[posicion]}")
    print(f"Cantidad de dias de entro por semana: {arr_cantidades_dias_por_semana[posicion]}")
    print(f"Precio Abono: {arr_precios_abonos[posicion]}")
    print(f"Codigo Cliente: {arr_codigos_clientes[posicion]}")

def buscar_por_codigo(arr_codigos_clientes,codigo):
    i = 0
    while i < len (arr_codigos_clientes) and arr_codigos_clientes[i] != codigo:
        i += 1
    return i

def buscar_mas_entrena(arr_cantidades_dias_por_semana):
    posicon_mayor = 0
    for i in range (len(arr_cantidades_dias_por_semana)):
        if arr_cantidades_dias_por_semana[i] > arr_cantidades_dias_por_semana[posicon_mayor]:
            posicon_mayor = i
    return posicon_mayor

def mostrar_array(arr):
    for i in range (len(arr)):
        print(f"{arr[i]}")

def calcular_promedio_dias_entreno(arr_cantidaes_dias_por_semana):
    acum = 0
    for i in range (len(arr_cantidaes_dias_por_semana)):
        acum += arr_cantidaes_dias_por_semana[i]
    promedio = acum / len(arr_cantidaes_dias_por_semana)
    return promedio    

def crear_nuevo_arreglo_que_entranan_mayor_al_promedio(arr_cantidades_dias_por_semana,arr_codigos_clientes):
    promedio = calcular_promedio_dias_entreno(arr_cantidades_dias_por_semana)
    nuevo_arreglo = []
    for i in range (len(arr_cantidades_dias_por_semana)):
        if arr_cantidades_dias_por_semana[i] > promedio:
            nuevo_arreglo.append(arr_codigos_clientes[i])
    return nuevo_arreglo
    

def intercambiar(arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_tipos_abonos,arr_cantidades_dias_por_semana,arr_precios_abonos,arr_codigos_clientes):
    for i in range (len(arr_precios_abonos)):
        for j in range (len(arr_precios_abonos)):
            if arr_precios_abonos[i] > arr_precios_abonos[j]:
                intercambiar(arr_tipos_abonos,i,j)
                intercambiar(arr_cantidades_dias_por_semana,i,j)
                intercambiar(arr_precios_abonos,i,j)
                intercambiar(arr_codigos_clientes,i,j)

def cargar(arr_tipos_abonos,arr_cantidades_dias_por_semana,arr_precios_abonos,arr_codigos_clientes):

    precio_abono = ingresar_precio_abono()
    while precio_abono != -1:

        tipo_abono = ingresar_tipo_abono()
        dias_entreno = ingresar_cantidad_dias_por_semana()
        codigo_cliente = ingresar_codigo_cliente()

        arr_precios_abonos.append(precio_abono)
        arr_tipos_abonos.append(tipo_abono)
        arr_cantidades_dias_por_semana.append(dias_entreno)
        arr_codigos_clientes.append(codigo_cliente)

        precio_abono = ingresar_precio_abono()

tipos_abonos = []
cantidades_dias_por_semana = []
precios_abonos = []
codigos_clientes = []


cargar(tipos_abonos,cantidades_dias_por_semana,precios_abonos,codigos_clientes)

if len (tipos_abonos) > 0:

    print("--- Punto 2 ---")
    posicion = int(input("Ingrese posicion para mostrar datos en esa posicion: "))
    if posicion < 0 or posicion >= len(tipos_abonos):
        print("Posicion ingresada no es valida")
    else:
        print("--- Datos del cliente en la posicion ingresada ---")
        mostrar_por_cliente(tipos_abonos,cantidades_dias_por_semana,precios_abonos,codigos_clientes,posicion)


    print("--- Punto 3 ---")
    codigo = int(input("Ingrese el codigo del cliente para poder ver sus datos: "))
    while codigo <= 0 or codigo >= 6 :
        codigo = int(input("Ingrese el codigo del cliente para poder ver sus datos: "))
    indice = buscar_por_codigo(codigos_clientes,codigo)
    mostrar_por_cliente(tipos_abonos,cantidades_dias_por_semana,precios_abonos,codigos_clientes,indice)

    print("--- Punto 4 ---")
    indice_2 = buscar_mas_entrena(cantidades_dias_por_semana)
    mostrar_por_cliente(tipos_abonos,cantidades_dias_por_semana,precios_abonos,codigos_clientes,indice_2)

    print("--- Punto 5 ---")
    print("--- Tipos de abonos ---")
    mostrar_array(tipos_abonos)
    print("--- Cantidades de dias por semana ---")
    mostrar_array(cantidades_dias_por_semana)
    print("--- Precios Abonos ---")
    mostrar_array(precios_abonos)
    print("--- Codigos Clientes ---")
    mostrar_array(codigos_clientes)

    print("--- Punto 6 ---")
    promedio = calcular_promedio_dias_entreno(cantidades_dias_por_semana)
    print(f"Promedio de entreno por semana: {promedio}")

    print("--- Punto 7 ---")
    nuevos_codigos = crear_nuevo_arreglo_que_entranan_mayor_al_promedio(cantidades_dias_por_semana,codigos_clientes)
    print("Los codigos de los clientes que entrenan mas dias que el promedio son:")
    mostrar_array(nuevos_codigos)
    
    print("--- Punto 8 ---")
    ordenar(tipos_abonos,cantidades_dias_por_semana,precios_abonos,codigos_clientes)
    print("--- DATOS ORDENADOS ---")
    print("--- Precios Abonos ---")
    mostrar_array(precios_abonos)
    print("--- Tipos de abonos ---")
    mostrar_array(tipos_abonos)
    print("--- Cantidades de dias por semana ---")
    mostrar_array(cantidades_dias_por_semana)
    print("--- Codigos Clientes ---")
    mostrar_array(codigos_clientes)
    print("--- DATOS ORDENADOS ---")

else:
    print("NO HAY DATOS CARGADOS")