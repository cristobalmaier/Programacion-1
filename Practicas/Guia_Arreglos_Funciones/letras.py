# Cargar un arreglo con letras hasta ingresar una X 

# Crear una función que cuente la cantidad de letra A ingresadas y retorne ese valor.

def contador_letras(arr_letras):
    cont = 0
    for i in range(len(arr_letras)):
        if arr_letras[i] == "A":
            cont += 1
    return cont

def cargar(arr_letras):
    letra = input("Ingrese letra: ").upper()
    while letra != "X":
        arr_letras.append(letra)
        letra = input("Ingrese letra: ").upper()

letras = []

cargar(letras)
print(letras)
contadorLetraA = contador_letras(letras)
print(f"Cantidad de veces de A ingresadas: {contadorLetraA}")