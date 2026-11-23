"""
-------------------------------------------
7. DICCIONARIOS ('mapa') Y RECORRIDOS + NOTA SOBRE map() (UF2.4)
-------------------------------------------

 - Metodos de dict:
    • keys(), values(), items(): vistas de claves, valores y tuplas (clave, valor)
    • get(calve, default): obtiene el valor sin lanzar KeyError si no existe
    • setdefault(clave, default): devuelve valor si existe; si no, lo inserta con default
    • pop(clave, default) / popitem() / del(dic[clave]) / clear() / copy()
 - Funcion integrada map(funcion, iterable): aplica una funcion a cada elemento de un iterable
   y devuelve un iterador (suele convertirse con list(map(...)))                                

"""

mapa = {1: "uno", 2: "dos", 3: "tres"}

print(list(mapa))                   # [1, 2, 3] (lista de claves)
print(mapa.get(6, "no esta"))       # "no esta" (no falla)
mapa.setdefault(4, "cuatro")        # Inserta 4: "cuatro" al no existir
mapa_copia = mapa.copy()            # Copia con distinta referencia

# Las 3 formas de recorrer un diccionario
for clave in mapa.keys():
    print("Clave:", clave)

for valor in mapa.values():
    print("Valor:", valor)

for clave, valor in mapa.items():
    print(f"{clave} -> {valor}")

# Nota extra: list() + funcion nativa map()
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x ** 2, numeros))    # [1, 4, 9, 16]