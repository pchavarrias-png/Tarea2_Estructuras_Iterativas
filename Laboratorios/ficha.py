
# Laboratorio 3 - Ejercicio 4
# Ficha de ingreso, horario y reseñas

# Paso 1: Datos de la bicicleta
bicicleta = ("Trek", "Marlin 5", 29, "Rojo")

marca, modelo, rodado, color = bicicleta

print("=== FICHA DE INGRESO ===")
print("Marca:", marca)
print("Modelo:", modelo)
print("Rodado:", rodado)
print("Color:", color)

# Paso 2: Dias de atencion
dias_atencion = {"lunes", "martes", "miercoles", "jueves", "viernes", "sabado"}

print("\n=== DIAS DE ATENCION ===")

for dia in sorted(dias_atencion):
    print(dia)

print("Total de dias de atencion:", len(dias_atencion))

# Paso 3: Resenas de clientes
resenas = [
    "Excelente servicio",
    "Atencion rapida",
    "Muy buen trabajo"
]

print("\n=== RESENAS DE CLIENTES ===")

for resena in resenas:
    print("-", resena)

print("Total de resenas:", len(resenas))

