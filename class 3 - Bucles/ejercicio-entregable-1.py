"""
Crear un menú con 5 opciones válidas (1 al 5).

Opción 1: Crear producto. Al ingresar esta opción se pide ingresar el nombre del producto. Guardar en una variable.

Opción 2: Modificar precio. Solicita un valor decimal. Guardar en una variable.

Opción 3: Eliminar producto. Muestra un mensaje de eliminación realizada correctamente. En la variable de nombre poner ""

Opción 4: Mostrar los datos del producto guardado, solo si existe, caso contrario informar que no hay producto cargado.

Opción 5: Salir. Muestra un mensaje de despedida.

Se debe validar que la opción ingresada no sea menor a 0. Hasta que no se ingrese un 5, se debe volver a mostrar el menú.
"""

precio_modificado = 0

print("""Ingrese una opcion
    1: Crear producto
    2: Modificar precio
    3: Eliminar producto
    4: Mostrar los datos del producto guardado
    5: Salir
""")

opcion = int(input("Ingrese una opcion: "))

while opcion > 0 and opcion < 6:
    if opcion == 1:
        print("Crear producto")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        print(f"Producto: {nombre} Pecio: {precio}")
    elif opcion == 2:
        print("Modificar Precio")
        p
        print(f"El precio actualizado es:{precio_modificado}")