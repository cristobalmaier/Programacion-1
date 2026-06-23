suma_edades = 0
contador = 0
mayor_edad = 0
dni_mayor = 0
contador_a = 0

dni = int(input("ingrese su dni: "))

while  dni != 0 :
    edad = int(input("ingrese su edad: "))

    while edad < 18:
        edad = int(input("no puede registrarse, ingrese una edad valida: "))

    suma_edades += edad

    if contador_a == 0:
        mayorEdad = edad
        mayorDNI = dni
    else:
        if edad > mayor_edad:
            mayor_edad = edad
            mayorDNI = dni    


    contador_a += 1

if contador_a > 0:
    promedio = suma_edades / contador_a
    print(f"El promedio de edades de los pacientes es: {promedio}")
    print(f"DNI mayor: {dni_mayor}, edad mayor: {mayor_edad}")