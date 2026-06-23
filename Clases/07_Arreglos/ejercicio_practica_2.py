#Ingresar un arreglo de 10 componentes:

#a.Imprimir la cuarta componente.

# b.Imprimir las componentes en orden invertida.

# c.Imprimir el producto entre la primera y la última componente.

# d.Imprimir las componentes de índice impar.

# e.Imprimir la suma de las componentes de índice par.

# f.Imprimir la multiplicación de las componentes de índice impar.

# g.Imprimir el arreglo que resulta de intercambiar la primera con la última componente.

n = 10
valores = [] # Lista vacia
acumValores = 0

for i in range(n):
    num = int(input("Ingrese numero: "))
    valores.append(num)

print(f"Cuarto componente: {valores[4]}") # A

valores.reverse() # B
print(f"Asi se ve la lista invertida: {valores}") # B

producto = valores[0] * valores[-1]
print(f"Producto: {producto}") # C

for i in range(len(valores)): # D
    if i % 2 != 0:
        print(f"Estos son los valores con indeice impar: {valores[i]}")

for i in range(len(valores)): # E
    if i % 2 == 0:
        acumValores += valores[i]
        print(f"Suma de los valores con indeice par: {acumValores}")

for i in range(len(valores)): # F
    if i % 2 != 0:
        acumValores *= valores[i]
        print(f"Multiplicacion de los valores con indeice impar: {acumValores}")

aux = valores[0]
valores[0] = valores[-1]
valores[-1] = aux

print(f"Arreglo intercambiado: {valores}") # G