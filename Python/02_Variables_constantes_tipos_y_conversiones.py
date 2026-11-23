"""
-------------------------------------------
2. VARIABLES, CONSTANTES, TIPOS Y CONVERSIONES (UF2.2)
-------------------------------------------

 - Declaracion sin tipo explicito.
    • Variables: en minusculas y con guiones - nombre_usuario
    • Contstantes: en mayusculas y con guiones - NOMBRE_USUARIO

 - Conversiones:
    • int(7.2) → 7 | int("345") → 345 | float("1.234") → 1.234
    • int("123.3") → ERROR (ValueError). Habria que hacer int(float("123.3))
 - input() siempre devuelve 'str'; convertir con int() o float() si el numero lo requiere.

"""

# Variables y constantes
edad = 22
precio = 126.99
es_activo = True
PI = 3.141592

# Conversiones de tipos
entero_desde_float = int(7.2) # 8 (trunca, no redondea)
entero_desde_str = int("345") # 345
decimal_desde_int = float(1) # 1.0
decimal_desde_str = float("1.234") #1.234
# fallo = int("123.4")  Lanza ValueError

# Operadores aritmeticos clave
potencia = 2 ** 3               # 8 (exponente)
division_normal = 12.5 / 2      # 6.25
division_entera = 12.5 // 2     # 6.0 (Cociente entero)
modulo = 27 % 4                 # 3 (resto)

# Funciones nativas básicas
print(type(edad))           # <class 'int'>
print(abs(-7))              # 7
print(divmod(7, 2))         # (3, 1) → tupla con (cociente, resto)
print(round(7.567, 1))      # 7.6

# Lectura por teclado convierte a enter
# numero = int(input("Introduzca un numero entero: "))