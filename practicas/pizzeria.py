"""
Desarrollar un algoritmo que brinde información sobre las compras de una pizzería. Para ello se ingresa, por cada uno de los pedidos, la siguiente información:

Número de mesa
Cantidad de pizzas grandes
Tipo de pizza. "M" para muzzarella, "J" para jamón, "N" para napolitana

La carga termina cuando en número de pedido se ingresa un 0.

Los precios de las pizzas según la variedad son los siguientes:

Muzzarella $5500
Jamón $7000
Napolitana $6500

Solo se compra un tipo de pizza por mesa.

Se pide:

El valor de ticket promedio en monto.
La cantidad de pizzas vendidas en total.
El porcentaje de pizzas de jamón sobre el total de pizzas.
En el caso que la compra supere los 36.000 pesos, se deberá calcular un descuento del 15% en el ticket. Calcularlo y mostrar el monto a pagar.
Mostrar el total consumido en cada compra.
"""

contador_mesas = 0
cantidad_jamon = 0
acum_dinero = 0
total_pizzas = 0

muzzarella = 5500
jamon = 7000
napolitana = 6500

numero_pedido = int(input("Ingrese un número de pedido, 0 para salir: "))

while numero_pedido != 0:

    numero_mesa = int(input("Ingrese un número de mesa: "))
    while numero_mesa <= 0:
        numero_mesa = int(input("Error! Ingrese un número de mesa válido: "))

    cantidad_pizzas_grandes = int(input("Ingrese la cantidad de pizzas grandes: "))
    while cantidad_pizzas_grandes <= 0:
        cantidad_pizzas_grandes = int(input("Error! Ingrese una cantidad válida: "))

    tipo_pizza = input("Ingrese el tipo de pizza M/J/N: ")
    while tipo_pizza != "M" and tipo_pizza != "J" and tipo_pizza != "N":
        tipo_pizza = input("Error! Ingrese un tipo de pizza válido: ")

    contador_mesas += 1

    if tipo_pizza == "M":
        total = muzzarella * cantidad_pizzas_grandes

    elif tipo_pizza == "J":
        total = jamon * cantidad_pizzas_grandes
        cantidad_jamon += cantidad_pizzas_grandes

    else:
        total = napolitana * cantidad_pizzas_grandes

    if total > 36000:
        descuento = total * 0.15
        total_final = total - descuento
    else:
        total_final = total

    acum_dinero += total_final
    total_pizzas += cantidad_pizzas_grandes

    print(f"Total consumido: ${total}")

    if total > 36000:
        print(f"Descuento aplicado: ${descuento}")

    print(f"Monto final a pagar: ${total_final}")

    numero_pedido = int(input("Ingrese un número de pedido, 0 para salir: "))

if contador_mesas > 0:

    porcentaje = (cantidad_jamon / total_pizzas) * 100
    promedio = acum_dinero / contador_mesas

    print(f"Cantidad total de pizzas vendidas: {total_pizzas}")
    print(f"Porcentaje de pizzas de jamón: {porcentaje:.2f}%")
    print(f"Promedio de ticket: ${promedio:.2f}")