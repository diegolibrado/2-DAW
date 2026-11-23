"""
-------------------------------------------
15. CONTROL DEL PUNTERO (tell() Y seek()), PROPIEDADES Y CIERRE SEGURO (UF2.10 + UF2.8)
-------------------------------------------

 - El puntero indica en que BYTE se hara la siguiente lectura o escritura
 - tell(): devuelve la posicion actual del puntero (entero en bytes)
 - seek(byte): desplaza el puntero al principio del archivo
    • archivo.seek(0)   → rebobina el untero al principio del archivo
    • archivo.seek(pos) → salta a una posicion guardada previamente con tell()
 - Propiedades del objeto File:
    • archivo.name      → nombre del fichero
    • archivo.mode      → modo de apertura (r, r+, wb...)
    • archivo.encoding  → codificacion deel fichero (solo en TEXTO)
    • archivo.closed    → True si esta cerrado, False si esta abierto.

"""

# Preparamos un archivo base con contenido conocido (solo ASCII para ver 1 letra = 1 byte)
prep = open("puntero.txt", "w", encoding="utf-8")
prep.write("ABDCEFGHIJ\n")      # Bytes 0..9 son 'A'..'J'
prep.write("1234567890\n")      # Segunda linea
prep.close()

# =============================================================================
# PARTE A: PROPIEDADES DEL OBJETO FILE Y MOVIMIENTO DEL PUNTERO
# =============================================================================

archivo = open("puntero.txt", "r", encoding="utf-8")

# 1. Consultar propiedades mientras el archivo esta abierto
print("--- PROPIEDADES DEL ARCHIVO ---")
print("Nombre (name): ",            archivo.name)           # puntero.txt
print("Modo (mode): ",              archivo.mode)           # r
print("Codificacion (enc): ",       archivo.encoding)       # utf-8 (texto)
print("¿Esta cerrado?: ",           archivo.closed)         # false

# 2. Ver como avanza el puntero con tell() al leer
print("--- SEGUIMIENTO DEEL PUNTERO ---")
print("Posicion inicial: ", archivo.tell())                 # 0 porque 'r' empieza al inicio

trozo1 = archivo.read(4)                                    # lee ABCD
print("Leido: ", trozo1, "| Puntero ahora en: ", archivo.tell())

trozo2 = archivo.read(3)                                    # Lee "EFG" desde el byte 4
print("Leído:", trozo2, "| Puntero ahora en:", archivo.tell())  # Byte 7

# 3. Trampa del final de archivo (EOF): leer hasta el final y volver a leer sin seek(0)
resto = archivo.read()                                      # Lee todo lo que quedaba hasta el final
print("Puntero al final: ", archivo.tell())

lectura_vacia = archivo.read()                              # DEVUELVE "" PORQUE YA ESTÁ AL FINAL
print("Segundo read() sin seek(0):", repr(lectura_vacia))   # ''

# 4. Rebobinar con seek(0) y saltar a bytes concretos
archivo.seek(0)                                     # Vuelve al byte 0 (inicio exacto)
print("Tras seek(0), puntero en:", archivo.tell())  # 0
print("Primera línea completa:", archivo.readline().strip())  # "ABCDEFGHIJ"

# Saltar directamente al byte 5 (la letra 'F', porque A=0, B=1, C=2, D=3, E=4, F=5)
archivo.seek(5)
print("Desde byte 5 (3 chars):", archivo.read(3))   # "FGH"

archivo.close()
print("¿Cerrado tras close()?:", archivo.closed)    # True

# =============================================================================
# PARTE B: PATRÓN CLÁSICO DE LOS APUNTES CON 'r+', tell() Y seek()
# =============================================================================
# Objetivo: abrir en lectura/escritura ('r+'), llegar al final sin sobrescribir nada,
# guardar esa posición con tell(), escribir contenido nuevo y volver atrás con seek()
# para leer ÚNICAMENTE lo que acabamos de añadir.

archivo = open("puntero.txt", "r+", encoding="utf-8")

# Paso 1: En 'r+', el puntero empieza en 0. Si escribiéramos ahora, machacaríamos "ABCD...".
# Por eso leemos todo primero para llevar el puntero hasta el final del archivo.
contenido_previo = archivo.read()

# Paso 2: Guardamos en una variable el byte exacto donde termina el contenido antiguo.
final_de_archivo = archivo.tell()
print("\n--- PATRÓN r+ CON tell() Y seek() ---")
print("El contenido antiguo termina en el byte:", final_de_archivo)

# Paso 3: Escribimos nuevas líneas a partir de ese final.
# Al escribir, el puntero vuelve a desplazarse hacia el nuevo final.
nuevas_lineas = ["Nueva linea 1\n", "Nueva linea 2\n"]
archivo.writelines(nuevas_lineas)

# Paso 4: Retrocedemos el puntero justo al marcador que guardamos antes de escribir.
archivo.seek(final_de_archivo)

# Paso 5: Ahora leemos desde ese punto: solo aparecerá lo recién escrito.
print("Línea añadida 1:", archivo.readline().strip())  # Nueva linea 1
print("Línea añadida 2:", archivo.readline().strip())  # Nueva linea 2

archivo.close()

# =============================================================================
# PARTE C: APERTURA SEGURA COMBINANDO UF2.8 (EXCEPCIONES) Y UF2.10 (FILE)
# =============================================================================
# Si el archivo no existe o hay un error al leerlo, no se cae el programa y
# 'finally' garantiza el cierre comprobando la propiedad 'closed'.

fichero = None

try:
    fichero = open("archivo_que_no_existe.txt", "r", encoding="utf-8")
    datos = fichero.read()
    print(datos)
except IOError as error_es:
    print("\nError de entrada/salida detectado:", error_es)
except Exception as error_general:
    print("\nOtro error inesperado:", error_general)
finally:
    # Comprobamos que se llegó a asignar (no es None) y que sigue abierto
    if fichero is not None and not fichero.closed:
        fichero.close()
        print("Fichero cerrado de forma segura en finally.")


"""
IMPORTANTE:

 - r / rb: solo lectura, puntero al inicio.   
 - w / wb: solo escritura, sobrescribe el fichero si existe o lo crea si no existe, puntero al inicio.   
 - a / ab: añadido (append), conserva el contenido anterior, crea el fichero si no existe y coloca el puntero al final si ya existía. 

"""