
# Archivo: ejercicio_2.py
# Curso: Principios de Programación 1
# Autor: Pablo Gerardo Chavarría Segura
# Fecha: 22/11/2026
# Versión: 1.0
# Descripción: Registro semanal de consumo de agua.

# Constantes
DIAS = 7
UMBRAL = 150

# Inicialización de variables
consumo_total = 0
mayor_consumo = 0
dias_superiores = 0

# Registro del consumo durante siete días
for dia in range(1, DIAS + 1):
    consumo = float(input(f"Ingrese el consumo del día {dia} en litros: "))

    # Validación del consumo
    while consumo < 0:
        print("Error: el consumo no puede ser negativo.")
        consumo = float(input("Ingrese nuevamente el consumo: "))

    # Acumulador
    consumo_total = consumo_total + consumo

    # Comparación del consumo máximo
    if consumo > mayor_consumo:
        mayor_consumo = consumo

    # Contador de días superiores al umbral
    if consumo > UMBRAL:
        dias_superiores = dias_superiores + 1

# Cálculo del promedio
promedio = consumo_total / DIAS

# Resultados finales
print("\n--- RESUMEN SEMANAL ---")
print("Consumo total:", consumo_total, "litros")
print("Promedio diario:", promedio, "litros")
print("Mayor consumo:", mayor_consumo, "litros")
print("Días con consumo superior a 150 litros:", dias_superiores)
