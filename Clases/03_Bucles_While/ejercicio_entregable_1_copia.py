nombre_producto = ""
precio_modificado = 0
opcion = 0

while opcion != 5:
    print("\n--- MENÚ ---")
    print("1: Crear producto")
    print("2: Modificar precio")
    print("3: Eliminar producto")
    print("4: Mostrar datos")
    print("5: Salir")
    print("6: Aplicar Descuento")
    
    opcion = int(input("Elija una opción: "))

    if opcion < 0:
        print("Error: La opción no puede ser menor a 0.")
    
    elif opcion == 1:
        nombre_producto = input("Nombre del producto: ")
        precio_producto = float(input("Precio: "))
        print("Producto cargado.")

    elif opcion == 2:
        if nombre_producto != "":
            print("Modificar Precio")
            precio_modificado = float(input("Ingrese el nuevo valor al producto: "))
            precio_producto = precio_modificado
            print(f"El nuevo precio es:{precio_modificado}")
        else:
            print("NO se puede modificar porque no hay un producto existente")

    elif opcion == 3:
        nombre_producto = ""
        print("Producto eliminado correctamente.")

    elif opcion == 4:
        if nombre_producto != "":
            print(f"Producto: {nombre_producto} - Precio: ${precio_producto}")
        else:
            print("No hay producto cargado.")

    elif opcion == 6:
        if nombre_producto != "":
            porcentaje = float(input("Ingrese un porcentaje: "))
            precio_producto -= (precio_producto * porcentaje / 100)
            precio_desucento = precio_producto
            print(f"Tu producto con descuento queda: {precio_desucento} ")
        else:
            print("No se puede aplicar descuento porque no hay un producto")

    elif opcion == 5:
        print("¡Hasta luego! Gracias por usar el sistema.")
        
    else:
        print("Opción no válida, intente de nuevo.")