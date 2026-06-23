import os
os.system("clear")

# 1. Definir Precios Base
motos = 500
autos = 800
camionetas = 1000

# 2. Entrada de datos
es_finde = input("¿Es Fin de Semana? (S/N): ").upper()
tipo = input("Vehículo: M (Moto), A (Auto), T (Camioneta), C (Camión): ").upper()

# Determinar precio base inicial
if tipo == "M":
    precio_base = motos
elif tipo == "A":
    precio_base = autos
elif tipo == "T":
    precio_base = camionetas
elif tipo == "C":
    ejes = int(input("Ingrese cantidad de ejes: "))
    precio_base = camionetas + (300 * ejes)
else:
    precio_base = 0
    print("Tipo no válido")

# 3. Aplicar Recargos (Solo si no es finde)
total_a_pagar = precio_base

if es_finde == "N":
    hora = int(input("Ingrese la hora (0-23): "))
    if hora >= 20 or hora <= 5:
        # Horario NO PICO: +5%
        total_a_pagar = precio_base * 1.05
    else:
        # Horario PICO: +10%
        total_a_pagar = precio_base * 1.10

print(f"\nEL TOTAL A COBRAR ES: ${total_a_pagar}")

# 4. Gestión de Pago y Vuelto
pago = float(input("Ingrese monto entregado por el conductor: "))

if pago >= total_a_pagar:
    vuelto = pago - total_a_pagar
    if vuelto > 0:
        print(f"Cobro exitoso. Entregar vuelto de: ${vuelto}")
    else:
        print("Cobro exitoso. No hay vuelto.")
else:
    falta = total_a_pagar - pago
    print(f"Dinero insuficiente. Faltan: ${falta}")