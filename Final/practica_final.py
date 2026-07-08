"""
1.Ingresar los siguientes datos en arreglos paralelos hasta que el número de pedido sea 0 (cero): 
    Número de pedido. 
    Tipo de menú (valores posibles: “CLÁSICO”, “VEGETARIANO”, “SIN TACC”). 
    Mes de entrega (valor entre 1 y 12). 
    Cantidad de viandas solicitadas (valor positivo). 

Importante: Realizar la validación de al menos dos de los datos ingresados. 

2. Mostrar los datos de un pedido: Crear una función para mostrar todos los datos asociados  un pedido,
recibiendo como parámetro una posición y todos los arreglos correspondientes. 
3. Crear e invocar una función que permita buscar un pedido por número de pedido. 
Esta función debe devolver la posición en la que se encuentra. Una vez finalizada la carga de datos del punto 1, 
ingresar por consola un número de pedido, invocar la función y luego mostrar los datos correspondientes utilizando la función del punto 2. 
4. Crear e invocar una función que determine el pedido con la mayor cantidad de viandas solicitadas. La función debe devolver la posición. Luego, mostrar todos los datos de ese pedido utilizando la función del punto 2. 
5.Crear una función que, dado un arreglo, muestre todos los valores del mismo. 
6. Crear e invocar una función que ordene de forma descendente todos los pedidos según el mes de entrega. Luego, mostrar todos los arreglos paralelos invocando, las veces que sea necesario, la función del punto 5. 
"""

def ingresar_numero_pedido():
    numero_pedido = int(input("Ingrese numero de pedido: "))
    while numero_pedido < 0:
        numero_pedido = int(input("Ingrese numero de pedido: "))
    return numero_pedido

def ingresar_tipo_menu():
    tipo_menu = input("Seleccione menu (CLÁSICO, VEGETARIANO, SIN TACC): ")
    while tipo_menu != "CLÁSICO" and tipo_menu != "VEGETARIANO" and tipo_menu != "SIN TACC":
        tipo_menu = input("Seleccione menu (CLÁSICO, VEGETARIANO, SIN TACC): ")
    return tipo_menu

def ingresar_mes_entrega():
    mes_entraga = int(input("Ingrese mes de entrega: "))
    while mes_entraga < 1 or mes_entraga > 12:
        mes_entraga = int(input("Ingrese mes de entrega: "))
    return mes_entraga

def ingresar_viandas():
    viandas = int(input("Ingrese viandas solicitadas: "))
    while viandas <= 0:
        viandas = int(input("Ingrese viandas solicitadas: "))
    return viandas

def cargar(arr_numeros_pedidos,arr_tipos_menus,arr_meses_entregas,arr_viandas):

    numero_pedido = ingresar_numero_pedido()
    while numero_pedido != 0:

        tipo_menu = ingresar_tipo_menu()
        mes_entrega = ingresar_mes_entrega()
        cantidad_viandas = ingresar_viandas()

        arr_numeros_pedidos.append(numero_pedido)
        arr_tipos_menus.append(tipo_menu)
        arr_meses_entregas.append(mes_entrega)
        arr_viandas.append(cantidad_viandas)

        numero_pedido = ingresar_numero_pedido()


def mostrar(arr_numeros_pedidos,arr_tipos_menus,arr_meses_entregas,arr_viandas,posicion):
    print(f"Numero Pedido: {arr_numeros_pedidos[posicion]}")
    print(f"Tipo de Menu: {arr_tipos_menus[posicion]}")
    print(f"Mes de Entrega: {arr_meses_entregas[posicion]}")
    print(f"Cantidad de Viandas: {arr_viandas[posicion]}")

def buscar_por_numero_pedido(arr_numeros_pedidos,numero):
    i = 0
    while i < len(arr_numeros_pedidos) and arr_numeros_pedidos[i] != numero:
        i += 1
    return i

def buscar_pedido_mayor_viandas(arr_cantidad_viandas):
    posicion_mayor = 0
    for i in range (len(arr_cantidad_viandas)):
        if arr_cantidad_viandas[i] > arr_cantidad_viandas[posicion_mayor]:
            posicion_mayor = i
    return posicion_mayor

def mostrar_array(arr):
    for i in range (len(arr)):
        print(arr[i])

def intercambiar (arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_numeros_pedidos,arr_tipos_menus,arr_meses_entregas,arr_viandas):
    for i in range (len(arr_meses_entregas)):
        for j in range (len(arr_meses_entregas)):
            if arr_meses_entregas[i] < arr_meses_entregas[j]:
                intercambiar(arr_numeros_pedidos,i,j)
                intercambiar(arr_tipos_menus,i,j)
                intercambiar(arr_meses_entregas,i,j)
                intercambiar(arr_viandas,i,j)

numeros_pedidos = []
tipos_menus = []
meses_entregas = []
cantidades_viandas = []

cargar(numeros_pedidos,tipos_menus,meses_entregas,cantidades_viandas)

if len(numeros_pedidos) > 0:

    print("---- Punto 2 ----")
    posicion = int(input("Ingrese una posicion para ver los datos: "))
    while posicion < 0 or posicion >= len(numeros_pedidos):
        posicion = int(input("Ingrese una posicion para ver los datos: "))
    mostrar(numeros_pedidos,tipos_menus,meses_entregas,cantidades_viandas,posicion)

    print("---- Punto 3 ----")
    numero = int(input("Ingrese numero de pedido: "))
    indice = buscar_por_numero_pedido(numeros_pedidos,numero)
    if indice < len(numeros_pedidos):
        mostrar(numeros_pedidos,tipos_menus,meses_entregas,cantidades_viandas,indice)
    else:
        print("NO hay datos cargados con ese numero de pedido")
    
    print("---- Punto 4 ----")
    posicon_mayor = buscar_pedido_mayor_viandas(cantidades_viandas)
    mostrar(numeros_pedidos,tipos_menus,meses_entregas,cantidades_viandas,posicon_mayor)

    print("---- Punto 5 ----")
    print("---- Numeros de Pedidos ----")
    mostrar_array(numeros_pedidos)
    print("---- Tipos de menu ----")
    mostrar_array(tipos_menus)
    print("---- Meses de entregas ----")
    mostrar_array(meses_entregas)
    print("---- Cantidades de viandas ----")
    mostrar_array(cantidades_viandas)

    print("---- Punto 6 ----")
    ordenar(numeros_pedidos,tipos_menus,meses_entregas,cantidades_viandas)
    print("|---- ORDENADO ----|")
    print("---- Numeros de Pedidos ----")
    mostrar_array(numeros_pedidos)
    print("---- Tipos de menu ----")
    mostrar_array(tipos_menus)
    print("---- Meses de entregas ----")
    mostrar_array(meses_entregas)
    print("---- Cantidades de viandas ----")
    mostrar_array(cantidades_viandas)
    print("|---- ORDENADO ----|")
else:
    print("NO HAY DATOS CARGADOS")