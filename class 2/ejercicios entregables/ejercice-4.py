num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))

if num1 < num2 and num1 < num3:
    print(f"El menor es {num1}")
elif num2 < num1 and num2 < num3:
    print(f"El menor es {num2}")
else:
    print(f"El menor es {num3}")