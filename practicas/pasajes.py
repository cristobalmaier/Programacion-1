import os
os.system("clear")

PrecioBaseMotos = 500
PrecioBaseAutos = 800
PrecioBaseCamionetas = 1000

# 1. Pedimos los datos principales primero
FindeDeSemana = input("¿Es Finde de Semana? (S o N): ").upper()
opc = input("Ingrese el tipo de vehiculo: M (Moto), A (Auto), T (Camioneta), C (Camion): ").upper()

total = 0 # Inicializamos la variable para que no de error al final

# --- Lógica para determinar el PRECIO BASE según el vehículo ---
if opc == "M":
    precio_base = PrecioBaseMotos
elif opc == "A":
    precio_base = PrecioBaseAutos
elif opc == "T":
    precio_base = PrecioBaseCamionetas
elif opc == "C":
    cantidadEjes = int(input("Ingrese el total de ejes extras del camion: "))
    # El camión es base de camioneta + 300 por eje
    precio_base = PrecioBaseCamionetas + (300 * cantidadEjes)
else:
    print("Opción de vehículo no válida")
    precio_base = 0

# --- Lógica de RECARGOS según el día y la hora ---
if FindeDeSemana == "S":
    # Fines de semana: Valor base sin cambios
    total = precio_base
else:
    # Días de semana: Preguntamos la hora
    horario = int(input("Ingrese el horario actual (0-23): "))
    
    if horario >= 20 or horario <= 5:
        # Horario NO PICO: +5% (Se multiplica por 1.05)
        total = precio_base * 1.05
        print("Aplicado recargo de hora NO PICO (5%)")
    else:
        # Horario PICO: +10% (Se multiplica por 1.10)
        total = precio_base * 1.10
        print("Aplicado recargo de hora PICO (10%)")

# --- Mostrar resultado y cobrar ---
print(f"\nEl monto final a pagar es: ${total}")

MontoEntregado = float(input("Ingrese el monto entregado por el conductor: "))

if MontoEntregado == total:
    print("Monto correcto, no hay vuelto.")
elif MontoEntregado > total:
    vuelto = MontoEntregado - total # Es el dinero entregado menos el costo
    print(f"El peaje debe devolver: ${vuelto}")
else:
    falta = total - MontoEntregado
    print(f"Dinero insuficiente. Faltan pagar: ${falta}")