"""
Ingresar las medidas de dos ángulos expresados en grados minutos y segundos y hallar
la suma. (recordar que los minutos y los segundos no deben excederse de 60).
"""

angulo1 = float(input("Ingrese el primer ángulo: "))
angulo2 = float(input("Ingrese el segundo ángulo: "))

grados = int(angulo1)
minutos = int(angulo1 - grados)
segundos = int(angulo2 - grados * 60 - minutos * 60)

grados = int(angulo2)
minutos = int(angulo2 - grados)
segundos = int(angulo1 - grados * 60 - minutos * 60)

print(grados,minutos,segundos)