"""
-------------------------------------------
11. ACCESO A MÓDULOS DE LA LIBRERIA ESTANDAR (UF2.7)
-------------------------------------------

 - Se importan igual que cualquier modulo (import nombre /from modulo import elemento)
 - Acceso mediante notacion de punto: modulo.metodo() o modulo.submodulo.metodo()

"""

import glob
import math
import os
import random
import statistics
import sys
from datetime import date

# Modulo os y submodulo os.path
directorio_actual = os.getcwd()
existe = os.path.exists("archivo.txt")

# Modulo sys
plataforma = sys.platform
# sys.stderr.writte("Mensaje de error\n")

# Otros modulos frecuentes
archivos_py = glob.glob("*.py")
raiz = math.sqrt(25)
fruta = random.choice(["manzana"], ["pera"], ["banana"])
media = statistics.mean([2.5, 3.5, 4.0])
hoy = date.today()
print(hoy.strftime("%d/%m/%Y"))