"""
Una agencia aeroespacial necesita un sistema para gestionar los satélites que tiene en órbita alrededor de diferentes
planetas del sistema solar. Para ello, se deben mantener 4 arreglos paralelos:

- planetas (Cadenas de caracteres: "Tierra", "Marte", "Jupiter", "Saturno", "FIN")

- nombres_satelites (Cadenas de caracteres, únicos)

- alturas_orbitas (Valores flotantes en km, mayores a 0)

- combustibles_restantes (Valores flotantes en litros, mayores o iguales a 0, y nunca mayores a la altura de su órbita)

Funciones a desarrollar:

- cargar_satelites: Solicita los datos al usuario validando las entraźdas. Si el satélite ya existe en el sistema,
 se debe actualizar su combustible restante (validando contra la altura de órbita ya existente). Si no existe, se agregan todos los datos a las listas. Finaliza al ingresar "FIN" en el planeta.

- calcular_mas_lejano_marte: Debe buscar primero la posición del primer satélite de "Marte" mediante una función de búsqueda secundaria. A partir de ahí, encontrar y retornar el índice del satélite de Marte que tenga la mayor altura de órbita.

- calcular_promedio_combustible_tierra: Debe calcular y retornar el promedio de combustible restante únicamente de los satélites que orbitan la "Tierra".

- eliminar_satelites_secos: Debe recorrer los arreglos en paralelo y eliminar por completo a todo satélite cuyo combustible restante sea menor a 10 litros.

- ordenar_satelites: Debe ordenar todos los arreglos en paralelo alfabéticamente de la A a la Z según el nombre_satelite (utilizando el método burbuja clásico).

- mostrar_por_planeta: Debe recibir un planeta por parámetro y listar únicamente los satélites pertenecientes a ese planeta.
"""

def ingresar_planeta():
    planeta = input("Ingrese un planeta (Tierra, Marte, Jupiter, Saturno, FIN): ")
    while planeta != "Tierra" and planeta != "Marte" and planeta != "Jupiter" and planeta != "Saturno" and planeta != "FIN":
        planeta = input("ERROR! Ingrese un planeta(Tierra, Marte, Jupiter, Saturno, FIN): ")
    return planeta

def ingresar_satelite():
    satelite = input("Ingrese Satelite: ")
    while satelite == "":
        satelite = input("Ingrese Satelite: ")
    return satelite

def ingresar_altura_orbitas():
    altura_orbitas = float(input("Ingrese altura orbitas: "))
    while altura_orbitas <= 0:
        altura_orbitas = float(input("ERROR! Ingrese altura orbitas: "))
    return altura_orbitas

def ingresar_combustible(altura_orbitas):
    combustible = float(input("Ingrese combustible: "))
    while combustible < 0 or combustible > altura_orbitas:
        combustible = float(input("ERROR! Ingrese combustible: "))
    return combustible

def buscar_satelite_repetido(arr_satelites, satelite):
    i = 0
    while i < len(arr_satelites) and arr_satelites[i] != satelite:
        i += 1
    return i # Retorna la posición o el largo si no lo encontró

def cargar (arr_planetas, arr_satelites, arr_alturas_orbitas, arr_combustibles):
    planeta = ingresar_planeta()
    while planeta != "FIN":
        
        satelite = ingresar_satelite()
        indice = buscar_satelite_repetido(arr_satelites, satelite)
        if indice < len(arr_satelites):
            nuevo_combustible = ingresar_combustible(arr_alturas_orbitas[indice])
            arr_combustibles[indice] = nuevo_combustible
            print("Se actualizo el combustible del satelite")
        else:
            altura_orbitas = ingresar_altura_orbitas()
            combustible = ingresar_combustible(altura_orbitas)
            arr_planetas.append(planeta)
            arr_satelites.append(satelite)
            arr_alturas_orbitas.append(altura_orbitas)
            arr_combustibles.append(combustible)
            print("Se agrego el satelite")
        
        planeta = ingresar_planeta()

def buscar_primer_satelite_marte(arr_planetas):
    i = 0
    while i < len (arr_planetas) and arr_planetas[i] != "Marte":
        i += 1
    return i

def calcular_mas_lejano_marte (arr_planetas, arr_satelites, arr_altura_orbitas):
    indice_mayor = buscar_primer_satelite_marte(arr_planetas)
    for i in range (len(arr_planetas)):
        if arr_planetas[i] == "Marte":
            if arr_altura_orbitas[i] > arr_altura_orbitas[indice_mayor]:
                indice_mayor = i
    return indice_mayor

def calcular_promedio_combustible_tierra(arr_planetas , arr_combustibles):
    acum = 0
    cont = 0
    promedio = 0

    for i in range (len(arr_combustibles)):
        if arr_planetas[i] == "Tierra":
            acum += arr_combustibles[i]
            cont += 1
    
    if cont > 0:
        promedio = acum / cont
    else:
        print("No hay planteas en la tierra para calcular el combustible")
    return promedio

def eliminar_satelites_secos(arr_planetas, arr_satelites, arr_alturas_orbitas, arr_combustibles):
    i = 0
    while i < len(arr_planetas):
        if arr_combustibles[i] < 10:
            print("---- Eliminando planetas ----")
            arr_planetas.pop(i)
            arr_satelites.pop(i)
            arr_alturas_orbitas.pop(i)
            arr_combustibles.pop(i)
            print("---- Se eliminaro los planetas -----")
        else:
            i += 1

def intercambiar (arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr_planetas, arr_satelites, arr_alturas_orbitas, arr_combustibles):
    for i in range (len(arr_planetas)):
        for j in range (len(arr_planetas)):
            if arr_satelites[i] > arr_satelites[j]:
                intercambiar(arr_planetas,i,j)
                intercambiar(arr_satelites,i,j)
                intercambiar(arr_alturas_orbitas,i,j)
                intercambiar(arr_combustibles,i,j)

def mostrar(arr_planetas, arr_satelites, arr_alturas_orbitas, arr_combustibles, parametro):
    for i in range (len(arr_planetas)):
        if arr_planetas[i] == parametro:
            print(f"Planeta: {arr_planetas[i]}")
            print(f"Satelite: {arr_satelites[i]}")
            print(f"Altura Orbita: {arr_alturas_orbitas[i]}")
            print(f"Combustible: {arr_combustibles[i]}")

planetas = []
satelites = []
alturas_orbitas = []
combustibles = []

cargar(planetas,satelites,alturas_orbitas,combustibles)

if len (planetas) > 0:

    print("---- Punto 1: Satélite más lejano de Marte ----")
    pos_inicial = buscar_primer_satelite_marte(planetas)

    if pos_inicial < len(planetas):
        indice_maximo = calcular_mas_lejano_marte(planetas,satelites,alturas_orbitas)
        print(f"Satelite mas lejano de Marte: {satelites[indice_maximo]}")
        print(f"Orbita: {alturas_orbitas[indice_maximo]} km")
    else:
        print("No se encontraron satelites en Marte")

    print("---- Punto 2: Promedio combustible Tierra ----")
    promedio = calcular_promedio_combustible_tierra(planetas,combustibles)
    print(f"Promedio de combustible: {promedio}")

    print("---- Punto 3: Eliminando satelites con combustible menor a 10 litros ----")
    eliminar_satelites_secos(planetas,satelites,alturas_orbitas,combustibles)
    
    print("---- Punto 4: Ordenando satelites por planeta ----")
    ordenar(planetas,satelites,alturas_orbitas,combustibles)

    print("---- Punto 5: Mostrar satelites por planeta ----")
    mostrar(planetas,satelites,alturas_orbitas,combustibles,"Tierra")
    mostrar(planetas,satelites,alturas_orbitas,combustibles,"Marte")
    mostrar(planetas,satelites,alturas_orbitas,combustibles,"Jupiter")
    mostrar(planetas,satelites,alturas_orbitas,combustibles,"Saturno")

else:
    print("No se ingresaron satelites")