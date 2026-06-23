# Ingresar un número entero
# crear una función que determine si el número 
# es primo

def ValidadNumeroPrimo(n):
    contador = 0
    for i in range(1, n+1):
        if n % i == 0:
            contador += 1
    if contador == 2:
        print("Tu numero es primo")
    else:
        print("Tu numero NO ES PRIMO")

n = int(input("Ingrese un numero: "))

ValidadNumeroPrimo(n)