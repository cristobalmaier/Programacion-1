def calcularPorcentajePapas(contadorPapas, contadorChizitos):
    totalPaquetes = contadorPapas + contadorChizitos
    if totalPaquetes > 0:
        porcentaje = (contadorPapas / totalPaquetes) * 100
    else:
        porcentaje = 0
    return porcentaje

def determinarMayor(contadorBebida, contadorComida):
    if contadorBebida > contadorComida:
        print("Hay mas amigos que llevaron bebida")
    elif contadorComida > contadorBebida:
        print("Hay mas amigos que llevaron comida")
    else:
        print("Hay la misma cantidad de amigos que llevaron comida y bebida")

def validarLitros(acumLitros, contadorPersonas):
    litrosNecesarios = contadorPersonas * 2
    if acumLitros >= litrosNecesarios:
        print("Alcanza la bebida")
    else:
        print("No alcanza la bebida")

contadorPapas = 0
contadorChizitos = 0

contadorBebida = 0
contadorComida = 0

acumLitros = 0

contadorPersonas = 0

nombre = input("Ingrese nombre (FIN para salir): ")

while nombre != "FIN":

    comida = input("Ingrese Comida (C) o Bebida (B): ")
    while comida != "C" and comida != "B":
        comida = input("ERROR! Ingrese C o B: ")

    litrosBebida = 0

    if comida == "B":

        litrosBebida = float(input("Ingrese cantidad de litros: "))

        while litrosBebida < 0:
            litrosBebida = float(input("ERROR! Ingrese litros validos: "))

    paquetes = input("Seleccione Papas fritas (P) o Chizitos (C): ")

    while paquetes != "P" and paquetes != "C":
        paquetes = input("ERROR! Ingrese P o C: ")

    cantidadPaquetes = int(input("Ingrese cantidad de paquetes: "))

    while cantidadPaquetes < 0:
        cantidadPaquetes = int(input("ERROR! Ingrese cantidad valida: "))

    if comida == "B":
        contadorBebida += 1
        acumLitros += litrosBebida
    else:
        contadorComida += 1

    if paquetes == "P":
        contadorPapas += cantidadPaquetes
    else:
        contadorChizitos += cantidadPaquetes

    if comida == "B":
        if contadorBebida == 1:
            mayorLitros = litrosBebida
            amigoMayor = nombre
        elif litrosBebida > mayorLitros:
            mayorLitros = litrosBebida
            amigoMayor = nombre

    contadorPersonas += 1

    nombre = input("Ingrese nombre (FIN para salir): ")

if contadorPersonas > 0:

    porcentajePapas = calcularPorcentajePapas(contadorPapas,contadorChizitos)

    print(f"Porcentaje de papas fritas: {porcentajePapas:.2f}%")

    determinarMayor(contadorBebida,contadorComida)

    validarLitros(acumLitros,contadorPersonas)

    if contadorBebida > 0:
        print(f"El amigo que mas gaseosa llevo fue: {amigoMayor}")
    else:
        print("Ningun amigo llevo bebida")