
# Archivo: ejercicio_1.py
# Curso: Principios de Programación 1
# Autor: Pablo Gerardo Chavarría Segura
# Fecha: 22/11/2026
# Versión: 1.0
# Descripción: Simulación de calentamiento de una cámara experimental.

# Entrada de datos
temperatura_actual = float(input("Ingrese la temperatura inicial en °C: "))
temperatura_objetivo = float(input("Ingrese la temperatura objetivo en °C: "))
incremento = float(input("Ingrese el incremento por ciclo en °C: "))

# Inicialización del contador
ciclos = 0

# Validación y proceso
if temperatura_objetivo <= temperatura_actual:
    print("Error: el objetivo debe ser mayor que la temperatura inicial.")

elif incremento <= 0:
    print("Error: el incremento debe ser mayor que cero.")

else:
    # Ciclo de calentamiento
    while temperatura_actual < temperatura_objetivo:
        temperatura_actual = temperatura_actual + incremento
        ciclos = ciclos + 1

        print("Ciclo:", ciclos, "- Temperatura:", temperatura_actual, "°C")

    # Resultados finales
    print("Temperatura final:", temperatura_actual, "°C")
    print("Total de ciclos:", ciclos)
