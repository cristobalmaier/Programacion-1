"""
Ingresar la medida de un ángulo y determinar si es agudo, obtuso, recto, nulo o llano. Si
el valor ingresado es mayor a 180º mostrar la leyenda “ángulo no válido” e ingresar un
nuevo valor.
"""

angulo = float(input("Ingrese el ángulo: "))

if angulo > 180:
    print("Ángulo no válido")
else:
    if angulo > 90:
        print("Ángulo obtuso")
    elif angulo > 45:
        print("Ángulo recto")
    elif angulo > 0:
        print("Ángulo agudo")
    else:
        print("Ángulo nulo")