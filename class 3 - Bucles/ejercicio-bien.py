# Ingresar numeros por teclado
# hasta que se ingrese un 0
# calcular el porcentaje de los numeros positivos y pares

# Ninteres / Ntotal * 100

contador_pares = 0
contador_total = 0

n = int(input("Ingrese un numero: "))
while n != 0:
    if n % 2 == 0 and n > 0:
        contador_pares += 1
    contador_total += 1
    n = int(input("Ingrese un numero: "))

if contador_total > 0:
    porcentaje = (contador_pares / contador_total) * 100
    print(f"El porcentaje es: {porcentaje}")