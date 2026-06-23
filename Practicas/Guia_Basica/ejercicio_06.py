"""
Ingresar las edades de dos personas. Si una de ellas es mayor de edad y la otra menor
de edad, calcular y mostrar su promedio. En caso contrario mostrar las dos edades
"""

edad1 = int(input("Ingrese la edad de la primera persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))

if edad1 > edad2:
    print(f"El promedio de edad es: {(edad1 + edad2) / 2}")
else:
    print(f"{edad1} {edad2}")