
# Laboratorio 3 - Ejercicio 3
# Validador del número de serie
# Taller de bicicletas Rueda Libre

LARGO = 11

serie = input("Número de serie del cuadro: ").strip().upper()

# Paso 1: Contar letras, dígitos y otros símbolos
letras = 0
digitos = 0
otros = 0

for caracter in serie:
    if caracter.isalpha():
        letras += 1
    elif caracter.isdigit():
        digitos += 1
    else:
        otros += 1

print(f"Letras: {letras} | Dígitos: {digitos} | Otros símbolos: {otros}")

# Paso 2: Validar longitud y posiciones
valido = True

if len(serie) != LARGO:
    print(f"Error: debe tener {LARGO} caracteres y tiene {len(serie)}.")
    valido = False
else:
    for posicion in range(3):
        if not serie[posicion].isalpha():
            caracter = serie[posicion]
            print(f"Error: carácter {posicion + 1} ({caracter}) debe ser letra.")
            valido = False

    for posicion in range(3, LARGO):
        if not serie[posicion].isdigit():
            caracter = serie[posicion]
            print(f"Error: carácter {posicion + 1} ({caracter}) debe ser dígito.")
            valido = False

# Paso 3: Mostrar resultado
if valido:
    print(f"Número de serie válido, código de fabricante: {serie[:3]}")
else:
    print("Número de serie inválido. Revíselo en el cuadro de la bicicleta.")
