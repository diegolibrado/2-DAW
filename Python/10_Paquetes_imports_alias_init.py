"""
-------------------------------------------
10. PAQUETES, IMPORTS, ALIAS Y __init__.py
-------------------------------------------

 - Estructura de carpetas tipica:
    mi_proyecto/
     |--- main.py
     |--- paquete/
          |--- __init__.py          <-- Convierte la carpeta en paquete; puede definir __all__
          |--- modulo1.py
          |--- subpaquete/
               |--- __init__.py
               |--- modulo2.py
 
 - Orden: 1º Libreria estandar, 2º terceros, 3º propios (alfabetico y linea en blanco entre bloques)

"""

# --- Contenido de paquete/__init__.py ---
# Define que modulos se exportan al hacer 'from paquete import *'
__all__ = ["modulo1", "modulo2", "modulo3"]

# --- Ejemplos de importacion en main.py ---

# 1. Importacion normal usando namespace completo
import modulo
import paquete.modulo1
import paquete.subpaquete.modulo2

print(modulo.funcion())
print(paquete.modulo1.funcion())

# 2. Importacion con alias ('as') para acortar namespace
import paquete.subpaquete.modulo2 as psm
print(funcion())

# 3. Importacion directa con 'from ... import ...'
from paquete.subpaquete.modulo2 import funcion, variable
print(funcion())

# 4. Alias en 'from ... import' para evitar conflictos de nombres iguales
from paquete.modulo1 import CONSTANTE_1 as C1
from paquete.subpaquete.modulo2 import CONSTANTE1 as CS1
print(C1, CS1)