# Ingresar 10 numeros decimales guardarlos en un arrelgo
# calcular el promedio
# mostrar valores

n = 10
valores = [] # Lista vacia
acumValores = 0

for i in range(n):
    num = int(input("Ingrese numero: "))
    valores.append(num)

for i in range(len(valores)): # devuelve la cantidad de elementos que contiene un objeto
    print(valores[i])

for i in range(len(valores)): # Acumula los valores de la lista de valores
    acumValores += valores[i]

promedio = acumValores / len(valores) #  Si no sabemos cuantos numeros va ser el ciclo
print(f"El promedio es: {promedio}")