def ingresar_reserva():
    numero_reserva = input("Ingrese el número de reserva: ")
    while numero_reserva < 0:
        numero_reserva = input("Ingrese el número de reserva: ")
    return numero_reserva

def ingresar_tipo_alojamiento():
    tipo_alojamiento = input("Ingrese el tipo de alojamiento (CARPA, RODANTE, CABAÑA): ")
    while tipo_alojamiento != "CARPA" and tipo_alojamiento != "RODANTE" and tipo_alojamiento != "CABAÑA":
        tipo_alojamiento = input("Ingrese el tipo de alojamiento (CARPA, RODANTE, CABAÑA): ")
    return tipo_alojamiento

def ingresar_mes_ingreso():
    mes_ingreso = input("Ingrese el mes de ingreso (1-12): ")
    while mes_ingreso < 1 or mes_ingreso > 12:
        mes_ingreso = input("Ingrese el mes de ingreso (1-12): ")
    return mes_ingreso

def ingresar_dias_estadia():
    dias_estadia = input("Ingrese la cantidad de días de estadía: ")
    while dias_estadia < 0:
        dias_estadia = input("Ingrese la cantidad de días de estadía: ")
    return dias_estadia

def mostrar_por_posicion(arr_reservas, arr_tipos_alojamiento, arr_meses_ingreso, arr_dias_estadia, posicion):
    print(f"Reserva: {arr_reservas[posicion]}")
    print(f"Tipo de alojamiento: {arr_tipos_alojamiento[posicion]}")
    print(f"Mes de ingreso: {arr_meses_ingreso[posicion]}")
    print(f"Días de estadía: {arr_dias_estadia[posicion]}")

def buscar_por_reserva(arr_reservas, reserva):
    i = 0
    while i < len(arr_reservas) and arr_reservas[i] != reserva:
        i += 1
    return i

def reserva_mayor_estadia(arr_dias_estadia):
    posicion_mayor = 0
    for i in range(len(arr_dias_estadia)):
        if arr_dias_estadia[i] > arr_dias_estadia[posicion_mayor]:
            posicion_mayor = i
    return posicion_mayor

def mostrar_array(arr):
    for i in range(len(arr)):
        print(f"{arr[i]}")

def calcular_promedio_estadia(arr_dias_estadia):
    acum = 0
    for i in range(len(arr_dias_estadia)):
        acum += arr_dias_estadia[i]
    promedio = acum / len(arr_dias_estadia)
    return promedio

def intercambiar(arr, i, j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_reservas, arr_tipos_alojamiento, arr_meses_ingreso, arr_dias_estadia):
    for i in range(len(arr_meses_ingreso)):
        for j in range(len(arr_meses_ingreso)):
            if arr_meses_ingreso[i] > arr_meses_ingreso[j]:
                intercambiar(arr_reservas, i, j)
                intercambiar(arr_tipos_alojamiento, i, j)
                intercambiar(arr_meses_ingreso, i, j)
                intercambiar(arr_dias_estadia, i, j)
    
def cargar(arr_reservas, arr_tipos_alojamiento, arr_meses_ingreso, arr_dias_estadia):
    reserva = ingresar_reserva()
    while reserva != 0:
        tipo_alojamiento = ingresar_tipo_alojamiento()
        mes_ingreso = ingresar_mes_ingreso()
        dias_estadia = ingresar_dias_estadia()

        arr_reservas.append(reserva)
        arr_tipos_alojamiento.append(tipo_alojamiento)
        arr_meses_ingreso.append(mes_ingreso)
        arr_dias_estadia.append(dias_estadia)

        reserva = ingresar_reserva()


reservas = []
tipos_alojamiento = []
meses_ingreso = []
dias_estadia = []

cargar(reservas, tipos_alojamiento, meses_ingreso, dias_estadia)

if len(tipos_alojamiento) > 0:
    print("--- Punto 1 ---")
    posicion = int(input("Ingrese la posición de la reserva a mostrar: "))
    mostrar_por_posicion(reservas, tipos_alojamiento, meses_ingreso, dias_estadia, posicion)

    print("--- Punto 2 ---")
    reserva = int(input("Ingrese el número de reserva a buscar: "))
    posicion = buscar_por_reserva(reservas, reserva)
    mostrar_por_posicion(reservas, tipos_alojamiento, meses_ingreso, dias_estadia, posicion)

    print("--- Punto 3 ---")
    posicion_mayor = reserva_mayor_estadia(dias_estadia)
    mostrar_por_posicion(reservas, tipos_alojamiento, meses_ingreso, dias_estadia, posicion_mayor)

    print("--- Punto 4 ---")
    print("Reservas:")
    mostrar_array(reservas)
    print("Tipos de alojamiento:")
    mostrar_array(tipos_alojamiento)
    print("Meses de ingreso:")
    mostrar_array(meses_ingreso)
    print("Días de estadía:")
    mostrar_array(dias_estadia)

    print("--- Punto 5 ---")
    promedio = calcular_promedio_estadia(dias_estadia)
    print(f"Promedio de días de estadía: {promedio}")

    print("--- Punto 6 ---")
    ordenar(reservas, tipos_alojamiento, meses_ingreso, dias_estadia)
    print("--- Reservas ordenadas por meses de ingreso (de mayor a menor) ---")
    print("Meses de ingreso:")
    mostrar_array(meses_ingreso)
    print("Reservas:")
    mostrar_array(reservas)
    print("Tipos de alojamiento:")
    mostrar_array(tipos_alojamiento)
    print("Días de estadía:")
    mostrar_array(dias_estadia)
else:
    print("No se ingresaron reservas.")