contadorPersona = 0
sumaEdad = 0
contadorGrupoA = 0

DNI = int(input("Ingrese su DNI: "))

while DNI != 0:

    edad = int(input("Ingrese su Edad: "))

    if edad < 18:
        print("No puede registrarse")

    else:
        # Validación grupo sanguíneo
        grupoSanguineo = input("Ingrese su grupo sanguineo (A, B, AB): ")
        while grupoSanguineo != "A" and grupoSanguineo != "B" and grupoSanguineo != "AB":
            grupoSanguineo = input("Error! Ingrese un grupo valido (A, B, AB): ")
        
        if grupoSanguineo == "A":
            contadorGrupoA += 1

        # Validación género
        genero = input("Ingrese su genero (M o F): ")
        while genero != "M" and genero != "F":
            genero = input("Error! Ingrese un genero valido (M o F): ")
        
        sumaEdad += edad
        contadorPersona += 1

        if contadorPersona == 1:
            mayorEdad = edad
            dni_mayor = DNI
        elif edad > mayorEdad:
            mayorEdad = edad
            dni_mayor = DNI

    DNI = int(input("Ingrese su DNI: "))

if contadorPersona > 0 :
    promedioEdadDonates = sumaEdad / contadorPersona
    porcentajeGrupoA = (contadorGrupoA / contadorPersona) * 100
    print(f"El DNI: {dni_mayor} es la persona con mayor edad: {mayorEdad}")
    print(f"Porcentaje del grupo A: {porcentajeGrupoA}")
    print(f"Promedio de edad de donantes:  {promedioEdadDonates}")
else:
    print("No hay personas validas para mostrar resultados")