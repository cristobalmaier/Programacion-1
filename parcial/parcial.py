def ingresar_continente():
    continente = input("Ingrese continente: (America, Asia, Oceania, Europa, Africa, FIN): ")
    while continente != "America" and continente != "Asia" and continente != "Oceania" and continente != "Europa" and continente != "Africa" and continente != "FIN":
        continente = input("Ingrese continente: (America, Asia, Oceania, Europa, Africa, FIN): ")
    return continente
 
 
def ingresar_nombre_montaña():
    montaña = input("Ingrese nombre Montaña: ")
    while montaña == "":
        montaña = input("Ingrese nombre Montaña: ")
    return montaña
 
 
def ingresar_altura_montaña():
    altura_montaña = float(input("Ingrese altura montaña: "))
    while altura_montaña < 0 :
        altura_montaña = float(input("Ingrese altura montaña: "))
    return altura_montaña



def eliminar_moñtanas_chicas(arr_continente,arr_nombre_montaña,arr_alturas_montañas,arr_altura_escalada):
    i = 0
    while i < len(arr_continente):
        if arr_altura_escalada[i] < 100:
            print(f"Elimimando la {arr_nombre_montaña[i]} con menos de 100 metros de escalada")
            arr_continente.pop(i)
            arr_nombre_montaña.pop(i)
            arr_alturas_montañas.pop(i)
            arr_altura_escalada.pop(i)
            print("Se saco la Montaña")
        else:
            i += 1


def ingresar_altura_escalada(altura_montaña):
    altura_escalada = float(input("Ingrese altura escalada: "))
    while altura_escalada < 0 or altura_escalada > altura_montaña:
        altura_escalada = float(input("Ingrese altura escalada: "))
    return altura_escalada

def buscar_nombre_repetido(arr_nombre_montaña,montaña_a_buscar):
    i = 0
    while i < len(arr_nombre_montaña) and arr_nombre_montaña[i] != montaña_a_buscar:
        i += 1
    return i
 
def calcular_montaña_mas_alta_asia(arr_continente,arr_nombre_montaña,arr_alturas_montañas,arr_altura_escalada):
    
    indice_mayor = buscar_elemento_asia(arr_continente)

    for i in range (len(arr_continente)):
        if arr_continente[i] == "Asia":
            if arr_alturas_montañas[i] > arr_alturas_montañas[indice_mayor]:
                indice_mayor = i
    return indice_mayor
 
 
def calcular_promedio_america(arr_continente,arr_altura_escalada):
    acum = 0
    cont = 0
    for i in range (len(arr_altura_escalada)):
        if arr_continente[i] == "America":
            acum += arr_altura_escalada[i]
            cont += 1
    promedio = acum / cont
    return promedio
 
def buscar_elemento_asia(arr_continente):
    i = 0
    while i < len(arr_continente) and arr_continente[i] != "Asia":
        i += 1
    return i

 
def calcular_montañas_escaladas(arr_nombre_montaña,arr_alturas_montañas,arr_alturas_escaladas):
    cont = 0
    for i in range (len(alturas_escaladas)):
        if arr_alturas_montañas[i] - arr_alturas_escaladas[i] == 0:
            cont += 1
            print(f"La montaña {arr_nombre_montaña[i]} SI escalo hasta la cima")
        else:
            print(f"La montaña {arr_nombre_montaña[i]} NO escalo hasta la cima")
    
    porcentaje = (cont / len(arr_alturas_escaladas)) * 100
    return porcentaje 
    
def intercambiar (arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux
 
 
def ordenar(arr_continentes,arr_nombres_montaña,arr_alturas_montañas,arr_alturas_escaladas):
    for i in range (len(arr_nombres_montaña)):
        for j in range (len(arr_nombres_montaña)):
            if arr_nombres_montaña[i] < arr_nombres_montaña[j]:
                intercambiar(arr_continentes,i,j)
                intercambiar(arr_nombres_montaña,i,j)
                intercambiar(arr_alturas_montañas,i,j)
                intercambiar(arr_alturas_escaladas,i,j) 
 
 
def mostrar(arr_continentes,arr_nombres_montaña,arr_alturas_montañas,arr_alturas_escaladas):
    for i in range (len(arr_continentes)):
        print(f"Continente: {arr_continentes[i]}")
        print(f"Nombre Montaña: {arr_nombres_montaña[i]}")
        print(f"Altura Montaña: {arr_alturas_montañas[i]}")
        print(f"Altura Escalada: {arr_alturas_escaladas[i]}")
 

def cargar (arr_continentes,arr_nombres_montaña,arr_alturas_montañas,arr_alturas_escaladas):
    
    continente = ingresar_continente()
    
    while continente != "FIN":
        
        nombre_montaña = ingresar_nombre_montaña()
        indice = buscar_nombre_repetido(arr_nombres_montaña,nombre_montaña)
        
        if indice < len(arr_nombres_montaña):
            altura_escalada = ingresar_altura_escalada(arr_alturas_escaladas[indice])
            arr_alturas_escaladas[indice] = altura_escalada
        
        else:
            altura_montaña = ingresar_altura_montaña()
            altura_escalada = ingresar_altura_escalada(altura_montaña)
            
            arr_nombres_montaña.append(nombre_montaña)
            arr_continentes.append(continente)
            arr_alturas_montañas.append(altura_montaña)
            arr_alturas_escaladas.append(altura_escalada)

        continente = ingresar_continente()
 
 
continentes = []
nombres_montañas = []
alturas_montañas = []
alturas_escaladas = []
 
cargar(continentes,nombres_montañas,alturas_montañas,alturas_escaladas)
 
 
if len (continentes) > 0:
    
    print("---- Punto 1 ----")

    indice_asia = buscar_elemento_asia(continentes)
    if indice_asia < len(continentes):
        indice_amyor = calcular_montaña_mas_alta_asia(continentes,nombres_montañas,alturas_montañas,alturas_escaladas)
        print(f"Montaña: {nombres_montañas[indice_amyor]}")
        print(f"Altura Escalada: {alturas_escaladas[indice_amyor]}")
    else:
        print("NO hay montañas en Asia")
    
    print("---- Punto 2 ----")
    promedio = calcular_promedio_america(continentes,alturas_escaladas)
    print(f"Promedio de escalado en America: {promedio}")
    
    print("---- Punto 3 ----")
    porcentaje = calcular_montañas_escaladas(nombres_montañas,alturas_montañas,alturas_escaladas)
    print(f"Porcentaje de montañas Escaladas hasta la cima: {porcentaje}%")
    
    print("---- Punto 4 ----")
    eliminar_moñtanas_chicas(continentes,nombres_montañas,alturas_montañas,alturas_escaladas)

    print("---- Punto 5 ----")
    ordenar(continentes,nombres_montañas,alturas_montañas,alturas_escaladas)
    mostrar(continentes,nombres_montañas,alturas_montañas,alturas_escaladas)
    
else:
    print("No hay datos cargados")