"""
1)
Se quiere llevar el control del habitat de osos Panda en una reserva, para lo cual se considera la siguiente información:

Nombre del panda
Peso
Cantidad de kilos de bambú consumidos en un día
Edad
La carga finaliza cuando en nombre del panda se ingresa la palabra FIN.

Se pide:

El promedio de peso de los pandas mayores a 3 años.
La máxima cantidad de kilos de bambú consumidos y el nombre del panda a quien corresponde.
El porcentaje de pandas cuyo peso es menor a 210 kilos.
Se deberán validar los datos de entrada
"""
contadorPandas = 0
contadorPesoPandas = 0
pesoPandasMayores = 0
contadorPandasMayores = 0
nombre = input("Ingrese el nombre del Panda: ")

while nombre != "FIN":
    peso = float(input("Ingrese el peso del Panda: "))
    while peso <= 0:
        peso = float(input("Ingrese un peso mayor a 0: "))

    kilosBambu = float(input("Ingrese la cantidad de kilos de cambu consumidos por dia: "))
    while kilosBambu <= 0:
        kilosBambu = float(input("Erro! Ingrese un valor positivo: "))
    edad = int(input("Ingrese la edad del Panda: "))
    while edad < 0:
        edad = int(input("Ingrese una edad mayor a 0: "))
    contadorPandas += 1

    if peso < 210:
        contadorPesoPandas += 1

    if edad > 3:
        contadorPandasMayores += 1
        pesoPandasMayores += peso
    
    if contadorPandas == 1:
        mayorBambu = kilosBambu
        nomnbreMayorPanda = nombre
    elif kilosBambu > mayorBambu:
        mayorBambu = kilosBambu
        nomnbreMayorPanda = nombre      
    
    nombre = input("Ingrese el nombre del Panda: ")

if contadorPandas > 0:

    if contadorPandasMayores > 0:
        promedioPeso = pesoPandasMayores / contadorPandasMayores
        print (f"El promedio de peso de los pandas mayores a 3 años son: {promedioPeso}")
    
    print(f"Maxima cantidad de bambu consumidos en un dia: {mayorBambu} fue el panda: {nomnbreMayorPanda}")

    porcentajePesoMenor = (contadorPesoPandas / contadorPandas) * 100
    print(f"El porcentaje de peso de los pandas menores a 210kg es: {porcentajePesoMenor}")