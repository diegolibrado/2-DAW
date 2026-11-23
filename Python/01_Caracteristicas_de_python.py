"""
-------------------------------------------
1. CARACTERISTICAS DE PYTHON (UF2.1 - DIAPOSITIVAS 4 Y 5)
-------------------------------------------

 - Interpretado: traduce el codigo fuente a bytecode la primera vez.
 - Tipado dinamico: el tipo lo define el valor en tiempo de ejecucion y puede cambiar.
 - Alto nivel, multiplataforma, multiparadigma y sintaxis simple.

"""

# Ejemplo de tipado dinamico: la misma variable cambia de tipo sin dar error.
dato = 10           # En tiempo de ejecucion es 'int'
dato = "texto"      # Ahora pasa a ser 'string'
print(dato)