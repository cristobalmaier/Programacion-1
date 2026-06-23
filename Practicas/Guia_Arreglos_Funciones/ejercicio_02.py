# 1. COMPLETÁ LA FUNCIÓN PARA QUE RECORRA EL ARREGLO CON UN 'FOR' 
# Y EL ÍNDICE 'i'. SI ENCUENTRA LA NOTA QUE BUSCA, DEBE RETORNAR EL ÍNDICE 'i'.
# SI TERMINA EL CICLO Y NO LA ENCUENTRA, DEBE RETORNAR EL LARGO DEL ARREGLO.

def buscar_nota(arr_notas, nota_buscada):
    i = 0
    while i < len(arr_notas) and arr_notas[i] != nota_buscada:
        i += 1
    return i

# PROGRAMA PRINCIPAL
notas_primer_parcial = [4, 7, 10, 2, 8]

# 2. LLAMÁ A LA FUNCIÓN PASÁNDOLE TU LISTA REAL Y LA NOTA 10.
# GUARDA EL RESULTADO EN UNA VARIABLE LLAMADA 'posicion'.

posicion = buscar_nota(notas_primer_parcial,10)

# 3. IMPRIMÍ LA VARIABLE 'posicion' PARA VER QUÉ TE DEVUELVE EN LA TERMINAL.

print(posicion)