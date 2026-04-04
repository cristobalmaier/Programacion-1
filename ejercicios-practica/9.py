"""
Se ingresa el código de tipo de llamada: 1. Local 2. Interurbana 3. Internacional y la
duración en minutos de la misma. Si el minuto cuesta $0.25 para la llamada local, $0.40
para la llamada interurbana y $1.05 para la llamada internacional, diseñar un algoritmo
que permita calcular el monto a pagar por dicha llamada.
"""

print("""
1. Local
2. Interurbana
3. Internacional 
""")

cod_llamado = int(input("Ingrese un codigo de tipo de llamada: "))
duracion_minutos = int(input("Ingrese la duracion de la llamada en minutos: "))

if cod_llamado == 1:
    total = duracion_minutos * 0.25
    print(f"Total a pagar: {total}")
elif cod_llamado == 2:
    total = duracion_minutos * 0.40
    print(f"Total a pagar: {total}")
elif cod_llamado == 3:
    total = duracion_minutos * 1.05
    print(f"Total a pagar: {total}")
else:
    print("Ingresaste un codigo invalido")