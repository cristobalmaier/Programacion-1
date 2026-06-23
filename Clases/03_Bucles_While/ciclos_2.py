sumatoria = 0
contador = 0
n = int(input("Ingrese un numero: "))

while n != 0:
    sumatoria = sumatoria + n
    contador += 1
    n = int(input("Ingrese un numero: "))

if contador > 0:
    promedio = sumatoria / contador
    print(f"El promedio de los numeros es: {promedio}")
else:
    print("No se ingresaron datos.")