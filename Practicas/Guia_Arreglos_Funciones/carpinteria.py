"""
La carpintería "La banqueta loca" quiere llevar el registro de los pedidos del mes, para ello se ingresan:

    día entre 1 y 31
    cantidad no negativa
    código cliente entre 10 y 15
    modelo Redondo, alta, baja (guardar en mayusculas)
    la carga finaliza con dia 0

Se pide:

    la cantidad de ventas realizadas
    la cantidad de banquetas encargadas
    el promedio de ventas
    la cantidad de banquetas pedidas x cliente
    porcentajes de banquetas de cada cliente sobre el total
"""

def ingresar_dia():
    dia = int(input("Ingrese día: "))
    while dia < 0 or dia > 31:
        dia = int(input("Ingrese día: "))
    return dia

def ingresar_cantidad():
    cantidad = int(input("Ingrese cantidad: "))
    while cantidad < 0:
        cantidad = int(input("Ingrese cantidad: "))
    return cantidad

def ingresar_codigo_cliente():
    codigo_cliente = int(input("Ingrese código cliente: "))
    while codigo_cliente < 10 or codigo_cliente > 15:
        codigo_cliente = int(input("Ingrese código cliente: "))
    return codigo_cliente

def ingresar_modelo():
    modelo = input("Ingrese modelo (REDONDO, ALTA, BAJA): ")
    while modelo != "REDONDO" and modelo != "ALTA" and modelo != "BAJA":
        modelo = input("Ingrese modelo (REDONDO, ALTA, BAJA): ")
    return modelo

def cargar(arr_dias, arr_cantidades, arr_codigos_clientes, arr_modelos):
    dia = ingresar_dia()
    while dia != 0:
        cantidad = ingresar_cantidad()
        codigo_cliente = ingresar_codigo_cliente()
        modelo = ingresar_modelo()

        arr_dias.append(dia)
        arr_cantidades.append(cantidad)
        arr_codigos_clientes.append(codigo_cliente)
        arr_modelos.append(modelo)

        dia = ingresar_dia()

def calcular_cantidad_ventas(arr_cantidades):
    return len(arr_cantidades)

def calcular_cantidad_banquetas(arr_cantidades):
    acumBanquetas = 0
    for i in range(len(arr_cantidades)):
        acumBanquetas += arr_cantidades[i]
    return acumBanquetas

def promedio_ventas(arr_cantidades):
    banquetas = calcular_cantidad_banquetas(arr_cantidades)
    promedio = banquetas / len(arr_cantidades)
    return promedio

def cantidad_banquetas_x_cliente(arr_codigos_clientes, arr_cantidades, codigo_cliente):
    acum = 0
    for i in range(len(arr_codigos_clientes)):
        if arr_codigos_clientes[i] == codigo_cliente:
            acum += arr_cantidades[i]
    return acum

dias = []
cantidades = []
codigos_clientes = []
modelos = []

cargar(dias, cantidades, codigos_clientes, modelos)

if len(codigos_clientes) > 0:
    
    ventasRealizas = calcular_cantidad_ventas(cantidades)
    print(f"Cantidad de ventas realizadas: {ventasRealizas}")
    banquetasEncargadas = calcular_cantidad_banquetas(cantidades)
    print(f"Cantidad de banquetas encargadas: {banquetasEncargadas}")
    promedioVentas = promedio_ventas(cantidades)
    print(f"Promedio de ventas: ${promedioVentas:.2f}")

    for i in range(10, 16):
        cantidad_banquetas = cantidad_banquetas_x_cliente(codigos_clientes, cantidades, i)
        print(f"El cliente {i} pidió {cantidad_banquetas} banquetas.")
    
    for i in range(10, 16):
        cantidad_banquetas = cantidad_banquetas_x_cliente(codigos_clientes, cantidades, i)
        porcentaje = (cantidad_banquetas / banquetasEncargadas) * 100
        print(f"El cliente {i} representa el {porcentaje:.2f}% de las banquetas pedidas.")