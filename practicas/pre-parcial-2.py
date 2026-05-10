"""
Se ingresan 30 números enteros entre -999 y 999.

1) Mostrar el máximo y el mínimo.

2) indicar el porcentaje de números múltiplos de 3 y 5 simultáneamente.
"""

contador_numeros = 0
contador_multiplos = 0
while contador_numeros != 30:
    contador_numeros += 1
    num = int(input("Ingrese un número: "))
    while num > 999 or num < -999:
        num = int(input("Error! Ingrese un número entre -999 y 999: "))
    if num % 3 == 0 and num % 5 == 0:
        print("El número es múltiplo de 3 y 5")
        contador_multiplos += 1
    elif num % 3 == 0:
        print("El número es múltiplo de 3")
    elif num % 5 == 0:
        print("El número es múltiplo de 5")
    
    if contador_numeros == 1:
        maximo = num
        minimo = num
    else:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

porcentaje = (contador_multiplos / 30) * 100
print(f"El máximo es {maximo}")
print(f"El mínimo es {minimo}")
print(f"El porcentaje de números múltiplos de 3 y 5 simultáneamente es {porcentaje:.2f}%")