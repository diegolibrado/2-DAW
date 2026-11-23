"""
-------------------------------------------
6. MÉTODOS DE LISTAS Y COPIA POR REFERENCIA VS VALOR (UF2.4)
-------------------------------------------

 - lista2 = lista1 → MISMA referencia (modificar una modifica la otra)
 - lista3 = lista1[:] → COPIA real indepeniente.
 - Agregacion: append(elemento), extend(otra_lista), insert(posicion, elemento)
 - Eliminacion: pop() [ultimo], pop(indice), remove(valor)
 - Orden/Busqueda: sort(), sort(reverse=True), reverse(), count(), index(), max(), min(), len()

"""

# Diferencia critica al copiar listas
lista1 = ["A", "B", "C"]           
lista2 = lista1                 # Referencia compartida
lista3 = lista1[:]              # Copia independiente mediante slicing
del lista1[1]                   # Elimina "B" en lista1 y lista2, pero NO en lista3
print(lista1, lista2, lista3)   # ['A', 'C'] ['A', 'C'] ['A', 'B', 'C']

# Metodos de  modificacion y ordenacion
nombres = ["Alvaro", "Miguel", "David"]     
nombres.append("Jose")                      # Añade al final
nombres.extend(["Jorge", "Juan"])           # Añade varios elementos de otra lista
nombres.insert(0, "Alberto")                # Inserta en el indice 0
nombres.pop(3)                              # Elimina por indice
nombres.remove("Jose")                      # Elimina la primera aparicion del valor
nombres.sort()                              # Orden ascendente
nombres.sort(reverse=True)                  # Orden descendente