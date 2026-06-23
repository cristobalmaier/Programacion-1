num = int(input("Ingrese un numero: "))

if num > 0:
    resultado = num ** 0.5
    print(f"La raíz cuadrada es: {resultado}")
elif num < 0:
    resultado = num * num
    print(f"El cuadrado es: {resultado}")
else:
    print("Error. Ha ingresado un valor nulo")