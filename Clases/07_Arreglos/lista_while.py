# Ingresar numeros deciamles guardarlos en un arreglo
# hasta que ingrese 0

valores = []
contadorPar = 0
cont = 0
acumValores = 0
n = float(input("Ingrese numero: "))

while n != 0:
    valores.append(n)    
    n = float(input("Ingrese numero: "))

# Calcular el porcentaje de valores pares
for i in range (len(valores)):
    if valores[i] % 2 == 0:
        contadorPar += 1

# Calcular el promedio de los valores que estan en posiciones impares
for i in range(len(valores)):
    if i % 2 != 0: #Veo si el indice es impar
        acumValores += valores[i]
        cont += 1

if len(valores) > 0:
    porcentaje = contadorPar / len(valores) * 100
    print(f"El porcentaje de valores pares es: {porcentaje:.2f}%")

    if cont > 0:
        promedio = acumValores / cont
        print(f"El promedio de los indices impares es: {promedio}")
    else:
        print("No se ingresaron valores en posiciones/indices impares")
else:
    print("No se ingresaron valores")