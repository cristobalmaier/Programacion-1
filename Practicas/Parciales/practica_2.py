"""
Se desea crear un sistema que gestione el inventario de juegos de mesa disponibles en una tienda.
El usuario debe ingresar la cantidad de juegos a registrar.
    Se deberán almacenar tres listas paralelas con los siguientes datos:
        ● Nombre del juego
        ● Precio base del juego
        ● Precio final con impuestos (IVA del 21%)
Se pide: ✔️
    Crear una función que reciba el precio base del juego, calcule el precio final con IVA, y lo retorne
    para ser agregado al arreglo correspondiente. ✔️
    Crear otra función que inserte un nuevo juego llamado "AJEDREZ PREMIUM" con precio base de
    $9999 y su precio final con IVA, en una posición determinada por el usuario (Ingreso por teclado)
    La posición siempre se ingresa correcta, no debe validar.
    Para aprobar el examen cada programa no debe tener errores
"""

def ingresar_juego():
    juego = input("Ingrese nombre del juego: ")
    while juego == "":
        juego = input("Ingrese nombre del juego: ")
    return juego

def ingresar_precio_base():
    precio_base = int(input("Ingrese precio base: "))
    while precio_base < 0:
        precio_base = int(input("Ingrese precio base: "))
    return precio_base

def calcular_precio_final(precio_base):
    precio_final = precio_base * 1.21
    return precio_final

def insertar_juego(arr_nombres,arr_precios_bases,arr_precios_finales):
    posicion = int(input("Ingrese la posición para insertar el juego: "))
    arr_nombres.insert(posicion, "AJEDREZ PREMIUM")
    arr_precios_bases.insert(posicion, 9999)
    arr_precios_finales.insert(posicion, calcular_precio_final(9999))

def cargar(arr_nombres,arr_precios_bases,arr_precios_finales):
    cont = 0
    cantidad_juegos = int(input("Ingrese la cantidad de juegos a registrar: "))

    while cont < cantidad_juegos:
        juego = ingresar_juego()
        arr_nombres.append(juego)

        precios_base = ingresar_precio_base()
        arr_precios_bases.append(precios_base)

        precio_final = calcular_precio_final(precios_base)
        arr_precios_finales.append(precio_final)

        cont += 1

def mostrar_juegos(arr_nombres,arr_precios_bases,arr_precios_finales):
    for i in range(len(arr_nombres)):
        print(f"Juego: {arr_nombres[i]}")
        print(f"Precio Base: ${arr_precios_bases[i]:.2f}")
        print(f"Precio Final: ${arr_precios_finales[i]:.2f}")

nombres = []
precios_bases = []
precios_finales = []

cargar(nombres,precios_bases,precios_finales)

if len(nombres) > 0:
    mostrar_juegos(nombres,precios_bases,precios_finales)
    insertar_juego(nombres,precios_bases,precios_finales)
    print("\nDespués de insertar el juego 'AJEDREZ PREMIUM':\n")
    mostrar_juegos(nombres,precios_bases,precios_finales)
else:
    print("No se han registrado juegos.")