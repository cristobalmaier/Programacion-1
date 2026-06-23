# DEFINICIÓN (El molde)
def mostrar_precios_duplicados(arr_precios):
    # 1. Escribí el ciclo FOR para recorrer "arr_precios" elemento por elemento
    for i in range(len(arr_precios)):
        print(arr_precios[i] * 2)

# PROGRAMA PRINCIPAL
mis_precios_reales = [10, 100, 1500]

# 2. Llamá a la función pasándole tu lista real

mostrar_precios_duplicados(mis_precios_reales)