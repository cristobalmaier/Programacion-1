hora = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))

if minutos > 15:
    hora += 1  

if hora == 0:
    hora = 1

importe = hora * 45
print(f"Tenes que pagar: ${importe}")