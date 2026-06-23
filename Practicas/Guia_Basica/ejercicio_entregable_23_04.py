contador_pares = 0
contador_impares = 0
mayor_par = 0
menor_descartado = 0
contador_cienes = 0
suma_cienes = 0

while contador_pares < 30:
    num = int(input("Ingrese un numero: "))
    
    if num % 2 == 0:
        contador_pares += 1

        if contador_pares == 1: 
            mayor_par = num
        else:
            if num > mayor_par:
                mayor_par = num

        if num > 101:
            contador_cienes += 1 
            suma_cienes += num

        if num % 7 == 0 and num > 0: 
            suma = 0
            print(f"[Modo múltiplo de 7] Ingresá {num} números para calcular la suma: ")
            for i in range(num):
                aux = int(input("Ingrese un numero: "))
                suma += aux
            print(f"Suma de los {num} valores ingresados: {suma}")
        
    else:
        contador_impares += 1

        if contador_impares == 1: 
            menor_descartado = num
        elif num < menor_descartado:
                menor_descartado = num


if contador_cienes > 0:
    promedio = suma_cienes / contador_cienes
    print(f"Promedio de pares mayores a 101: {promedio}")
else:
    print("No se pudo calcular el promedio (no hubo pares mayores a 101)")

print(f"Cantidad de valores descartados: {contador_impares}")
print(f"Mayor de los pares: {mayor_par}")

if contador_impares > 0:
    print(f"Menor valor descartado: {menor_descartado}")
else:
    print("No hubo valores descartados")