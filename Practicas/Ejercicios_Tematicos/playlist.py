"""
Desarrollar un algoritmo para:

Se ingresan los nombres de 8 playlist. Por cada playlist se pide la cantidad de canciones y la duración total en minutos de todas las canciones que la componen. Calcular y mostrar:

El nombre de la playlist que tiene la mayor cantidad de canciones.
El nombre de la playlist que tiene la menor duración en minutos de sus canciones.
El promedio de la duración total en minutos de todas las canciones de la playlist.
"""
acumDuracion = 0

for i in range (8):
    nombre = str(input("Ingrese nombre de la playlist: "))
    while nombre == "":
        nombre = str(input("Error! Ingrese un nombre: "))

    cantidadCanciones = int(input("Ingrese la cantidad de canciones de la playlist: "))
    while cantidadCanciones <= 0:
        cantidadCanciones = int(input("Error! Ingrese un valor mayor a 0: "))
    
    duracion = float(input("Ingrese la duracion total de minutos de todas las canciones: "))
    while duracion < 0:
        duracion = float(input("Error! Ingrese una duracion positiva: "))

    acumDuracion += duracion

    if i == 0:
        mayorCanciones = cantidadCanciones
        mayorNombre = nombre

        menorDuracion = duracion
        menorNombre = nombre
    else:
        if cantidadCanciones > mayorCanciones:
            mayorCanciones = cantidadCanciones
            mayorNombre = nombre

        if duracion < menorDuracion:
            menorDuracion = duracion
            menorNombre = nombre
    
promedio = acumDuracion / 8

print(f"La playlist {mayorNombre} tiene la mayor cantidad de canciones")
print(f"La playlist {menorNombre} tiene la menor duracion en minutos de sus canciones")
print(f"El promedio de duración es: {promedio} minutos")