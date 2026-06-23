"""
Una cerealera desea clasificar sus clientes de acuerdo a las toneladas que le compran.
    - Cliente que compra menos de 100 toneladas: chico.
    - Cliente que compra entre 100 y 300 toneladas: mediano.
    - Cliente que compra más de 300 toneladas: grande.
Se desea diseñar un algoritmo que permita el ingreso de las toneladas por cliente.
Finaliza el ingreso de datos cuando se ingrese un cliente igual a 000.
Luego muestre la siguiente información por pantalla:
    - Cantidad de clientes.
    - Calcular el valor total de toneladas vendidas, sabiendo que la tonelada cuesta 250
    dólares, y que los clientes grandes tienen un descuento del 5%.
    - Porcentaje de toneladas vendidas por categoría. (cantidad_categoria*100/Total)
"""

cliente = int(input("Ingrese la cantidad de toneladas: "))

contador_clientes = 0
cantidad_chico = 0
cantidad_mediano = 0
cantidad_grande = 0
total_toneladas = 0
toneladas_chico = 0
toneladas_mediano = 0
toneladas_grande = 0

acumDinero = 0

while cliente != 000:

    if cliente < 100:
        total = 250 * cliente
        acumDinero += total
        cantidad_chico += 1
        total_toneladas += cliente
        toneladas_chico += cliente
        
    elif cliente >= 100 and cliente <= 300:
        total = 250 * cliente
        acumDinero += total
        cantidad_mediano += 1
        total_toneladas += cliente
        toneladas_mediano += cliente
    else:
        total = 250 * cliente
        descuento = total * 0.05
        total_final = total - descuento
        acumDinero += total_final
        cantidad_grande += 1
        total_toneladas += cliente
        toneladas_grande += cliente

    contador_clientes += 1
    cliente = int(input("Ingrese la cantidad de toneladas: "))



if contador_clientes > 0:
    print(f"Total vendido: {acumDinero}")
    print(f"Cantidad de clientes: {contador_clientes}")
    if total_toneladas > 0:
        porcentaje_chico = (toneladas_chico / total_toneladas) * 100
        porcentaje_mediano = (toneladas_mediano / total_toneladas) * 100
        porcentaje_grande = (toneladas_grande / total_toneladas) * 100
        print(f"porcentaje de toneladas chico: {porcentaje_chico}")
        print(f"porcentaje de toneladas mediano: {porcentaje_mediano}")
        print(f"porcentaje de toneladas grande: {porcentaje_grande}")