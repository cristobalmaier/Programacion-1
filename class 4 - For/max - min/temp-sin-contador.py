temp = float(input("Ingrese la temperatura: "))

contador_maximo = 0

if temp != 0:
    maximo = temp
    minimo = temp
    while temp != 0:

        if temp > maximo:
            maximo = temp
            contador_maximo = 1 # Para resetear el contador hay que usra un if y poner el contador en 0
        elif temp == maximo:
                contador_maximo += 1
        if temp < minimo:
            minimo = temp
        
        temp = float(input("Ingrese otra temperatura: "))
        print(f"La maxima temperatura es: {maximo}")
else:
    print("No se registraron temperaturas")