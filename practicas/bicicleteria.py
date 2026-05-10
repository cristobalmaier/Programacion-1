"""
Jaime quiere registrar las ventas de bicicletas de su negocio en un día, considerando que tiene dos modelos. Bicicleta de paseo $60.000 y bicicleta todo terreno $75.200 pesos.

Por cada venta registra el número de factura y el modelo P para paseo y T para todo terreno.

La carga finaliza cuando se ingresa en número de factura un -1.

    Cargar la cantidad

    Se pide calcular el porcentaje de bicicletas de paseo por sobre el total vendido.

    El total de recaudación del día.
"""
import os
os.system ("clear")

PrecioBiciPaseo = 60000
PrecioBiciTodoTerreno = 72000
totalBicisPaseo = 0
totalBicisTodoTerreno = 0
cantidad_todoTerreno = 0
cantidad_paseo = 0

factura = int(input("Ingrese numero de factura: "))

while factura != -1:
    modelo_bici = (input("Ingrese el modelo de bicleta para registar P (Paseo) o T (Todo Terreno): ")).upper()
    if modelo_bici == "P":
        cantidad_paseo = int(input("Ingrese la cantidad de bicis de Paseo: "))
        totalBicisPaseo = cantidad_paseo * PrecioBiciPaseo
    elif modelo_bici == "T":
        cantidad_todoTerreno = int(input("Ingrese la cantidad de bicis de Todo Terreno: "))
        totalBicisTodoTerreno = cantidad_todoTerreno * PrecioBiciTodoTerreno
    else:
        print("Modelo de bici equivocado, vuelve a intentar")
    
    factura = int(input("Ingrese numero de factura: "))
else:
    print("Has salido del sistema, vuelva pronto!")

totalRecaudado = totalBicisPaseo + totalBicisTodoTerreno
totalBicis = cantidad_paseo + cantidad_todoTerreno
porcentajeBicisPaseo = (cantidad_paseo / totalBicis) * 100 

print(f"Total de bicis vendidas: {totalBicis}")
print(f"Total Recaudado: ${totalRecaudado}")
print(f"Porcentaje de bicis que son de paseo: {porcentajeBicisPaseo}")