"""
Convertir longitudes de millas a Km. y de pulgadas a cm., si:
1 milla = 1.60935 Km.
1 pulgada = 2.534 cm
"""

millas = float(input("Ingrese la longitud en millas: "))

km = millas * 1.60935
cm = millas * 2.534

print(f"La longitud en km es: {km}")
print(f"La longitud en cm es: {cm}")