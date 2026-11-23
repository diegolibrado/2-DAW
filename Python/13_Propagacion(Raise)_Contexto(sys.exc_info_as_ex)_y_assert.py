"""
-------------------------------------------
13. PROPAGACION (RAISE), CONTEXTO (sys.exc_info / as ex) Y ASSERT (UF2.8 - IMPORTANTE)
-------------------------------------------

 - raise: relanza la excepcion actual o lanza una nueva con mensaje personalizado
 - Contexto en except:
    • except Tipo as ex → acceso al mensaje (ex), tipo (type(ex)) y argumentos (ex.args)
    • sys.exc_info()    → tupla de 3 elementos: (tipo, valor, traceback)
 - assert condicion: si es False, lanza AssertionError (validacion de datos)

"""

import sys

def dividir(dividendo, divisor):
    try:
        return dividendo/divisor
    except ZeroDivisionError:
        # Propagamos una excepcion con informaicon de contexto mas clara
        raise ZeroDivisionError("El divisor no puede ser cero")

def main():
    try:
        print(dividir(5, 0))
    except ZeroDivisionError as ex:
        print("Ha ocurrido una excepcion: ", ex)
        print("Tupla sys.exc_info(): ", sys.exc_info())
        print("Tipo: ", type(ex))
        print("Argumentos: ", ex.args)

    # Validacion con assert
    try:
        edad = -5
        assert edad >= 0, "La edad no puede ser negativa"
    except AssertionError as err:
        print("Fallo de validacion assert: ", err)

main()