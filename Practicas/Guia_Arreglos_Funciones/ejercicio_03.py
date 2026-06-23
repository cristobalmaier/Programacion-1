# 1. COMPLETÁ LA FUNCIÓN PARA QUE RECORRA 'arr_precios' CON UN 'FOR' E ÍNDICE 'i'.
# SI EL PRECIO EN ESA POSICIÓN ES MAYOR O IGUAL A 500, AGREGALO AL ARREGLO 'arr_caros' USANDO APPEND.
def filtrar_caros(arr_precios, arr_caros):
    for i in range(len(arr_precios)):
        if arr_precios[i] >= 500:
            arr_caros.append(arr_precios[i])

# PROGRAMA PRINCIPAL
precios_productos = [120, 550, 80, 1500, 499, 600]
lista_caros_real = []

# 2. LLAMÁ A LA FUNCIÓN PASÁNDOLE TUS DOS ARREGLOS REALES.
filtrar_caros(precios_productos,lista_caros_real)

# 3. IMPRIMÍ 'lista_caros_real' PARA VER SI SE LLENÓ CORRECTAMENTE.

print(lista_caros_real)

arbol = 1
