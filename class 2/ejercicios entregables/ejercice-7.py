num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 == 0:
    print("El primer número no puede ser cero")
elif num2 % num1 == 0:
    print(f"{num2} SI es multiplo de {num1}")
else:
    print(f"{num2} NO es multiplo de {num1}")