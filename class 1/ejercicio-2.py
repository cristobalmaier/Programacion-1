# Solicitar nombre apellido dni,edad,peso y altura
# Guardar cada dato en una variable
# el nombre y apeliido convertirlos en mayuscula
# Mostrarlo asi
# Apeliido y Nombre
# DNI
# Edad
# Edad en 35 años:
# IMC 25.06

nombre = str(input("Ingrese un nombre: "))
apellido = str(input("Ingrese un apellido: "))
DNI = int(input("Ingrese su DNI: "))
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))


nombre = (nombre.upper())
apellido = (apellido.upper())
edad_futura = edad + 35
IMC = peso / (altura**2)

print(f"Apellido y Nombre: {apellido} {nombre}")
print(f"DNI: {DNI}")
print(f"Edad: {edad}")
print(f"Edad en 35 años: {edad_futura}")
print(f"IMC: {IMC}")