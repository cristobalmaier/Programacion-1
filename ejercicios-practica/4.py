# Hallar la longitud de la hipotenusa de un triángulo dada la medida de sus catetos

import math

cateto1 = float(input("Ingrese la medida del primer cateto: "))
cateto2 = float(input("Ingrese la medida del segundo cateto: "))

# La fórmula correcta solo lleva dos catetos
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print(f"La longitud de la hipotenusa es: {hipotenusa}")