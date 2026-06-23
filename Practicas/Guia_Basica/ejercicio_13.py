"""
Ingresar dos números y sin resolver la multiplicación mostrar una leyenda según el
producto sea negativo, positivo o cero.
"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 * num2 > 0:
    print("El producto es positivo")
elif num1 * num2 < 0:
    print("El producto es negativo")
else:
    print("El producto es cero")