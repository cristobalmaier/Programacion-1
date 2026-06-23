valores = []
contadorPar = 0
cont = 0
acumValores = 0
n = float(input("Ingrese numero: "))

while n != 0:
    valores.append(n)    
    n = float(input("Ingrese numero: "))

# ---------MAXIMO-----------------------
maximo = valores[0]
posMaximo = 0

for i in range(len(valores)):
    if valores[i] > maximo:
        maximo = valores[i]
        posMaximo = i

print(f"El maximo es: {maximo} en la posicion {posMaximo}")

# ----------MAXIMO----------------------

# ------- Buscar un numero en un arreglo -------
busqueda = int(input("Ingrese numero a buscar: "))

i = 0
while i < len(n) and valores[i] != busqueda:
    i += 1

if i == len(valores):
    print("NO SE ENCONTRO EN EL ARREGLO")
else:
    print(f"EL NUMERO ESTA EN EL ARREGLO EN LA POSICION: {i}")

# ------- Buscar un numero en un arreglo -------