"""
-------------------------------------------
12. TRY, MULTIPLES EXCEPTS Y FINALLY (UF2.8 - IMPORTANTE)
-------------------------------------------

 - try: codigo susceptible de lanzar errores
 - except TipoError: captura un error concreto (solo se ejecuta UNO como maximo)
 - except (Error1, Error2): captura varios tipos de error en un mismo bloque.
 - except: captura generica (siempre al final)
 - finally: SE EJECUTA SIEMPRE (haya error o no). Ideal para liberar recursos, cerrar ficheros...

"""

archivo = None
try:
    arhcivo = open("miarchivo.txt", "r")
    resultado = 10 / 0
except IOError:
    print("Error de entrada/salida al abrir o leer archivo")
except ZeroDivisionError:
    print("No se permite la division por cero")
except (ValueError, TypeError):
    print("Error de tipo o valor de los datos")
except:
    print("Ha ocurrido otro error no contemplado anteriormente")
finally:
    # Lipieza garantizada: si el archivo llego a abrir y sigue abierto, se cierra
    if archivo is not None and not archivo.closed:
        archivo.close()
        print("Arhcivo cerrado en finally")