"""
Una empresa de envíos desea registrar información sobre los paquetes entregados durante el día.

De cada envío se ingresa:

- Número de seguimiento (0 para finalizar)
- Nombre del cliente
- Peso del paquete en kg
- Tipo de envío:
    1 = Normal
    2 = Express
    3 = Internacional

Los precios por kg son:

- Normal: $2000
- Express: $3500
- Internacional: $5000

Además:
- Si el paquete pesa más de 20 kg, se aplica un recargo del 8%.

Se pide:

a) Mostrar por cada envío:
    - Nombre del cliente
    - Tipo de envío
    - Total a pagar

b) Informar al finalizar:
    - Cantidad de envíos de cada tipo
    - Peso del paquete más liviano
    - Promedio de peso de los envíos internacionales
    - Total recaudado por la empresa
    - Porcentaje de envíos Express sobre el total
    - Cantidad total de kg enviados
"""

normal = 2000
express = 3500
Internacional = 5000
contadorNormal = 0
contadorExpress = 0
contadorInternacional = 0
contador = 0
acumPesoInternacional = 0
AcumDinero = 0
AcumPeso = 0

numero_seguimiento = int(input("Ingrese numero de seguimiento (0.Salir): "))

while numero_seguimiento != 0:

    nombre = input("Ingrese nombre del cliente: ")
    while nombre == "":
        nombre = input("Error! Ingrese un nombre:")
    
    peso = float(input("Ingrese peso del paquete (kg): "))
    while peso < 0:
        peso = float(input("Error! Ingrese un peso positivo: "))

    tipo_envio = int(input("Seleccione tipo de envio: 1.Normal 2.Express 3.Internacional "))
    while tipo_envio < 1 or tipo_envio > 3:
        tipo_envio = int(input("Error! Seleccione un tipo de envio valido: 1.Normal 2.Express 3.Internacional "))
    
    if tipo_envio == 1:
        contadorNormal += 1
        total = peso * normal
        if peso >= 20:
            total *= 1.08
        AcumDinero += total
        AcumPeso += peso

    elif tipo_envio == 2:
        contadorExpress += 1
        total = peso * express
        if peso >= 20:
            total *= 1.08
        AcumDinero += total
        AcumPeso += peso
    else:
        contadorInternacional += 1
        acumPesoInternacional += peso
        total = peso * Internacional
        if peso >= 20:
            total *= 1.08
        
        AcumDinero += total
        AcumPeso += peso

    if contador == 0:
        paqueteLiviano = peso
    else:
        if peso < paqueteLiviano:
            paqueteLiviano = peso
    
    contador += 1
    print(f"Nombre del cliente: {nombre}")
    print(f"Tipo de envio: {tipo_envio}")
    print(f"Total a pagar: {total}")

    numero_seguimiento = int(input("Ingrese numero de seguimiento (0.Salir): "))

if contador > 0:
    print(f"Cantidad de paquetes de Normal: {contadorNormal}")
    print(f"Cantiad de paquetes de Express: {contadorExpress}")
    print(f"Cantidad de paquetes de Internacional: {contadorInternacional}")
    print(f"Paquete mas liviano: {paqueteLiviano} kg")
    if contadorInternacional > 0:
        promedio = acumPesoInternacional / contadorInternacional
        print(f"Promedio de los pesos de internacional: {promedio}")


print(f"Total Recaudado: {AcumDinero}")
porcentaje = (contadorExpress / contador) * 100
if contadorExpress > 0:
    print(f"Porcentaje de paquetes Express: {porcentaje}")
print(f"Total de KG enviados: {AcumPeso}")

