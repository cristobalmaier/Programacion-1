"""
Ingresar un numero de dos cifras, si es mayor que 50 mostrarlo invertido. Sino mostrar
la cifra que corresponde a las unidades
"""

num1 = int(input("Ingrese un numero de 2 cifras: "))

if num1 > 50:
    digito = num1 % 10
    unidad = num1 // 10
    print(digito,unidad)
else:
    print(num1)