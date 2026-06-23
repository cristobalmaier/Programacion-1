num1 = int(input("Ingrese un numero de 3 cifras: "))

if num1 >= 100 and num1 <= 999:
    numActualizado = num1 // 10
    segundoDigito = numActualizado % 10
    print(f"El segundo digito es {segundoDigito}")
else:
    print("El numero no tiene 3 cifras")