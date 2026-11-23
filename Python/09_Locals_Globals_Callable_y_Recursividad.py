"""
-------------------------------------------
9. LOCALS(), GLOBALS(), CALLABLE() Y RECURSIVIDAD (UF2.5 - IMPORTANTE)
-------------------------------------------

 - locals(): devuelve un diccionario con las variables y funciones del ambito local actual
 - globals(): devuelve un diccionario con las variables y funciones del ambito global
 - Comprobacion dinamica antes de ejecutar una funcion:
    • 'nombre' in locals() / globals()  → comprueba si existe en el ambito
    • callable(locals()['nombre'])      → comprueba si el objeto es invocable (una funcion).
 - Recursividad: una funcion se llama a si misma hasta cumplir condicion de parada

"""

def funcion_prueba():
    return "Ejecutada correctamente"

nombre_de_la_funcion = "funcion_prueba"

# Comprobar si existe en el ambito local/global y si puede ser llamada
if nombre_de_la_funcion in locals():
    if callable(locals()[nombre_de_la_funcion]):
        print("La funcion ", locals()[nombre_de_la_funcion], "puede ser llamada")
        print(locals()[nombre_de_la_funcion]()) # Invocacion dinamica
    else:
        print("El elemento ", locals()[nombre_de_la_funcion], "No puede ser llamado")

# Ejemplo de funcion recursiva con limite de intentos
def jugar(intento = 1):
    respuesta = input("¿De que color es una naranja?")
    if respuesta != "naranja":
        if intento < 3:
            print("¡Fallaste! Intentalo de nuevo")
            intento += 1
            jugar(intento)  # Llamada recursiva
        else:
            print("¡Perdiste!")
    else:
        print("¡Ganaste!")