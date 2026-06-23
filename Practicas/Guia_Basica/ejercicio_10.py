"""
El usuario deberá pensar en uno de los siguientes personajes: Lio Messi, Mauricio Macri
y Mirtha Legrand. El programa mediante algunas preguntas convenientes (edad, sexo,
ocupación, etc.) deberá mostrar de que personaje se trata. Ejemplo: si es hombre y
deportista tendrá que decir Lio Messi
"""

sexo = input("¿Es hombre o mujer? ").lower()

if sexo == "mujer":
    print("Tu personaje es: Mirtha Legrand")
elif sexo == "hombre":
    ocupacion = input("Jugo en la seleccion ? (si o no): ")
    if ocupacion == "si":
        print("Tu personaje es: Lionel Messi")
    else:
        print("Tu personaje es: Mauricio Macri")