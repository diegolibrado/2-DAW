"""
-------------------------------------------
14. ABRIR FICHEROS DE TEXTO Y BINARIOS: r, rb, w, wb (UF2.10)
-------------------------------------------

 - open(ruta, modo): devuelve un objeto File y coloca el puntero segun el modo.
 - Diferencia Texto vs Binario:
    • Texto ('r', 'w', 'a')         → lee y escribe cadenas (str) con codificacion (UTF-8)
    • Binario ('rb', 'wb', 'ab')    → lee y escribe bytes puros (b"..."), sin codificacion      
 - Reglas de oro de los modos:
    • 'r' / 'rb' → solo lectura; falla si no existe; puntero al INICIO
    • 'w' / 'wb'  -> solo escritura; CREA si no existe; SOBRESCRIBE TODO si existe; puntero al INICIO.
    • 'a' / 'ab'  -> añadir al final; CREA si no existe; NO borra lo anterior; puntero al FINAL.
    • Añadir '+'  -> habilita lectura y escritura a la vez ('r+', 'w+', 'a+', 'rb+', etc.).        
 - Metodos de escritura: write(cadena) y writelines(lista_de_cadenas)
 - Metodos de lectura: read([bytes]), realine([bytes]) y readlines()                                         

"""

# ==================================================================
# PARTE A: MODO TEXTO ('w', 'a', 'r') → SE TRABAJA CON str
# ==================================================================

# 1. ESCRITURA EN MODO ('w')
# Si 'notas.txt' no existe, lo crea. Si ya existia, BORRA todo su contenido previo.
archivo = open("notas.txt", "w", encoding="utf-8")

# write() escribe exactamente la cadena que le pases (NO pone salto de linea solo)
archivo.write("Linea 1: Introduccion a Python\n")

# writelines() recibe la lista/tupla de cadenas y las escribe seguidas
# OJO: hay que añadir |n manualmente si queremos que se salte la linea entre cadenas
lineas_a_escribir = [
    "Linea 2: Manejo de ficheros\n",
    "Linea 3: Modos de apertura\n"
]
archivo.writelines(lineas_a_escribir)

# Siempre cerrar para volcar los datos de buffer al disco y liberar el archivo
archivo.close()

# 2. AÑADIR CONTENIDO SIN BORRAR ('a')
# Como 'notas.txt' ya existe, el puntero empueza directamente AL FINAL del archivo
archivo = open("notas.txt", "a", encoding="utf-8")
archivo.write("Linea 4: Agregada sin borrar lo anterior\n")
archivo.close()

# 3. LECTURA EN MODO TEXTO ('r') → LAS 4 FORMAS
# Forma 1: read() sin argumentos → devuelve TODO el fichero en un unico str
archivo = open("notas.txt", "r", encoding="utf-8")
contenido_completo = archivo.read()
print("--- LECTURA COMPLETA CON read() ---")
print(contenido_completo)
archivo.close()

# Forma 2: read(n) con parametro → lee solo los primeros 'n' caracteres/bytes
archivo = open("notas.txt", "r", encoding="utf-8")
primeros_7 = archivo.read(7)            # Lee "linea 1"
siguientes_10 = archivo.read(10)        # Continua donde se quedo: ": Introduc"
print("--- LECTURA PARCIAL CON read(n) ---")
print(primeros_7, "|", siguientes_10)
archivo.close/()


# Forma 3: readline() → lee UNA linea cada vez que se invoca (incluye el '\n' final)
archivo = open("notas.txt", "r", encoding="utf-8")
primera_linea = archivo.readline()      # "Linea 1: Introduccion a Python\n"
segunda_linea = archivo.readline()      # "Linea2: Manejo de ficheros\n"
print("--- LECTURA LINEA A LINEA CON readline() ---")
print("1ª: ", primera_linea.strip())    # .strip() quita el '\n' sobrante al imprimir
print("2ª: ", segunda_linea.strip())
archivo.close()

# Forma 4: readlines() → devuelve una LISTA donde cada elemento es una linea del archivo
archivo = open("notas.txt", "r", encoding="utf-8")
lista_de_lineas = archivo.realines()
print("--- LECTUAR EN LISTA CON realines() ---")
for linea in lista_de_lineas:
    print("→ ", linea.strip())
archivo.close()

# ==================================================================
# PARTE B: MODO BINARIO ('wb', 'rb') -> SE TRABAJA CON bytes
# ==================================================================

# 4. ESCRITURA EN MODO BINARIO ('wb')
# No admite el parámetro encoding, porque guarda bytes crudos sin interpretar texto.
archivo_bin = open("datos.bin", "wb")

# En modo 'wb' NO se puede pasar un str normal ("Hola") -> lanzaría TypeError.
# Opción 1: literal de bytes usando el prefijo b"..." (solo caracteres ASCII)
archivo_bin.write(b"Cabecera binaria\n")

# Opción 2: convertir un texto con tildes/ñ a bytes usando .encode("utf-8")
texto_con_tildes = "Información en español\n"
archivo_bin.write(texto_con_tildes.encode("utf-8"))

archivo_bin.close()


# 5. LECTURA EN MODO BINARIO ('rb')
archivo_bin = open("datos.bin", "rb")
datos_crudos = archivo_bin.read()      # Devuelve un objeto de tipo <class 'bytes'>
archivo_bin.close()

print("--- LECTURA BINARIA CON 'rb' ---")
print("Tipo de dato devuelto:", type(datos_crudos))       # <class 'bytes'>
print("Bytes crudos:", datos_crudos)                      # b'Cabecera binaria\nInformaci\xc3\xb3n...'
print("Decodificado a str:", datos_crudos.decode("utf-8"))


# 6. CASO REAL DE EXAMEN/PRÁCTICA: COPIAR UN ARCHIVO BINARIO (ej. una imagen o .bin)
# Se abre el origen en 'rb' y el destino en 'wb' para copiar los bytes exactos sin alterarlos.
origen = open("datos.bin", "rb")
destino = open("copia_datos.bin", "wb")

bytes_originales = origen.read()       # Lee todos los bytes exactos
destino.write(bytes_originales)        # Escribe los mismos bytes en la copia

origen.close()
destino.close()

