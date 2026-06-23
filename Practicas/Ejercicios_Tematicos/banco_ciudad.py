cantidad_cliente_1 = 0
cantidad_cliente_2 = 0
cantidad_cliente_3 = 0
contador = 0
acumEdad3 = 0

tipo_cliente = int(input("Ingrese numero de cliente: "))

while tipo_cliente < 0 or tipo_cliente > 3:
    tipo_cliente = int(input("ERROR! Ingrese numero de cliente valido: "))

while tipo_cliente != 0:
    nombre = input("Ingrese su nombre: ")
    while nombre == "":
        nombre = input("ERROR! Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    while edad < 0 or edad > 110:
        edad = int(input("ERROR! Ingrese una edad valida:"))
    
    if tipo_cliente == 1:
        cantidad_cliente_1 += 1
    elif tipo_cliente == 2:
        cantidad_cliente_2 += 1
    else:
        cantidad_cliente_3 += 1
        acumEdad3 += edad
    
    if contador == 0:
        minimo = edad
    elif edad < minimo:
        minimo = edad

    contador += 1
    
    print(f"Nombre del cliente: {nombre}")
    print(f"Tipo de cliente: {tipo_cliente}")
    tipo_cliente = int(input("Ingrese numero de cliente: "))

if contador > 0:
    print(f"Cantidad de clientes tipo 1: {cantidad_cliente_1}")
    print(f"Cantidad de clientes tipo 2: {cantidad_cliente_2}")
    print(f"Cantidad de clientes tipo 3: {cantidad_cliente_3}")
    print(f"La edad del cliente mas joven: {minimo}")
   
    if cantidad_cliente_3 > 0:
        promedioEdades3 = acumEdad3 / cantidad_cliente_3
        print(f"El promedio de edad de los clientes tipo 3: {promedioEdades3}")