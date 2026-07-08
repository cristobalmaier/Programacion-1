def ingresar_vehiculo():
    vehiculo = input("Seleccion un vehiculo (SEDAN, SUV, PICKUP): ")
    while vehiculo != "SEDAN" and vehiculo != "SUV" and vehiculo != "PICKUP":
        vehiculo = input("ERROR, Seleccion un vehiculo (SEDAN, SUV, PICKUP): ")
    return vehiculo

def ingresar_años_garantia():
    garantia = int(input("Ingrese año de garantia del (1 y 5): "))
    while garantia < 1 or garantia > 5:
        garantia = int(input("ERROR,Ingrese año de garantia del (1 y 5): "))
    return garantia

def ingresar_precio_vehiculo():
    precio_vehiculo = int(input("Ingrese precio vehiculo: "))
    while precio_vehiculo < 0 and precio_vehiculo < -1:
        precio_vehiculo = int(input("Ingrese precio vehiculo: "))
    return precio_vehiculo

def ingresar_codigo_vendedor():
    codigo = int(input("Ingrese codigo del vendedor (1 al 4 ): "))
    while codigo < 1 or codigo > 4:
        codigo = int(input("Ingrese codigo del vendedor (1 al 4 ): "))
    return codigo

def mostrar(arr_vehiculos,arr_años_garantia,arr_precios_vehiculos,arr_codigos_vendedor,posicion):
    print("--- MOSTRAR ---")
    print(f"Tipo de Vehiculo: {arr_vehiculos[posicion]}")
    print(f"Años de Garantia: {arr_años_garantia[posicion]}")
    print(f"Precio Vehiculo: {arr_precios_vehiculos[posicion]}")
    print(f"Codigo del Vendedor: {arr_codigos_vendedor[posicion]}")

def buscar_por_codigo(arr_codigos_vendedor,codigo):
    i = 0
    while i < len (arr_codigos_vendedor) and arr_codigos_vendedor[i] != codigo:
        i += 1
    return i

def auto_mayor_años_garantia(arr_años_garantia):
    posicion_mayor = 0
    for i in range (len(arr_años_garantia)):
        if arr_años_garantia[i] > arr_años_garantia[posicion_mayor]:
            posicion_mayor = i
    return posicion_mayor

def mostrar_array(arr):
    for i in range (len(arr)):
        print(f"{arr[i]}")

def calcular_promedio(arr_años_garantia):
    acum = 0
    for i in range (len(arr_años_garantia)):
        acum += arr_años_garantia[i]
    promedio = acum/len(arr_años_garantia)
    return promedio

def filtrado_ventas(arr_codigos_vendedores,arr_años_garantia):
    nuevo_arreglo = []
    promedio = calcular_promedio(arr_años_garantia)
    for i in range (len(arr_años_garantia)):
        if arr_años_garantia[i] > promedio:
            nuevo_arreglo.append(arr_codigos_vendedores[i])
    return nuevo_arreglo

def intercambiar(arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_vehiculos,arr_años_garantia,arr_precios_vehiculos,arr_codigos_vendedor):
    for i in range (len(arr_precios_vehiculos)):
        for j in range (len(arr_precios_vehiculos)):
            if arr_precios_vehiculos[i] > arr_precios_vehiculos[j]:
                intercambiar(arr_precios_vehiculos,i,j)
                intercambiar(arr_años_garantia,i,j)
                intercambiar(arr_vehiculos,i,j)
                intercambiar(arr_codigos_vendedor,i,j)

def cargar(arr_vehiculos,arr_años_garantia,arr_precios_vehiculos,arr_codigos_vendedor):

    precio = ingresar_precio_vehiculo()
    while precio != -1:

        vehiculo = ingresar_vehiculo()
        arr_vehiculos.append(vehiculo)

        años_garantia = ingresar_años_garantia()
        arr_años_garantia.append(años_garantia)

        codigo_vendedor = ingresar_codigo_vendedor()
        arr_codigos_vendedor.append(codigo_vendedor)

        arr_precios_vehiculos.append(precio)
        precio = ingresar_precio_vehiculo()

vehiculos = []
años_garantias = []
precios_vehiculos = []
codigos_vendedores = []

cargar(vehiculos,años_garantias,precios_vehiculos,codigos_vendedores)

if len (vehiculos) > 0:

    posicion = int(input("Ingrese la posicion para ver sus datos: "))
    while posicion < 0 or posicion >= len(vehiculos):
        posicion = int(input("Ingrese la posicion para ver sus datos: "))
    mostrar(vehiculos,años_garantias,precios_vehiculos,codigos_vendedores,posicion)

    codigo = int(input("Ingrese codigo del vendedor: "))
    while codigo < 0 or codigo > 4:
        codigo = int(input("Ingrese codigo del vendedor: "))
    posicon = buscar_por_codigo(codigos_vendedores,codigo)
    mostrar(vehiculos,años_garantias,precios_vehiculos,codigos_vendedores,posicon)

    posicion_mayor = auto_mayor_años_garantia(años_garantias)
    print("-- AUTO CON MAS GARANTIAS ---")
    mostrar(vehiculos,años_garantias,precios_vehiculos,codigos_vendedores,posicion_mayor)

    print("VEHICULOS")
    mostrar_array(vehiculos)
    print("AÑOS GARANTIAS")
    mostrar_array(años_garantias)
    print("PRECIOS VEHICULOS")
    mostrar_array(precios_vehiculos)
    print("CODIGOS VENDEDORES")
    mostrar_array(codigos_vendedores)

    promedio = calcular_promedio(años_garantias)
    print(f"PROMEDIO DE AÑOS DE GARANTIAS: {promedio}")

    nuevo_array = filtrado_ventas(codigos_vendedores,años_garantias)
    print("Los codigos de los vendedores que superamen la cantidad de años de garantia al promedio son: ")
    mostrar_array(nuevo_array)

    ordenar(vehiculos,años_garantias,precios_vehiculos,codigos_vendedores)
    print("-- DATOS ORDENADOS --")
    print("-- VEHICULOS --")
    mostrar_array(vehiculos)
    print("-- AÑOS GARANTIAS --")
    mostrar_array(años_garantias)
    print("-- PRECIOS VEHICULOS --")
    mostrar_array(precios_vehiculos)
    print("-- CODIGOS VENDEDORES --")
    mostrar_array(codigos_vendedores)