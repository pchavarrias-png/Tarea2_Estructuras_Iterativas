
# Archivo: ejercicio_4.py
# Curso: Principios de Programación 1
# Autor: Pablo Gerardo Chavarría Segura
# Fecha: 22/11/2026
# Versión: 1.0
# Descripción: Control de abastecimiento de una expedición.

# Constantes
AGUA_INICIAL = 150
ALIMENTO_INICIAL = 100

# Inicialización de variables
agua_disponible = AGUA_INICIAL
alimento_disponible = ALIMENTO_INICIAL
agua_consumida = 0
alimento_consumido = 0
dias_completados = 0

# Entrada y validación de jornadas
jornadas = int(input("Ingrese las jornadas de la expedición (1 a 30): "))

while jornadas < 1 or jornadas > 30:
    print("Error: ingrese un número entre 1 y 30.")
    jornadas = int(input("Ingrese nuevamente las jornadas: "))

# Simulación de la expedición
for dia in range(1, jornadas + 1):

    # Verificación de recursos
    if agua_disponible == 0 or alimento_disponible == 0:
        break

    print("\n--- Jornada", dia, "---")
    print("Agua disponible:", agua_disponible, "litros")
    print("Alimento disponible:", alimento_disponible, "unidades")

    # Entrada y validación del agua
    consumo_agua = float(input("Ingrese el consumo de agua: "))

    while consumo_agua <= 0 or consumo_agua > agua_disponible:
        print("Error: consumo de agua inválido.")
        consumo_agua = float(input("Ingrese nuevamente el consumo de agua: "))

    # Entrada y validación del alimento
    consumo_alimento = float(input("Ingrese el consumo de alimento: "))

    while consumo_alimento <= 0 or consumo_alimento > alimento_disponible:
        print("Error: consumo de alimento inválido.")
        consumo_alimento = float(input("Ingrese nuevamente el consumo de alimento: "))

    # Actualización de recursos y acumuladores
    agua_disponible = agua_disponible - consumo_agua
    alimento_disponible = alimento_disponible - consumo_alimento

    agua_consumida = agua_consumida + consumo_agua
    alimento_consumido = alimento_consumido + consumo_alimento

    dias_completados = dias_completados + 1

    # Resultados de la jornada
    print("Agua restante:", agua_disponible, "litros")
    print("Alimento restante:", alimento_disponible, "unidades")

    # Interrupción anticipada
    if (agua_disponible == 0 or alimento_disponible == 0) and dia < jornadas:
        print("Recursos agotados. Expedición interrumpida.")
        break

# Cálculo de promedios
if dias_completados > 0:
    promedio_agua = agua_consumida / dias_completados
    promedio_alimento = alimento_consumido / dias_completados
else:
    promedio_agua = 0
    promedio_alimento = 0

# Estado final
if dias_completados == jornadas:
    estado = "Expedición completada"
else:
    estado = "Expedición interrumpida por falta de recursos"

# Informe final
print("--- INFORME FINAL ---")
print("Jornadas completadas:", dias_completados)
print("Agua consumida:", agua_consumida, "litros")
print("Alimento consumido:", alimento_consumido, "unidades")
print("Agua restante:", agua_disponible, "litros")
print("Alimento restante:", alimento_disponible, "unidades")
print("Promedio diario de agua:", promedio_agua, "litros")
print("Promedio diario de alimento:", promedio_alimento, "unidades")
print("Estado:", estado)
