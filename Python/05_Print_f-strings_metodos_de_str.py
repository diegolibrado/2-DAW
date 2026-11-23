"""
-------------------------------------------
5.PRINT, F-STRINGS Y METODOS DE STR (UF2.4)
-------------------------------------------

 - print() acepta sep, end, file y flush. Con '+' hay que convertir numeros con strt()
 - f-strings: f"Texto {variable:.2f}" evalua expresiones directamente dentro de {}
 - Metodos str mas usados: upper/lower/title, find/count, isdigit/isalpha, replace/strip, split/join.
 
"""

semanas = 4
decimal = 1.2345
print("¡Feliz "  + str(2026) + "!", end="\n")
print(f"En {semanas} semanas hay {7 * semanas} dias.")
print(f"Valor redondeado a 2 decimales: {decimal:.2f}")     # 1.24

cadena = " python, guia, curso "
limpia = cadena.strip()                 # Quita espacios de los extremos
lista_palabras = limpia.split(", ")     # ['python', 'guia', 'curso']
unida = " - ".join(lista_palabras)      # 'python - guia - curso'
posicion = limpia.find("guia")          # Devuelve indice de inicio o -1 si no existe. 