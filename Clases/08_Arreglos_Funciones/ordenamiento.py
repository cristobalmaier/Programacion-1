def intercambiar(arr,i,j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def ordenar(arr1,arr2):
    for i in range (len(arr1)):
        for j in range (len(arr1)):
            if arr1[i] > arr1[j]:
                intercambiar(arr1,i,j)
                intercambiar(arr2,i,j)

def mostrar(arr1,arr2):
    for i in range(len(arr1)):
        print(arr1[i], arr2[i])

# Codigo principal
edades = [10,6,4]
nombres = ["Pepe","Jorge","Roberto"]

ordenar(edades,nombres)
mostrar(edades,nombres)