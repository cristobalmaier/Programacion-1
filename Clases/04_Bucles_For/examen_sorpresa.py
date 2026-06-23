# Desarrolle un algoritmo en Python para determinar el factorial de un numero ingresado por el teclado
# Ejemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
import os
os.system("clear")

num = int(input("Ingrese un numero: "))
if num > 0:
    factorial = 1
    for i in range(num,0,-1): # start stop step
        factorial *= i
    print(factorial)
else:
    print("El numero debe ser positivo")