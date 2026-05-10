contadorHombres = 0
contadorHombresMayores = 0
contadorHombresTerciarios = 0
contadorHombresMayores30 = 0

contadorMujeres = 0
contadorMujeresTerciarios = 0
contadorMujeresSecundarios = 0
acumEdadMujeresSecu = 0

acumEdadPrimario = 0
contPrim = 0

acumEdadSecundario = 0
contSecu = 0

acumEdadTerciario = 0
contTerciario = 0


opc = int(input("Ingrese 0 para salir o 1 para seguir: "))

while opc != 0:
    edad = int(input("Ingrese edad: "))
    while edad < 0 or edad > 110:
        edad = int(input("Error! Ingrese una edad valida: "))
    
    sexo = int(input("Ingrese Sexo (1. Femenino 2. Masculino): "))
    while sexo != 1 and sexo != 2:
        sexo = int(input("Error! Ingrese 1 (Femenino) o 2 (Masculino): "))
    
    estudios = int(input("Ingrese sus estudios (1. Primarios, 2. Secundarios, 3. Terciarios): "))
    while estudios != 1 and estudios != 2 and estudios != 3:
        estudios = int(input("Error! Ingrese 1, 2 o 3: "))
    
    # Promedios por estudio
    if estudios == 1:
        contPrim += 1
        acumEdadPrimario += edad
    elif estudios == 2:
        contSecu += 1
        acumEdadSecundario += edad
    else:
        contTerciario += 1
        acumEdadTerciario += edad

    # Mujeres
    if sexo == 1:
        contadorMujeres += 1

        if estudios == 3:
            contadorMujeresTerciarios += 1

        if edad > 40 and estudios == 2:
            contadorMujeresSecundarios += 1
            acumEdadMujeresSecu += edad

    # Hombres
    if sexo == 2:
        contadorHombres += 1

        if edad > 45:
            contadorHombresMayores += 1

        if edad > 30:
            contadorHombresMayores30 += 1

            if estudios == 3:
                contadorHombresTerciarios += 1

    opc = int(input("Ingrese 0 para salir o 1 para seguir: "))


# Promedios por estudio
if contPrim > 0:
    print(f"Promedio edad Primario: {acumEdadPrimario / contPrim}")
else:
    print("No se cargaron personas con estudios primarios")

if contSecu > 0:
    print(f"Promedio edad Secundario: {acumEdadSecundario / contSecu}")
else:
    print("No se cargaron personas con estudios secundarios")

if contTerciario > 0:
    print(f"Promedio edad Terciario: {acumEdadTerciario / contTerciario}")
else:
    print("No se cargaron personas con estudios terciarios")


# Mujeres
if contadorMujeres > 0:
    print(f"Cantidad de mujeres encuestadas: {contadorMujeres}")

    porcentajeMujeresTerciario = (contadorMujeresTerciarios / contadorMujeres) * 100
    print(f"Porcentaje de mujeres con estudios terciarios: {porcentajeMujeresTerciario}")

    if contadorMujeresSecundarios > 0:
        promedioMujeresSecundario = acumEdadMujeresSecu / contadorMujeresSecundarios
        print(f"Promedio de edad de mujeres >40 con secundarios: {promedioMujeresSecundario}")
    else:
        print("No hay mujeres mayores de 40 con estudios secundarios")


# Hombres
if contadorHombres > 0:
    print(f"Cantidad de hombres mayores a 45 años: {contadorHombresMayores}")

    if contadorHombresMayores30 > 0:
        porcentajeHombresTerciarios = (contadorHombresTerciarios / contadorHombresMayores30) * 100
        print(f"Porcentaje de hombres mas 30 con estudios terciarios: {porcentajeHombresTerciarios}")
    else:
        print("No hay hombres mayores a 30")