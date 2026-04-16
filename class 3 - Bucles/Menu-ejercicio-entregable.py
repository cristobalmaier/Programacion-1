nombre_producto = ""
precio_producto = 0.0
opcion = 0

while opcion != 5:
    print("\n--- MENU ---")
    print("1: Crear producto")
    print("2: Modificar precio")
    print("3: Eliminar producto")
    print("4: Mostrar datos")
    print("5: Salir")
    
    opcion = int(input("Elija una opción: "))

    if opcion < 0:
        print("Error: La opción no puede ser menor a 0.")
    
    elif opcion == 1:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio: "))
        print("Producto creado exitosamente.")

    elif opcion == 2:
        if nombre_producto != "":
            nuevo_precio = float(input("Ingrese el nuevo valor decimal: "))
            precio_producto = nuevo_precio
            print(f"Precio actualizado a: ${precio_producto}")
        else:
            print("Error: No hay un producto cargado para modificar.")

    elif opcion == 3:
        nombre_producto = ""
        precio_producto = 0.0 
        print("Producto Eliminado.")

    elif opcion == 4:
        if nombre_producto != "":
            print(f"Datos guardados -> Producto: {nombre_producto} , Precio: ${precio_producto}")
        else:
            print("No hay un producto cargado.")

    elif opcion == 5:
        print("!Nos vemos! Gracias por usar el sistema.")
    else:
        print("Opción no válida, intente nuevamente.")