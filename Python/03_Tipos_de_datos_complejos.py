"""
-------------------------------------------
3. TIPOS DE DATOS COMPLEJOS: TUPLAS, LISTAS Y DICCIONARIOS (UF2.2)
-------------------------------------------

 - Tupla ( ): Coleccion INMUTABLE (no se puede modificar ni añadir elementos)
 - Lista [ ]: Coleccion MUTABLE (permite modificar por indice y añadir con .append())
 - Diccionario { }: Coleccion de pares clave:valor (mutable, permite 'del')
 - Slicing[inicio:fin]: Extrae porciones; indices negativos recorren desde el final (-1 es el ultimo)

"""

# TUPLAS (inmutables)
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
print(mi_tupla[1])          # 15 (el primer indice es el 0)
print(mi_tupla[1:4])        # (15, 2.8, 'otro dato') → el fin (4) no se incluye
print(mi_tupla[3:])         # ('otro dato', 25) → desde el indice 3 al final
print(mi_tupla[:2])         # ('cadena de texto', 15) → desde el inicio hasta el indice 1 (el 2 no se incluye)
print(mi_tupla[-1])         # 25 (ultimo elemento)

# LISTAS (mutables)
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
mi_lista[2] = 3.8                   # Modifica el tercer elemento
mi_lista.append('Nuevo dato')       # Añade al final

# DICCIONARIOS (clave:valor)
mi_diccionario = {'clave_1': 'valor_1', 'clave_2': 'valor_2', 'clave_3': 'valor_3'}
print(mi_diccionario['clave_2'])        # Accede por clave -> 'valor_2'
mi_diccionario['clave_1'] = 'Nuevo'     # Modifica el valor
del(mi_diccionario['clave_2'])          # Elimina la entrada 'clave_2'