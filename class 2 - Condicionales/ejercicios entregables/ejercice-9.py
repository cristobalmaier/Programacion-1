año = int(input("Ingrese un año: "))

if año % 400 == 0:
    print("Año bisiesto")
elif año % 100 == 0:
    print("Año común")
elif año % 4 == 0:
    print("Año bisiesto")
else:
    print("Año común")