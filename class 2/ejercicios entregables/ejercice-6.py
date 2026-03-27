num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un numero: "))

suma = num1 + num2
diferencia_cuadrados = (num1**2) - (num2**2)
promedio = (num1 + num2) / 2

if suma > diferencia_cuadrados:
    print(f"Tu promedio es {promedio}")
else:
    print("La suma no es mayor que la diferencia de sus cuadrados.")