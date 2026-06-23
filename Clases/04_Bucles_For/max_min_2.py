# maximo y minimo Temperatura

temp = float(input("Ingrese una temperatura: "))
cont_temps = 0

while temp != 0:
    
    if cont_temps == 0:
        maximo = temp
        minimo = temp

    if temp > maximo:
        maximo = temp
    if temp < minimo:
        minimo = temp
    
    cont_temps += 1

    temp = float(input("Ingrese una temperatura: "))

