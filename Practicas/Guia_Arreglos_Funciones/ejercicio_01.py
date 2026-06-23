# DEFINICIÓN (El molde de la función)
def cargar_precio_producto(arr_precios, precio_nuevo):
    # 1. Escribí acá adentro la línea para agregar el precio al arreglo
    arr_precios.append(precio_nuevo)

# PROGRAMA PRINCIPAL (Tus datos reales)
mis_precios_reales = [10,100]

# 2. Escribí acá abajo la línea para llamar a la función, 
# pasándole tu lista real y un precio real de 1500.

cargar_precio_producto(mis_precios_reales,1500)

print(mis_precios_reales)