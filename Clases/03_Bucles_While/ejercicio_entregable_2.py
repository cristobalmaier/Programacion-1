# Un restaurante vende pizzas y empanadas, y necesita que realicemos un programa para registrar sus ventas del día.

# Se debe registrar ventas hasta que número de factura sea un negativo.

# Por cada factura, solicitar indicar si se vende pizza ("P") o empanadas ("E"), y luego el monto en pesos. 

# Mostrar:

    # La cantidad de facturas cargadas de empanadas y de pizzas, y la cantidad total recaudado por cada producto. 
    # Con un mensaje que producto recaudó más.
    # El porcentaje de facturas que corresponden a las empanadas.
    # El promedio en pesos de las facturas correspondientes a las pizzas.

# Extra: validad el producto no sea dostitno de P o E, los montos deben ser positivos


cant_pizzas = 0
cant_empanadas = 0
cant_total = 0
monto_pizzas = 0
monto_empanadas = 0
monto_total = 0

factura = int(input("Ingrese el numero de Factura: "))


while factura > 0:
    producto = input("Ingrese el producto (P o E): ").upper()
    monto = float(input("Ingrese el monto (en pesos): "))

    if producto == "P":
        cant_pizzas += 1
        monto_pizzas += monto

    elif producto == "E":
        cant_empanadas +=1
        monto_empanadas += monto
    
    factura = int(input("Ingrese el numero de Factura: "))

monto_total = monto_pizzas + monto_empanadas
cant_total = cant_pizzas + cant_empanadas

print(f"Producto: {producto}, monto: {monto}")
print(f"Cantidad de pizzas: {cant_pizzas}, Cantidad de empanadas: {cant_empanadas}")
print(f"Cantidad Recaudado de Empandas: {monto_empanadas}, Cantidad Recaudado de Pizzas: {monto_pizzas}")



if monto_pizzas > monto_empanadas:
    print("Las pizzas recaudaron mas")
else:
    print("Las Empanadas recaudaron mas")

if cant_pizzas > 0:
    print(f"El promedio de cantidad de pesos de las facturas de Pizza son: {monto_pizzas / cant_pizzas}")

if cant_total > 0:
    porcentaje_empanadas = (cant_empanadas / cant_total) * 100
    print(f"El porcentaje de facturas de empanadas es: {porcentaje_empanadas}")
