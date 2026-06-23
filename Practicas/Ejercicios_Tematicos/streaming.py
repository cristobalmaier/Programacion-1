basico = 5000
estandar = 9000
premium = 15000

contadorPlanBasico = 0
contadorPlanEstandar = 0
contadorPlanPremium = 0
contador = 0

acumEdadPremium = 0
acumTotalRecaudado = 0
acumMesesContratos = 0
acumMesesContratosBasicos = 0
acumMesesContratosEstandar = 0
acumMesesContratosPremium = 0

numeroCliente = int(input("Ingrese numero Cliente (0. Salir): "))

while numeroCliente != 0:
    nombre = input("Ingrese nombre del usuario: ")
    while nombre == "":
        nombre = input("Error! Ingrese nombre del cliente: ")
    edad = int(input("Ingrese edad del cliente: "))
    while edad < 0 or edad > 110:
        edad = int(input("ERROR! Ingrese una edad valida: "))
    tipoPlan = int(input("Seleccione plan: 1.Basico 2.Estandar 3.Premium: "))
    while tipoPlan < 1 or tipoPlan > 3:
        tipoPlan = int(input("ERROR! Seleccione plan valido: "))
    mesesContratados = int(input("Ingrese meses para contratar: "))
    while mesesContratados < 0:
        mesesContratados = int(input("ERROR! Ingrese meses a contratar: "))
    
    if tipoPlan == 1:
        contadorPlanBasico += 1
        total = basico * mesesContratados
        if mesesContratados > 6:
            total *= 0.85
        acumTotalRecaudado += total
        acumMesesContratos += mesesContratados
        acumMesesContratosBasicos += mesesContratados
    elif tipoPlan == 2:
        contadorPlanEstandar += 1
        total = estandar * mesesContratados
        if mesesContratados > 6:
            total *= 0.85
        
        acumTotalRecaudado += total
        acumMesesContratos += mesesContratados
        acumMesesContratosEstandar += mesesContratados
    else:
        contadorPlanPremium +=1
        total = premium * mesesContratados
        if mesesContratados > 6:
            total *= 0.85
        if mesesContratados > 12:
                total *= 1.08
        
        acumEdadPremium += edad
        acumTotalRecaudado += total
        acumMesesContratos += mesesContratados
        acumMesesContratosPremium += mesesContratados
    print(f"Nombre: {nombre}")
    print(f"Tipo Plan: {tipoPlan}")
    print(f"Total a pagar: ${total}")

    if contador == 0:
        mayorEdad = edad
        mayorNombre = nombre
    elif edad > mayorEdad:
        mayorEdad = edad
        mayorNombre = nombre
    
    contador += 1
    numeroCliente = int(input("Ingrese numero Cliente (0. Salir): ")) 

if contador > 0:
    print(f"Usuarios Tipo de plan Basico: {contadorPlanBasico}")
    print(f"Usuarios Tipo de plan Estandar: {contadorPlanEstandar}")
    print(f"Usuarios Tipo de plan Premium: {contadorPlanPremium}")
    print(f"Usuario mas grande: {mayorNombre} {mayorEdad} años")
    if contadorPlanPremium > 0:
        promedioEdadPremium = acumEdadPremium / contadorPlanPremium
        print(f"El promedio de edad de los clientes Premium: {promedioEdadPremium}")
    print(f"Total Recaudado de la empresa: ${acumTotalRecaudado}")
    porcentajeUsuariosEstandar = (contadorPlanEstandar / contador) * 100
    print(f"El porcentaje de los usuarios estandar: {porcentajeUsuariosEstandar}%")
    print(f"Total de meses contratados: {acumMesesContratos}")

    porcentajeMesesContratosBasico = (acumMesesContratosBasicos/acumMesesContratos) * 100
    porcentajeMesesContratosEstandar = (acumMesesContratosEstandar/acumMesesContratos) * 100
    porcentajeMesesContratosPremium = (acumMesesContratosPremium/acumMesesContratos) * 100

    print(f"Porcentaje de meses contratos de Basico: {porcentajeMesesContratosBasico:.2f}%")
    print(f"Porcentaje de meses contratos de Estandar: {porcentajeMesesContratosEstandar:.2f}%")
    print(f"Porcentaje de meses contratos de Premium: {porcentajeMesesContratosPremium:.2f}%")