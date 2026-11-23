"""
-------------------------------------------
8. DECLARACION Y TODOS LOS TIPOS DE PARAMETROS (UF2.5) 
-------------------------------------------

 - def nombre(parametro1, parametro_defecto='valor'): (sin espacios en '=')
 - Sin 'return', la función devuelve None
 - Paso por keywords: unica forma de alterar el orden al invocar.
 - Parametros arbitrarios:
    • *arbitrarios  → llegan como TUPLA (siempre despues de los fijos)
    • **kwords      → llegan como DICCIONARIO (clave=valor).
 - Desempaquetado al llamar:
    • funcion(*lista_o_tupla)
    • funcion(**diccionario)

"""

def saludar(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"

print(saludar("Diego"))                                 # Usa el valor por omision
print(saludar(mensaje="Buen dia", nombre="Lucas"))      # Paso por keywords (orden cambiado)

def recorrer_parametros(parametro_fijo, *arbitrarios, **kwords):
    print("Fijo: ", parametro_fijo)
    for argumento in arbitrarios:
        print("Arbitrario (tupla): ", argumento)
    for clave in kwords:
        print("Keyword (dict): ", clave, "=", kwords[clave])

recorrer_parametros("fijo", "arb1", "arb2", clave1="valor1", clave2="valor2")

# Desempaquetado de parametros en la invocacion
def calcular(importe, descuento):
    return importe - (importe * descuento/100)

datos_lista = [1500, 10]
print(calcular(*datos_lista))                       # Desempaqueta lista/tupla → 1350.0

datos_dict = {"descuento": 10, "importe": 1500}
print(calcular(**datos_dict))                       # Desempaqueta diccionario → 1350.0