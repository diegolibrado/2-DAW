"""
-------------------------------------------
4. ESTRUCTURAS DE CONTROL: IF, WHILE / DO-WHILE Y FOR (UF2.3)
-------------------------------------------

 - Indentacioón obligatoria de 4 espacios
 - Condicionales: if /elif /else
 - while: requiere inicializar y modificar la variable de control
 - NO existe 'do-while' nativo en Python → se simula con 'while True:' + 'if ... : break'.
 - for: itera sobre listas, strings o range(inicio, fin, paso)

"""

# 1. CONDICIONALES (if / elif / else)
compra = 150
if compra <= 100:
    print("Pago en efectivo")
elif compra > 100 and compra < 300:
    print("Pago con tarjeta de debito")
else:
    print("Pago con tarjeta de crédito")

# 2. BUCLE WHILE ESTÁNDAR
i = 1
while i < 3:
    print(i)
    i +=  1     # Si no se modifica la variable de control, seria bucle infinito

# 3. SIMULACION DE DO-WHILE (while + if + break)
# Garantiza que el cuerpo se ejecute al menos una vez antes de evaluar la salida
contador = 1
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break   # Rompe el bucle cuando se cumpla la condicion de salida

# 4. BUCLE FOR SOBRE ITERABLES Y RANGE()
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Luis']
for nombre in mi_lista:
    print(nombre)

for letra in "AMIGO":
    print(letra)

# range(inicio, fin_no_incluido, paso)
for num in range(2, 10, 2):     # 2, 4, 5, 6 (de 2 en 2)
    print(num)

for num in range(10, 5, -1):    # 10, 9, 8, 7, 6 (cuenta atras con un paso negativo)
    print(num)