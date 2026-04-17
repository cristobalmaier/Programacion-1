n = 10

for i in range (n):
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su genero: ")

    if i == 0:
        edad_maxima = edad
        nombre_max = nombre
        genero_max = genero

        edad_minima = edad
        nombre_minima = nombre
        genero_min = genero
    
    else:
        if edad > edad_maxima:
            edad_maxima = edad
            nombre_max = nombre
            genero_max = genero
    
        if edad < edad_minima:
            edad_minima = edad
            nombre_minima = nombre
            genero_min = genero